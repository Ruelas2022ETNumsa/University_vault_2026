"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => SetmovePlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian2 = require("obsidian");

// src/modal-detector.ts
var SETTINGS_MODAL_SELECTORS = Object.freeze({
  modal: ".modal.mod-settings",
  modalContainer: ".modal-container",
  closeButton: ".modal-close-button",
  sidebar: ".vertical-tab-header",
  content: ".vertical-tab-content-container",
  anyModal: ".modal",
  searchInput: "input[type='search'], input[type='text'], input:not([type])"
});
var SettingsModalLifecycle = class {
  constructor(callbacks) {
    this.callbacks = callbacks;
    this.observers = /* @__PURE__ */ new Map();
    this.attached = /* @__PURE__ */ new Map();
  }
  trackDocument(doc) {
    if (this.observers.has(doc)) {
      this.scanDocument(doc);
      return;
    }
    const root = doc.body ?? doc.documentElement;
    if (!root) {
      return;
    }
    const ViewMutationObserver = doc.defaultView?.MutationObserver ?? MutationObserver;
    const observer = new ViewMutationObserver(() => {
      this.scanDocument(doc);
    });
    observer.observe(root, {
      childList: true,
      subtree: true,
      characterData: true,
      attributes: true,
      attributeFilter: ["class", "placeholder", "type"]
    });
    this.observers.set(doc, observer);
    this.scanDocument(doc);
  }
  untrackDocument(doc) {
    const observer = this.observers.get(doc);
    observer?.disconnect();
    this.observers.delete(doc);
    for (const [modalEl, record] of this.attached) {
      if (record.match.doc === doc) {
        this.detachModal(modalEl, record);
      }
    }
  }
  stop() {
    for (const observer of this.observers.values()) {
      observer.disconnect();
    }
    this.observers.clear();
    for (const [modalEl, record] of this.attached) {
      this.detachModal(modalEl, record);
    }
  }
  scanDocument(doc) {
    const matches = findSettingsModals(doc);
    const activeModals = new Set(matches.map((match) => match.modalEl));
    for (const match of matches) {
      if (this.attached.has(match.modalEl)) {
        continue;
      }
      const cleanup = this.callbacks.onAttach(match) ?? void 0;
      this.attached.set(match.modalEl, { cleanup, match });
    }
    for (const [modalEl, record] of this.attached) {
      if (record.match.doc !== doc) {
        continue;
      }
      if (!modalEl.isConnected || !activeModals.has(modalEl)) {
        this.detachModal(modalEl, record);
      }
    }
  }
  detachModal(modalEl, record) {
    this.attached.delete(modalEl);
    record.cleanup?.();
    this.callbacks.onDetach?.(record.match);
  }
};
function registerSettingsModalLifecycle(workspace, callbacks) {
  const lifecycle = new SettingsModalLifecycle(callbacks);
  lifecycle.trackDocument(window.document);
  const openRef = workspace.on("window-open", (workspaceWindow, popoutWindow) => {
    lifecycle.trackDocument(workspaceWindow.doc ?? popoutWindow.document);
  });
  const closeRef = workspace.on(
    "window-close",
    (workspaceWindow, popoutWindow) => {
      lifecycle.untrackDocument(workspaceWindow.doc ?? popoutWindow.document);
    }
  );
  return () => {
    workspace.offref(openRef);
    workspace.offref(closeRef);
    lifecycle.stop();
  };
}
function findSettingsModals(root) {
  const matches = [];
  const modalEls = Array.from(
    root.querySelectorAll(SETTINGS_MODAL_SELECTORS.anyModal)
  );
  for (const modalEl of modalEls) {
    const match = toEnhancedModalMatch(modalEl);
    if (match) {
      matches.push(match);
    }
  }
  return matches;
}
function toSettingsModalMatch(element) {
  if (!isHTMLElement(element)) {
    return null;
  }
  if (!element.matches(SETTINGS_MODAL_SELECTORS.modal)) {
    return null;
  }
  const containerEl = element.closest(
    SETTINGS_MODAL_SELECTORS.modalContainer
  );
  if (!containerEl) {
    return null;
  }
  const contentEl = element.querySelector(SETTINGS_MODAL_SELECTORS.content);
  const hasRequiredStructure = isHTMLElement(element.querySelector(SETTINGS_MODAL_SELECTORS.sidebar)) && isHTMLElement(contentEl) && isHTMLElement(element.querySelector(SETTINGS_MODAL_SELECTORS.closeButton));
  if (!hasRequiredStructure) {
    return null;
  }
  const doc = element.ownerDocument;
  const win = doc.defaultView;
  if (!win) {
    return null;
  }
  return {
    modalEl: element,
    containerEl,
    contentEl,
    doc,
    kind: "settings",
    win
  };
}
function toEnhancedModalMatch(element) {
  return toSettingsModalMatch(element) ?? toCatalogModalMatch(element);
}
function toCatalogModalMatch(element) {
  if (!isHTMLElement(element)) {
    return null;
  }
  if (!element.matches(SETTINGS_MODAL_SELECTORS.anyModal)) {
    return null;
  }
  if (element.matches(SETTINGS_MODAL_SELECTORS.modal)) {
    return null;
  }
  const containerEl = element.closest(
    SETTINGS_MODAL_SELECTORS.modalContainer
  );
  if (!containerEl) {
    return null;
  }
  if (!isHTMLElement(element.querySelector(SETTINGS_MODAL_SELECTORS.closeButton))) {
    return null;
  }
  if (!looksLikeCatalogBrowser(element)) {
    return null;
  }
  const doc = element.ownerDocument;
  const win = doc.defaultView;
  if (!win) {
    return null;
  }
  return {
    modalEl: element,
    containerEl,
    contentEl: null,
    doc,
    kind: "catalog",
    win
  };
}
function looksLikeCatalogBrowser(modalEl) {
  const text = modalEl.textContent ?? "";
  const hasCatalogCount = /\bShowing\s+[\d,]+\s+(themes|plugins)\b/i.test(text);
  const hasCatalogControls = /\bShow installed only\b/i.test(text) && (/\bLight themes only\b/i.test(text) || /\bthemes\b/i.test(text) || /\bplugins\b/i.test(text));
  const hasCatalogResults = Boolean(
    modalEl.querySelector(
      [
        ".community-modal-search-results",
        ".community-item",
        ".community-item-name",
        ".theme-card",
        ".theme-list"
      ].join(", ")
    )
  );
  const hasSearchInput = Array.from(
    modalEl.querySelectorAll(SETTINGS_MODAL_SELECTORS.searchInput)
  ).some((input) => {
    const placeholder = input.getAttribute("placeholder") ?? "";
    return /filter|search community plugins|search/i.test(placeholder);
  });
  return hasSearchInput && (hasCatalogCount || hasCatalogControls || hasCatalogResults);
}
function isHTMLElement(value) {
  if (typeof value !== "object" || value === null || !("ownerDocument" in value) || !("nodeType" in value) || value.nodeType !== Node.ELEMENT_NODE) {
    return false;
  }
  const element = value;
  const view = element.ownerDocument.defaultView;
  return Boolean(view && value instanceof view.HTMLElement);
}

