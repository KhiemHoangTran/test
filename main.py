import http.server
import socketserver
import webbrowser
import threading

PORT = 8080

HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SPHEREx Sky Explorer - NASA Space Apps</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body { background-color: #0b0f19; color: #e2e8f0; font-family: system-ui, -apple-system, sans-serif; }
    canvas { image-rendering: pixelated; }
  </style>
</head>
<body class="min-h-screen flex flex-col">

  <header class="bg-slate-900 border-b border-slate-800 px-6 py-4 flex flex-wrap justify-between items-center gap-4">
    <div class="flex items-center space-x-3">
      <div class="w-3 h-3 rounded-full bg-indigo-500 animate-pulse"></div>
      <h1 class="text-xl font-bold tracking-wider bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent">
        SPHEREx SKY EXPLORER
      </h1>
      <span class="text-xs bg-indigo-950 text-indigo-300 border border-indigo-800 px-2 py-0.5 rounded">Python Local Server</span>
    </div>
    <button id="shareBtn" class="text-sm bg-slate-800 hover:bg-slate-700 border border-slate-700 px-3 py-1.5 rounded transition">
      🔗 Sao chép URL tọa độ
    </button>
  </header>

  <main class="flex-1 grid grid-cols-1 lg:grid-cols-12 gap-6 p-6 max-w-7xl w-full mx-auto">

    <!-- Cột điều khiển -->
    <section class="lg:col-span-4 space-y-5 bg-slate-900/70 p-5 rounded-xl border border-slate-800 h-fit">
      <div>
        <h2 class="text-sm font-semibold uppercase tracking-wider text-slate-400 mb-3">1. Tọa độ & Mục tiêu</h2>
        <label class="block text-xs text-slate-400 mb-1">Mục tiêu thử nghiệm (Presets)</label>
        <select id="presetSelect" class="w-full bg-slate-950 border border-slate-700 rounded p-2 text-sm mb-3 outline-none">
          <option value="wise0855">WISE 0855 (Sao lùn nâu di chuyển nhanh)</option>
          <option value="barnard">Sao Barnard (Chuyển động riêng lớn)</option>
          <option value="eps_indi">Epsilon Indi B (Cặp sao lùn nâu)</option>
          <option value="rw_aur">RW Aurigae (Sao biến quang)</option>
          <option value="r_dra">R Draconis (Sao biến quang)</option>
        </select>

        <div class="grid grid-cols-2 gap-3 mb-3">
          <div>
            <label class="block text-xs text-slate-400 mb-1">Xích kinh (RA)</label>
            <input id="raInput" type="text" value="08h55m10.831s" class="w-full bg-slate-950 border border-slate-700 rounded p-2 text-sm">
          </div>
          <div>
            <label class="block text-xs text-slate-400 mb-1">Độ nghiêng (Dec)</label>
            <input id="decInput" type="text" value="-07d14m42.53s" class="w-full bg-slate-950 border border-slate-700 rounded p-2 text-sm">
          </div>
        </div>

        <div class="mb-4">
          <div class="flex justify-between text-xs text-slate-400 mb-1">
            <span>Phạm vi quan sát (FOV)</span>
            <span id="fovValue">10 arcmin</span>
          </div>
          <input id="fovInput" type="range" min="5" max="30" value="10" class="w-full accent-indigo-500">
        </div>

        <button id="loadBtn" class="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-2 rounded transition">
          Tải dữ liệu vùng trời
        </button>
      </div>

      <hr class="border-slate-800">

      <div>
        <h2 class="text-sm font-semibold uppercase tracking-wider text-slate-400 mb-3">2. Xử lý Dải sóng & Hình ảnh</h2>
        <label class="block text-xs text-slate-400 mb-1">Chế độ dải phổ (102 Channels)</label>
        <select id="bandMode" class="w-full bg-slate-950 border border-slate-700 rounded p-2 text-sm mb-3">
          <option value="coadd">Cộng gộp 6 mảng cảm biến (Tăng SNR)</option>
          <option value="band1">Mảng 1: 0.75 - 1.11 µm (Sao & Thiên hà)</option>
          <option value="band4">Mảng 4: 2.42 - 3.82 µm (Băng H2O / Hữu cơ)</option>
          <option value="band6">Mảng 6: 4.42 - 5.00 µm (CO / CO2 / Sao lùn nâu)</option>
        </select>

        <div class="space-y-2 text-sm">
          <label class="flex items-center space-x-2 cursor-pointer">
            <input id="diffMode" type="checkbox" class="accent-indigo-500 rounded">
            <span>Trừ ảnh (Epoch hiện tại - Epoch 1)</span>
          </label>
          <label class="flex items-center space-x-2 cursor-pointer">
            <input id="overlayCatalog" type="checkbox" checked class="accent-indigo-500 rounded">
            <span>Chồng dữ liệu kính viễn vọng Gaia / WISE</span>
          </label>
          <label class="flex items-center space-x-2 cursor-pointer">
            <input id="showMeta" type="checkbox" class="accent-indigo-500 rounded">
            <span>Hiển thị cảnh báo nhiễu (Contamination)</span>
          </label>
        </div>
      </div>
    </section>

    <!-- Cột hiển thị bầu trời -->
    <section class="lg:col-span-5 flex flex-col items-center bg-slate-900/70 p-5 rounded-xl border border-slate-800">
      <div class="w-full flex justify-between items-center mb-3">
        <span class="text-sm font-semibold text-slate-300">Khung nhìn SPHEREx</span>
        <span id="epochBadge" class="text-xs bg-cyan-950 text-cyan-300 border border-cyan-800 px-2.5 py-1 rounded font-mono">
          Epoch 1 (05/2025)
        </span>
      </div>

      <div class="relative w-full aspect-square max-w-[420px] bg-black rounded-lg overflow-hidden border border-slate-700">
        <canvas id="skyCanvas" width="420" height="420" class="w-full h-full cursor-crosshair"></canvas>
      </div>

      <div class="w-full max-w-[420px] mt-4 space-y-3">
        <div class="flex items-center justify-between gap-2">
          <button id="playBtn" class="bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-1.5 rounded text-sm font-medium transition w-28">
            ⏸ Tạm dừng
          </button>
          <input id="epochSlider" type="range" min="0" max="3" value="0" class="flex-1 accent-cyan-400">
          <select id="speedSelect" class="bg-slate-950 border border-slate-700 rounded px-2 py-1.5 text-xs">
            <option value="800">Chậm</option>
            <option value="450" selected>Vừa</option>
            <option value="200">Nhanh</option>
          </select>
        </div>
        <p class="text-xs text-slate-400 text-center">
          💡 <em>Nhấp trực tiếp vào vật thể trên bản đồ để trích xuất quang phổ 102 dải.</em>
        </p>
      </div>
    </section>

    <!-- Cột Quang phổ -->
    <section class="lg:col-span-3 flex flex-col justify-between bg-slate-900/70 p-5 rounded-xl border border-slate-800 space-y-5">
      <div>
        <h2 class="text-sm font-semibold uppercase tracking-wider text-slate-400 mb-2">3. Phổ Cận