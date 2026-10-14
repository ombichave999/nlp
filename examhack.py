<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <script>
    if (window.location.hostname !== 'examhack-py.vercel.app' && window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1' && !window.location.hostname.endsWith('.github.io')) {
      // Keep domain clean
    }
  </script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GenAI_and_Data_Analytics_Lab.ipynb - Colaboratory</title>
  <link rel="icon" type="image/x-icon" href="https://colab.research.google.com/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Roboto+Mono:ital,wght@0,400;0,500;1,400&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --colab-bg: #ffffff;
      --colab-surface: #f8f9fa;
      --colab-border: #dadce0;
      --colab-text-primary: #202124;
      --colab-text-secondary: #5f6368;
      --colab-text-muted: #80868b;
      --colab-accent-orange: #f9ab00;
      --colab-accent-dark-orange: #e37400;
      --colab-accent-blue: #1a73e8;
      --colab-accent-blue-hover: #174ea6;
      --colab-cell-bg: #f8f9fa;
      --colab-cell-active-border: #4285f4;
      --colab-code-font: 'Roboto Mono', Consolas, 'Courier New', monospace;
      --colab-ui-font: 'Google Sans', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      --colab-output-bg: #ffffff;
      --colab-sidebar-bg: #ffffff;
      --colab-toolbar-border: #e8eaed;
      --colab-btn-hover: #f1f3f4;
      
      /* Syntax Highlighting Light */
      --tok-kw: #a71d5d;
      --tok-builtin: #0086b3;
      --tok-str: #183691;
      --tok-comm: #969896;
      --tok-num: #0086b3;
      --tok-magic: #d73a49;
      --tok-fn: #795da3;
    }

    [data-theme="dark"] {
      --colab-bg: #1e1e1e;
      --colab-surface: #252526;
      --colab-border: #3c3c3c;
      --colab-text-primary: #e8eaed;
      --colab-text-secondary: #9aa0a6;
      --colab-text-muted: #70757a;
      --colab-cell-bg: #2d2d2d;
      --colab-cell-active-border: #8ab4f8;
      --colab-output-bg: #1e1e1e;
      --colab-sidebar-bg: #252526;
      --colab-toolbar-border: #333333;
      --colab-btn-hover: #333333;
      
      /* Syntax Highlighting Dark */
      --tok-kw: #c586c0;
      --tok-builtin: #4ec9b0;
      --tok-str: #ce9178;
      --tok-comm: #6a9955;
      --tok-num: #b5cea8;
      --tok-magic: #f48771;
      --tok-fn: #dcdcaa;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--colab-bg);
      color: var(--colab-text-primary);
      font-family: var(--colab-ui-font);
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      user-select: text;
    }

    /* Top Google Colab Header */
    .colab-navbar {
      height: 52px;
      border-bottom: 1px solid var(--colab-border);
      background: var(--colab-bg);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      flex-shrink: 0;
      z-index: 100;
    }

    .colab-navbar-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .colab-logo-container {
      display: flex;
      align-items: center;
      cursor: pointer;
      text-decoration: none;
    }

    .title-and-menu {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .notebook-title-row {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .notebook-title {
      font-size: 15px;
      font-weight: 500;
      color: var(--colab-text-primary);
      border: 1px solid transparent;
      padding: 1px 6px;
      border-radius: 4px;
      outline: none;
      white-space: nowrap;
    }

    .notebook-title:focus {
      border-color: var(--colab-accent-blue);
      background: var(--colab-surface);
    }

    .drive-status-badge {
      display: flex;
      align-items: center;
      gap: 4px;
      font-size: 12px;
      color: var(--colab-text-secondary);
      cursor: default;
    }

    .menubar {
      display: flex;
      align-items: center;
      gap: 16px;
      font-size: 12px;
      color: var(--colab-text-secondary);
      user-select: none;
    }

    .menu-item {
      cursor: pointer;
      padding: 2px 4px;
      border-radius: 4px;
      transition: background 0.15s;
    }

    .menu-item:hover {
      background: var(--colab-btn-hover);
      color: var(--colab-text-primary);
    }

    .colab-navbar-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* RAM & Disk Status Pill */
    .hardware-pill {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 4px 10px;
      border: 1px solid var(--colab-border);
      border-radius: 16px;
      font-size: 11.5px;
      color: var(--colab-text-secondary);
      cursor: pointer;
      background: var(--colab-surface);
      transition: all 0.2s;
    }

    .hardware-pill:hover {
      border-color: var(--colab-accent-blue);
      background: var(--colab-btn-hover);
    }

    .hw-status-dot {
      width: 7px;
      height: 7px;
      background-color: #34a853;
      border-radius: 50%;
    }

    .meter-container {
      display: flex;
      flex-direction: column;
      gap: 2px;
      width: 50px;
    }

    .meter-bar {
      height: 3.5px;
      background: #e0e0e0;
      border-radius: 2px;
      overflow: hidden;
    }

    [data-theme="dark"] .meter-bar {
      background: #444;
    }

    .meter-fill {
      height: 100%;
      background: #34a853;
    }

    .share-btn {
      background-color: var(--colab-accent-blue);
      color: #ffffff;
      border: none;
      padding: 6px 16px;
      border-radius: 18px;
      font-size: 13px;
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      transition: background 0.15s;
    }

    .share-btn:hover {
      background-color: var(--colab-accent-blue-hover);
    }

    .header-icon-btn {
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      cursor: pointer;
      color: var(--colab-text-secondary);
      border: none;
      background: transparent;
      transition: background 0.15s;
    }

    .header-icon-btn:hover {
      background: var(--colab-btn-hover);
      color: var(--colab-text-primary);
    }

    .user-avatar {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: #ea4335;
      color: white;
      font-weight: bold;
      font-size: 13px;
      display: flex;
      align-items: center;
      justify-content: center;
      user-select: none;
    }

    /* Sub Toolbar (Add Code / Add Text / Search / Jump) */
    .colab-toolbar {
      height: 44px;
      border-bottom: 1px solid var(--colab-toolbar-border);
      background: var(--colab-bg);
      display: flex;
      align-items: center;
      padding: 0 16px;
      gap: 10px;
      flex-shrink: 0;
      z-index: 90;
    }

    .tool-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 4px;
      font-size: 12.5px;
      font-weight: 500;
      color: var(--colab-text-secondary);
      background: transparent;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.15s;
    }

    .tool-btn:hover {
      background: var(--colab-btn-hover);
      color: var(--colab-text-primary);
      border-color: var(--colab-border);
    }

    .tool-btn.highlight {
      color: var(--colab-accent-blue);
    }

    .toolbar-divider {
      width: 1px;
      height: 20px;
      background: var(--colab-border);
      margin: 0 4px;
    }

    .search-box-wrapper {
      position: relative;
      flex: 1;
      max-width: 420px;
    }

    .search-input {
      width: 100%;
      height: 32px;
      padding: 0 10px 0 32px;
      border-radius: 6px;
      border: 1px solid var(--colab-border);
      background: var(--colab-surface);
      color: var(--colab-text-primary);
      font-size: 12.5px;
      font-family: inherit;
      outline: none;
      transition: all 0.2s;
    }

    .search-input:focus {
      border-color: var(--colab-accent-blue);
      background: var(--colab-bg);
      box-shadow: 0 1px 3px rgba(66, 133, 244, 0.15);
    }

    .search-icon {
      position: absolute;
      left: 9px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--colab-text-muted);
      pointer-events: none;
    }

    .quick-nav-select {
      height: 32px;
      padding: 0 8px;
      border-radius: 6px;
      border: 1px solid var(--colab-border);
      background: var(--colab-surface);
      color: var(--colab-text-primary);
      font-size: 12.5px;
      font-family: inherit;
      outline: none;
      cursor: pointer;
    }

    /* Main Workspace Layout */
    .colab-main-workspace {
      display: flex;
      flex: 1;
      height: calc(100vh - 96px);
      overflow: hidden;
    }

    /* Left Activity Bar */
    .activity-bar {
      width: 48px;
      background: var(--colab-sidebar-bg);
      border-right: 1px solid var(--colab-border);
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: 10px;
      gap: 16px;
      flex-shrink: 0;
      z-index: 50;
    }

    .activity-icon-btn {
      width: 36px;
      height: 36px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
      cursor: pointer;
      color: var(--colab-text-secondary);
      border: none;
      background: transparent;
      position: relative;
      transition: all 0.15s;
    }

    .activity-icon-btn:hover {
      background: var(--colab-btn-hover);
      color: var(--colab-text-primary);
    }

    .activity-icon-btn.active {
      color: var(--colab-accent-blue);
      background: rgba(26, 115, 232, 0.1);
    }

    .activity-icon-btn.active::before {
      content: '';
      position: absolute;
      left: 0;
      top: 6px;
      bottom: 6px;
      width: 3px;
      background: var(--colab-accent-blue);
      border-radius: 0 2px 2px 0;
    }

    /* Collapsible Left Drawer (Table of Contents) */
    .colab-drawer {
      width: 290px;
      background: var(--colab-sidebar-bg);
      border-right: 1px solid var(--colab-border);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      transition: width 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      overflow: hidden;
    }

    .colab-drawer.collapsed {
      width: 0;
      border-right: none;
    }

    .drawer-header {
      height: 44px;
      padding: 0 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--colab-border);
      font-size: 13px;
      font-weight: 500;
      color: var(--colab-text-primary);
    }

    .drawer-close-btn {
      background: transparent;
      border: none;
      cursor: pointer;
      color: var(--colab-text-secondary);
      padding: 4px;
      border-radius: 4px;
    }

    .drawer-close-btn:hover {
      background: var(--colab-btn-hover);
    }

    .toc-scroll-area {
      flex: 1;
      overflow-y: auto;
      padding: 10px 8px;
    }

    .toc-item {
      display: flex;
      align-items: center;
      padding: 6px 10px;
      font-size: 12.5px;
      color: var(--colab-text-secondary);
      border-radius: 6px;
      cursor: pointer;
      text-decoration: none;
      line-height: 1.35;
      margin-bottom: 2px;
      transition: all 0.15s;
    }

    .toc-item:hover {
      background: var(--colab-btn-hover);
      color: var(--colab-text-primary);
    }

    .toc-item.active {
      background: rgba(26, 115, 232, 0.12);
      color: var(--colab-accent-blue);
      font-weight: 500;
    }

    .toc-item.level-2 {
      padding-left: 24px;
      font-size: 12px;
    }

    .toc-item.level-3 {
      padding-left: 36px;
      font-size: 11.5px;
    }

    /* Notebook Canvas Area */
    .colab-canvas {
      flex: 1;
      overflow-y: auto;
      padding: 24px 32px 120px 32px;
      scroll-behavior: smooth;
    }

    .notebook-container {
      max-width: 960px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* Notebook Cell Common */
    .colab-cell {
      position: relative;
      border-radius: 8px;
      border: 1px solid transparent;
      transition: border-color 0.15s;
      margin-bottom: 8px;
    }

    .colab-cell:hover {
      border-color: var(--colab-border);
    }

    .colab-cell:focus-within {
      border-color: var(--colab-cell-active-border);
    }

    /* Top Cell Action Bar on Hover */
    .cell-hover-bar {
      position: absolute;
      top: -14px;
      right: 14px;
      background: var(--colab-bg);
      border: 1px solid var(--colab-border);
      border-radius: 16px;
      display: none;
      align-items: center;
      padding: 2px 6px;
      gap: 4px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.12);
      z-index: 20;
    }

    .colab-cell:hover .cell-hover-bar {
      display: flex;
    }

    .cell-action-btn {
      background: transparent;
      border: none;
      font-size: 11px;
      font-family: inherit;
      color: var(--colab-text-secondary);
      padding: 4px 8px;
      cursor: pointer;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s;
    }

    .cell-action-btn:hover {
      background: var(--colab-btn-hover);
      color: var(--colab-text-primary);
    }

    .copy-btn.copied {
      background: #e6f4ea;
      color: #137333;
      font-weight: 500;
    }

    [data-theme="dark"] .copy-btn.copied {
      background: #133a1e;
      color: #81c995;
    }

    /* Text / Markdown Cell */
    .text-cell {
      padding: 12px 18px;
      line-height: 1.6;
      color: var(--colab-text-primary);
    }

    .text-cell h1 {
      font-size: 22px;
      font-weight: 600;
      margin-bottom: 8px;
      color: var(--colab-text-primary);
      border-bottom: 1px solid var(--colab-border);
      padding-bottom: 6px;
    }

    .text-cell h2 {
      font-size: 18px;
      font-weight: 600;
      margin: 14px 0 6px 0;
      color: var(--colab-text-primary);
    }

    .text-cell h3 {
      font-size: 14.5px;
      font-weight: 600;
      margin: 12px 0 4px 0;
      color: var(--colab-accent-blue);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .text-cell p {
      font-size: 13.5px;
      margin-bottom: 8px;
      color: var(--colab-text-primary);
    }

    .text-cell ol, .text-cell ul {
      margin-left: 22px;
      margin-bottom: 10px;
      font-size: 13.5px;
    }

    .text-cell li {
      margin-bottom: 4px;
    }

    /* Code Cell */
    .code-cell {
      border: 1px solid var(--colab-border);
      background: var(--colab-cell-bg);
      border-radius: 8px;
      overflow: hidden;
    }

    .code-editor-row {
      display: flex;
      align-items: stretch;
      min-height: 48px;
    }

    /* Run Button Gutter */
    .run-gutter {
      width: 48px;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: 10px;
      background: transparent;
      user-select: none;
      flex-shrink: 0;
    }

    .run-btn {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: 1px solid var(--colab-border);
      background: var(--colab-bg);
      color: var(--colab-text-secondary);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s;
    }

    .run-btn:hover {
      border-color: var(--colab-accent-blue);
      color: var(--colab-accent-blue);
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    .run-btn.running svg {
      animation: colab-spin 0.6s linear infinite;
    }

    @keyframes colab-spin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    .execution-counter {
      font-size: 11px;
      color: var(--colab-text-muted);
      margin-top: 4px;
      font-family: var(--colab-code-font);
    }

    /* Code Text Area */
    .code-content {
      flex: 1;
      padding: 10px 14px 10px 4px;
      font-family: var(--colab-code-font);
      font-size: 13px;
      line-height: 1.5;
      overflow-x: auto;
      white-space: pre;
    }

    /* Syntax Tokens */
    .tok-kw { color: var(--tok-kw); font-weight: 500; }
    .tok-builtin { color: var(--tok-builtin); }
    .tok-str { color: var(--tok-str); }
    .tok-comm { color: var(--tok-comm); font-style: italic; }
    .tok-num { color: var(--tok-num); }
    .tok-magic { color: var(--tok-magic); font-weight: 500; }
    .tok-fn { color: var(--tok-fn); }

    /* Output Cell Area */
    .cell-output-wrapper {
      background: var(--colab-output-bg);
      border-top: 1px solid var(--colab-border);
      padding: 12px 16px 12px 48px;
      font-family: var(--colab-code-font);
      font-size: 12.5px;
      line-height: 1.5;
      overflow-x: auto;
      position: relative;
    }

    .output-header {
      font-size: 11px;
      color: var(--colab-text-muted);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: var(--colab-ui-font);
    }

    .output-text {
      white-space: pre-wrap;
      color: var(--colab-text-primary);
    }

    /* Output Graphics & Charts */
    .output-plot-container {
      margin-top: 12px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      align-items: flex-start;
    }

    .plot-card {
      background: #ffffff;
      border: 1px solid #d0d0d0;
      border-radius: 4px;
      padding: 8px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }

    /* Toast Notification */
    .toast-msg {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #323232;
      color: #ffffff;
      padding: 8px 18px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 500;
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
      z-index: 1000;
      transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      pointer-events: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .toast-msg.show {
      transform: translateX(-50%) translateY(0);
    }

    /* Hardware Info Modal */
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.4);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 999;
    }

    .modal-overlay.active {
      display: flex;
    }

    .hw-modal {
      background: var(--colab-bg);
      border: 1px solid var(--colab-border);
      border-radius: 8px;
      width: 380px;
      padding: 20px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    }

    .hw-modal h3 {
      font-size: 15px;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .hw-stat-row {
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      margin: 8px 0;
      color: var(--colab-text-secondary);
    }

    .hw-stat-row span:last-child {
      color: var(--colab-text-primary);
      font-weight: 500;
    }

    .modal-close-btn {
      margin-top: 16px;
      width: 100%;
      background: var(--colab-accent-blue);
      color: white;
      border: none;
      padding: 8px;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 500;
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-thumb {
      background: var(--colab-border);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-track {
      background: transparent;
    }

    @media (max-width: 768px) {
      .colab-drawer {
        position: absolute;
        left: 48px;
        top: 96px;
        bottom: 0;
        z-index: 60;
        box-shadow: 2px 0 10px rgba(0,0,0,0.2);
      }
      .colab-navbar-right .hardware-pill,
      .menubar {
        display: none;
      }
      .colab-canvas {
        padding: 12px 14px 80px 14px;
      }
    }
  </style>
</head>
<body data-theme="light">

  <!-- 1. Google Colab Top Navbar -->
  <header class="colab-navbar">
    <div class="colab-navbar-left">
      <!-- Colab Interlocking Orange Loops Logo -->
      <a href="#" class="colab-logo-container" title="Google Colaboratory">
        <svg viewBox="0 0 32 32" width="30" height="30">
          <g fill="none" fill-rule="evenodd">
            <!-- Left loop (Gold) -->
            <path d="M10.5 8C6.91 8 4 10.91 4 14.5S6.91 21 10.5 21c2.14 0 4.04-1.04 5.22-2.63A7.95 7.95 0 0113.8 14.5c0-1.4.36-2.72.99-3.87A6.47 6.47 0 0010.5 8z" fill="#F9AB00"/>
            <!-- Right loop (Orange) -->
            <path d="M21.5 8c-1.89 0-3.59.81-4.78 2.1A7.95 7.95 0 0118.2 14.5c0 1.55-.44 3-1.2 4.23A6.48 6.48 0 0021.5 21C25.09 21 28 18.09 28 14.5S25.09 8 21.5 8z" fill="#E37400"/>
            <!-- Overlap lens -->
            <path d="M14.79 10.63A7.95 7.95 0 0118.2 14.5c0 1.55-.44 3-1.2 4.23A7.95 7.95 0 0113.8 14.5c0-1.4.36-2.72.99-3.87z" fill="#EA8600"/>
          </g>
        </svg>
      </a>

      <div class="title-and-menu">
        <div class="notebook-title-row">
          <span class="notebook-title" contenteditable="true" spellcheck="false">GenAI_and_Data_Analytics_Lab.ipynb</span>
          <span class="drive-status-badge" title="All changes saved in Drive">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM19 18H6c-2.21 0-4-1.79-4-4 0-2.05 1.53-3.76 3.56-3.97l1.07-.11.5-.95C8.08 7.14 9.94 6 12 6c2.62 0 4.88 1.86 5.39 4.43l.3 1.5 1.53.11c1.56.1 2.78 1.41 2.78 2.96 0 1.65-1.35 3-3 3z"/></svg>
            Saved to Drive
          </span>
        </div>

        <nav class="menubar">
          <span class="menu-item" onclick="triggerSearch()">File</span>
          <span class="menu-item" onclick="copyAllPracticals()">Edit</span>
          <span class="menu-item" onclick="toggleDrawer()">View</span>
          <span class="menu-item" onclick="showToast('Cell inserted')">Insert</span>
          <span class="menu-item" onclick="runAllCells()">Runtime</span>
          <span class="menu-item" onclick="toggleTheme()">Tools</span>
          <span class="menu-item" onclick="showToast('GenAI Colab Lab v2.5')">Help</span>
        </nav>
      </div>
    </div>

    <div class="colab-navbar-right">
      <!-- RAM & Disk Connected Widget -->
      <div class="hardware-pill" onclick="openHardwareModal()" title="RAM: 0.86GB / 12.68GB | Disk: 24.31GB / 107.72GB">
        <span class="hw-status-dot"></span>
        <div class="meter-container">
          <div class="meter-bar"><div class="meter-fill" style="width: 14%;"></div></div>
          <div class="meter-bar"><div class="meter-fill" style="width: 25%;"></div></div>
        </div>
        <span>Connected</span>
      </div>

      <!-- Quick Theme Toggle -->
      <button class="header-icon-btn" onclick="toggleTheme()" title="Toggle Dark/Light Mode">
        <span id="theme-icon">🌙</span>
      </button>

      <!-- Share Button -->
      <button class="share-btn" onclick="copyCurrentUrl()">
        <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34 3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"/></svg>
        Share
      </button>

      <!-- Settings Icon -->
      <button class="header-icon-btn" onclick="openHardwareModal()" title="Notebook settings">
        <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>
      </button>

      <!-- Account Avatar -->
      <div class="user-avatar" title="Logged in as ombichave999@gmail.com">O</div>
    </div>
  </header>

  <!-- 2. Sub-Toolbar with Quick Jump & Search -->
  <div class="colab-toolbar">
    <button class="tool-btn highlight" onclick="showToast('New code cell added')">
      <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>
      Code
    </button>
    <button class="tool-btn" onclick="showToast('New text cell added')">
      <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>
      Text
    </button>
    
    <div class="toolbar-divider"></div>

    <!-- Quick Search Box -->
    <div class="search-box-wrapper">
      <svg class="search-icon" viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
      <input type="text" id="searchInput" class="search-input" placeholder="Filter practicals, questions or keywords... (Ctrl+F)" oninput="filterNotebook(this.value)">
    </div>

    <!-- Practical Jump Select -->
    <select class="quick-nav-select" onchange="scrollToPractical(this.value)">
      <option value="">Jump to Practical...</option>
      <option value="prac-1">Practical 1: Mini GenAI - Next Word Prediction</option>
      <option value="prac-2">Practical 2: Text Gen & BART Summarization</option>
      <option value="prac-3">Practical 3: AI Tutor Chatbot (Gemini API)</option>
      <option value="prac-4">Practical 4: Intro to GenAI (Gemini 6 Tasks)</option>
      <option value="prac-5">Practical 5: GPT-2 & Gemini Customer Service</option>
      <option value="prac-6">Practical 6: Superstore Data Analysis & Plots</option>
      <option value="prac-7">Practical 7: Dimensionality Reduction (PCA)</option>
      <option value="prac-8">Practical 8: ANOVA & Hypothesis T-Tests</option>
    </select>

    <button class="tool-btn" onclick="copyAllPracticals()" title="Copy all code snippets to clipboard">
      <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
      Copy All Code
    </button>
  </div>

  <!-- 3. Main Workspace: Activity Bar + Drawer + Notebook Canvas -->
  <div class="colab-main-workspace">
    
    <!-- Vertical Activity Bar -->
    <div class="activity-bar">
      <button class="activity-icon-btn active" id="btn-toc" onclick="toggleDrawer()" title="Table of contents">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M3 9h14V7H3v2zm0 4h14v-2H3v2zm0 4h14v-2H3v2zm16 0h2v-2h-2v2zm0-10v2h2V7h-2zm0 6h2v-2h-2v2z"/></svg>
      </button>
      <button class="activity-icon-btn" onclick="focusSearch()" title="Find and replace">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
      </button>
      <button class="activity-icon-btn" onclick="showToast('Code Snippets available')" title="Code snippets">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/></svg>
      </button>
      <button class="activity-icon-btn" onclick="showToast('Filesystem: Sample - Superstore.csv mounted')" title="Files">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm0 12H4V8h16v10z"/></svg>
      </button>
    </div>

    <!-- Collapsible Table of Contents Drawer -->
    <aside class="colab-drawer" id="colabDrawer">
      <div class="drawer-header">
        <span>Table of contents</span>
        <button class="drawer-close-btn" onclick="toggleDrawer()" title="Close drawer">✕</button>
      </div>
      <div class="toc-scroll-area">
        <a href="#prac-1" class="toc-item">Practical 1: Next Word Prediction</a>
        <a href="#prac-2" class="toc-item">Practical 2: Text Gen & Summarization</a>
        <a href="#prac-2-a" class="toc-item level-2">Part A: Predefined Text Gen</a>
        <a href="#prac-2-b" class="toc-item level-2">Part B: BART Transformer</a>
        <a href="#prac-3" class="toc-item">Practical 3: Gemini AI Tutor Chatbot</a>
        <a href="#prac-4" class="toc-item">Practical 4: Intro to GenAI (Gemini)</a>
        <a href="#prac-4-1" class="toc-item level-2">Sub-Part 1: Text Generation</a>
        <a href="#prac-4-2" class="toc-item level-2">Sub-Part 2: Story Generation</a>
        <a href="#prac-4-3" class="toc-item level-2">Sub-Part 3: Question Answering</a>
        <a href="#prac-4-4" class="toc-item level-2">Sub-Part 4: Hindi Translation</a>
        <a href="#prac-4-5" class="toc-item level-2">Sub-Part 5: Leave Application</a>
        <a href="#prac-4-6" class="toc-item level-2">Sub-Part 6: MCQ Generation</a>
        <a href="#prac-5" class="toc-item">Practical 5: GPT-2 & Gemini Customer</a>
        <a href="#prac-5-1" class="toc-item level-2">Sub-Part 1: Local GPT-2 Text Gen</a>
        <a href="#prac-5-2" class="toc-item level-2">Sub-Part 2: Customer Email Reply</a>
        <a href="#prac-6" class="toc-item">Practical 6: Superstore Data Analysis</a>
        <a href="#prac-7" class="toc-item">Practical 7: PCA Dimensionality Reduction</a>
        <a href="#prac-8" class="toc-item">Practical 8: Statistical Analysis (ANOVA & T-Tests)</a>
        <a href="#prac-8-a" class="toc-item level-2">Part A: One-Way ANOVA</a>
        <a href="#prac-8-b" class="toc-item level-2">Part B: One-Sample T-Test</a>
        <a href="#prac-8-c" class="toc-item level-2">Part C: Two-Sample T-Test</a>
      </div>
    </aside>

    <!-- Notebook Canvas -->
    <main class="colab-canvas" id="canvasScroll">
      <div class="notebook-container">

        <!-- ==========================================
             PRACTICAL NO. 1
             ========================================== -->
        <section id="prac-1" class="practical-block">
          <!-- Text Cell: Aim, Theory, Algorithm -->
          <div class="colab-cell text-cell">
            <div class="cell-hover-bar">
              <button class="cell-action-btn" onclick="copyTextFromElement(this)">Copy Text</button>
            </div>
            <h1>Practical No. 1: Mini Generative AI – Next Word Prediction</h1>
            <h3>Aim</h3>
            <p>To understand the basic concept of Generative Artificial Intelligence by developing a simple next-word prediction model using Python.</p>
            <h3>Theory</h3>
            <p>Generative Artificial Intelligence (Generative AI) is a branch of AI that creates new content such as text, images, audio, and code by learning patterns from existing data. One of the simplest text generation techniques is next-word prediction, where the system predicts the most probable next word based on previously learned word sequences. This concept is the basic building block of modern Large Language Models (LLMs) like ChatGPT.</p>
            <h3>Algorithm</h3>
            <ol>
              <li>Start the program.</li>
              <li>Create a list of sample sentences.</li>
              <li>Split each sentence into individual words.</li>
              <li>Store every word along with its next word in a dictionary.</li>
              <li>Display the learned model.</li>
              <li>Accept a starting word from the user.</li>
              <li>Randomly select the next word from the learned dictionary.</li>
              <li>Repeat the process until no next word is available or the desired number of words is generated.</li>
              <li>Display the generated text.</li>
              <li>Stop.</li>
            </ol>
          </div>

          <!-- Code Cell -->
          <div class="colab-cell code-cell">
            <div class="cell-hover-bar">
              <button class="cell-action-btn copy-btn" onclick="copyCode(this)">
                <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
                Copy Code
              </button>
            </div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)" title="Run cell (Ctrl+Enter)">
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
                </button>
                <span class="execution-counter">[1]</span>
              </div>
              <div class="code-content"><span class="tok-kw">import</span> random

<span class="tok-comm"># Training sentences</span>
sentences = [
    <span class="tok-str">"I love data science"</span>,
    <span class="tok-str">"I love machine learning"</span>,
    <span class="tok-str">"data science is amazing"</span>,
    <span class="tok-str">"machine learning is powerful"</span>,
    <span class="tok-str">"I enjoy learning python"</span>
]

<span class="tok-comm"># Dictionary to store word relationships</span>
model = {}

<span class="tok-comm"># Build the model</span>
<span class="tok-kw">for</span> sentence <span class="tok-kw">in</span> sentences:
    words = sentence.split()
    <span class="tok-kw">for</span> i <span class="tok-kw">in</span> <span class="tok-builtin">range</span>(<span class="tok-builtin">len</span>(words) - <span class="tok-num">1</span>):
        current_word = words[i]
        next_word = words[i + <span class="tok-num">1</span>]
        <span class="tok-kw">if</span> current_word <span class="tok-kw">not in</span> model:
            model[current_word] = []
        model[current_word].append(next_word)

<span class="tok-builtin">print</span>(<span class="tok-str">"Learned Model"</span>)
<span class="tok-builtin">print</span>(model)

<span class="tok-comm"># User input</span>
word = <span class="tok-builtin">input</span>(<span class="tok-str">"
Enter starting word: "</span>)
generated_text = word

<span class="tok-comm"># Generate text</span>
<span class="tok-kw">for</span> i <span class="tok-kw">in</span> <span class="tok-builtin">range</span>(<span class="tok-num">5</span>):
    <span class="tok-kw">if</span> word <span class="tok-kw">in</span> model:
        word = random.choice(model[word])
        generated_text = generated_text + <span class="tok-str">" "</span> + word
    <span class="tok-kw">else</span>:
        <span class="tok-kw">break</span>

<span class="tok-builtin">print</span>(<span class="tok-str">"
Generated Text:"</span>)
<span class="tok-builtin">print</span>(generated_text)</div>
            </div>

            <!-- Output block -->
            <div class="cell-output-wrapper">
              <div class="output-header">
                <svg viewBox="0 0 24 24" width="12" height="12" fill="#34a853"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                Executed in 0.12s
              </div>
              <div class="output-text">Learned Model
{'I': ['love', 'love', 'enjoy'], 'love': ['data', 'machine'], 'data': ['science', 'science'], 'machine': ['learning', 'learning'], 'learning': ['python', 'is']}

Enter starting word: love

Generated Text:
love data science is amazing</div>
            </div>
          </div>

          <!-- Text Cell: Conclusion -->
          <div class="colab-cell text-cell">
            <h3>Conclusion</h3>
            <p>The practical demonstrated the implementation of a simple next-word prediction model using Python. It helped in understanding how Generative AI learns patterns from text and generates meaningful sentences by predicting one word at a time. This concept forms the foundation of modern text generation models.</p>
          </div>
        </section>


        <!-- ==========================================
             PRACTICAL NO. 2
             ========================================== -->
        <section id="prac-2" class="practical-block">
          <div class="colab-cell text-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn" onclick="copyTextFromElement(this)">Copy Text</button></div>
            <h1>Practical No. 2: Text Generation and Text Summarization using Generative AI</h1>
            <h3>Aim</h3>
            <p>To understand the concepts of text generation and text summarization using Python.</p>
            <h3>Theory</h3>
            <p>Generative AI can create new text as well as summarize lengthy content into a shorter form. Text generation involves producing meaningful sentences based on given input, while text summarization extracts the most important information from a paragraph. These techniques are widely used in chatbots, content creation, search engines, virtual assistants, and document analysis systems.</p>
          </div>

          <!-- Part A -->
          <div id="prac-2-a" class="colab-cell text-cell">
            <h2>Part A: Text Generation</h2>
            <h3>Objective</h3>
            <p>To generate text based on user input using predefined responses.</p>
            <h3>Algorithm</h3>
            <ol>
              <li>Start the program.</li>
              <li>Create a dictionary containing keywords and corresponding generated text.</li>
              <li>Accept input from the user.</li>
              <li>Check whether the keyword exists in the dictionary.</li>
              <li>Display the generated text.</li>
              <li>Stop the program.</li>
            </ol>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar">
              <button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button>
            </div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[2]</span>
              </div>
              <div class="code-content">responses = {
    <span class="tok-str">"ai"</span>: <span class="tok-str">"Artificial Intelligence is transforming the world."</span>,
    <span class="tok-str">"python"</span>: <span class="tok-str">"Python is a popular programming language for AI."</span>,
    <span class="tok-str">"data"</span>: <span class="tok-str">"Data is the foundation of machine learning."</span>
}

word = <span class="tok-builtin">input</span>(<span class="tok-str">"Enter a keyword (ai/python/data): "</span>).lower()

<span class="tok-kw">if</span> word <span class="tok-kw">in</span> responses:
    <span class="tok-builtin">print</span>(<span class="tok-str">"
Generated Text:"</span>)
    <span class="tok-builtin">print</span>(responses[word])
<span class="tok-kw">else</span>:
    <span class="tok-builtin">print</span>(<span class="tok-str">"No text available for the given keyword."</span>)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">Enter a keyword (ai/python/data): python

Generated Text:
Python is a popular programming language for AI.</div>
            </div>
          </div>

          <!-- Part B -->
          <div id="prac-2-b" class="colab-cell text-cell">
            <h2>Part B: Text Summarization using Hugging Face Transformer</h2>
            <h3>Objective</h3>
            <p>To summarize a paragraph by extracting important sentences.</p>
            <h3>Algorithm</h3>
            <ol>
              <li>Start the program.</li>
              <li>Import the pipeline function from the transformers library.</li>
              <li>Load the pre-trained summarization pipeline.</li>
              <li>Store the input paragraph in a variable.</li>
              <li>Generate the summary by specifying the maximum and minimum summary length.</li>
              <li>Display the generated summary.</li>
              <li>Stop the program.</li>
            </ol>
          </div>

          <!-- Pip Installation Cell -->
          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[3]</span>
              </div>
              <div class="code-content"><span class="tok-comm"># Step 1: Uninstall existing packages</span>
<span class="tok-magic">!pip uninstall -y transformers torch torchvision torchaudio</span>

<span class="tok-comm"># Step 2: Install compatible versions</span>
<span class="tok-magic">!pip install -q torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0</span>
<span class="tok-magic">!pip install -q transformers==4.52.4 sentencepiece accelerate</span>

<span class="tok-comm"># Step 3: Restart session if prompted (Run -> Restart Session)</span></div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">Found existing installation: transformers 4.38.2
Uninstalling transformers-4.38.2:
  Successfully uninstalled transformers-4.38.2
Successfully installed torch-2.6.0 torchvision-0.21.0 torchaudio-2.6.0 transformers-4.52.4</div>
            </div>
          </div>

          <!-- Summarization Program -->
          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[4]</span>
              </div>
              <div class="code-content"><span class="tok-kw">from</span> transformers <span class="tok-kw">import</span> pipeline

<span class="tok-comm"># Load summarization pipeline</span>
summarizer = pipeline(
    task=<span class="tok-str">"summarization"</span>,
    model=<span class="tok-str">"facebook/bart-large-cnn"</span>
)

<span class="tok-comm"># Input paragraph</span>
text = <span class="tok-str">"""
Artificial Intelligence is transforming every industry by automating tasks,
improving decision-making, and generating human-like content.
Generative AI is a branch of AI capable of creating text, images,
music, videos, and even software code.
"""</span>

<span class="tok-comm"># Generate summary</span>
summary = summarizer(text, max_length=<span class="tok-num">40</span>, min_length=<span class="tok-num">15</span>)

<span class="tok-comm"># Display original text</span>
<span class="tok-builtin">print</span>(<span class="tok-str">"Original Text:
"</span>)
<span class="tok-builtin">print</span>(text)

<span class="tok-comm"># Display summary</span>
<span class="tok-builtin">print</span>(<span class="tok-str">"
Generated Summary:
"</span>)
<span class="tok-builtin">print</span>(summary[<span class="tok-num">0</span>][<span class="tok-str">"summary_text"</span>])</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">Original Text:

Artificial Intelligence is transforming every industry by automating tasks,
improving decision-making, and generating human-like content.
Generative AI is a branch of AI capable of creating text, images,
music, videos, and even software code.


Generated Summary:

Generative AI is a branch of AI capable of creating text, images, music, videos, and even software code.</div>
            </div>
          </div>

          <div class="colab-cell text-cell">
            <h3>Conclusion</h3>
            <p>The practical demonstrated how a pre-trained BART Transformer model can summarize lengthy text into a concise and meaningful form. It provided hands-on experience in using Generative AI for Natural Language Processing (NLP) tasks and highlighted the practical applications of AI-powered text summarization in education, business, and content analysis.</p>
          </div>
        </section>


        <!-- ==========================================
             PRACTICAL NO. 3
             ========================================== -->
        <section id="prac-3" class="practical-block">
          <div class="colab-cell text-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn" onclick="copyTextFromElement(this)">Copy Text</button></div>
            <h1>Practical No. 3: AI Tutor Chatbot using Google Gemini API</h1>
            <h3>Aim</h3>
            <p>To develop an AI Tutor Chatbot using the Google Gemini API that interacts with users and answers programming-related questions in a conversational manner.</p>
            <h3>Theory</h3>
            <p>A chatbot is a conversational AI application that communicates with users using Natural Language Processing (NLP). Modern chatbots are powered by Large Language Models (LLMs), which understand user queries and generate human-like responses. In this practical, the Google Gemini API is used to create an AI Tutor that explains coding concepts to beginners. A system instruction is provided to define the chatbot's personality, making it friendly, encouraging, and suitable for learning.</p>
            <h3>Algorithm</h3>
            <ol>
              <li>Start the program.</li>
              <li>Import the required <code>google.genai</code> library.</li>
              <li>Initialize the Gemini client using the API key.</li>
              <li>Create a chat session using the Gemini 2.5 Flash model.</li>
              <li>Set the system instruction to define the chatbot's role as an AI tutor.</li>
              <li>Display a welcome message.</li>
              <li>Accept user input in a loop.</li>
              <li>Send the user's message to the Gemini model.</li>
              <li>Display the AI-generated response.</li>
              <li>Repeat until the user enters <code>exit</code>.</li>
              <li>Stop the program.</li>
            </ol>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[5]</span>
              </div>
              <div class="code-content"><span class="tok-kw">import</span> os
<span class="tok-kw">from</span> google <span class="tok-kw">import</span> genai

<span class="tok-comm"># Initialize Gemini client</span>
client = genai.Client(api_key=<span class="tok-str">"AQ." + "Ab8RN6JkmZk7st62RATnSJpe-0NqOvT2JBmN-YSJ0eWorqxnVw"</span>)

<span class="tok-comm"># Create AI Tutor Chat</span>
chat = client.chats.create(
    model=<span class="tok-str">"gemini-3.5-flash"</span>,
    config=genai.types.GenerateContentConfig(
        system_instruction=<span class="tok-str">"You are a brilliant AI tutor explaining coding to beginners. Be encouraging and use emojis."</span>
    )
)

<span class="tok-builtin">print</span>(<span class="tok-str">"AI Tutor: Hello! I'm your GenAI tutor. Ask me anything!"</span>)

<span class="tok-kw">while</span> <span class="tok-kw">True</span>:
    user_input = <span class="tok-builtin">input</span>(<span class="tok-str">"You: "</span>)
    <span class="tok-kw">if</span> user_input.lower() == <span class="tok-str">"exit"</span>:
        <span class="tok-builtin">print</span>(<span class="tok-str">"AI Tutor: Thank you! Happy Learning 😊"</span>)
        <span class="tok-kw">break</span>
    response = chat.send_message(user_input)
    <span class="tok-builtin">print</span>(<span class="tok-str">"AI Tutor:"</span>, response.text)
    <span class="tok-builtin">print</span>()</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">AI Tutor: Hello! I'm your GenAI tutor. Ask me anything!
You: what is gen ai
AI Tutor: Hello there, future tech superstar! 🌟 That is an absolute **excellent** question to ask.

Let's dive into the exciting world of **Gen AI** (which is short for **Generative Artificial Intelligence**)!

---

### What is Gen AI? 🤖

In the simplest terms, **Generative AI** is a type of artificial intelligence that can **create brand-new things**!

Before Gen AI, older AI systems were mostly like "judges" or "detectives." They could look at a photo and say: "That's a cat!" or predict if it will rain tomorrow.

But **Generative AI** is like an **artist, writer, and programmer** all rolled into one! Instead of just reading data, it writes new data.

---

### What can Gen AI create? 🌟

It's not just one thing! Gen AI can create all sorts of cool stuff:

1. **Text 📝**: It can write essays, poems, emails, or even chat with you (just like I am doing right now!)
2. **Images 🎨**: You can type *"a cute golden retriever puppy wearing a space suit on Mars"* and it will draw it!
3. **Code 💻**: (My personal favorite!) It can write computer code in languages like Python, JavaScript, or C++.
4. **Music & Video 🎵🎥**: It can compose songs or make short video clips from just a text description.

---
You: exit
AI Tutor: Thank you! Happy Learning 😊</div>
            </div>
          </div>

          <div class="colab-cell text-cell">
            <h3>Conclusion</h3>
            <p>The practical demonstrated the development of an AI Tutor Chatbot using the Google Gemini API. The chatbot interacted with users in natural language, answered programming-related questions, and provided beginner-friendly explanations. This practical helped in understanding the implementation of conversational AI using Large Language Models (LLMs).</p>
          </div>
        </section>


        <!-- ==========================================
             PRACTICAL NO. 4
             ========================================== -->
        <section id="prac-4" class="practical-block">
          <div class="colab-cell text-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn" onclick="copyTextFromElement(this)">Copy Text</button></div>
            <h1>Practical No. 4: Introduction to Generative AI using Gemini API</h1>
            <h3>Aim</h3>
            <p>To understand the basic concepts of Generative AI and perform different text-generation tasks using the Gemini API and Python.</p>
            <h3>Theory</h3>
            <p>Generative AI is a branch of Artificial Intelligence that can generate new content such as text, images, audio, code, and other forms of information. In this practical, the Gemini API is used with Python to perform various text-generation tasks through suitable prompts.</p>
            <h3>Software / Requirements</h3>
            <ul>
              <li>Python</li>
              <li>Google Colab / Jupyter Notebook</li>
              <li>Gemini API</li>
              <li>google-generativeai Python library</li>
            </ul>
          </div>

          <!-- Sub-Part 1 -->
          <div id="prac-4-1" class="colab-cell text-cell">
            <h2>Sub-Part 1: Basic Text Generation</h2>
            <h3>Problem Statement</h3>
            <p>Write a Python program to use Generative AI to explain Artificial Intelligence in simple words.</p>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[6]</span>
              </div>
              <div class="code-content"><span class="tok-magic">!pip -q install google-generativeai</span>
<span class="tok-kw">import</span> google.generativeai <span class="tok-kw">as</span> genai

API_KEY = <span class="tok-str">"AQ." + "Ab8RN6JkmZk7st62RATnSJpe-0NqOvT2JBmN-YSJ0eWorqxnVw"</span>
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(<span class="tok-str">"gemini-3.5-flash"</span>)
response = model.generate_content(<span class="tok-str">"Explain Artificial Intelligence in simple words."</span>)
<span class="tok-builtin">print</span>(response.text)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">At its simplest, **Artificial Intelligence (AI)** is when computers and machines are programmed to "think," learn, and make decisions, much like a human brain does.

Normally, computers can only do exactly what we tell them to do. But with AI, computers can look at information, learn from it, and figure things out on their own.

Here is an easy way to understand how it works:

### 1. How AI learns (The "Dog" Example)
Imagine you want to teach a child what a dog is. You don't give them a list of rules like, *"A dog has four legs, fur, and a tail."* Instead, you point at dogs and say, "Dog!"
AI works the exact same way:
* We show a computer **millions of pictures** of dogs.
* The computer spots patterns (snouts, floppy ears, wagging tails).
* Soon, when it sees a new dog, it says: *"That's a dog!"*</div>
            </div>
          </div>

          <!-- Sub-Part 2 -->
          <div id="prac-4-2" class="colab-cell text-cell">
            <h2>Sub-Part 2: AI-Based Story Generation</h2>
            <h3>Problem Statement</h3>
            <p>Write a Python program to generate a short story on a topic entered by the user using Generative AI.</p>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[7]</span>
              </div>
              <div class="code-content">topic = <span class="tok-builtin">input</span>(<span class="tok-str">"Enter topic: "</span>)
prompt = f<span class="tok-str">"Write a short story on {topic}"</span>
response = model.generate_content(prompt)
<span class="tok-builtin">print</span>(response.text)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">Enter topic: machine learning
The servers in Basement Lab 4 hummed like a colony of digital cicadas. For six months, Dr. Elena Vance had lived on black coffee and cold bagels, chasing a ghost in the machine.

Aura was a neural network designed for a singular, monumental task: to translate the untranslatable.

Elena's dataset consisted of thousands of ancient, clay tablets from a lost Bronze Age civilization, the *Kiri*. For two millennia, the script had remained stubbornly undeciphered.

Elena was trying a different approach. She wasn't teaching Aura grammar rules. Instead, she was feeding the machine human emotion, context, and structural logic.

"Epoch 1," Elena whispered, clicking the run script.

At first, Aura was blind. Her "weights"—the millions of mathematical connections mimicking biological synapses—were entirely random noise.

Elena watched the monitor. "Gradient descent," she murmured.

With every mistake, Aura adjusted her parameters, taking a tiny step down a steep mathematical mountain toward understanding.

By Epoch 1,000, Aura had discovered nouns.</div>
            </div>
          </div>

          <!-- Sub-Part 3 -->
          <div id="prac-4-3" class="colab-cell text-cell">
            <h2>Sub-Part 3: Question Answering using Generative AI</h2>
            <h3>Problem Statement</h3>
            <p>Write a Python program that accepts a question from the user and generates an answer using Generative AI.</p>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[8]</span>
              </div>
              <div class="code-content">question = <span class="tok-builtin">input</span>(<span class="tok-str">"Ask anything: "</span>)
response = model.generate_content(question)
<span class="tok-builtin">print</span>(response.text)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">Ask anything: how does PYTHON WORKS?
To understand how Python works, it helps to look at it from two angles: **how your code is executed** and **what happens behind the scenes**.

Here is a step-by-step breakdown of how Python works, from the moment you write a line of code to when your computer actually runs it.

---

### Part 1: The 3-Step Execution Process

When you run a Python program (like `hello.py`), Python does not immediately run the code on the CPU. Instead, it follows this journey:

```text
[ Source Code (.py) ]
         │
         ▼ (Step 1: Compilation)
[ Bytecode (.pyc) ]
         │
         ▼ (Step 2: Python Virtual Machine - PVM)
[ Machine Code (0s & 1s) ]
         │
         ▼ (Step 3: Hardware Execution)
[ Computer CPU Runs It! ]
```</div>
            </div>
          </div>

          <!-- Sub-Part 4 -->
          <div id="prac-4-4" class="colab-cell text-cell">
            <h2>Sub-Part 4: Text Translation using Generative AI</h2>
            <h3>Problem Statement</h3>
            <p>Write a Python program to translate a given English sentence into Hindi using Generative AI.</p>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[9]</span>
              </div>
              <div class="code-content">text = <span class="tok-str">"Artificial Intelligence is the future."</span>
prompt = f<span class="tok-str">"Translate into Hindi:
{text}"</span>
response = model.generate_content(prompt)
<span class="tok-builtin">print</span>(response.text)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">Here is the translation of "Artificial Intelligence is the future" in Hindi:

**कृत्रिम बुद्धिमत्ता ही भविष्य है।**
(Pronounced: *Kritrim buddhimatta hi bhavishya hai*)

Alternatively, in modern/common Hindi, you can also say:
**आर्टिफिशियल इंटेलिजेंस ही भविष्य है।**</div>
            </div>
          </div>

          <!-- Sub-Part 5 -->
          <div id="prac-4-5" class="colab-cell text-cell">
            <h2>Sub-Part 5: Professional Content Generation</h2>
            <h3>Problem Statement</h3>
            <p>Write a Python program to generate a professional leave application for two days using Generative AI.</p>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[10]</span>
              </div>
              <div class="code-content">prompt = <span class="tok-str">"""
Write a professional leave application for 2 days.
"""</span>
response = model.generate_content(prompt)
<span class="tok-builtin">print</span>(response.text)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">Here are three professional templates you can use for a 2-day leave application. Choose the one that best fits your situation:

### Option 1: General/Personal Leave (Best for planned personal days)

**Subject:** Leave Application: [Your Name] – [Start Date] to [End Date]

Dear [Manager's Name],

I am writing to formally request two days of leave, starting from [Start Date] to [End Date]. I need to attend to some personal matters that require my presence.

Before my departure, I will ensure that all my pending tasks are up to date. I have also requested [Colleague's Name] to support any urgent queries during my absence.

Thank you for your understanding.

Sincerely,
[Your Name]
[Your Designation]</div>
            </div>
          </div>

          <!-- Sub-Part 6 -->
          <div id="prac-4-6" class="colab-cell text-cell">
            <h2>Sub-Part 6: Multiple-Choice Question Generation</h2>
            <h3>Problem Statement</h3>
            <p>Write a Python program to generate 10 multiple-choice questions with answers on a given topic using Generative AI.</p>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[11]</span>
              </div>
              <div class="code-content">topic = <span class="tok-str">"Machine Learning"</span>
prompt = f<span class="tok-str">"""
Generate 10 multiple-choice questions on {topic}
with answers.
"""</span>
response = model.generate_content(prompt)
<span class="tok-builtin">print</span>(response.text)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">### Question 1: Supervised vs. Unsupervised Learning
Which of the following algorithms is an example of **unsupervised learning**?
*   A) Linear Regression
*   B) K-Means Clustering
*   C) Decision Tree
*   D) Support Vector Machine (SVM)

**Answer: B) K-Means Clustering**
*Explanation:* Unsupervised learning deals with unlabeled data. K-Means clustering groups data points into clusters without predefined labels.

---

### Question 2: Classification Metrics
In a binary classification problem (e.g., spam detection), if a model predicts an email is "Spam" when it is actually "Not Spam", what is this called?
*   A) True Positive
*   B) False Negative (Type II error)
*   C) False Positive (Type I error)
*   D) True Negative

**Answer: C) False Positive (Type I error)**
*Explanation:* A False Positive occurs when the model incorrectly predicts the positive class (Spam) when the actual reality is negative (Not Spam).</div>
            </div>
          </div>

          <div class="colab-cell text-cell">
            <h3>Conclusion</h3>
            <p>The practical demonstrated different applications of Generative AI using Python and the Gemini API, including text generation, story generation, question answering, translation, professional content creation, and MCQ generation. The next-word prediction sub-part further demonstrated the basic principle of text generation by learning word-to-word relationships from sample sentences.</p>
          </div>
        </section>


        <!-- ==========================================
             PRACTICAL NO. 5
             ========================================== -->
        <section id="prac-5" class="practical-block">
          <div class="colab-cell text-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn" onclick="copyTextFromElement(this)">Copy Text</button></div>
            <h1>Practical No. 5: Text Generation and Prompt-Based Response Generation using Generative AI</h1>
            <h3>Aim</h3>
            <p>To understand and implement different text-generation applications using pre-trained Generative AI models and Python.</p>
            <h3>Theory</h3>
            <p>Generative AI models are capable of creating new text based on a given prompt. Pre-trained language models can be used to complete sentences, generate responses, and perform various natural language tasks. In this practical, two approaches to Generative AI are demonstrated. The first sub-part uses the GPT-2 pre-trained model through the Hugging Face Transformers library for local text generation. The second sub-part uses the Gemini API to generate a customer-service response based on a predefined company policy and customer message.</p>
            <h3>Software / Requirements</h3>
            <ul>
              <li>Python</li>
              <li>Google Colab / Jupyter Notebook</li>
              <li>Hugging Face Transformers</li>
              <li>PyTorch</li>
              <li>Gemini API</li>
              <li>Internet connection</li>
            </ul>
            <h3>General Algorithm</h3>
            <ol>
              <li>Start the program.</li>
              <li>Install and import the required libraries.</li>
              <li>Select the required Generative AI model.</li>
              <li>Provide an appropriate prompt or input.</li>
              <li>Generate text using the selected model.</li>
              <li>Display the generated response.</li>
              <li>Stop.</li>
            </ol>
          </div>

          <!-- Sub-Part 1: Local GPT-2 -->
          <div id="prac-5-1" class="colab-cell text-cell">
            <h2>Sub-Part 1: Local Text Generation using GPT-2</h2>
            <h3>Problem Statement</h3>
            <p>Write a Python program to generate and complete text using the pre-trained GPT-2 language model available through the Hugging Face Transformers library.</p>
            <h3>Theory</h3>
            <p>GPT-2 is a pre-trained language model developed for natural language generation. It predicts the next words based on the words already provided in a prompt. The Hugging Face <code>pipeline()</code> function provides a simple way to use pre-trained models for tasks such as text generation. In this program, GPT-2 generates text based on a starting sentence.</p>
            <h3>Algorithm</h3>
            <ol>
              <li>Install the transformers and torch libraries.</li>
              <li>Import the pipeline function from Transformers.</li>
              <li>Create a text-generation pipeline using GPT-2.</li>
              <li>Provide a starting sentence as the prompt.</li>
              <li>Generate text using the model.</li>
              <li>Set the maximum length of the generated text.</li>
              <li>Display the generated text.</li>
              <li>Stop.</li>
            </ol>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[12]</span>
              </div>
              <div class="code-content"><span class="tok-magic">!pip install transformers torch</span>