// src/geometry.ts
var MIN_MODAL_WIDTH = 640;
var MIN_MODAL_HEIGHT = 420;
var HALF_HEIGHT_RATIO = 0.5;
function measureHostBounds(viewport) {
  return {
    x: 0,
    y: 0,
    width: sanitizePositiveNumber(viewport.innerWidth) ?? 0,
    height: sanitizePositiveNumber(viewport.innerHeight) ?? 0
  };
}
function getMinimumModalSize(hostBounds) {
  return {
    width: Math.min(MIN_MODAL_WIDTH, Math.max(hostBounds.width, 0)),
    height: Math.min(MIN_MODAL_HEIGHT, Math.max(hostBounds.height, 0))
  };
}
function isUsableHostBounds(hostBounds) {
  return Number.isFinite(hostBounds.x) && Number.isFinite(hostBounds.y) && hostBounds.width > 0 && hostBounds.height > 0;
}
function clampModalRect(rect, hostBounds) {
  const normalizedHost = normalizeHostBounds(hostBounds);
  const minimumSize = getMinimumModalSize(normalizedHost);
  const width = clampDimension(rect.width, normalizedHost.width, minimumSize.width);
  const height = clampDimension(rect.height, normalizedHost.height, minimumSize.height);
  const maxX = normalizedHost.x + normalizedHost.width - width;
  const maxY = normalizedHost.y + normalizedHost.height - height;
  return {
    x: clampNumber(rect.x, normalizedHost.x, maxX),
    y: clampNumber(rect.y, normalizedHost.y, maxY),
    width,
    height
  };
}
function getCenteredRect(rect, hostBounds) {
  const normalizedHost = normalizeHostBounds(hostBounds);
  const clampedRect = clampModalRect(
    {
      x: normalizedHost.x,
      y: normalizedHost.y,
      width: rect.width,
      height: rect.height
    },
    normalizedHost
  );
  return {
    ...clampedRect,
    x: normalizedHost.x + (normalizedHost.width - clampedRect.width) / 2,
    y: normalizedHost.y + (normalizedHost.height - clampedRect.height) / 2
  };
}
function applyGeometryPreset(preset, currentRect, hostBounds) {
  const normalizedHost = normalizeHostBounds(hostBounds);
  const minimumSize = getMinimumModalSize(normalizedHost);
  if (preset === "center") {
    return getCenteredRect(currentRect, normalizedHost);
  }
  if (preset === "bottom-half") {
    const height = clampDimension(
      normalizedHost.height,
      normalizedHost.height * HALF_HEIGHT_RATIO,
      minimumSize.height
    );
    return clampModalRect(
      {
        x: normalizedHost.x,
        y: normalizedHost.y + normalizedHost.height - height,
        width: normalizedHost.width,
        height
      },
      normalizedHost
    );
  }
  const width = minimumSize.width;
  return clampModalRect(
    {
      x: preset === "dock-right" ? normalizedHost.x + normalizedHost.width - width : normalizedHost.x,
      y: normalizedHost.y,
      width,
      height: normalizedHost.height
    },
    normalizedHost
  );
}
function getRestoredGeometry(geometry, hostBounds) {
  if (geometry === null) {
    return null;
  }
  if (!isUsableHostBounds(hostBounds)) {
    return null;
  }
  if (!isPersistedGeometryCompatible(geometry) || geometry.width < MIN_MODAL_WIDTH || geometry.height < MIN_MODAL_HEIGHT) {
    return null;
  }
  const maximumReasonableWidth = Math.max(
    geometry.lastAppliedBounds.width,
    hostBounds.width
  );
  const maximumReasonableHeight = Math.max(
    geometry.lastAppliedBounds.height,
    hostBounds.height
  );
  if (geometry.width > maximumReasonableWidth || geometry.height > maximumReasonableHeight) {
    return null;
  }
  return clampModalRect(geometry, hostBounds);
}
function isPersistedGeometryCompatible(geometry) {
  return isFiniteRect(geometry) && geometry.lastAppliedBounds.width > 0 && geometry.lastAppliedBounds.height > 0 && geometry.x >= 0 && geometry.y >= 0;
}
function isFiniteRect(rect) {
  return Number.isFinite(rect.x) && Number.isFinite(rect.y) && Number.isFinite(rect.width) && Number.isFinite(rect.height);
}
function normalizeHostBounds(hostBounds) {
  return {
    x: Number.isFinite(hostBounds.x) ? hostBounds.x : 0,
    y: Number.isFinite(hostBounds.y) ? hostBounds.y : 0,
    width: sanitizePositiveNumber(hostBounds.width) ?? 0,
    height: sanitizePositiveNumber(hostBounds.height) ?? 0
  };
}
function clampDimension(value, available, minimum) {
  const safeAvailable = sanitizePositiveNumber(available) ?? 0;
  const safeMinimum = Math.min(sanitizePositiveNumber(minimum) ?? 0, safeAvailable);
  const safeValue = sanitizePositiveNumber(value) ?? safeMinimum;
  if (safeAvailable === 0) {
    return 0;
  }
  return clampNumber(safeValue, safeMinimum, safeAvailable);
}
function clampNumber(value, minimum, maximum) {
  if (maximum < minimum) {
    return minimum;
  }
  return Math.min(Math.max(value, minimum), maximum);
}
function sanitizePositiveNumber(value) {
  return Number.isFinite(value) && value > 0 ? value : null;
}

