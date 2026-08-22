# ocr_pipeline — 扫描书高保真"夹心"OCR

给扫描版学术书 PDF 叠加**可精准选中、复制无假空格**的文字层,同时**逐字节保留原书图像流**。
为一个具体需求而生:把普特南《理性、真理与历史》和罗蒂《哲学和自然之镜》的扫描版
变成"原版一模一样 + 全文可检索"的 PDF——最终两本书都验收通过,本目录是完整可复用的管线。

## 三条硬指标

1. **图像零重编码**——文字层画在原 PDF 页上(`render_mode=3` 不可见),验收时逐页比对图像流 MD5:0 差异,渲染像素完全一致。
2. **复制不出假空格**——文本层逐字定位,每字 fontsize=分配步进(字形步进=字距,阅读器无从推断空格);识别串里夹在汉字间的模型假空格在组装时正则删除。
3. **GPU 提速 6–10 倍**——rapidocr_onnxruntime 1.2.3 只认 CPU/CUDA EP,`patch_session()` 猴补丁把 ONNX Runtime 会话换成 `DmlExecutionProvider`(任何 N/A 卡,零额外依赖)。RTX 4060 Laptop 实测 ~1.0 页/秒 vs CPU 全核 0.10 页/秒,结果逐字一致。

## 架构:两阶段 + 独立验收

```
build_ocr_pdf.py ocr    原 PDF → 灰度渲染(长边 2400px)→ RapidOCR(PP-OCRv3)→ JSONL 缓存(断点续跑)
build_ocr_pdf.py apply  原 PDF 页上叠逐字不可见文字层 → save(garbage=3, deflate) → 无损档
build_compressed.py     灰度扫描书另做压缩增强档:背景白化 → Otsu 二值 → 连通域去尘 → 1-bit PNG
verify_output.py        验收:图像流 MD5 / 渲染像素抽样 / round-trip 字符比对
```

- 缓存与组装解耦:排版可反复重调,不需重新 OCR;OCR 中断重跑自动跳过已缓存页。
- 行块按"视觉行聚类 → 行内左→右"重排,修复页码插进段落的阅读顺序问题。
- 字体用 PyMuPDF 内置 `china-s`,保存时自动子集化(生僻字无字形但复制文本仍正确,提取走 ToUnicode)。

## 用法

```bash
PY=python  # 依赖:pymupdf rapidocr_onnxruntime onnxruntime-directml pillow opencv-python numpy

# 1) OCR(GPU;--pages 1-based,如 "2,3,50-60";重跑自动续)
python build_ocr_pdf.py ocr --pdf 书.pdf --cache cache.jsonl --device dml
#   CPU 兜底(限线程防卡机):--device cpu --threads 4

# 2) 组装文字层(秒级,可反复重跑)
python build_ocr_pdf.py apply --pdf 书.pdf --cache cache.jsonl --out 书_OCR.pdf

# 3) 验收 + 目检
python verify_output.py --src 书.pdf --out 书_OCR.pdf --cache cache.jsonl
python quality_report.py   # 全书置信度报告,定位低置信页
```

## 经验教训(每一条都真实踩过)

1. **`extract_image()` 不应用 PDF `/Decode` 数组**。源书 1-bit 图带 `[1 0]` 反相解码时,重构出的 PNG 是反的,嵌回去就是黑底白字。铁律:**永不直通 `extract_image()` 的字节**;判断极性/编码一律用"原生 `get_pixmap` 渲染后的灰度分布"。
2. **二值源书不要再压缩**。罗蒂书图像是 CCITT G4(约 12–38KB/页),任何重编码(PIL PNG / 灰度 JPEG)都只会更大更糊——无损档就是最优压缩档。压缩增强只对灰度 JPEG 扫描书有意义(普特南 61MB→21.6MB,白底黑字更锐)。
3. **别和 PyMuPDF 低层 API 搏斗**。`update_stream(new=True)` 手工拷 CCITT 裸流会被改写 `/Filter`,双重编码整页报废。
4. **二值扫描书直接喂 OCR 会识别稀烂**。1-bit 锯齿破坏检测/识别,必须先经灰度抗锯齿渲染(长边 2400px)。
5. **`--pages` 用 1-based**。曾经 0-based 传参导致整页错位,样张"压缩后空白"其实是没处理到的页。
6. **CPU 跑长任务要限线程**(`--threads`),否则吃满全部核心,机器没法用;有 GPU 就走 DML。
7. **验收自动化是底线**。图像流 MD5 比对、渲染像素抽样比对、round-trip 字符比对三件套,加上红框叠加目检图(`crop_overlay.py` 思路:OCR 行框画回渲染页),四次翻车全部是它们抓住的。

## 实战记录(2026-08-22)

| 书 | 页数 | 源 | 交付 |
|---|---|---|---|
| 理性、真理与历史(普特南,童世骏/李光程 译) | 314 | 283DPI 灰度 JPEG, 61MB | 无损档 66MB + 压缩增强档 21.6MB,round-trip 313/313 |
| 哲学和自然之镜(罗蒂,李幼蒸 译) | 521 | CCITT G4 二值, 19.9MB | 仅无损档 23.9MB(见教训 2),round-trip 515/515 |

全书 OCR 置信度均值 ≈0.88;形近字偶错(肯定→背定类)是 PP-OCRv3 移动端模型的上限,置信度报告可定位重查。

## 已知局限

- 旋转 90° 的侧排页码/竖排文字检不出(cls 只支持 0°/180°),正文不受影响。
- `china-s` 字体覆盖有限:生僻字在页面上无字形,但复制出的文本仍正确。

## License

与本仓库一致:CC BY-NC 4.0。