<span class="tok-kw">from</span> transformers <span class="tok-kw">import</span> pipeline

<span class="tok-kw">def</span> <span class="tok-fn">generate_local_text</span>(prompt_text: <span class="tok-builtin">str</span>):
    <span class="tok-builtin">print</span>(<span class="tok-str">"Loading model... (This may take a moment on the first run)"</span>)
    <span class="tok-comm"># Initialize a text-generation pipeline using standard open-source gpt2</span>
    generator = pipeline(<span class="tok-str">'text-generation'</span>, model=<span class="tok-str">'gpt2'</span>)
    <span class="tok-builtin">print</span>(<span class="tok-str">"Generating response..."</span>)
    <span class="tok-comm"># Generate text based on the prompt</span>
    outputs = generator(
        prompt_text,
        max_length=<span class="tok-num">60</span>,
        num_return_sequences=<span class="tok-num">1</span>,
        pad_token_id=<span class="tok-num">50256</span>  <span class="tok-comm"># Prevents warning output</span>
    )
    <span class="tok-kw">return</span> outputs[<span class="tok-num">0</span>][<span class="tok-str">'generated_text'</span>]

<span class="tok-kw">if</span> __name__ == <span class="tok-str">"__main__"</span>:
    <span class="tok-comm"># Give the model a starting sentence to complete</span>
    sample_prompt = <span class="tok-str">"Artificial Intelligence will change the future of programming by"</span>
    result = generate_local_text(sample_prompt)
    <span class="tok-builtin">print</span>(<span class="tok-str">"
--- Result ---"</span>)
    <span class="tok-builtin">print</span>(result)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">--- Result ---
Artificial Intelligence will change the future of programming by empowering the human mind and making it more powerful.

A big question for AI will be whether it can be used to perform complex tasks such as translating text, performing mathematical calculations,

In a paper published in the journal Current Biology, researchers from MIT and Stanford University found that AI can do these tasks without wo

They found the AI system can perform complex tasks even without humans, and this is the first time we have been able to successfully use AI t</div>
            </div>
          </div>

          <!-- Sub-Part 2: Customer Service -->
          <div id="prac-5-2" class="colab-cell text-cell">
            <h2>Sub-Part 2: Customer Service Response Generation using Gemini</h2>
            <h3>Problem Statement</h3>
            <p>Write a Python program to generate a polite customer-service email response using Generative AI based on a predefined refund policy and customer message.</p>
            <h3>Theory</h3>
            <p>Generative AI can generate context-specific responses by combining instructions, rules, and user input into a single prompt. This technique is commonly used in customer support applications. In this program, a refund policy and a customer email are provided to the Gemini model. The model uses the given policy to generate an appropriate and polite response.</p>
            <h3>Algorithm</h3>
            <ol>
              <li>Import the Gemini API library.</li>
              <li>Create a Gemini client using the API key.</li>
              <li>Define the company refund policy.</li>
              <li>Define the customer email.</li>
              <li>Combine the policy and customer message into a prompt.</li>
              <li>Send the prompt to the Gemini model.</li>
              <li>Generate the response.</li>
              <li>Display the drafted email reply.</li>
              <li>Stop.</li>
            </ol>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[13]</span>
              </div>
              <div class="code-content"><span class="tok-kw">import</span> os
<span class="tok-kw">from</span> google <span class="tok-kw">import</span> genai

client = genai.Client(api_key=<span class="tok-str">"AQ." + "Ab8RN6JkmZk7st62RATnSJpe-0NqOvT2JBmN-YSJ0eWorqxnVw"</span>)

<span class="tok-comm"># 1. Provide your custom rules</span>
refund_policy = <span class="tok-str">"Policy: We only allow refunds if the item is broken and reported within 7 days."</span>

<span class="tok-comm"># 2. Simulate an incoming customer message</span>
customer_email = <span class="tok-str">"Hi, I bought a shirt 2 days ago but the zipper is completely broken. Can I get my money back?"</span>

<span class="tok-comm"># 3. Combine rules and the message into a prompt</span>
prompt = f<span class="tok-str">"""
Use our company policy to answer the customer email politely.
{refund_policy}
Customer Email: {customer_email}
"""</span>

<span class="tok-comm"># 4. Generate the reply</span>
response = client.models.generate_content(
    model=<span class="tok-str">'gemini-3.5-flash'</span>,
    contents=prompt
)
<span class="tok-builtin">print</span>(<span class="tok-str">"Drafted Email Reply:"</span>)
<span class="tok-builtin">print</span>(response.text)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">Drafted Email Reply:
Subject: Refund Request - Broken Zipper

Hi there,

Thank you for reaching out to us, and I am so sorry to hear that the zipper on your new shirt is broken!

According to our company policy, we are happy to offer a full refund for any items that arrive damaged or broken, as long as it is reported within 7 days.

To help us process this for you as quickly as possible, could you please reply with your order number or a copy of your receipt?

Once we have that information, we will get your refund processed right away.

Thank you for your patience, and please let us know if you have any other questions!

Best regards,

[Your Name/Company Name]</div>
            </div>
          </div>

          <div class="colab-cell text-cell">
            <h3>Conclusion</h3>
            <p>The practical demonstrated two applications of Generative AI. The first sub-part used the GPT-2 pre-trained model to generate text from a given prompt. The second sub-part demonstrated how Gemini can generate a context-aware customer-service response by using predefined rules and customer information. Thus, the practical provided an understanding of both local text generation and prompt-based intelligent response generation.</p>
          </div>
        </section>


        <!-- ==========================================
             PRACTICAL NO. 6
             ========================================== -->
        <section id="prac-6" class="practical-block">
          <div class="colab-cell text-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn" onclick="copyTextFromElement(this)">Copy Text</button></div>
            <h1>Practical No. 6: Data Analysis and Visualization for AI-Based Insights</h1>
            <h3>Aim</h3>
            <p>To analyze a dataset using Python and perform data visualization to identify trends, patterns, and relationships that support Predictive AI and Machine Learning workflows.</p>
            <h3>Theory</h3>
            <p>Artificial Intelligence systems depend on data to identify patterns and generate useful insights. Before applying Machine Learning or Predictive AI techniques, it is important to understand the available data through Data Analysis and Visualization.</p>
            <p>Exploratory Data Analysis (EDA) is the process of examining and understanding a dataset using statistical methods and graphical representations.</p>
            <p>In this practical, the Superstore dataset is analyzed using Python libraries:</p>
            <ul>
              <li><strong>Pandas</strong> – used for loading, processing, grouping, and analyzing data.</li>
              <li><strong>Matplotlib</strong> – used for creating graphs and charts.</li>
              <li><strong>Seaborn</strong> – used for creating attractive statistical visualizations.</li>
            </ul>
            <p>Three types of analysis are performed:</p>
            <ol>
              <li><strong>Yearly Sales Trend</strong> – identifies how sales change over different years.</li>
              <li><strong>Sales by Category</strong> – compares total sales among different product categories.</li>
              <li><strong>Sales vs Profit</strong> – examines the relationship between sales and profit.</li>
            </ol>
            <p>These visualizations help understand the data before developing a Predictive AI/ML model. The analysis itself is not Generative AI; rather, it is a supporting stage in an AI workflow.</p>
            <h3>AI Workflow</h3>
            <p><code>Data → Data Analysis & Visualization → Machine Learning/Predictive AI → Predictions & Insights</code></p>
            <h3>Software and Requirements</h3>
            <ul>
              <li>Python 3.x</li>
              <li>Google Colab / Jupyter Notebook</li>
              <li>Pandas</li>
              <li>Matplotlib</li>
              <li>Seaborn</li>
              <li>Superstore Dataset (<code>Sample - Superstore.csv</code>)</li>
            </ul>
            <h3>General Algorithm</h3>
            <ol>
              <li>Start.</li>
              <li>Import the required Python libraries.</li>
              <li>Load the Superstore dataset using Pandas.</li>
              <li>Convert the Order Date column into datetime format.</li>
              <li>Group the sales data according to the year.</li>
              <li>Plot the yearly sales trend using a line chart.</li>
              <li>Calculate and visualize total sales for each category using a bar chart.</li>
              <li>Plot Sales against Profit using a scatter plot.</li>
              <li>Analyze the graphs to identify trends and relationships.</li>
              <li>Display the completion message.</li>
              <li>Stop.</li>
            </ol>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[14]</span>
              </div>
              <div class="code-content"><span class="tok-kw">import</span> pandas <span class="tok-kw">as</span> pd
<span class="tok-kw">import</span> matplotlib.pyplot <span class="tok-kw">as</span> plt
<span class="tok-kw">import</span> seaborn <span class="tok-kw">as</span> sns

<span class="tok-comm"># Load dataset</span>
df = pd.read_csv(<span class="tok-str">"/content/Sample - Superstore.csv"</span>, encoding=<span class="tok-str">'latin1'</span>)

<span class="tok-comm"># Convert Order Date to datetime</span>
df[<span class="tok-str">'Order Date'</span>] = pd.to_datetime(df[<span class="tok-str">'Order Date'</span>])

<span class="tok-comm"># 1. Sales trend over time</span>
df_grouped = df.groupby(df[<span class="tok-str">'Order Date'</span>].dt.year)[<span class="tok-str">'Sales'</span>].sum()
df_grouped.plot(kind=<span class="tok-str">'line'</span>, marker=<span class="tok-str">'o'</span>, title=<span class="tok-str">'Yearly Sales Trend'</span>)
plt.xlabel(<span class="tok-str">'Year'</span>)
plt.ylabel(<span class="tok-str">'Total Sales'</span>)
plt.show()

<span class="tok-comm"># 2. Sales by Category</span>
plt.figure(figsize=(<span class="tok-num">6</span>, <span class="tok-num">4</span>))
sns.barplot(x=df[<span class="tok-str">'Category'</span>], y=df[<span class="tok-str">'Sales'</span>], estimator=<span class="tok-builtin">sum</span>, ci=<span class="tok-kw">None</span>)
plt.title(<span class="tok-str">'Total Sales by Category'</span>)
plt.xticks(rotation=<span class="tok-num">45</span>)
plt.show()

<span class="tok-comm"># 3. Profit vs. Sales scatter plot</span>
plt.figure(figsize=(<span class="tok-num">6</span>, <span class="tok-num">4</span>))
sns.scatterplot(x=df[<span class="tok-str">'Sales'</span>], y=df[<span class="tok-str">'Profit'</span>], alpha=<span class="tok-num">0.5</span>)
plt.title(<span class="tok-str">'Sales vs Profit'</span>)
plt.xlabel(<span class="tok-str">'Sales'</span>)
plt.ylabel(<span class="tok-str">'Profit'</span>)
plt.show()</div>
            </div>

            <!-- Output with Visual Charts -->
            <div class="cell-output-wrapper">
              <div class="output-header"><svg viewBox="0 0 24 24" width="12" height="12" fill="#34a853"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> Visualizations Generated</div>
              
              <div class="output-plot-container">
                <!-- Plot 1: Yearly Sales Trend -->
                <div class="plot-card">
                  <svg viewBox="0 0 540 320" width="500" height="295" style="background:#fff; font-family:sans-serif;">
                    <text x="270" y="28" text-anchor="middle" font-size="16" font-weight="500" fill="#111">Yearly Sales Trend</text>
                    <text x="50" y="45" font-size="11" fill="#333">1e7</text>
                    <!-- Axes -->
                    <line x1="80" y1="50" x2="80" y2="250" stroke="#000" stroke-width="1.2"/>
                    <line x1="80" y1="250" x2="500" y2="250" stroke="#000" stroke-width="1.2"/>
                    <line x1="80" y1="50" x2="500" y2="50" stroke="#000" stroke-width="1.2"/>
                    <line x1="500" y1="50" x2="500" y2="250" stroke="#000" stroke-width="1.2"/>
                    <!-- Y Ticks -->
                    <text x="72" y="248" text-anchor="end" font-size="11" fill="#333">1.20</text>
                    <text x="72" y="215" text-anchor="end" font-size="11" fill="#333">1.22</text>
                    <text x="72" y="182" text-anchor="end" font-size="11" fill="#333">1.24</text>
                    <text x="72" y="149" text-anchor="end" font-size="11" fill="#333">1.26</text>
                    <text x="72" y="116" text-anchor="end" font-size="11" fill="#333">1.28</text>
                    <text x="72" y="83" text-anchor="end" font-size="11" fill="#333">1.30</text>
                    <text x="72" y="54" text-anchor="end" font-size="11" fill="#333">1.32</text>
                    <!-- X Ticks -->
                    <text x="105" y="268" font-size="11" fill="#333">1925</text>
                    <text x="155" y="268" font-size="11" fill="#333">1950</text>
                    <text x="205" y="268" font-size="11" fill="#333">1975</text>
                    <text x="255" y="268" font-size="11" fill="#333">2000</text>
                    <text x="305" y="268" font-size="11" fill="#333" font-weight="bold">2025</text>
                    <text x="355" y="268" font-size="11" fill="#333">2050</text>
                    <text x="405" y="268" font-size="11" fill="#333">2075</text>
                    <text x="455" y="268" font-size="11" fill="#333">2100</text>
                    <!-- Data Point -->
                    <circle cx="318" cy="142" r="5" fill="#1f77b4"/>
                    <!-- Labels -->
                    <text x="290" y="295" text-anchor="middle" font-size="13" fill="#111">Year</text>
                    <text x="24" y="150" text-anchor="middle" font-size="13" fill="#111" transform="rotate(-90,24,150)">Total Sales</text>
                  </svg>
                </div>

                <!-- Plot 2: Total Sales by Category -->
                <div class="plot-card">
                  <svg viewBox="0 0 540 320" width="500" height="295" style="background:#fff; font-family:sans-serif;">
                    <text x="270" y="28" text-anchor="middle" font-size="16" font-weight="500" fill="#111">Total Sales by Category</text>
                    <text x="45" y="45" font-size="11" fill="#333">1e6</text>
                    <!-- Axes -->
                    <line x1="75" y1="50" x2="75" y2="240" stroke="#000" stroke-width="1.2"/>
                    <line x1="75" y1="240" x2="490" y2="240" stroke="#000" stroke-width="1.2"/>
                    <line x1="75" y1="50" x2="490" y2="50" stroke="#000" stroke-width="1.2"/>
                    <line x1="490" y1="50" x2="490" y2="240" stroke="#000" stroke-width="1.2"/>
                    <!-- Y Ticks -->
                    <text x="68" y="244" text-anchor="end" font-size="11" fill="#333">0</text>
                    <text x="68" y="198" text-anchor="end" font-size="11" fill="#333">1</text>
                    <text x="68" y="152" text-anchor="end" font-size="11" fill="#333">2</text>
                    <text x="68" y="106" text-anchor="end" font-size="11" fill="#333">3</text>
                    <text x="68" y="60" text-anchor="end" font-size="11" fill="#333">4</text>
                    <!-- Bars -->
                    <!-- Office Supplies -->
                    <rect x="110" y="74" width="95" height="166" fill="#3274a1"/>
                    <!-- Technology -->
                    <rect x="235" y="55" width="95" height="185" fill="#3274a1"/>
                    <!-- Furniture -->
                    <rect x="360" y="64" width="95" height="176" fill="#3274a1"/>
                    <!-- X Labels rotated -->
                    <text x="145" y="260" font-size="11" fill="#222" transform="rotate(45,145,260)">Office Supplies</text>
                    <text x="270" y="260" font-size="11" fill="#222" transform="rotate(45,270,260)">Technology</text>
                    <text x="395" y="260" font-size="11" fill="#222" transform="rotate(45,395,260)">Furniture</text>
                    <text x="24" y="145" text-anchor="middle" font-size="13" fill="#111" transform="rotate(-90,24,145)">Sales</text>
                  </svg>
                </div>

                <!-- Plot 3: Sales vs Profit Scatter -->
                <div class="plot-card">
                  <svg viewBox="0 0 540 320" width="500" height="295" style="background:#fff; font-family:sans-serif;">
                    <text x="270" y="28" text-anchor="middle" font-size="16" font-weight="500" fill="#111">Sales vs Profit</text>
                    <!-- Box border -->
                    <line x1="75" y1="45" x2="75" y2="250" stroke="#000" stroke-width="1.2"/>
                    <line x1="75" y1="250" x2="500" y2="250" stroke="#000" stroke-width="1.2"/>
                    <line x1="75" y1="45" x2="500" y2="45" stroke="#000" stroke-width="1.2"/>
                    <line x1="500" y1="45" x2="500" y2="250" stroke="#000" stroke-width="1.2"/>
                    <!-- Y Ticks -->
                    <text x="68" y="245" text-anchor="end" font-size="10" fill="#333">-6000</text>
                    <text x="68" y="215" text-anchor="end" font-size="10" fill="#333">-4000</text>
                    <text x="68" y="185" text-anchor="end" font-size="10" fill="#333">-2000</text>
                    <text x="68" y="155" text-anchor="end" font-size="10" fill="#333">0</text>
                    <text x="68" y="125" text-anchor="end" font-size="10" fill="#333">2000</text>
                    <text x="68" y="95" text-anchor="end" font-size="10" fill="#333">4000</text>
                    <text x="68" y="65" text-anchor="end" font-size="10" fill="#333">6000</text>
                    <text x="68" y="48" text-anchor="end" font-size="10" fill="#333">8000</text>
                    <!-- X Ticks -->
                    <text x="75" y="266" font-size="10" fill="#333">0</text>
                    <text x="175" y="266" font-size="10" fill="#333">5000</text>
                    <text x="275" y="266" font-size="10" fill="#333">10000</text>
                    <text x="375" y="266" font-size="10" fill="#333">15000</text>
                    <text x="475" y="266" font-size="10" fill="#333">20000</text>
                    <!-- Axis Labels -->
                    <text x="287" y="290" text-anchor="middle" font-size="12" fill="#111">Sales</text>
                    <text x="22" y="150" text-anchor="middle" font-size="12" fill="#111" transform="rotate(-90,22,150)">Profit</text>
                    <!-- Scatter cluster dots -->
                    <g fill="#4e90c6" opacity="0.6">
                      <circle cx="85" cy="154" r="3"/><circle cx="92" cy="152" r="3.5"/><circle cx="98" cy="156" r="3"/><circle cx="104" cy="150" r="3"/>
                      <circle cx="110" cy="160" r="3"/><circle cx="115" cy="148" r="3.5"/><circle cx="125" cy="142" r="3"/><circle cx="130" cy="168" r="3"/>
                      <circle cx="138" cy="138" r="3"/><circle cx="145" cy="172" r="3.5"/><circle cx="152" cy="134" r="3"/><circle cx="160" cy="130" r="3"/>
                      <circle cx="170" cy="126" r="3.5"/><circle cx="178" cy="180" r="3"/><circle cx="185" cy="122" r="3"/><circle cx="195" cy="190" r="3"/>
                      <circle cx="205" cy="116" r="3.5"/><circle cx="218" cy="205" r="3"/><circle cx="230" cy="110" r="3"/><circle cx="242" cy="225" r="3"/>
                      <circle cx="260" cy="100" r="3.5"/><circle cx="280" cy="90" r="4"/><circle cx="310" cy="85" r="4"/><circle cx="370" cy="62" r="4.5"/>
                      <circle cx="480" cy="175" r="4"/><circle cx="170" cy="245" r="3.5"/>
                    </g>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <div class="colab-cell text-cell">
            <h3>Interpretation</h3>
            <p>The generated visualizations provide useful insights into the dataset:</p>
            <ul>
              <li>The <strong>Yearly Sales Trend</strong> helps identify whether sales are increasing or decreasing over time.</li>
              <li>The <strong>Sales by Category</strong> graph helps identify which product category contributes the most to total sales.</li>
              <li>The <strong>Sales vs Profit</strong> scatter plot helps understand the relationship between sales and profit.</li>
            </ul>
            <p>These observations can be useful for making business decisions and can also serve as a foundation for developing Predictive AI and Machine Learning models.</p>
            <h3>Conclusion</h3>
            <p>The practical successfully demonstrates Data Analysis and Visualization using Python. Pandas was used for data processing, while Matplotlib and Seaborn were used to visualize sales trends, category-wise sales, and the relationship between sales and profit.</p>
          </div>
        </section>


        <!-- ==========================================
             PRACTICAL NO. 7
             ========================================== -->
        <section id="prac-7" class="practical-block">
          <div class="colab-cell text-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn" onclick="copyTextFromElement(this)">Copy Text</button></div>
            <h1>Practical No. 7: Dimensionality Reduction using PCA</h1>
            <h3>Aim</h3>
            <p>To implement Principal Component Analysis (PCA) using Python and reduce the dimensions of the Wine dataset for visualization.</p>
            <h3>Theory</h3>
            <p>PCA (Principal Component Analysis) is a dimensionality reduction technique used in Machine Learning. It converts a dataset with many features into a smaller number of principal components while retaining important information.</p>
            <p>In this practical, the Wine dataset containing 13 features is standardized and reduced to 2 principal components. The reduced data is then visualized using a scatter plot.</p>
            <h3>Software and Requirements</h3>
            <ul>
              <li>Python 3.x</li>
              <li>Google Colab / Jupyter Notebook</li>
              <li>Pandas</li>
              <li>Matplotlib</li>
              <li>Scikit-learn</li>
            </ul>
            <h3>Algorithm</h3>
            <ol>
              <li>Import the required libraries.</li>
              <li>Load the Wine dataset.</li>
              <li>Create a DataFrame from the dataset.</li>
              <li>Standardize the features.</li>
              <li>Apply PCA with 2 components.</li>
              <li>Plot the two principal components.</li>
              <li>Display the graph.</li>
              <li>Stop.</li>
            </ol>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[15]</span>
              </div>
              <div class="code-content"><span class="tok-kw">import</span> pandas <span class="tok-kw">as</span> pd
<span class="tok-kw">import</span> matplotlib.pyplot <span class="tok-kw">as</span> plt
<span class="tok-kw">from</span> sklearn.decomposition <span class="tok-kw">import</span> PCA
<span class="tok-kw">from</span> sklearn.preprocessing <span class="tok-kw">import</span> StandardScaler
<span class="tok-kw">from</span> sklearn.datasets <span class="tok-kw">import</span> load_wine

<span class="tok-comm"># Load dataset</span>
data = load_wine()

<span class="tok-comm"># Create DataFrame</span>
df = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

<span class="tok-comm"># Standardize data</span>
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

<span class="tok-comm"># Apply PCA</span>
pca = PCA(n_components=<span class="tok-num">2</span>)
pca_data = pca.fit_transform(df_scaled)

<span class="tok-comm"># Display reduced dimensions</span>
<span class="tok-builtin">print</span>(<span class="tok-str">"Original Features:"</span>, df.shape[<span class="tok-num">1</span>])
<span class="tok-builtin">print</span>(<span class="tok-str">"Reduced Features:"</span>, pca_data.shape[<span class="tok-num">1</span>])

<span class="tok-comm"># Visualize PCA results</span>
plt.scatter(
    pca_data[:, <span class="tok-num">0</span>],
    pca_data[:, <span class="tok-num">1</span>],
    c=data.target,
    cmap=<span class="tok-str">"viridis"</span>,
    edgecolors=<span class="tok-str">"k"</span>
)
plt.xlabel(<span class="tok-str">"Principal Component 1"</span>)
plt.ylabel(<span class="tok-str">"Principal Component 2"</span>)
plt.title(<span class="tok-str">"PCA on Wine Dataset"</span>)
plt.show()</div>
            </div>

            <!-- Output block with Viridis Scatter Chart -->
            <div class="cell-output-wrapper">
              <div class="output-text">Original Features: 13
Reduced Features: 2</div>
              <div class="output-plot-container">
                <div class="plot-card">
                  <svg viewBox="0 0 540 330" width="500" height="305" style="background:#fff; font-family:sans-serif;">
                    <text x="270" y="24" text-anchor="middle" font-size="15" font-weight="500" fill="#111">PCA on Wine Quality Dataset</text>
                    <!-- Box border -->
                    <line x1="75" y1="40" x2="75" y2="270" stroke="#000" stroke-width="1.2"/>
                    <line x1="75" y1="270" x2="490" y2="270" stroke="#000" stroke-width="1.2"/>
                    <line x1="75" y1="40" x2="490" y2="40" stroke="#000" stroke-width="1.2"/>
                    <line x1="490" y1="40" x2="490" y2="270" stroke="#000" stroke-width="1.2"/>
                    <!-- Y Ticks -->
                    <text x="68" y="274" text-anchor="end" font-size="10" fill="#333">-4</text>
                    <text x="68" y="245" text-anchor="end" font-size="10" fill="#333">-3</text>
                    <text x="68" y="216" text-anchor="end" font-size="10" fill="#333">-2</text>
                    <text x="68" y="187" text-anchor="end" font-size="10" fill="#333">-1</text>
                    <text x="68" y="158" text-anchor="end" font-size="10" fill="#333">0</text>
                    <text x="68" y="129" text-anchor="end" font-size="10" fill="#333">1</text>
                    <text x="68" y="100" text-anchor="end" font-size="10" fill="#333">2</text>
                    <text x="68" y="71" text-anchor="end" font-size="10" fill="#333">3</text>
                    <!-- X Ticks -->
                    <text x="100" y="286" font-size="10" fill="#333">-4</text>
                    <text x="195" y="286" font-size="10" fill="#333">-2</text>
                    <text x="285" y="286" font-size="10" fill="#333">0</text>
                    <text x="380" y="286" font-size="10" fill="#333">2</text>
                    <text x="470" y="286" font-size="10" fill="#333">4</text>
                    <!-- Axis Labels -->
                    <text x="282" y="310" text-anchor="middle" font-size="12" fill="#111">Principal Component 1</text>
                    <text x="24" y="155" text-anchor="middle" font-size="12" fill="#111" transform="rotate(-90,24,155)">Principal Component 2</text>
                    
                    <!-- Cluster 1: Yellow (Top Left) -->
                    <g fill="#fde725" stroke="#000" stroke-width="1.2">
                      <circle cx="160" cy="90" r="4.5"/><circle cx="170" cy="78" r="4.5"/><circle cx="180" cy="85" r="4.5"/><circle cx="165" cy="115" r="4.5"/>
                      <circle cx="190" cy="100" r="4.5"/><circle cx="155" cy="105" r="4.5"/><circle cx="175" cy="120" r="4.5"/><circle cx="195" cy="110" r="4.5"/>
                      <circle cx="185" cy="72" r="4.5"/><circle cx="170" cy="135" r="4.5"/><circle cx="160" cy="140" r="4.5"/><circle cx="200" cy="140" r="4.5"/>
                      <circle cx="145" cy="100" r="4.5"/><circle cx="130" cy="115" r="4.5"/><circle cx="120" cy="128" r="4.5"/><circle cx="215" cy="65" r="4.5"/>
                    </g>
                    <!-- Cluster 2: Teal (Bottom Center) -->
                    <g fill="#21918c" stroke="#000" stroke-width="1.2">
                      <circle cx="200" cy="170" r="4.5"/><circle cx="215" cy="180" r="4.5"/><circle cx="230" cy="195" r="4.5"/><circle cx="245" cy="188" r="4.5"/>
                      <circle cx="260" cy="210" r="4.5"/><circle cx="275" cy="205" r="4.5"/><circle cx="290" cy="220" r="4.5"/><circle cx="305" cy="215" r="4.5"/>
                      <circle cx="320" cy="235" r="4.5"/><circle cx="300" cy="245" r="4.5"/><circle cx="265" cy="230" r="4.5"/><circle cx="250" cy="225" r="4.5"/>
                      <circle cx="340" cy="210" r="4.5"/><circle cx="355" cy="190" r="4.5"/><circle cx="330" cy="185" r="4.5"/><circle cx="310" cy="265" r="4.5"/>
                    </g>
                    <!-- Cluster 3: Deep Purple (Right) -->
                    <g fill="#440154" stroke="#000" stroke-width="1.2">
                      <circle cx="370" cy="130" r="4.5"/><circle cx="385" cy="115" r="4.5"/><circle cx="400" cy="100" r="4.5"/><circle cx="415" cy="95" r="4.5"/>
                      <circle cx="430" cy="110" r="4.5"/><circle cx="445" cy="120" r="4.5"/><circle cx="420" cy="135" r="4.5"/><circle cx="405" cy="145" r="4.5"/>
                      <circle cx="390" cy="155" r="4.5"/><circle cx="425" cy="150" r="4.5"/><circle cx="435" cy="140" r="4.5"/><circle cx="450" cy="105" r="4.5"/>
                      <circle cx="465" cy="90" r="4.5"/><circle cx="475" cy="80" r="4.5"/><circle cx="410" cy="75" r="4.5"/><circle cx="425" cy="85" r="4.5"/>
                    </g>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <div class="colab-cell text-cell">
            <h3>Conclusion</h3>
            <p>The practical demonstrated the implementation of PCA on the Wine dataset. It showed how high-dimensional data (13 features) can be effectively reduced to 2 principal components for 2D visualization while preserving the cluster structures of the classes.</p>
          </div>
        </section>


        <!-- ==========================================
             PRACTICAL NO. 8
             ========================================== -->
        <section id="prac-8" class="practical-block">
          <div class="colab-cell text-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn" onclick="copyTextFromElement(this)">Copy Text</button></div>
            <h1>Practical No. 8: Statistical Analysis and Hypothesis Testing for AI</h1>
            <h3>Aim</h3>
            <p>To apply statistical techniques in Python for analyzing data and understanding how ANOVA and hypothesis testing support data-driven and AI-based decision-making.</p>
            <h3>Objectives</h3>
            <ul>
              <li>Perform One-Way ANOVA to compare multiple groups and apply a post-hoc test.</li>
              <li>Perform One-Sample T-Test to compare a sample mean with a hypothesized population mean.</li>
              <li>Perform Two-Sample T-Test to compare the means of two independent groups.</li>
              <li>Perform Paired T-Test to compare before-and-after measurements.</li>
              <li>Formulate hypotheses and interpret the test results.</li>
            </ul>
            <h3>Theory</h3>
            <p>Hypothesis Testing is a statistical method used to determine whether there is sufficient evidence to support a claim about data.</p>
            <p>ANOVA (Analysis of Variance) is used to compare the means of three or more groups. If ANOVA shows a significant difference, post-hoc tests (such as Tukey HSD) are performed.</p>
            <p>T-Tests are used to compare means. One-sample, two-sample, and paired t-tests are used for different types of comparisons.</p>
            <p>In AI and Machine Learning, statistical testing helps in data analysis, feature evaluation, model evaluation, and evidence-based decision-making.</p>
          </div>

          <!-- Part A: One-Way ANOVA -->
          <div id="prac-8-a" class="colab-cell text-cell">
            <h2>Part A: One-Way ANOVA</h2>
            <h3>Problem Statement</h3>
            <p>Consider the exam scores of students from three different classes. Perform a One-Way ANOVA test to determine whether there is a significant difference in the mean exam scores among the classes. If significant, perform a Tukey HSD post-hoc test.</p>
            <p><code>Class A: [85, 90, 88, 82, 87]</code><br>
               <code>Class B: [76, 78, 80, 81, 75]</code><br>
               <code>Class C: [92, 88, 94, 89, 90]</code></p>
            <h3>Hypothesis</h3>
            <ul>
              <li><strong>H₀ (Null Hypothesis):</strong> There is no significant difference in the mean scores of the three classes.</li>
              <li><strong>H₁ (Alternative Hypothesis):</strong> There is a significant difference in the mean scores of at least one class.</li>
            </ul>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[16]</span>
              </div>
              <div class="code-content"><span class="tok-kw">import</span> numpy <span class="tok-kw">as</span> np
<span class="tok-kw">from</span> scipy <span class="tok-kw">import</span> stats
<span class="tok-kw">from</span> statsmodels.stats.multicomp <span class="tok-kw">import</span> pairwise_tukeyhsd

<span class="tok-comm"># Data: exam scores for each class</span>
class_A = [<span class="tok-num">85</span>, <span class="tok-num">90</span>, <span class="tok-num">88</span>, <span class="tok-num">82</span>, <span class="tok-num">87</span>]
class_B = [<span class="tok-num">76</span>, <span class="tok-num">78</span>, <span class="tok-num">80</span>, <span class="tok-num">81</span>, <span class="tok-num">75</span>]
class_C = [<span class="tok-num">92</span>, <span class="tok-num">88</span>, <span class="tok-num">94</span>, <span class="tok-num">89</span>, <span class="tok-num">90</span>]

<span class="tok-comm"># Perform One-Way ANOVA</span>
f_statistic, p_value = stats.f_oneway(
    class_A, class_B, class_C
)

<span class="tok-comm"># Display results</span>
<span class="tok-builtin">print</span>(<span class="tok-str">"F-Statistic:"</span>, f_statistic)
<span class="tok-builtin">print</span>(<span class="tok-str">"P-Value:"</span>, p_value)

<span class="tok-comm"># Draw conclusion</span>
alpha = <span class="tok-num">0.05</span>
<span class="tok-kw">if</span> p_value &lt; alpha:
    <span class="tok-builtin">print</span>(<span class="tok-str">"Reject the Null Hypothesis: There is a significant difference in the mean exam scores."</span>)
<span class="tok-kw">else</span>:
    <span class="tok-builtin">print</span>(<span class="tok-str">"Fail to Reject the Null Hypothesis: There is no significant difference in the mean exam scores."</span>)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">F-Statistic: 28.583333333333343
P-Value: 2.727133500331835e-05
Reject the Null Hypothesis: There is a significant difference in the mean exam scores.</div>
            </div>
          </div>

          <div class="colab-cell text-cell">
            <h3>Interpretation</h3>
            <p>Since the p-value is less than 0.05, the null hypothesis is rejected. There is a significant difference between the mean scores of the classes. The Tukey test identifies which specific groups differ.</p>
          </div>

          <!-- Part B: One-Sample T-Test -->
          <div id="prac-8-b" class="colab-cell text-cell">
            <h2>Part B: One-Sample T-Test</h2>
            <h3>Problem Statement</h3>
            <p>Consider the following student scores and compare their mean with a hypothesized population mean of 70 using a One-Sample T-Test.</p>
            <p><code>Student Scores: [72, 88, 64, 74, 67, 79, 85, 75, 89, 77]</code></p>
            <h3>Hypothesis</h3>
            <ul>
              <li><strong>H₀:</strong> The sample mean is equal to 70.</li>
              <li><strong>H₁:</strong> The sample mean is significantly different from 70.</li>
            </ul>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[17]</span>
              </div>
              <div class="code-content"><span class="tok-kw">import</span> scipy.stats <span class="tok-kw">as</span> stats
<span class="tok-kw">import</span> numpy <span class="tok-kw">as</span> np

<span class="tok-comm"># Given student scores</span>
student_scores = [<span class="tok-num">72</span>, <span class="tok-num">88</span>, <span class="tok-num">64</span>, <span class="tok-num">74</span>, <span class="tok-num">67</span>, <span class="tok-num">79</span>, <span class="tok-num">85</span>, <span class="tok-num">75</span>, <span class="tok-num">89</span>, <span class="tok-num">77</span>]

<span class="tok-comm"># Hypothesized population mean</span>
hypothesized_mean = <span class="tok-num">70</span>

<span class="tok-comm"># Perform one-sample t-test</span>
t_statistic, p_value = stats.ttest_1samp(
    student_scores,
    hypothesized_mean
)

<span class="tok-comm"># Output the results</span>
<span class="tok-builtin">print</span>(f<span class="tok-str">"T-statistic: {t_statistic}"</span>)
<span class="tok-builtin">print</span>(f<span class="tok-str">"P-value: {p_value}"</span>)

<span class="tok-comm"># Interpretation</span>
alpha = <span class="tok-num">0.05</span>
<span class="tok-kw">if</span> p_value &lt; alpha:
    <span class="tok-builtin">print</span>(<span class="tok-str">"Reject the null hypothesis: The sample mean is significantly different from 70."</span>)
<span class="tok-kw">else</span>:
    <span class="tok-builtin">print</span>(<span class="tok-str">"Fail to reject the null hypothesis: The sample mean is not significantly different from 70."</span>)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">T-statistic: 2.6249999999999996
P-value: 0.027583862030934297
Reject the null hypothesis: The sample mean is significantly different from 70.</div>
            </div>
          </div>

          <div class="colab-cell text-cell">
            <h3>Interpretation</h3>
            <p>If the p-value is less than 0.05, the null hypothesis is rejected, indicating that the sample mean is significantly different from the hypothesized mean of 70.</p>
          </div>

          <!-- Part C: Two-Sample T-Test -->
          <div id="prac-8-c" class="colab-cell text-cell">
            <h2>Part C: Two-Sample T-Test</h2>
            <h3>Problem Statement</h3>
            <p>A company wants to compare the time taken to complete a task between two groups of employees.</p>
            <p><code>Group I – Experience (0–1 year): [85, 95, 100, 80, 90, 97, 104, 95, 88, 92, 94, 99]</code><br>
               <code>Group II – Experience (1–2 years): [83, 85, 96, 92, 100, 104, 94, 95, 88, 90, 93, 94]</code></p>
            <p>Perform a Two-Sample T-Test.</p>
            <h3>Hypothesis</h3>
            <ul>
              <li><strong>H₀:</strong> There is no significant difference in the mean task completion times.</li>
              <li><strong>H₁:</strong> There is a significant difference in the mean task completion times.</li>
            </ul>
          </div>

          <div class="colab-cell code-cell">
            <div class="cell-hover-bar"><button class="cell-action-btn copy-btn" onclick="copyCode(this)">Copy Code</button></div>
            <div class="code-editor-row">
              <div class="run-gutter">
                <button class="run-btn" onclick="simulateRun(this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
                <span class="execution-counter">[18]</span>
              </div>
              <div class="code-content"><span class="tok-kw">import</span> scipy.stats <span class="tok-kw">as</span> stats
<span class="tok-kw">import</span> numpy <span class="tok-kw">as</span> np

<span class="tok-comm"># Data for both groups</span>
group1 = [<span class="tok-num">85</span>, <span class="tok-num">95</span>, <span class="tok-num">100</span>, <span class="tok-num">80</span>, <span class="tok-num">90</span>, <span class="tok-num">97</span>, <span class="tok-num">104</span>, <span class="tok-num">95</span>, <span class="tok-num">88</span>, <span class="tok-num">92</span>, <span class="tok-num">94</span>, <span class="tok-num">99</span>]
group2 = [<span class="tok-num">83</span>, <span class="tok-num">85</span>, <span class="tok-num">96</span>, <span class="tok-num">92</span>, <span class="tok-num">100</span>, <span class="tok-num">104</span>, <span class="tok-num">94</span>, <span class="tok-num">95</span>, <span class="tok-num">88</span>, <span class="tok-num">90</span>, <span class="tok-num">93</span>, <span class="tok-num">94</span>]

<span class="tok-comm"># Perform Two-Sample T-Test</span>
t_stat, p_value = stats.ttest_ind(group1, group2)

<span class="tok-comm"># Display the result</span>
<span class="tok-builtin">print</span>(f<span class="tok-str">"T-statistic: {t_stat}"</span>)
<span class="tok-builtin">print</span>(f<span class="tok-str">"P-value: {p_value}"</span>)

<span class="tok-comm"># Hypothesis testing conclusion</span>
alpha = <span class="tok-num">0.05</span>
<span class="tok-kw">if</span> p_value &lt; alpha:
    <span class="tok-builtin">print</span>(<span class="tok-str">"Reject the null hypothesis: There is a significant difference in the mean times."</span>)
<span class="tok-kw">else</span>:
    <span class="tok-builtin">print</span>(<span class="tok-str">"Fail to reject the null hypothesis: There is no significant difference in the mean times."</span>)</div>
            </div>
            <div class="cell-output-wrapper">
              <div class="output-text">T-statistic: 0.16119885358127883
P-value: 0.8734079490313532
Fail to reject the null hypothesis: There is no significant difference in the mean times.</div>
            </div>
          </div>

          <div class="colab-cell text-cell">
            <h3>Interpretation</h3>
            <p>If the p-value is greater than 0.05, the null hypothesis is not rejected. Therefore, there is no statistically significant difference between the mean task completion times of the two groups.</p>
            <h3>Conclusion</h3>
            <p>ANOVA and different types of T-Tests were successfully performed using Python. These statistical techniques help in validating patterns, comparing groups, and supporting data-driven decisions in AI and Machine Learning applications.</p>
          </div>
        </section>

      </div>
    </main>
  </div>

  <!-- Hardware Info Modal -->
  <div class="modal-overlay" id="hwModal" onclick="closeHardwareModal(event)">
    <div class="hw-modal" onclick="event.stopPropagation()">
      <h3>
        Backend Resources
        <span style="font-size: 12px; color: #34a853; font-weight: normal;">● Connected</span>
      </h3>
      <p style="font-size: 12px; color: var(--colab-text-secondary); margin-bottom: 12px;">
        Python 3 Google Compute Engine backend (GPU T4)
      </p>
      
      <div class="hw-stat-row">
        <span>System RAM:</span>
        <span>0.86 GB / 12.68 GB (7%)</span>
      </div>
      <div class="meter-bar" style="height: 6px; margin-bottom: 12px;"><div class="meter-fill" style="width: 7%;"></div></div>

      <div class="hw-stat-row">
        <span>Disk Storage:</span>
        <span>24.31 GB / 107.72 GB (22%)</span>
      </div>
      <div class="meter-bar" style="height: 6px; margin-bottom: 16px;"><div class="meter-fill" style="width: 22%;"></div></div>

      <div class="hw-stat-row">
        <span>Runtime shape:</span>
        <span>Standard</span>
      </div>
      <div class="hw-stat-row">
        <span>Accelerator:</span>
        <span>T4 GPU</span>
      </div>

      <button class="modal-close-btn" onclick="closeHardwareModal()">Close</button>
    </div>
  </div>

  <!-- Toast Notification element -->
  <div class="toast-msg" id="toast">
    <svg viewBox="0 0 24 24" width="16" height="16" fill="#34a853"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
    <span id="toast-text">Action completed</span>
  </div>

  <script>
    // Theme Toggle Functionality
    function toggleTheme() {
      const current = document.body.getAttribute('data-theme') || 'light';
      const target = current === 'dark' ? 'light' : 'dark';
      document.body.setAttribute('data-theme', target);
      localStorage.setItem('colab_theme', target);
      document.getElementById('theme-icon').textContent = target === 'dark' ? '☀️' : '🌙';
      showToast(`Switched to ${target} mode`);
    }

    // Load saved theme
    (function initTheme() {
      const saved = localStorage.getItem('colab_theme');
      if (saved) {
        document.body.setAttribute('data-theme', saved);
        const icon = document.getElementById('theme-icon');
        if (icon) icon.textContent = saved === 'dark' ? '☀️' : '🌙';
      }
    })();

    // Collapsible Left Drawer (Table of Contents)
    function toggleDrawer() {
      const drawer = document.getElementById('colabDrawer');
      const btn = document.getElementById('btn-toc');
      drawer.classList.toggle('collapsed');
      btn.classList.toggle('active', !drawer.classList.contains('collapsed'));
    }

    // Toast Notification helper
    let toastTimer;
    function showToast(msg) {
      const toast = document.getElementById('toast');
      const text = document.getElementById('toast-text');
      text.textContent = msg;
      toast.classList.add('show');
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => {
        toast.classList.remove('show');
      }, 2200);
    }

    // Copy Code from individual code cell
    function copyCode(btn) {
      const codeCell = btn.closest('.code-cell');
      const codeContent = codeCell.querySelector('.code-content');
      const rawText = codeContent.innerText;
      
      navigator.clipboard.writeText(rawText).then(() => {
        btn.classList.add('copied');
        const origHtml = btn.innerHTML;
        btn.innerHTML = '✓ Copied!';
        showToast('Code copied to clipboard');
        setTimeout(() => {
          btn.classList.remove('copied');
          btn.innerHTML = origHtml;
        }, 1800);
      }).catch(err => {
        console.error('Copy failed:', err);
      });
    }

    // Copy Text from markdown text cell
    function copyTextFromElement(btn) {
      const cell = btn.closest('.text-cell');
      const text = cell.innerText;
      navigator.clipboard.writeText(text).then(() => {
        showToast('Text copied to clipboard');
      });
    }

    // Copy All Code across all practicals
    function copyAllPracticals() {
      const codeBlocks = document.querySelectorAll('.code-content');
      let combined = '';
      codeBlocks.forEach((cb, idx) => {
        combined += `\n# --- CELL ${idx + 1} ---\n` + cb.innerText + '\n';
      });
      navigator.clipboard.writeText(combined.trim()).then(() => {
        showToast('All practicals code copied to clipboard!');
      });
    }

    // Simulate Running a cell
    function simulateRun(btn) {
      btn.classList.add('running');
      btn.innerHTML = '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 4V1L8 5l4 4V6c3.31 0 6 2.69 6 6 0 1.01-.25 1.97-.7 2.8l1.46 1.46A7.93 7.93 0 0020 12c0-4.42-3.58-8-8-8zm0 14c-3.31 0-6-2.69-6-6 0-1.01.25-1.97.7-2.8L5.24 7.74A7.93 7.93 0 004 12c0 4.42 3.58 8 8 8v3l4-4-4-4v3z"/></svg>';
      
      setTimeout(() => {
        btn.classList.remove('running');
        btn.innerHTML = '<svg viewBox="0 0 24 24" width="14" height="14" fill="#34a853"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>';
        showToast('Cell executed successfully in 0.35s');
        setTimeout(() => {
          btn.innerHTML = '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>';
        }, 1500);
      }, 450);
    }

    function runAllCells() {
      showToast('Running all notebook cells...');
      const runBtns = document.querySelectorAll('.run-btn');
      runBtns.forEach((btn, idx) => {
        setTimeout(() => simulateRun(btn), idx * 120);
      });
    }

    // Smooth Scroll to practical
    function scrollToPractical(id) {
      if (!id) return;
      const target = document.getElementById(id);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        // highlight briefly
        target.style.outline = '2px solid var(--colab-accent-blue)';
        setTimeout(() => { target.style.outline = ''; }, 1600);
      }
    }

    // Live Search & Filter
    function filterNotebook(query) {
      const q = query.trim().toLowerCase();
      const sections = document.querySelectorAll('.practical-block');
      
      sections.forEach(sec => {
        if (!q) {
          sec.style.display = 'block';
          return;
        }
        const text = sec.innerText.toLowerCase();
        if (text.includes(q)) {
          sec.style.display = 'block';
        } else {
          sec.style.display = 'none';
        }
      });
    }

    function focusSearch() {
      const inp = document.getElementById('searchInput');
      inp.focus();
      inp.select();
    }

    function triggerSearch() {
      focusSearch();
    }

    // Hardware Modal open/close
    function openHardwareModal() {
      document.getElementById('hwModal').classList.add('active');
    }
    function closeHardwareModal() {
      document.getElementById('hwModal').classList.remove('active');
    }

    // Copy Current URL
    function copyCurrentUrl() {
      navigator.clipboard.writeText(window.location.href).then(() => {
        showToast('Notebook URL copied');
      });
    }

    // Keyboard shortcut Ctrl+F / Cmd+F to focus internal search
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'f') {
        e.preventDefault();
        focusSearch();
      }
    });
  </script>
</body>
</html>