// src/drag-resize.ts
function createDragResizeSession(options) {
  let active = null;
  const onPointerDown = (event) => {
    if (!options.isEnabled() || event.button !== 0) {
      return;
    }
    const target = event.target;
    if (!(target instanceof options.modalEl.ownerDocument.defaultView.Element)) {
      return;
    }
    if (options.canStart && !options.canStart(target)) {
      return;
    }
    if (options.mode === "resize" && !target.closest("[data-setmove-role='resize-handle']")) {
      return;
    }
    active = {
      pointerId: event.pointerId,
      startX: event.clientX,
      startY: event.clientY,
      startRect: options.getCurrentRect()
    };
    options.handleEl.setPointerCapture?.(event.pointerId);
    options.modalEl.classList.add("setmove--is-interacting");
    options.modalEl.classList.add(`setmove--is-${options.mode === "drag" ? "dragging" : "resizing"}`);
    options.modalEl.setCssStyles({ userSelect: "none" });
    options.onStateChange?.(true);
    event.preventDefault();
  };
  const onPointerMove = (event) => {
    if (!active || event.pointerId !== active.pointerId) {
      return;
    }
    const deltaX = event.clientX - active.startX;
    const deltaY = event.clientY - active.startY;
    const nextRect = options.mode === "drag" ? {
      ...active.startRect,
      x: active.startRect.x + deltaX,
      y: active.startRect.y + deltaY
    } : {
      ...active.startRect,
      width: active.startRect.width + deltaX,
      height: active.startRect.height + deltaY
    };
    const clamped = clampModalRect(nextRect, options.getHostBounds());
    options.onUpdate(clamped);
  };
  const onPointerUp = (event) => {
    if (!active || event.pointerId !== active.pointerId) {
      return;
    }
    const deltaX = event.clientX - active.startX;
    const deltaY = event.clientY - active.startY;
    const nextRect = options.mode === "drag" ? {
      ...active.startRect,
      x: active.startRect.x + deltaX,
      y: active.startRect.y + deltaY
    } : {
      ...active.startRect,
      width: active.startRect.width + deltaX,
      height: active.startRect.height + deltaY
    };
    const clamped = clampModalRect(nextRect, options.getHostBounds());
    options.onUpdate(clamped);
    options.onCommit?.(clamped);
    finishInteraction(event.pointerId);
  };
  const onPointerCancel = (event) => {
    if (!active || event.pointerId !== active.pointerId) {
      return;
    }
    options.onUpdate(active.startRect);
    finishInteraction(event.pointerId);
  };
  const finishInteraction = (pointerId) => {
    options.handleEl.releasePointerCapture?.(pointerId);
    options.modalEl.classList.remove("setmove--is-interacting");
    options.modalEl.classList.remove("setmove--is-dragging", "setmove--is-resizing");
    options.modalEl.setCssStyles({ userSelect: "" });
    options.onStateChange?.(false);
    active = null;
  };
  options.handleEl.addEventListener("pointerdown", onPointerDown);
  options.handleEl.addEventListener("pointermove", onPointerMove);
  options.handleEl.addEventListener("pointerup", onPointerUp);
  options.handleEl.addEventListener("pointercancel", onPointerCancel);
  return {
    destroy() {
      if (active) {
        finishInteraction(active.pointerId);
      }
      options.handleEl.removeEventListener("pointerdown", onPointerDown);
      options.handleEl.removeEventListener("pointermove", onPointerMove);
      options.handleEl.removeEventListener("pointerup", onPointerUp);
      options.handleEl.removeEventListener("pointercancel", onPointerCancel);
    }
  };
}

