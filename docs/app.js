const state = { snapshot: null, history: [], chart: "tps" };

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const setText = (selector, value) => { const node = $(selector); if (node) node.textContent = value ?? "—"; };
const clamp = (value, min, max) => Math.min(max, Math.max(min, Number(value) || 0));
const esc = (value) => String(value ?? "").replace(/[&<>'"]/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));

function formatNumber(value, options = {}) {
  const number = Number(value);
  if (!Number.isFinite(number)) return "Unavailable";
  const { currency = false, unit = "", digits = 2, compact = true } = options;
  const formatter = new Intl.NumberFormat("en-US", {
    notation: compact && Math.abs(number) >= 10_000 ? "compact" : "standard",
    maximumFractionDigits: digits,
    minimumFractionDigits: options.minimumDigits ?? 0,
    style: currency ? "currency" : "decimal",
    currency: currency ? "USD" : undefined,
  });
  return `${formatter.format(number)}${unit}`;
}

function formatPct(value, signed = true) {
  const number = Number(value);
  if (!Number.isFinite(number)) return "Unavailable";
  const sign = signed && number > 0 ? "+" : "";
  return `${sign}${number.toFixed(2)}%`;
}

function compactAddress(value) {
  if (!value) return "Unknown";
  return value.length > 18 ? `${value.slice(0, 8)}…${value.slice(-6)}` : value;
}

function relativeTime(value) {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "unknown";
  const seconds = Math.round((Date.now() - date.getTime()) / 1000);
  if (seconds < 60) return `${Math.max(0, seconds)}s ago`;
  if (seconds < 3600) return `${Math.round(seconds / 60)}m ago`;
  if (seconds < 86400) return `${Math.round(seconds / 3600)}h ago`;
  return `${Math.round(seconds / 86400)}d ago`;
}

function setTrack(selector, value) {
  const node = $(selector);
  if (node) requestAnimationFrame(() => { node.style.width = `${clamp(value, 2, 100)}%`; });
}

function renderHealth(snapshot) {
  const score = clamp(snapshot.health?.score, 0, 100);
  const circumference = 2 * Math.PI * 72;
  setText("#health-score", String(Math.round(score)));
  setText("#health-status", snapshot.health?.status || "unknown");
  const arc = $("#health-arc");
  arc.style.strokeDasharray = circumference;
  requestAnimationFrame(() => { arc.style.strokeDashoffset = circumference * (1 - score / 100); });

  const container = $("#health-components");
  container.replaceChildren();
  for (const component of snapshot.health?.components || []) {
    const row = document.createElement("div");
    row.className = "component-row";
    const pct = component.weight ? component.score / component.weight * 100 : 0;
    row.innerHTML = `<header><span>${esc(component.name)}</span><span>${esc(component.score)} / ${esc(component.weight)}</span></header><div class="bar-track"><i style="width:${clamp(pct, 0, 100)}%"></i></div>`;
    container.append(row);
  }
}

function renderSignals(snapshot) {
  const network = snapshot.metrics?.network || {};
  const validators = snapshot.metrics?.validators || {};
  setText("#metric-tps", formatNumber(network.tps, { digits: 0 }));
  setText("#metric-slot-time", formatNumber(network.slotTimeSeconds, { digits: 3 }));
  setText("#metric-epoch", network.epoch ? `#${network.epoch}` : "—");
  setText("#metric-epoch-progress", formatPct(network.epochProgressPct, false));
  setText("#validator-count", `${formatNumber(validators.active, { digits: 0 })} active`);
  setText("#metric-delinquent", formatPct(validators.delinquentStakePct, false));
  setTrack("#tps-track", clamp((network.tps || 0) / 70, 5, 100));
  setTrack("#slot-track", clamp(100 - ((network.slotTimeSeconds || 1) - 0.35) * 130, 5, 100));
  setTrack("#epoch-track", network.epochProgressPct || 0);
  setTrack("#delinquent-track", clamp(100 - (validators.delinquentStakePct || 0) * 20, 5, 100));
}

function trendClass(node, value) {
  if (!node) return;
  node.classList.toggle("negative", Number(value) < 0);
}

function renderEconomics(snapshot) {
  const e = snapshot.metrics?.economics || {};
  setText("#sol-price", formatNumber(e.solPriceUsd, { currency: true, digits: 2, compact: false }));
  setText("#sol-change", formatPct(e.solPriceChange24hPct));
  trendClass($("#sol-change"), e.solPriceChange24hPct);
  setText("#sol-updated", e.solPriceUpdatedAt ? `source timestamp · ${relativeTime(e.solPriceUpdatedAt)}` : "source timestamp unavailable");
  setText("#tvl", formatNumber(e.tvlUsd, { currency: true }));
  setText("#stablecoins", formatNumber(e.stablecoinSupplyUsd, { currency: true }));
  setText("#dex-volume", formatNumber(e.dexVolume24hUsd, { currency: true }));
  setText("#dex-change", formatPct(e.dexVolumeChange1dPct));
  trendClass($("#dex-change"), e.dexVolumeChange1dPct);
  setText("#fees", formatNumber(e.fees24hUsd, { currency: true }));
  setText("#fees-change", formatPct(e.feesChange1dPct));
  trendClass($("#fees-change"), e.feesChange1dPct);
  setText("#circulating", formatNumber(e.circulatingSupplySol, { digits: 2 }));
}

function renderValidators(snapshot) {
  const validators = snapshot.metrics?.validators || {};
  setText("#active-validators", `${formatNumber(validators.active, { digits: 0 })} active`);
  const rows = validators.topByStake || [];
  const max = Math.max(...rows.map(row => Number(row.activatedStakeSol) || 0), 1);
  const container = $("#validator-bars");
  container.replaceChildren();
  for (const row of rows) {
    const item = document.createElement("div");
    item.className = "validator-row";
    item.title = row.votePubkey || "";
    const width = clamp(Number(row.activatedStakeSol) / max * 100, 2, 100);
    item.innerHTML = `<span class="validator-id">${esc(compactAddress(row.votePubkey))}</span><div class="bar-track" aria-label="${esc(formatNumber(row.activatedStakeSol, { unit: ' SOL' }))} activated stake"><i style="width:${width}%"></i></div><span class="validator-value">${esc(formatNumber(row.activatedStakeSol, { unit: ' SOL' }))} · ${esc(row.commissionPct)}%</span>`;
    container.append(item);
  }
}

function renderAnomalies(snapshot) {
  const anomalies = snapshot.anomalies || [];
  setText("#anomaly-count", anomalies.length);
  const container = $("#anomaly-list");
  container.replaceChildren();
  if (!anomalies.length) {
    container.innerHTML = `<div class="empty-state"><i></i><strong>No active anomaly</strong><small>Signals are inside learned and explicit thresholds.</small></div>`;
    return;
  }
  for (const anomaly of anomalies) {
    const item = document.createElement("article");
    item.className = `anomaly-item ${anomaly.severity === "critical" ? "critical" : ""}`;
    item.innerHTML = `<header><strong>${esc(anomaly.metric)}</strong><span>${esc(String(anomaly.severity).toUpperCase())}</span></header><p>${esc(formatNumber(anomaly.value, { unit: anomaly.unit || "", compact: false }))} · ${esc(formatPct(anomaly.deltaPct))} vs ${esc(anomaly.method)}</p>`;
    container.append(item);
  }
}

function renderSources(snapshot) {
  const container = $("#source-grid");
  container.replaceChildren();
  for (const source of snapshot.sources || []) {
    const safeUrl = String(source.url || "").startsWith("https://") ? source.url : "./";
    const card = document.createElement("article");
    card.className = "source-card";
    card.innerHTML = `<header><a href="${esc(safeUrl)}" target="_blank" rel="noopener noreferrer">${esc(source.name)}</a><i aria-label="source connected"></i></header><p>${esc((source.metrics || []).join(" · "))}</p>`;
    container.append(card);
  }
  const errors = snapshot.coverage?.errors || [];
  const errorBox = $("#source-errors");
  if (errors.length) {
    errorBox.hidden = false;
    errorBox.textContent = `Partial observation: ${errors.map(error => `${error.source}: ${error.message}`).join(" · ")}`;
  } else {
    errorBox.hidden = true;
    errorBox.textContent = "";
  }
}

const chartMeta = {
  tps: { label: "TPS", unit: " tx/s", digits: 0 },
  solPriceUsd: { label: "SOL price", currency: true, digits: 2 },
  tvlUsd: { label: "TVL", currency: true, digits: 2 },
};

function renderChart() {
  const key = state.chart;
  const meta = chartMeta[key];
  const values = state.history
    .map(row => ({ date: new Date(row.generatedAt), value: Number(row[key]) }))
    .filter(row => !Number.isNaN(row.date.getTime()) && Number.isFinite(row.value));
  const container = $("#history-chart");
  if (!values.length) {
    container.innerHTML = `<svg viewBox="0 0 900 240"><text class="empty-chart" x="450" y="122">History begins with this observation</text></svg>`;
    setText("#chart-current", "—"); setText("#chart-delta", "Waiting for history");
    return;
  }
  const display = value => formatNumber(value, { currency: meta.currency, digits: meta.digits, unit: meta.unit || "" });
  const latest = values.at(-1).value;
  const first = values[0].value;
  const delta = first ? (latest - first) / Math.abs(first) * 100 : 0;
  setText("#chart-current", display(latest));
  setText("#chart-delta", values.length > 1 ? `${formatPct(delta)} across visible history` : "Baseline observation captured");

  if (values.length === 1) {
    container.innerHTML = `<svg viewBox="0 0 900 240" preserveAspectRatio="none" aria-label="${esc(meta.label)} baseline observation"><line class="grid-line" x1="0" y1="120" x2="900" y2="120" stroke-dasharray="6 8"/><circle cx="450" cy="120" r="6" fill="#06100e" stroke="#42f5b3" stroke-width="3"/><text class="empty-chart" x="450" y="94">Baseline captured · trend activates on next observation</text></svg>`;
    setText("#axis-start", values[0].date.toLocaleDateString(undefined, { month: "short", day: "numeric" }));
    setText("#axis-mid", "Baseline");
    const table = $("#chart-data-table");
    table.innerHTML = `<table><thead><tr><th>Observed</th><th>${esc(meta.label)}</th></tr></thead><tbody><tr><td>${esc(values[0].date.toLocaleString())}</td><td>${esc(display(values[0].value))}</td></tr></tbody></table>`;
    return;
  }

  const width = 900, height = 240, padX = 8, padY = 24;
  let min = Math.min(...values.map(row => row.value));
  let max = Math.max(...values.map(row => row.value));
  const span = max - min || Math.max(Math.abs(max) * 0.08, 1);
  min -= span * 0.15; max += span * 0.15;
  const points = values.map((row, index) => {
    const x = values.length === 1 ? width / 2 : padX + index / (values.length - 1) * (width - padX * 2);
    const y = padY + (max - row.value) / (max - min) * (height - padY * 2);
    return { ...row, x, y };
  });
  const line = points.map((point, index) => `${index ? "L" : "M"}${point.x.toFixed(2)},${point.y.toFixed(2)}`).join(" ");
  const area = `${line} L${points.at(-1).x},${height} L${points[0].x},${height} Z`;
  const grid = [0.2, 0.5, 0.8].map(ratio => `<line class="grid-line" x1="0" y1="${height * ratio}" x2="${width}" y2="${height * ratio}"/>`).join("");
  const circles = points.map(point => `<circle class="point" cx="${point.x}" cy="${point.y}" r="4"><title>${esc(point.date.toLocaleString())}: ${esc(display(point.value))}</title></circle>`).join("");
  container.innerHTML = `<svg viewBox="0 0 ${width} ${height}" preserveAspectRatio="none" aria-label="${esc(meta.label)} history"><defs><linearGradient id="chartGradient" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#42f5b3" stop-opacity=".24"/><stop offset="1" stop-color="#42f5b3" stop-opacity="0"/></linearGradient></defs>${grid}<path class="area" d="${area}"/><path class="line" d="${line}"/>${circles}</svg>`;
  setText("#axis-start", values[0].date.toLocaleDateString(undefined, { month: "short", day: "numeric" }));
  setText("#axis-mid", values[Math.floor(values.length / 2)].date.toLocaleDateString(undefined, { month: "short", day: "numeric" }));

  const table = $("#chart-data-table");
  table.innerHTML = `<table><thead><tr><th>Observed</th><th>${esc(meta.label)}</th></tr></thead><tbody>${values.slice(-24).map(row => `<tr><td>${esc(row.date.toLocaleString())}</td><td>${esc(display(row.value))}</td></tr>`).join("")}</tbody></table>`;
}

function renderMeta(snapshot) {
  setText("#generated-at", relativeTime(snapshot.generatedAt));
  setText("#coverage-label", `${snapshot.coverage?.successfulSources ?? 0} / ${snapshot.coverage?.totalSources ?? 0} sources`);
  const ageMinutes = (Date.now() - new Date(snapshot.generatedAt).getTime()) / 60000;
  setText("#live-label", ageMinutes <= 90 ? "Live observation" : "Stale observation");
}

function render() {
  if (!state.snapshot) return;
  renderMeta(state.snapshot);
  renderHealth(state.snapshot);
  renderSignals(state.snapshot);
  renderEconomics(state.snapshot);
  renderValidators(state.snapshot);
  renderAnomalies(state.snapshot);
  renderSources(state.snapshot);
  renderChart();
}

async function loadData({ announce = false } = {}) {
  const refresh = $("#refresh-button");
  refresh?.classList.add("is-loading");
  refresh?.setAttribute("aria-busy", "true");
  try {
    const stamp = Date.now();
    const [snapshotResponse, historyResponse] = await Promise.all([
      fetch(`data/latest.json?v=${stamp}`, { cache: "no-store" }),
      fetch(`data/history.json?v=${stamp}`, { cache: "no-store" }),
    ]);
    if (!snapshotResponse.ok) throw new Error(`snapshot HTTP ${snapshotResponse.status}`);
    state.snapshot = await snapshotResponse.json();
    state.history = historyResponse.ok ? await historyResponse.json() : [];
    render();
    if (announce) setText("#live-label", "Observation refreshed");
  } catch (error) {
    console.error(error);
    setText("#live-label", "Data unavailable");
    const errorBox = $("#source-errors");
    errorBox.hidden = false;
    errorBox.textContent = `Dashboard data could not be loaded: ${error.message}`;
  } finally {
    refresh?.classList.remove("is-loading");
    refresh?.removeAttribute("aria-busy");
  }
}

function bindControls() {
  $("#refresh-button")?.addEventListener("click", () => loadData({ announce: true }));
  $$("[data-chart]").forEach(button => button.addEventListener("click", () => {
    $$("[data-chart]").forEach(item => item.classList.toggle("is-active", item === button));
    state.chart = button.dataset.chart;
    renderChart();
  }));
  $$("[data-view]").forEach(button => button.addEventListener("click", () => {
    const view = button.dataset.view;
    $$("[data-view]").forEach(item => item.classList.toggle("is-active", item === button));
    $$("[data-section]").forEach(section => {
      const views = section.dataset.section.split(/\s+/);
      section.classList.toggle("is-hidden", view !== "all" && !views.includes(view));
    });
    document.querySelector("main")?.scrollIntoView({ behavior: "smooth", block: "start" });
  }));
}

bindControls();
loadData();
setInterval(() => loadData(), 5 * 60 * 1000);
