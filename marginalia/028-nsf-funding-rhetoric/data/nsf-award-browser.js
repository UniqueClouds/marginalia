(() => {
  const PAGE_SIZE = 40;
  const EN_AREA_LABELS = {
    "计算机与计算": "Computing",
    "人工智能": "Artificial intelligence",
    "软件工程": "Software engineering",
    "创新研究": "Innovation research",
    "AI与社会 / 人本AI": "AI & society / human-centered AI",
    "计算社会科学": "Computational social science",
    "科学学 / 科学政策": "Science of science / science policy",
    "组织研究": "Organization studies",
  };
  const MESSAGES = {
    zh: {
      loading: "正在下载并解压约 29.6 MB 的压缩数据……",
      loaded: (count) => `已加载 ${count.toLocaleString()} 条记录。筛选和摘要阅读都在本地浏览器中进行。`,
      loadError: "数据加载失败：",
      unsupported: "当前浏览器不支持 gzip 解压，请下载 JSON 文件后查看。",
      empty: "没有符合条件的项目。",
      results: (n, total) => `显示 ${n.toLocaleString()} / ${total.toLocaleString()} 条匹配记录。每页 ${PAGE_SIZE} 条。`,
      page: (n, total) => `第 ${n} / ${total} 页`,
      amount: "奖项总额",
      awardId: "NSF 奖项号",
      pi: "PI",
      coPis: "共同 PI",
      institution: "学校 / 机构",
      program: "NSF 项目",
      directorate: "NSF 学部",
      division: "部门",
      elements: "项目要素",
      period: "项目期限",
      areas: "研究领域标签（本项目整理）",
      officialTags: "NSF 记录标签",
      abstract: "摘要原文（英文）",
      translation: "已有中文译文",
      noTranslation: "此记录没有附中文译文。",
      noAbstract: "NSF 记录未提供英文摘要。",
      publications: "NSF 记录列出的相关论文 / 成果",
      noPublications: "NSF 记录中没有列出论文成果。",
      publicationCaveat: "记录列为成果不代表该奖项是论文的唯一资助来源。",
      openAward: "打开 NSF 奖项原页",
      pageSize: `每页 ${PAGE_SIZE} 条`,
    },
    en: {
      loading: "Downloading and decompressing about 29.6 MB…",
      loaded: (count) => `Loaded ${count.toLocaleString()} records. Filtering and abstract reading now run in your browser.`,
      loadError: "Could not load the dataset: ",
      unsupported: "This browser does not support gzip decompression. Download the JSON file to inspect it.",
      empty: "No awards match these filters.",
      results: (n, total) => `Showing ${n.toLocaleString()} of ${total.toLocaleString()} matching records. ${PAGE_SIZE} per page.`,
      page: (n, total) => `Page ${n} of ${total}`,
      amount: "Total award amount",
      awardId: "NSF award ID",
      pi: "PI",
      coPis: "Co-PIs",
      institution: "Institution",
      program: "NSF program",
      directorate: "NSF directorate",
      division: "Division",
      elements: "Program elements",
      period: "Award period",
      areas: "Curated research-area labels",
      officialTags: "NSF record tags",
      abstract: "Original abstract (English)",
      translation: "Existing Chinese translation",
      noTranslation: "No Chinese translation is included for this record.",
      noAbstract: "The NSF record does not provide an English abstract.",
      publications: "Papers / outcomes listed by the NSF record",
      noPublications: "No publications are listed in the NSF record.",
      publicationCaveat: "A record listing does not establish that this award was the paper's sole funding source.",
      openAward: "Open original NSF award page",
      pageSize: `${PAGE_SIZE} per page`,
    },
  };

  const esc = (value) => String(value ?? "").replace(/[&<>"']/g, (ch) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  })[ch]);
  const normalize = (value) => String(value ?? "")
    .normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase();
  const asArray = (value) => Array.isArray(value) ? value : (value ? [value] : []);

  async function readGzipJson(response) {
    const bytes = await response.arrayBuffer();
    if ("DecompressionStream" in window) {
      try {
        const stream = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip"));
        return await new Response(stream).json();
      } catch (_decompressionError) {
        // Some static hosts may transparently decompress .gz responses.
        try { return JSON.parse(new TextDecoder().decode(bytes)); } catch (_parseError) { /* handled below */ }
      }
    }
    try { return JSON.parse(new TextDecoder().decode(bytes)); } catch (_parseError) {
      throw new Error("gzip decompression is unavailable or the data file is invalid");
    }
  }

  function init(root) {
    if (root.dataset.nsfInitialized === "true") return;
    root.dataset.nsfInitialized = "true";
    const locale = root.dataset.locale === "en" ? "en" : "zh";
    const msg = MESSAGES[locale];
    const loadButton = root.querySelector("[data-nsf-load]");
    const status = root.querySelector("[data-nsf-status]");
    const controls = root.querySelector("[data-nsf-controls]");
    const search = root.querySelector("[data-nsf-search]");
    const areaSelect = root.querySelector("[data-nsf-area]");
    const minInput = root.querySelector("[data-nsf-min]");
    const maxInput = root.querySelector("[data-nsf-max]");
    const sortSelect = root.querySelector("[data-nsf-sort]");
    const searchAbstract = root.querySelector("[data-nsf-search-abstract]");
    const resetButton = root.querySelector("[data-nsf-reset]");
    const resultsStatus = root.querySelector("[data-nsf-results-status]");
    const results = root.querySelector("[data-nsf-results]");
    const pagination = root.querySelector("[data-nsf-pagination]");
    const previous = root.querySelector("[data-nsf-prev]");
    const next = root.querySelector("[data-nsf-next]");
    const pageStatus = root.querySelector("[data-nsf-page-status]");
    let awards = null;
    let page = 0;
    let matches = [];
    let renderTimer = 0;

    const formatMoney = (amount) => amount == null
      ? "—"
      : new Intl.NumberFormat(locale === "zh" ? "zh-CN" : "en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 }).format(amount);
    const areaLabel = (value) => locale === "en" ? (EN_AREA_LABELS[value] || value) : value;
    const metadataRow = (label, value) => value
      ? `<tr><th>${esc(label)}</th><td>${esc(asArray(value).join(" · "))}</td></tr>`
      : "";

    function recordHtml(record) {
      const topics = asArray(record.researchAreas);
      const amount = formatMoney(record.amountUSD);
      const title = esc(record.title || "Untitled award");
      const pi = esc(record.pi || "—");
      const institution = esc(record.institution || "—");
      const tags = topics.length ? `<div class="nsf-tags">${topics.map((tag) => `<span>${esc(areaLabel(tag))}</span>`).join("")}</div>` : "";
      const abstract = record.abstractEnglish
        ? esc(record.abstractEnglish).replace(/\r?\n/g, "<br>")
        : `<em>${esc(msg.noAbstract)}</em>`;
      const translation = record.abstractChinese
        ? `<section class="nsf-abstract"><h4>${esc(msg.translation)}</h4><div class="nsf-abstract-text">${esc(record.abstractChinese).replace(/\r?\n/g, "<br>")}</div></section>`
        : `<p class="nsf-muted">${esc(msg.noTranslation)}</p>`;
      const pubs = asArray(record.publications);
      const pubHtml = pubs.length
        ? `<ul class="nsf-publications">${pubs.map((pub) => {
          const label = esc(pub.title || "Untitled publication");
          const url = /^https?:\/\//i.test(pub.url || "") ? pub.url : "";
          const linked = url ? `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${label}</a>` : label;
          const byline = [pub.authors, pub.venue, pub.year].filter(Boolean).map(esc).join(" · ");
          return `<li>${linked}${byline ? `<small>${byline}</small>` : ""}</li>`;
        }).join("")}</ul><p class="nsf-muted">${esc(msg.publicationCaveat)}</p>`
        : `<p class="nsf-muted">${esc(msg.noPublications)}</p>`;
      const awardUrl = /^https?:\/\//i.test(record.awardUrl || "") ? record.awardUrl : "";
      const awardLink = awardUrl ? `<p><a href="${esc(awardUrl)}" target="_blank" rel="noopener noreferrer">${esc(msg.openAward)} ↗</a></p>` : "";
      const startEnd = [record.startDate, record.endDate].filter(Boolean).join(" → ");
      const table = [
        metadataRow(msg.awardId, record.awardId),
        metadataRow(msg.pi, record.pi),
        metadataRow(msg.coPis, record.coPIs),
        metadataRow(msg.institution, record.institution),
        metadataRow(msg.amount, amount),
        metadataRow(msg.program, record.program),
        metadataRow(msg.directorate, record.directorate),
        metadataRow(msg.division, record.division),
        metadataRow(msg.elements, record.programElements),
        metadataRow(msg.period, startEnd),
        metadataRow(msg.areas, topics.map(areaLabel)),
        metadataRow(msg.officialTags, record.officialTags),
      ].filter(Boolean).join("");
      return `<details class="nsf-record"><summary><span class="nsf-record-amount">${esc(amount)}</span><span class="nsf-record-title">${title}</span><span class="nsf-record-id">#${esc(record.awardId || "")}</span><span class="nsf-record-meta">${pi} · ${institution}</span></summary><div class="nsf-record-body">${tags}<div class="nsf-table-wrap"><table class="nsf-meta-table"><tbody>${table}</tbody></table></div><section class="nsf-abstract"><h4>${esc(msg.abstract)}</h4><div class="nsf-abstract-text">${abstract}</div></section>${translation}<section class="nsf-abstract"><h4>${esc(msg.publications)}</h4>${pubHtml}</section>${awardLink}</div></details>`;
    }

    function filteredAwards() {
      const q = normalize(search.value.trim());
      const area = areaSelect.value;
      const min = minInput.value.trim() === "" ? null : Number(minInput.value);
      const max = maxInput.value.trim() === "" ? null : Number(maxInput.value);
      const includeAbstract = searchAbstract.checked;
      let list = awards.filter((record) => {
        const amount = Number(record.amountUSD || 0);
        if (min != null && amount < min) return false;
        if (max != null && amount > max) return false;
        const topicValues = [...asArray(record.researchAreas), ...asArray(record.themeTags), ...asArray(record.officialTags)];
        if (area && !topicValues.includes(area)) return false;
        if (!q) return true;
        const values = [record.awardId, record.title, record.pi, record.coPIs, record.institution,
          record.program, record.directorate, record.division, record.programElements,
          record.researchAreas, record.themeTags, record.officialTags];
        if (includeAbstract) values.push(record.abstractEnglish, record.abstractChinese);
        return normalize(values.flatMap(asArray).join(" ")).includes(q);
      });
      if (sortSelect.value === "amount-asc") list.sort((a, b) => (a.amountUSD || 0) - (b.amountUSD || 0));
      else if (sortSelect.value === "date-desc") list.sort((a, b) => Date.parse(b.startDate || "") - Date.parse(a.startDate || ""));
      else if (sortSelect.value === "title-asc") list.sort((a, b) => String(a.title || "").localeCompare(String(b.title || "")));
      else list.sort((a, b) => (b.amountUSD || 0) - (a.amountUSD || 0));
      return list;
    }

    function render() {
      if (!awards) return;
      matches = filteredAwards();
      const pageCount = Math.max(1, Math.ceil(matches.length / PAGE_SIZE));
      page = Math.min(page, pageCount - 1);
      const first = page * PAGE_SIZE;
      const visible = matches.slice(first, first + PAGE_SIZE);
      results.innerHTML = visible.length ? visible.map(recordHtml).join("") : `<p class="nsf-empty">${esc(msg.empty)}</p>`;
      resultsStatus.textContent = msg.results(matches.length, awards.length);
      pagination.hidden = matches.length === 0;
      previous.disabled = page <= 0;
      next.disabled = page >= pageCount - 1;
      pageStatus.textContent = msg.page(page + 1, pageCount);
    }

    function scheduleRender() {
      page = 0;
      window.clearTimeout(renderTimer);
      renderTimer = window.setTimeout(render, 180);
    }

    function fillAreas() {
      const values = new Set();
      awards.forEach((record) => asArray(record.researchAreas).forEach((x) => values.add(x)));
      Array.from(values).sort((a, b) => areaLabel(a).localeCompare(areaLabel(b))).forEach((value) => {
        const option = document.createElement("option");
        option.value = value;
        option.textContent = areaLabel(value);
        areaSelect.append(option);
      });
    }

    async function load() {
      if (awards) return;
      if (!("DecompressionStream" in window)) {
        status.textContent = msg.unsupported;
        return;
      }
      loadButton.disabled = true;
      status.textContent = msg.loading;
      try {
        const dataUrl = new URL(root.dataset.datasetUrl, window.location.href);
        const response = await fetch(dataUrl, { cache: "force-cache" });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const packageData = await readGzipJson(response);
        if (!Array.isArray(packageData.awards)) throw new Error("invalid award dataset");
        awards = packageData.awards;
        fillAreas();
        controls.hidden = false;
        status.textContent = msg.loaded(awards.length);
        loadButton.hidden = true;
        render();
      } catch (error) {
        loadButton.disabled = false;
        status.textContent = `${msg.loadError}${error.message}`;
      }
    }

    loadButton.addEventListener("click", load);
    [search, areaSelect, minInput, maxInput, sortSelect, searchAbstract].forEach((el) => {
      el.addEventListener(el === search ? "input" : "change", scheduleRender);
    });
    resetButton.addEventListener("click", () => {
      search.value = "";
      areaSelect.value = "";
      minInput.value = "";
      maxInput.value = "";
      sortSelect.value = "amount-desc";
      searchAbstract.checked = false;
      scheduleRender();
    });
    previous.addEventListener("click", () => { if (page > 0) { page -= 1; render(); } });
    next.addEventListener("click", () => {
      const pageCount = Math.ceil(matches.length / PAGE_SIZE);
      if (page + 1 < pageCount) { page += 1; render(); }
    });
  }

  function initAll() {
    document.querySelectorAll("[data-nsf-award-browser]").forEach(init);
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initAll);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAll, { once: true });
  } else {
    initAll();
  }
})();