// src/modal-enhancer.ts
var ENHANCED_CLASS = "setmove--settings-modal";
var HANDLE_CLASS = "setmove--drag-handle";
var RESIZE_HANDLE_CLASS = "setmove--resize-handle";
var CONTENT_CLASS = "setmove--settings-content";
var NON_DRAGGABLE_SELECTOR = [
  "input",
  "textarea",
  "select",
  "button",
  "a[href]",
  "[contenteditable='true']",
  ".setting-item",
  ".setting-item-control",
  ".vertical-tab-nav-item",
  ".clickable-icon",
  ".slider",
  ".dropdown",
  ".pcr-app",
  "[data-setmove-role='resize-handle']",
  "[data-setmove-role='preset-control']"
].join(", ");
var CATALOG_NON_DRAGGABLE_SELECTOR = [
  ".community-item",
  ".community-modal-search-results",
  ".community-modal-details",
  ".theme-card",
  ".theme-list"
].join(", ");
var ENHANCEABLE_MODAL_SELECTOR = ".modal.mod-settings, .modal.setmove--settings-modal";
var SVG_NAMESPACE = "http://www.w3.org/2000/svg";
var PRESET_ICON_COLOR = "currentColor";
var ICON_DEFINITIONS = {
  center: {
    fillRects: [{ x: 8, y: 7, width: 8, height: 10 }],
    paths: ["M4 5h16v14H4z"]
  },
  left: {
    fillRects: [{ x: 4, y: 5, width: 5, height: 14 }],
    paths: ["M4 5h16v14H4z", "M9 5v14"]
  },
  right: {
    fillRects: [{ x: 15, y: 5, width: 5, height: 14 }],
    paths: ["M4 5h16v14H4z", "M15 5v14"]
  },
  reset: {
    fillPaths: [
      "M6.7 7.4A8.6 8.6 0 1 1 5 16.6l2.3-1.3a5.9 5.9 0 1 0 1-6.3l2.1 2.1H4.2V4.9z"
    ]
  }
};
var VISIBLE_PRESET_CONTROLS_PLACEMENTS = /* @__PURE__ */ new Set([
  "bottom-right-horizontal"
]);
var ENHANCER_BY_MODAL = /* @__PURE__ */ new WeakMap();
var SettingsModalEnhancer = class {
  constructor(match, options) {
    this.onWindowResize = () => {
      this.applyEnabledState();
      if (!this.enabled || this.currentRect === null) {
        return;
      }
      this.currentRect = clampModalRect(this.currentRect, this.getHostBounds());
      this.applyRect(this.currentRect);
    };
    this.enabled = true;
    this.requestedEnabled = true;
    this.currentRect = null;
    this.modalEl = match.modalEl;
    this.containerEl = match.containerEl;
    this.doc = match.doc;
    this.kind = match.kind;
    this.win = match.win;
    this.settings = { ...options.settings };
    this.onGeometryPersist = options.onGeometryPersist;
    this.onResetGeometry = options.onResetGeometry;
    this.contentEl = match.contentEl;
    this.dragHandleEl = this.createDragHandle();
    this.defaultSize = this.measureModalRect();
    this.presetControlsEls = [
      this.createPresetControls("top-right-horizontal"),
      this.createPresetControls("bottom-right-horizontal"),
      this.createPresetControls("bottom-left-vertical")
    ];
    this.resizeHandleEl = this.createResizeHandle();
    this.styleSnapshot = this.captureInlineStyles();
    this.dragSession = this.createSession("drag", this.dragHandleEl);
    this.resizeSession = this.createSession("resize", this.resizeHandleEl);
    this.attach();
  }
  center() {
    const nextRect = getCenteredRect(this.getCurrentSize(), this.getHostBounds());
    this.currentRect = nextRect;
    this.applyRect(nextRect);
    return nextRect;
  }
  reset() {
    const nextRect = getCenteredRect(this.defaultSize, this.getHostBounds());
    this.currentRect = nextRect;
    this.applyRect(nextRect);
    return nextRect;
  }
  dockLeft() {
    return this.applyPreset("dock-left");
  }
  dockRight() {
    return this.applyPreset("dock-right");
  }
  async persistCurrentGeometry() {
    if (this.currentRect) {
      await this.persistGeometry(this.currentRect);
    }
  }
  toggleEnabled(force) {
    this.requestedEnabled = force ?? !this.requestedEnabled;
    this.applyEnabledState();
    return this.enabled;
  }
  updateSettings(settings) {
    this.settings = {
      ...this.settings,
      ...settings
    };
    this.toggleEnabled(this.enabled);
  }
  destroy() {
    this.win.removeEventListener("resize", this.onWindowResize);
    this.dragSession.destroy();
    this.resizeSession.destroy();
    ENHANCER_BY_MODAL.delete(this.modalEl);
    this.dragHandleEl.remove();
    for (const controlsEl of this.presetControlsEls) {
      controlsEl.remove();
    }
    this.resizeHandleEl.remove();
    this.modalEl.classList.remove(ENHANCED_CLASS, `${ENHANCED_CLASS}--disabled`);
    if (this.contentEl) {
      this.contentEl.classList.remove(CONTENT_CLASS);
      this.contentEl.setCssStyles({
        minHeight: "",
        overflow: ""
      });
    }
    this.restoreInlineStyles();
  }
  attach() {
    this.modalEl.classList.add(ENHANCED_CLASS);
    if (this.contentEl) {
      this.contentEl.classList.add(CONTENT_CLASS);
      this.contentEl.setCssStyles({
        minHeight: "0",
        overflow: "auto"
      });
    }
    this.modalEl.prepend(this.dragHandleEl);
    this.modalEl.append(...this.presetControlsEls);
    this.modalEl.append(this.resizeHandleEl);
    this.currentRect = this.resolveInitialRect();
    this.applyRect(this.currentRect);
    this.toggleEnabled(true);
    this.win.addEventListener("resize", this.onWindowResize);
  }
  applyPreset(preset) {
    const nextRect = applyGeometryPreset(
      preset,
      this.getCurrentSize(),
      this.getHostBounds()
    );
    this.currentRect = nextRect;
    this.applyRect(nextRect);
    return nextRect;
  }
  applyRect(rect) {
    this.currentRect = rect;
    this.modalEl.setCssStyles({
      position: "fixed",
      left: `${rect.x}px`,
      top: `${rect.y}px`,
      width: `${rect.width}px`,
      height: `${rect.height}px`,
      maxWidth: "none",
      maxHeight: "none"
    });
  }
  resolveInitialRect() {
    if (this.settings.rememberGeometry) {
      const restored = getRestoredGeometry(this.settings.geometry, this.getHostBounds());
      if (restored) {
        return restored;
      }
    }
    return getCenteredRect(this.measureModalRect(), this.getHostBounds());
  }
  getCurrentSize() {
    return this.currentRect ?? this.measureModalRect();
  }
  getCurrentRect() {
    return this.currentRect ? { ...this.currentRect } : {
      ...this.measureModalRect(),
      x: this.modalEl.offsetLeft || 0,
      y: this.modalEl.offsetTop || 0
    };
  }
  measureModalRect() {
    const rect = this.modalEl.getBoundingClientRect();
    return {
      width: rect.width || this.modalEl.offsetWidth || 900,
      height: rect.height || this.modalEl.offsetHeight || 640
    };
  }
  getHostBounds() {
    return measureHostBounds(this.win);
  }
  createDragHandle() {
    const handle = this.doc.createElement("div");
    handle.className = HANDLE_CLASS;
    handle.dataset.setmoveRole = "drag-handle";
    handle.setAttribute("role", "presentation");
    return handle;
  }
  createPresetControls(placement) {
    const controls = this.doc.createElement("div");
    controls.className = `setmove--preset-controls setmove--preset-controls-${placement}`;
    controls.dataset.setmoveRole = "preset-controls";
    controls.dataset.setmovePlacement = placement;
    this.addPresetButton(controls, "Dock window left", "left", async () => {
      this.dockLeft();
      await this.persistCurrentGeometry();
    });
    this.addPresetButton(controls, "Dock window right", "right", async () => {
      this.dockRight();
      await this.persistCurrentGeometry();
    });
    this.addPresetButton(controls, "Reset window geometry", "reset", async () => {
      if (this.onResetGeometry) {
        await this.onResetGeometry();
        return;
      }
      this.reset();
      await this.persistCurrentGeometry();
    });
    return controls;
  }
  addPresetButton(controls, label, icon, onClick) {
    const button = this.doc.createElement("button");
    button.type = "button";
    button.className = "setmove--preset-control";
    button.dataset.setmoveRole = "preset-control";
    button.setAttribute("aria-label", label);
    button.append(this.createIcon(icon));
    button.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      void onClick();
    });
    controls.append(button);
  }
  createIcon(icon) {
    const iconDefinition = ICON_DEFINITIONS[icon];
    const svg = this.doc.createElementNS(SVG_NAMESPACE, "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("aria-hidden", "true");
    for (const rectData of iconDefinition.fillRects ?? []) {
      const rect = this.doc.createElementNS(SVG_NAMESPACE, "rect");
      rect.setAttribute("x", String(rectData.x));
      rect.setAttribute("y", String(rectData.y));
      rect.setAttribute("width", String(rectData.width));
      rect.setAttribute("height", String(rectData.height));
      rect.setAttribute("rx", "0.75");
      rect.setAttribute("fill", PRESET_ICON_COLOR);
      rect.setAttribute("opacity", "0.85");
      svg.append(rect);
    }
    for (const pathData of iconDefinition.fillPaths ?? []) {
      const path = this.doc.createElementNS(SVG_NAMESPACE, "path");
      path.setAttribute("d", pathData);
      path.setAttribute("fill", PRESET_ICON_COLOR);
      svg.append(path);
    }
    for (const pathData of iconDefinition.paths ?? []) {
      const path = this.doc.createElementNS(SVG_NAMESPACE, "path");
      path.setAttribute("d", pathData);
      path.setAttribute("fill", "none");
      path.setAttribute("stroke", PRESET_ICON_COLOR);
      path.setAttribute("stroke-width", "1.8");
      path.setAttribute("stroke-linecap", "round");
      path.setAttribute("stroke-linejoin", "round");
      svg.append(path);
    }
    return svg;
  }
  createResizeHandle() {
    const handle = this.doc.createElement("button");
    handle.type = "button";
    handle.className = RESIZE_HANDLE_CLASS;
    handle.dataset.setmoveRole = "resize-handle";
    handle.setAttribute("aria-label", "Resize settings window");
    return handle;
  }
  applyEnabledState() {
    this.enabled = this.requestedEnabled && this.isWideEnoughForEnhancement();
    this.modalEl.classList.toggle(`${ENHANCED_CLASS}--disabled`, !this.enabled);
    this.syncHandleState(
      this.dragHandleEl,
      this.enabled && this.settings.movable
    );
    this.syncHandleState(
      this.resizeHandleEl,
      this.enabled && this.settings.resizable
    );
    for (const controlsEl of this.presetControlsEls) {
      const isVisible = this.enabled && VISIBLE_PRESET_CONTROLS_PLACEMENTS.has(
        controlsEl.dataset.setmovePlacement
      );
      controlsEl.hidden = !isVisible;
    }
    if (this.enabled) {
      this.currentRect = this.currentRect ?? this.resolveInitialRect();
      this.applyRect(this.currentRect);
    } else {
      this.restoreInlineStyles();
    }
  }
  isWideEnoughForEnhancement() {
    return !this.settings.disableOnNarrowWindows || this.win.innerWidth >= this.settings.narrowWindowThreshold;
  }
  syncHandleState(handleEl, isVisible) {
    handleEl.hidden = !isVisible;
    handleEl.classList.toggle("setmove--control-disabled", !isVisible);
  }
  createSession(mode, handleEl) {
    const interactionEl = mode === "drag" ? this.modalEl : handleEl;
    return createDragResizeSession({
      isEnabled: () => this.enabled && (mode === "drag" ? this.settings.movable : this.settings.resizable),
      handleEl: interactionEl,
      modalEl: this.modalEl,
      mode,
      canStart: (target) => mode === "drag" ? this.canStartDragFrom(target) : this.canStartResizeFrom(target),
      getCurrentRect: () => this.getCurrentRect(),
      getHostBounds: () => this.getHostBounds(),
      onUpdate: (rect) => {
        this.currentRect = rect;
        this.applyRect(rect);
      },
      onCommit: (rect) => {
        this.currentRect = rect;
        void this.persistGeometry(rect);
      }
    });
  }
  canStartDragFrom(target) {
    if (target.closest("[data-setmove-role='drag-handle']")) {
      return true;
    }
    if (target.closest(NON_DRAGGABLE_SELECTOR)) {
      return false;
    }
    if (this.kind === "catalog" && target.closest(CATALOG_NON_DRAGGABLE_SELECTOR)) {
      return false;
    }
    return target.closest(ENHANCEABLE_MODAL_SELECTOR) === this.modalEl;
  }
  canStartResizeFrom(target) {
    return Boolean(target.closest("[data-setmove-role='resize-handle']"));
  }
  async persistGeometry(rect) {
    if (!this.settings.rememberGeometry || !this.onGeometryPersist) {
      return;
    }
    await this.onGeometryPersist({
      schemaVersion: 1,
      x: rect.x,
      y: rect.y,
      width: rect.width,
      height: rect.height,
      lastAppliedBounds: this.getHostBounds()
    });
  }
  captureInlineStyles() {
    return {
      height: this.modalEl.style.height,
      left: this.modalEl.style.left,
      maxHeight: this.modalEl.style.maxHeight,
      maxWidth: this.modalEl.style.maxWidth,
      position: this.modalEl.style.position,
      top: this.modalEl.style.top,
      width: this.modalEl.style.width
    };
  }
  restoreInlineStyles() {
    this.modalEl.setCssStyles({
      height: this.styleSnapshot.height,
      left: this.styleSnapshot.left,
      maxHeight: this.styleSnapshot.maxHeight,
      maxWidth: this.styleSnapshot.maxWidth,
      position: this.styleSnapshot.position,
      top: this.styleSnapshot.top,
      width: this.styleSnapshot.width
    });
  }
};
function enhanceSettingsModal(match, options) {
  const existing = ENHANCER_BY_MODAL.get(match.modalEl);
  if (existing) {
    existing.updateSettings(options.settings);
    return existing;
  }
  const enhancer = new SettingsModalEnhancer(match, options);
  ENHANCER_BY_MODAL.set(match.modalEl, enhancer);
  return enhancer;
}

