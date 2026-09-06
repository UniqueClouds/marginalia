# 扫描书高保真夹心 OCR——把普特南和罗蒂变成'原版一模一样+全文可检索'的 PDF

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> 语言 / Language：**中文** · [English](014-sandwich-ocr-books.en.md)
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-08-22</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> analysis(工程复盘)</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #37</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-014</td></tr><tr><td>title</td><td>扫描书高保真夹心 OCR——把普特南和罗蒂变成'原版一模一样+全文可检索'的 PDF</td></tr><tr><td>date</td><td>2026-08-22</td></tr><tr><td>published</td><td>2026-08-22</td></tr><tr><td>kind</td><td>analysis(工程复盘)</td></tr><tr><td>issue</td><td>37</td></tr></table></details>

> 工程复盘。问题:扫描版学术书既不能检索也不能精准复制——怎么在**不动一个像素**的前提下给它装上文字层?结论先放开头:**用"夹心"架构——原 PDF 页上叠 `render_mode=3` 的逐字不可见文本层,图像流零重编码(MD5 级验收 0 差异);识别用 RapidOCR 打 DirectML 补丁(~1.0 页/秒,CPU 的 10 倍);防假空格的关键是让每个字符的 fontsize 恰好等于它的分配步进。两本书验收通过:普特南无损档 66MB + 压缩增强档 21.6MB,罗蒂无损档 23.9MB(CCITT G4 已是最优,不重压)。过程中踩了七个真实的坑,最贵的一个:`extract_image()` 不应用 PDF `/Decode` 数组,反相页直接变黑底白字。**

## 一、需求与约束

手头两本扫描书的痛点不同:

- **普特南**:283DPI 灰度 JPEG,完全没有文本层——不能检索、不能复制;
- **罗蒂**:更糟,流传的旧 OCR 版文本层稀烂,复制出来是 `CET |AREA BG BAB)` 这样的乱码加竖线假分词。

目标三连:**原版内容一模一样**(视觉零损失)、**文字可精准选中复制**(且复制不出多余空格)、**文件尽可能小**。这三条彼此牵制:任何重编码都破坏第一条;文本层做粗了破坏第二条;而"高保真"与"小体积"天然对冲——除非分书施策。

## 二、方案:夹心架构,两阶段解耦

```
build_ocr_pdf.py ocr    原 PDF → 灰度渲染(长边 2400px)→ RapidOCR → 行框+文本+置信度 → JSONL 缓存
build_ocr_pdf.py apply  原 PDF 页上叠逐字不可见文字层(render_mode=3)→ save(garbage=3) → 无损档
```

两个决定值得展开:

**图像流零重编码。** 不生成新 PDF,而是在原 PDF 的页对象上追加文字层后另存。`save(garbage=3, deflate=True)` 只整理结构、重压元数据流,**不触碰图像流**。验收脚本逐页比对图像流 MD5:0 差异;再抽样比对渲染像素:完全一致。"原版一模一样"由此从口号变成可断言的性质。

**缓存与组装解耦。** OCR 结果落 JSONL(每行一个页记录),组装阶段秒级完成、可反复重跑——后来四次调整文字层排版(修空格、修阅读顺序)都没有重新识别过一个字。中断续跑也免费获得:重跑时跳过已缓存页。

## 三、三个关键技术决定

### 1. 字符级定位 + "fontsize=步进",根治假空格

RapidOCR 给的是**行级**框。要让选中/复制精确到字,得把行切成单字摆放:按 CJK 全宽 1.0、Latin/数字 0.55、标点 0.45 的宽度配比,把行的总宽按权重切分给每个字符。

第一版的坑:字号取 `min(框高×0.72, …)`,结果字形比字距窄,**阅读器提取文本时按"字形间隙"推断空格**,复制出大量假空格(用户实测发现)。修复:让**每个字的 fontsize 恰好等于它分到的步进宽度**——CJK 字形的 advance 恰等于 fontsize,于是"字形步进=字符间距",间隙恒为零,任何阅读器都无从推断。再把识别串里夹在两个汉字之间的模型假空格(如"李幼 蒸译")在组装时正则删除。双保险之后,复制文本干净了。

### 2. DirectML 猴补丁,GPU 提速 6–10 倍

rapidocr_onnxruntime 1.2.3 的会话工厂只认 CPU/CUDA 两个 EP,机器上的 RTX 4060 完全使不上;而环境里已装的 onnxruntime-directml 明明带着 `DmlExecutionProvider`。解法是重写 `OrtInferSession.__init__`,把 provider 列表换成 DML:

| 设备 | 速度 | 备注 |
|---|---|---|
| CPU 全核(默认) | 0.10 页/秒 | 吃满所有核,机器卡到没法用 |
| CPU 限 4 线程 | 0.18 页/秒 | 防卡机兜底 |
| **DirectML** | **~1.0 页/秒** | CPU 基本空闲;输出与 CPU 逐字一致 |

521 页的书从 ~87 分钟缩到 ~9 分钟,而且全程电脑可用。

### 3. 二值书必须先灰度抗锯齿渲染

罗蒂书是 1-bit 二值扫描,直接喂 OCR 识别稀烂(旧版失败的根因)。锯齿边缘破坏检测与识别,必须先经 PyMuPDF 以长边 2400px 渲染成灰度——放大过程天然产生抗锯齿灰阶,识别质量立刻恢复正常(置信度均值 0.71→0.88)。

## 四、七条踩坑实录(按代价排序)

1. **`extract_image()` 不应用 PDF `/Decode` 数组**。罗蒂书的部分 1-bit 图带 `[1 0]` 反相解码;重构出的 PNG 极性是反的,直通嵌回就是**黑底白字**(用户翻开实测发现)。铁律:**永不直通 `extract_image()` 的字节**;极性/编码判断一律基于原生 `get_pixmap` 渲染——渲染永远正确应用 Decode。
2. **二值源书不要再压缩**。为了救体积先试直通(PNG 容器比 G4 裸流胖 ~30KB/页,19.9→36MB),再试自家重编码(去噪+PIL optimize,自以为 0.65×)——最后发现 0.65× 是和 extract_image 虚胖容器比的;对比真身 CCITT G4 裸流,PIL PNG 反而 ~1.7×。**G4 打不过,无损档就是最优压缩档**,压缩增强版只对灰度 JPEG 书有意义。
3. **别和 PyMuPDF 低层 API 搏斗**。试图手工拷贝 CCITT 裸流(`get_new_xref` + `update_object` + `update_stream(new=True)`),`update_stream` 无视我写的 `/Filter /CCITTFaxDecode` 强行改写成 FlateDecode,双重编码整页报废(渲染全白)。
4. **`--pages` 参数 0/1-based 混用导致整页错位**。样张里"压缩后空白"的页其实根本没被处理——目检截图前先怀疑自己的索引约定。
5. **CPU 跑满核会被用户投诉卡机**。长任务的默认姿态应该是:有 GPU 走 GPU,没 GPU 限线程(`--threads`)。
6. **检测参数调敏感(阈值 0.3→0.25 等)在这两本书上零增益**——v1/v2 逐页字符完全一致。缺字的真凶不是漏检,而是文本层字号过小导致选中高亮盖不住字形(见第三节 1)。先量化归因,再动手优化。
7. **验收自动化是底线**。图像流 MD5、渲染像素抽样、round-trip 字符比对三件套加上红框叠加目检图——上面每一次翻车都是它们抓住的,包括黑底白字那次的极性统计(dark%=91% 一眼定罪)。

## 五、实战数字

| 书 | 页数 | 源 | 交付 | round-trip |
|---|---|---|---|---|
| 理性、真理与历史(普特南) | 314 | 283DPI 灰度 JPEG, 61MB | 无损档 66MB + 压缩增强档 21.6MB(白底黑字,笔画更锐)| 313/313 |
| 哲学和自然之镜(罗蒂) | 521 | CCITT G4 二值, 19.9MB | 仅无损档 23.9MB(见坑 2)| 515/515 |

全书 OCR 置信度均值 ≈0.88。残余错误是形近字级别(肯定→背定),PP-OCRv3 移动端模型的上限;置信度报告可以定位低置信页重点校对。

## 六、局限与下一步

- 旋转 90° 的侧排页码检不出(cls 只支持 0°/180°),正文不受影响;
- 生僻字在 `china-s` 子集字体下可能无字形,但复制出的文本仍正确(提取走 ToUnicode);
- 若追求更小体积:JBIG2 编码可比 G4 再省 ~30%,但 Windows 下工具链(jbig2enc)不便,未做;PP-OCRv5 模型发布后换模型可再提精度。

管线完整代码在本仓库 [`ocr_pipeline/`](https://github.com/UniqueClouds/marginalia/tree/main/ocr_pipeline)(PR #36),含双语 README 与七条坑的工程版记录。


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [Read this note in English](014-sandwich-ocr-books.en.md)