// src/settings-tab.ts
var import_obsidian = require("obsidian");
var SetmoveSettingTab = class extends import_obsidian.PluginSettingTab {
  constructor(plugin) {
    super(plugin.app, plugin);
    this.pluginRef = plugin;
  }
  display() {
    const { containerEl } = this;
    const plugin = this.pluginRef;
    containerEl.empty();
    new import_obsidian.Setting(containerEl).setName("Window behavior").setHeading();
    containerEl.createEl("p", {
      cls: "setmove--settings-description",
      text: "Move and resize supported app dialogs so you can adjust options while keeping your notes and workspace visible."
    });
    new import_obsidian.Setting(containerEl).setName("Enable movable dialogs").setDesc("Allow supported app dialogs to be dragged from safe empty space.").addToggle(
      (toggle) => toggle.setValue(plugin.settings.movable).onChange(async (value) => {
        await plugin.updateSettings({ movable: value });
      })
    );
    new import_obsidian.Setting(containerEl).setName("Enable resizable dialogs").setDesc("Allow supported app dialogs to be resized from the bottom-right handle.").addToggle(
      (toggle) => toggle.setValue(plugin.settings.resizable).onChange(async (value) => {
        await plugin.updateSettings({ resizable: value });
      })
    );
    new import_obsidian.Setting(containerEl).setName("Remember window geometry").setDesc("Persist the last valid settings position and size for this vault.").addToggle(
      (toggle) => toggle.setValue(plugin.settings.rememberGeometry).onChange(async (value) => {
        await plugin.updateSettings({ rememberGeometry: value });
      })
    );
    new import_obsidian.Setting(containerEl).setName("Disable in narrow layouts").setDesc("Keep the plugin conservative in cramped desktop layouts.").addToggle(
      (toggle) => toggle.setValue(plugin.settings.disableOnNarrowWindows).onChange(async (value) => {
        await plugin.updateSettings({ disableOnNarrowWindows: value });
      })
    );
    new import_obsidian.Setting(containerEl).setName("Disable on mobile").setDesc("Leave mobile behavior as a no-op for this release.").addToggle(
      (toggle) => toggle.setValue(plugin.settings.disableOnMobile).onChange(async (value) => {
        await plugin.updateSettings({ disableOnMobile: value });
      })
    );
    new import_obsidian.Setting(containerEl).setName("Reset saved geometry").setDesc("Forget the saved position and size so settings reopens with the default layout.").addButton(
      (button) => button.setButtonText("Reset").onClick(async () => {
        await plugin.resetSavedGeometryCommand();
      })
    );
  }
};

// src/settings.ts
var SETTINGS_SCHEMA_VERSION = 1;
var GEOMETRY_SCHEMA_VERSION = 1;
var DEFAULT_NARROW_WINDOW_THRESHOLD = 720;
var DEFAULT_SETTINGS = Object.freeze({
  schemaVersion: SETTINGS_SCHEMA_VERSION,
  movable: true,
  resizable: true,
  rememberGeometry: true,
  showPresetControls: true,
  disableOnMobile: true,
  disableOnNarrowWindows: true,
  narrowWindowThreshold: DEFAULT_NARROW_WINDOW_THRESHOLD,
  geometry: null
});
function migrateSettingsData(data) {
  if (!isRecord(data)) {
    return cloneSettings(DEFAULT_SETTINGS);
  }
  return {
    schemaVersion: SETTINGS_SCHEMA_VERSION,
    movable: readBoolean(data.movable, DEFAULT_SETTINGS.movable),
    resizable: readBoolean(data.resizable, DEFAULT_SETTINGS.resizable),
    rememberGeometry: readBoolean(
      data.rememberGeometry,
      DEFAULT_SETTINGS.rememberGeometry
    ),
    showPresetControls: readBoolean(
      data.showPresetControls,
      DEFAULT_SETTINGS.showPresetControls
    ),
    disableOnMobile: readBoolean(
      data.disableOnMobile,
      DEFAULT_SETTINGS.disableOnMobile
    ),
    disableOnNarrowWindows: readBoolean(
      data.disableOnNarrowWindows,
      DEFAULT_SETTINGS.disableOnNarrowWindows
    ),
    narrowWindowThreshold: readPositiveNumber(
      data.narrowWindowThreshold,
      DEFAULT_SETTINGS.narrowWindowThreshold
    ),
    geometry: parseGeometry(data.geometry)
  };
}
async function loadSettings(dataStore) {
  return migrateSettingsData(await dataStore.loadData());
}
async function saveSettings(dataStore, settings) {
  await dataStore.saveData(serializeSettings(settings));
}
function clearSavedGeometry(settings) {
  return {
    ...serializeSettings(settings),
    geometry: null
  };
}
function serializeSettings(settings) {
  return {
    schemaVersion: SETTINGS_SCHEMA_VERSION,
    movable: settings.movable,
    resizable: settings.resizable,
    rememberGeometry: settings.rememberGeometry,
    showPresetControls: settings.showPresetControls,
    disableOnMobile: settings.disableOnMobile,
    disableOnNarrowWindows: settings.disableOnNarrowWindows,
    narrowWindowThreshold: settings.narrowWindowThreshold,
    geometry: settings.geometry ? cloneGeometry(settings.geometry) : null
  };
}
function parseGeometry(value) {
  if (!isRecord(value)) {
    return null;
  }
  const x = readFiniteNumber(value.x);
  const y = readFiniteNumber(value.y);
  const width = readPositiveNumber(value.width);
  const height = readPositiveNumber(value.height);
  const lastAppliedBounds = parseBoundsMetadata(value.lastAppliedBounds);
  if (x === null || y === null || width === null || height === null || lastAppliedBounds === null) {
    return null;
  }
  return {
    schemaVersion: GEOMETRY_SCHEMA_VERSION,
    x,
    y,
    width,
    height,
    lastAppliedBounds
  };
}
function parseBoundsMetadata(value) {
  if (!isRecord(value)) {
    return null;
  }
  const width = readPositiveNumber(value.width);
  const height = readPositiveNumber(value.height);
  if (width === null || height === null) {
    return null;
  }
  return { width, height };
}
function cloneSettings(settings) {
  return serializeSettings(settings);
}
function cloneGeometry(geometry) {
  return {
    schemaVersion: GEOMETRY_SCHEMA_VERSION,
    x: geometry.x,
    y: geometry.y,
    width: geometry.width,
    height: geometry.height,
    lastAppliedBounds: {
      width: geometry.lastAppliedBounds.width,
      height: geometry.lastAppliedBounds.height
    }
  };
}
function isRecord(value) {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}
function readBoolean(value, fallback) {
  return typeof value === "boolean" ? value : fallback;
}
function readFiniteNumber(value) {
  return typeof value === "number" && Number.isFinite(value) ? value : null;
}
function readPositiveNumber(value, fallback) {
  const numberValue = readFiniteNumber(value);
  if (numberValue !== null && numberValue > 0) {
    return numberValue;
  }
  return fallback ?? null;
}

// src/main.ts
var SetmovePlugin = class extends import_obsidian2.Plugin {
  constructor() {
    super(...arguments);
    this.settings = DEFAULT_SETTINGS;
    this.stopModalLifecycle = null;
    this.activeEnhancers = /* @__PURE__ */ new Set();
  }
  async onload() {
    this.settings = await loadSettings(this);
    await saveSettings(this, this.settings);
    this.addSettingTab(new SetmoveSettingTab(this));
    if (import_obsidian2.Platform.isMobile) {
      new import_obsidian2.Notice("Setmove is disabled on mobile.");
      return;
    }
    this.stopModalLifecycle = registerSettingsModalLifecycle(this.app.workspace, {
      onAttach: (match) => {
        const enhancer = enhanceSettingsModal(match, {
          settings: this.getEnhancerSettings(match.kind),
          onGeometryPersist: match.kind === "settings" ? async (geometry) => {
            await this.persistGeometry(geometry);
          } : void 0,
          onResetGeometry: match.kind === "settings" ? async () => {
            await this.resetSavedGeometryCommand();
          } : void 0
        });
        this.activeEnhancers.add(enhancer);
        return () => {
          this.activeEnhancers.delete(enhancer);
          enhancer.destroy();
        };
      }
    });
    this.register(() => {
      this.stopModalLifecycle?.();
      this.stopModalLifecycle = null;
    });
  }
  onunload() {
    this.stopModalLifecycle?.();
    this.stopModalLifecycle = null;
  }
  async updateSettings(partial) {
    this.settings = {
      ...this.settings,
      ...partial
    };
    await saveSettings(this, this.settings);
    this.applySettingsToOpenEnhancers();
  }
  async resetSavedGeometryCommand() {
    this.settings = clearSavedGeometry(this.settings);
    await saveSettings(this, this.settings);
    const enhancer = this.getOpenEnhancer();
    if (enhancer) {
      enhancer.reset();
    }
    this.applySettingsToOpenEnhancers();
    new import_obsidian2.Notice("Reset saved settings window geometry.");
  }
  async persistGeometry(geometry) {
    this.settings = {
      ...this.settings,
      geometry
    };
    await saveSettings(this, this.settings);
  }
  applySettingsToOpenEnhancers() {
    for (const enhancer of this.activeEnhancers) {
      enhancer.updateSettings(this.getEnhancerSettings(enhancer.kind));
    }
  }
  getOpenEnhancer() {
    const firstEnhancer = this.activeEnhancers.values().next();
    return firstEnhancer.done ? null : firstEnhancer.value;
  }
  getEnhancerSettings(kind) {
    return {
      ...this.settings,
      geometry: kind === "settings" ? this.settings.geometry : null,
      rememberGeometry: kind === "settings" && this.settings.rememberGeometry
    };
  }
};

/* nosourcemap */