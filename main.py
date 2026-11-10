< !DOCTYPE
html >
< html
lang = "vi" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > SPHEREx
Sky
Explorer - NASA
Space
Apps
Prototype < / title >
< script
src = "https://cdn.tailwindcss.com" > < / script >
< style >
body
{background - color:  # 0b0f19; color: #e2e8f0; font-family: system-ui, -apple-system, sans-serif; }
     canvas {image - rendering: pixelated;}
< / style >
    < / head >
        < body


class ="min-h-screen flex flex-col" >

< !-- Header -->
< header


class ="bg-slate-900 border-b border-slate-800 px-6 py-4 flex flex-wrap justify-between items-center gap-4" >

< div


class ="flex items-center space-x-3" >

< div


class ="w-3 h-3 rounded-full bg-indigo-500 animate-pulse" > < / div >

< h1


class ="text-xl font-bold tracking-wider bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent" >


SPHEREx
SKY
EXPLORER
< / h1 >
< span


class ="text-xs bg-indigo-950 text-indigo-300 border border-indigo-800 px-2 py-0.5 rounded" > 102 NIR Bands < / span >

< / div >
< div


class ="flex items-center space-x-3 text-sm" >

< button
id = "shareBtn"


class ="bg-slate-800 hover:bg-slate-700 border border-slate-700 px-3 py-1.5 rounded transition" >

🔗 Sao
chép
URL
tọa
độ
< / button >
< / div >
< / header >

< !-- Main
Workspace -->
< main


class ="flex-1 grid grid-cols-1 lg:grid-cols-12 gap-6 p-6 max-w-7xl w-full mx-auto" >

< !-- Cột
trái: Bảng
điều
khiển -->
< section


class ="lg:col-span-4 space-y-5 bg-slate-900/70 p-5 rounded-xl border border-slate-800 h-fit" >

< div >
< h2


class ="text-sm font-semibold uppercase tracking-wider text-slate-400 mb-3" > 1. Tọa độ & Mục tiêu < / h2 >

< label


class ="block text-xs text-slate-400 mb-1" > Mục tiêu thử nghiệm (Presets) < / label >

< select
id = "presetSelect"


class ="w-full bg-slate-950 border border-slate-700 rounded p-2 text-sm mb-3 focus:border-indigo-500 outline-none" >

< option
value = "wise0855" > WISE
0
855(Sao
lùn
nâu
di
chuyển
nhanh) < / option >
< option
value = "barnard" > Sao
Barnard(Chuyển
động
riêng
lớn) < / option >
< option
value = "eps_indi" > Epsilon
Indi
B(Cặp
sao
lùn
nâu) < / option >
< option
value = "rw_aur" > RW
Aurigae(Sao
biến
quang) < / option >
< option
value = "r_dra" > R
Draconis(Sao
biến
quang) < / option >
< / select >

< div


class ="grid grid-cols-2 gap-3 mb-3" >

< div >
< label


class ="block text-xs text-slate-400 mb-1" > Xích kinh (RA) < / label >

< input
id = "raInput"
type = "text"
value = "08h55m10.831s"


class ="w-full bg-slate-950 border border-slate-700 rounded p-2 text-sm" >

< / div >
< div >
< label


class ="block text-xs text-slate-400 mb-1" > Độ nghiêng (Dec) < / label >

< input
id = "decInput"
type = "text"
value = "-07d14m42.53s"


class ="w-full bg-slate-950 border border-slate-700 rounded p-2 text-sm" >

< / div >
< / div >

< div


class ="mb-4" >

< div


class ="flex justify-between text-xs text-slate-400 mb-1" >

< span > Phạm
vi
quan
sát(FOV) < / span >
< span
id = "fovValue" > 10
arcmin < / span >
< / div >
< input
id = "fovInput"
type = "range"
min = "5"
max = "30"
value = "10"


class ="w-full accent-indigo-500" >

< / div >

< button
id = "loadBtn"


class ="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-2 rounded transition" >


Tải
dữ
liệu
vùng
trời
< / button >
< / div >

< hr


class ="border-slate-800" >

< !-- Xử
lý
dải
sóng & Hình
ảnh -->
< div >
< h2


class ="text-sm font-semibold uppercase tracking-wider text-slate-400 mb-3" > 2. Xử lý Dải sóng & Hình ảnh < / h2 >

< label


class ="block text-xs text-slate-400 mb-1" > Chế độ dải phổ (102 Channels) < / label >

< select
id = "bandMode"


class ="w-full bg-slate-950 border border-slate-700 rounded p-2 text-sm mb-3" >

< option
value = "coadd" > Cộng
gộp
6
mảng
cảm
biến(Tăng
SNR) < / option >
< option
value = "band1" > Mảng
1: 0.75 - 1.11
µm(Sao & Thiên
hà) < / option >
< option
value = "band4" > Mảng
4: 2.42 - 3.82
µm(Băng
H2O / Hữu
cơ) < / option >
< option
value = "band6" > Mảng
6: 4.42 - 5.00
µm(CO / CO2 / Sao
lùn
nâu) < / option >
< / select >

< div


class ="space-y-2 text-sm" >

< label


class ="flex items-center space-x-2 cursor-pointer" >

< input
id = "diffMode"
type = "checkbox"


class ="accent-indigo-500 rounded" >

< span > Trừ
ảnh(Epoch
hiện
tại - Epoch
1) < / span >
< / label >
< label


class ="flex items-center space-x-2 cursor-pointer" >

< input
id = "overlayCatalog"
type = "checkbox"
checked


class ="accent-indigo-500 rounded" >

< span > Chồng
dữ
liệu
kính
viễn
vọng
Gaia / WISE < / span >
< / label >
< label


class ="flex items-center space-x-2 cursor-pointer" >

< input
id = "showMeta"
type = "checkbox"


class ="accent-indigo-500 rounded" >

< span > Hiển
thị
cảnh
báo
nhiễu(Contamination) < / span >
< / label >
< / div >
< / div >
< / section >

< !-- Cột
giữa: Màn
hình
hiển
thị
Bầu
trời(Blink
Comparator) -->
< section


class ="lg:col-span-5 flex flex-col items-center bg-slate-900/70 p-5 rounded-xl border border-slate-800" >

< div


class ="w-full flex justify-between items-center mb-3" >

< span


class ="text-sm font-semibold text-slate-300" > Khung nhìn SPHEREx < / span >

< span
id = "epochBadge"


class ="text-xs bg-cyan-950 text-cyan-300 border border-cyan-800 px-2.5 py-1 rounded font-mono" >


Epoch
1(05 / 2025)
< / span >
< / div >

< !-- Khung
Canvas -->
< div


class ="relative w-full aspect-square max-w-[420px] bg-black rounded-lg overflow-hidden border border-slate-700 shadow-inner" >

< canvas
id = "skyCanvas"
width = "420"
height = "420"


class ="w-full h-full cursor-crosshair" > < / canvas >

< / div >

< !-- Điều
khiển
Video / Blink -->
< div


class ="w-full max-w-[420px] mt-4 space-y-3" >

< div


class ="flex items-center justify-between gap-2" >

< button
id = "playBtn"


class ="bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-1.5 rounded text-sm font-medium transition w-28" >

⏸ Tạm
dừng
< / button >
< input
id = "epochSlider"
type = "range"
min = "0"
max = "3"
value = "0"


class ="flex-1 accent-cyan-400" >

< select
id = "speedSelect"


class ="bg-slate-950 border border-slate-700 rounded px-2 py-1.5 text-xs" >

< option
value = "800" > Chậm < / option >
< option
value = "450"
selected > Vừa < / option >
< option
value = "200" > Nhanh < / option >
< / select >
< / div >
< p


class ="text-xs text-slate-400 text-center" >

💡 < em > Nhấp
trực
tiếp
vào
vật
thể
đang
di
chuyển
hoặc
nhấp
nháy
trên
ảnh
để
trích
xuất
phổ
102
dải. < / em >
< / p >
< / div >
< / section >

< !-- Cột
phải: Quang
phổ & Siêu
dữ
liệu -->
< section


class ="lg:col-span-3 flex flex-col justify-between bg-slate-900/70 p-5 rounded-xl border border-slate-800 space-y-5" >

< div >
< h2


class ="text-sm font-semibold uppercase tracking-wider text-slate-400 mb-2" > 3. Phổ Cận Hồng Ngoại (0.75 - 5.0 µm) < / h2 >

< p
id = "selectedObjTitle"


class ="text-xs text-cyan-400 font-mono mb-3" > Đang chọn: Mục


tiêu
trung
tâm < / p >

< div


class ="bg-slate-950 border border-slate-800 rounded-lg p-2" >

< canvas
id = "spectrumCanvas"
width = "280"
height = "190"


class ="w-full" > < / canvas >

< / div >
< div


class ="mt-2 flex flex-wrap gap-1.5 text-[11px] text-slate-400" >

< span


class ="bg-slate-800 px-1.5 py-0.5 rounded" > H₂O: 1.4, 1.9, 3.0


µm < / span >
< span


class ="bg-slate-800 px-1.5 py-0.5 rounded" > CH₄: 1.7, 3.3


µm < / span >
< span


class ="bg-slate-800 px-1.5 py-0.5 rounded" > CO₂: 4.26


µm < / span >
< / div >
< / div >

< div


class ="bg-slate-950/80 p-3.5 rounded-lg border border-slate-800 text-xs space-y-1.5" >

< div


class ="font-semibold text-slate-300 mb-1" > Thông tin Vật thể & Siêu dữ liệu < / div >

< div
id = "objMeta"


class ="text-slate-400 space-y-1" > < / div >

< / div >
< / section >

< / main >

< script >
// Dữ
liệu
mô
phỏng
cho
các
mục
tiêu
chuẩn
của
thử
thách
const
PRESETS = {
    wise0855: {
        name: "WISE 0855-0714",
        ra: "08h55m10.831s",
        dec: "-07d14m42.53s",
        type: "moving",
        desc: "Sao lùn nâu lạnh nhất từng biết (lớp Y), cách Trái Đất 7.4 năm ánh sáng. Di chuyển rất nhanh qua các đợt quét.",
        pm: "8.1 arcsec/năm",
        dx: 14, dy: -9,
        specProfile: "browndwarf"
    },
    barnard: {
        name: "Sao Barnard",
        ra: "17h57m48.498s",
        dec: "+04d41m36.20s",
        type: "moving",
        desc: "Sao lùn đỏ có chuyển động riêng lớn nhất trên bầu trời so với Mặt Trời.",
        pm: "10.3 arcsec/năm",
        dx: -8, dy: -16,
        specProfile: "red_dwarf"
    },
    eps_indi: {
        name: "Epsilon Indi Ba/Bb",
        ra: "22h04m10.50s",
        dec: "-56d46m58.0s",
        type: "binary_moving",
        desc: "Hệ sao lùn nâu đôi (lớp T1 và T6) cùng dịch chuyển trên bầu trời.",
        pm: "4.7 arcsec/năm",
        dx: 10, dy: 8,
        specProfile: "browndwarf"
    },
    rw_aur: {
        name: "RW Aurigae",
        ra: "05h07m49.54s",
        dec: "+30d24m05.1s",
        type: "variable",
        desc: "Sao trẻ T Tauri có độ sáng thay đổi mạnh theo thời gian do đĩa bụi che khuất.",
        pm: "0.02 arcsec/năm (Tĩnh)",
        dx: 0, dy: 0,
        fluxVar: [1.0, 0.35, 0.85, 0.25],
        specProfile: "young_star"
    },
    r_dra: {
        name: "R Draconis",
        ra: "16h32m40.23s",
        dec: "+66d45m17.9s",
        type: "variable",
        desc: "Sao biến quang lớp Mira (sao khổng lồ đỏ) có chu kỳ biến thiên độ sáng lớn.",
        pm: "0.03 arcsec/năm (Tĩnh)",
        dx: 0, dy: 0,
        fluxVar: [0.3, 1.0, 0.45, 0.95],
        specProfile: "giant_star"
    }
};

const
EPOCHS = [
    "Epoch 1 (05/2025)",
    "Epoch 2 (11/2025)",
    "Epoch 3 (05/2026)",
    "Epoch 4 (11/2026)"
];

// Trạng
thái
ứng
dụng
let
currentKey = "wise0855";
let
currentEpoch = 0;
let
isPlaying = true;
let
timer = null;
let
bgStars = [];
let
selectedObject = "target"; // 'target'
hoặc
'bg_star'

// DOM
Elements
const
skyCanvas = document.getElementById("skyCanvas");
const
ctx = skyCanvas.getContext("2d");
const
specCanvas = document.getElementById("spectrumCanvas");
const
specCtx = specCanvas.getContext("2d");

const
presetSelect = document.getElementById("presetSelect");
const
raInput = document.getElementById("raInput");
const
decInput = document.getElementById("decInput");
const
fovInput = document.getElementById("fovInput");
const
fovValue = document.getElementById("fovValue");
const
bandMode = document.getElementById("bandMode");
const
diffMode = document.getElementById("diffMode");
const
overlayCatalog = document.getElementById("overlayCatalog");
const
showMeta = document.getElementById("showMeta");
const
epochSlider = document.getElementById("epochSlider");
const
epochBadge = document.getElementById("epochBadge");
const
playBtn = document.getElementById("playBtn");
const
speedSelect = document.getElementById("speedSelect");

// Tạo
sao
nền
cố
định
dựa
theo
hạt
giống
tọa
độ
function
generateField(seedStr)
{
    let
hash = 0;
for (let i = 0; i < seedStr.length; i++)
{
    hash = (hash << 5) - hash + seedStr.charCodeAt(i);
}
const
rand = () = > {
    hash = (hash * 16807) % 2147483647;
return (hash & 0x7fffffff) / 2147483647;
};

bgStars = [];
for (let i = 0; i < 45; i++)
{
bgStars.push({
    x: 20 + rand() * 380,
    y: 20 + rand() * 380,
    r: 1.2 + rand() * 2.5,
    flux: 0.4 + rand() * 0.6,
    gaia: rand() > 0.35,
    contaminated: rand() > 0.9
});
}
}

// Vẽ
bầu
trời
tại
Epoch
hiện
tại
function
renderSky()
{
    const
target = PRESETS[currentKey];
const
fovScale = 10 / parseFloat(fovInput.value);
const
isDiff = diffMode.checked;
const
mode = bandMode.value;

// Màu
nền
theo
chế
độ
ctx.fillStyle = isDiff ? "#111827": "#05070d";
ctx.fillRect(0, 0, skyCanvas.width, skyCanvas.height);

// Lưới
tọa
độ
mờ
ctx.strokeStyle = "rgba(148, 163, 184, 0.08)";
ctx.lineWidth = 1;
for (let i = 70; i < 420; i += 70)
{
ctx.beginPath();
ctx.moveTo(i, 0);
ctx.lineTo(i, 420);
ctx.stroke();
ctx.beginPath();
ctx.moveTo(0, i);
ctx.lineTo(420, i);
ctx.stroke();
}

// Nhiễu
nền
cảm
biến(giảm
khi
chọn
cộng
gộp
6
mảng)
const
noiseCount = mode == = "coadd" ? 80: 350;
ctx.fillStyle = "rgba(255,255,255,0.06)";
for (let i = 0; i < noiseCount; i++)
{
ctx.fillRect(Math.random() * 420, Math.random() * 420, 1.5, 1.5);
}

// Vẽ
sao
nền(Nếu
ở
chế
độ
Trừ
ảnh, sao
nền
tĩnh
bị
triệt
tiêu)
bgStars.forEach(s= > {
    const
sx = 210 + (s.x - 210) * fovScale;
const
sy = 210 + (s.y - 210) * fovScale;

if (!isDiff)
{
    drawStar(sx, sy, s.r, `rgba(226, 232, 240, ${s.flux})`);
}

// Chồng
lớp
danh
mục
Gaia / WISE
if (overlayCatalog.checked & & s.gaia)
{
    ctx.strokeStyle = "rgba(34, 197, 94, 0.65)";
ctx.lineWidth = 1;
ctx.strokeRect(sx - 5, sy - 5, 10, 10);
}

// Cảnh
báo
nhiễu(Contamination
flag)
if (showMeta.checked & & s.contaminated) {
ctx.strokeStyle = "rgba(239, 68, 68, 0.85)";
ctx.beginPath();
ctx.arc(sx, sy, 8, 0, Math.PI * 2);
ctx.stroke();
}
});

// Tính vị trí & độ sáng của Mục tiêu chính
const baseX = 210;
const baseY = 210;
const curX = baseX + target.dx * currentEpoch * fovScale;
const curY = baseY + target.dy * currentEpoch * fovScale;

let alpha = 1.0;
let radius = 4.2;
if (target.type == = "variable") {
alpha = target.fluxVar[currentEpoch];
radius = 2.5 + alpha * 3.5;
}

// Đổi
màu
hiển
thị
theo
dải
bước
sóng
chọn
let
targetColor = `rgba(251, 146, 60, ${alpha})`; // Cam
hồng
ngoại
mặc
định
if (mode === "band1")
targetColor = `rgba(147, 197, 253, ${alpha * 0.6})`;
if (mode === "band6")
targetColor = `rgba(248, 113, 113, ${alpha})`;

// Nếu
bật
chế
độ
Trừ
ảnh(Epoch
hiện
tại - Epoch
1)
if (isDiff) {
if (currentEpoch > 0 & & target.type !== "variable") {
// Bóng âm bản tại Epoch 1 (Màu xanh đậm / Đen)
drawStar(baseX, baseY, radius, "rgba(56, 189, 248, 0.45)");
ctx.strokeStyle = "rgba(56, 189, 248, 0.8)";
ctx.beginPath(); ctx.arc(baseX, baseY, 7, 0, Math.PI * 2); ctx.stroke();

// Điểm dương bản tại Epoch hiện tại
drawStar(curX, curY, radius + 0.8, "rgba(250, 204, 21, 1)");
} else if (target.type == = "variable") {
const diffFlux = Math.abs(alpha - target.fluxVar[0]);
drawStar(curX, curY, 2 + diffFlux * 4, `rgba(250, 204, 21, ${diffFlux + 0.2})`);
}
} else {
// Vẽ
mục
tiêu
bình
thường
drawStar(curX, curY, radius, targetColor);
if (target.type === "binary_moving") {
drawStar(curX + 9 * fovScale, curY - 6 * fovScale, radius * 0.75, targetColor);
}
}

// Khung
đánh
dấu
mục
tiêu
đang
chọn
ctx.strokeStyle = "rgba(99, 102, 241, 0.9)";
ctx.lineWidth = 1.5;
ctx.strokeRect(curX - 11, curY - 11, 22, 22);
}

function
drawStar(x, y, r, color)
{
    const
grad = ctx.createRadialGradient(x, y, 0.5, x, y, r * 2.5);
grad.addColorStop(0, "#ffffff");
grad.addColorStop(0.4, color);
grad.addColorStop(1, "rgba(0,0,0,0)");
ctx.fillStyle = grad;
ctx.beginPath();
ctx.arc(x, y, r * 2.5, 0, Math.PI * 2);
ctx.fill();
}

// Vẽ
biểu
đồ
phổ
102
kênh
cận
hồng
ngoại(0.75 - 5.0
µm)
function
renderSpectrum()
{
    const
target = PRESETS[currentKey];
specCtx.clearRect(0, 0, specCanvas.width, specCanvas.height);

// Trục
tọa
độ
specCtx.strokeStyle = "#334155";
specCtx.lineWidth = 1;
specCtx.beginPath();
specCtx.moveTo(30, 15);
specCtx.lineTo(30, 160);
specCtx.lineTo(270, 160);
specCtx.stroke();

// Nhãn
bước
sóng
specCtx.fillStyle = "#94a3b8";
specCtx.font = "10px monospace";
specCtx.fillText("0.75µm", 28, 175);
specCtx.fillText("2.5µm", 135, 175);
specCtx.fillText("5.0µm", 240, 175);

// Vẽ
102
điểm
dữ
liệu
phổ
specCtx.beginPath();
specCtx.strokeStyle = selectedObject == = "target" ? "#38bdf8": "#a855f7";
specCtx.lineWidth = 1.8;

for (let i = 0; i < 102; i++)
{
const
wl = 0.75 + (i / 101) * (5.0 - 0.75);
const
x = 32 + (i / 101) * 235;
let
flux = 0.5;

if (selectedObject === "target") {
if (target.specProfile == = "browndwarf") {
// Hấp thụ mạnh H2O và CH4, đỉnh phát xạ ở 4.5 µm
flux = 0.25 + 0.55 * Math.exp(-Math.pow((wl - 4.5) / 0.6, 2))
+ 0.3 * Math.exp(-Math.pow((wl - 1.25) / 0.15, 2))
- 0.2 * Math.exp(-Math.pow((wl - 3.3) / 0.2, 2));
} else if (target.specProfile == = "red_dwarf") {
flux = 0.75 * Math.exp(-Math.pow((wl - 1.6) / 1.8, 2));
} else {
const scale = target.fluxVar ? target.fluxVar[currentEpoch]: 1;
flux = (0.4 + 0.4 * Math.sin(wl * 1.5)) * scale;
}
} else {
       // Phổ
sao
nền
thông
thường(Blackbody
giảm
dần)
flux = 0.85 * Math.exp(-0.45 * (wl - 0.75));
}

const
y = 150 - Math.max(0.05, Math.min(0.95, flux)) * 125;
if (i === 0) specCtx.moveTo(x, y);
else specCtx.lineTo(x, y);
}
specCtx.stroke();

// Cập
nhật
thông
tin
Metadata
const
metaEl = document.getElementById("objMeta");
if (selectedObject === "target")
{
document.getElementById("selectedObjTitle").textContent = `Đang
chọn: ${target.name}
`;
metaEl.innerHTML = `
< div > < strong


class ="text-slate-200" > Loại:<

    / strong > ${target.desc} < / div >
< div > < strong


class ="text-slate-200" > Chuyển động riêng:<

    / strong > ${target.pm} < / div >
< div > < strong


class ="text-slate-200" > Tọa độ:<

    / strong > ${raInput.value}, ${decInput.value} < / div >
< div > < strong


class ="text-slate-200" > Trạng thái:<

    / strong > < span


class ="text-emerald-400" > Tín hiệu sạch (SNR cao) < / span > < / div >


`;
} else {
document.getElementById("selectedObjTitle").textContent = `Đang
chọn: Sao
nền
thuộc
danh
mục
Gaia
`;
metaEl.innerHTML = `
< div > < strong


class ="text-slate-200" > Loại:<

    / strong > Sao
dãy
chính(Đứng
yên
giữa
các
Epoch) < / div >
< div > < strong


class ="text-slate-200" > Danh mục chéo:<

    / strong > Khớp
vị
trí
với
Gaia
DR3 & WISE < / div >
< div > < strong


class ="text-slate-200" > Phổ:<

    / strong > Giảm
đều
ở
vùng
bước
sóng
dài < / div >
`;
}
}

function
updateEpoch(ep)
{
    currentEpoch = ep % 4;
epochSlider.value = currentEpoch;
epochBadge.textContent = EPOCHS[currentEpoch];
renderSky();
renderSpectrum();
}

function
startBlinkLoop()
{
if (timer)
clearInterval(timer);
const
speed = parseInt(speedSelect.value, 10);
timer = setInterval(() = > {
if (isPlaying)
updateEpoch(currentEpoch + 1);
}, speed);
}

// Sự
kiện
tương
tác
presetSelect.addEventListener("change", (e) = > {
currentKey = e.target.value;
const
t = PRESETS[currentKey];
raInput.value = t.ra;
decInput.value = t.dec;
selectedObject = "target";
generateField(t.ra + t.dec);
updateEpoch(0);
});

document.getElementById("loadBtn").addEventListener("click", () = > {
generateField(raInput.value + decInput.value);
renderSky();
renderSpectrum();
});

fovInput.addEventListener("input", (e) = > {
fovValue.textContent = `${e.target.value}
arcmin
`;
renderSky();
});

[bandMode, diffMode, overlayCatalog, showMeta].forEach(el= > {
el.addEventListener("change", renderSky);
});

epochSlider.addEventListener("input", (e) = > {
isPlaying = false;
playBtn.textContent = "▶ Phát Blink";
updateEpoch(parseInt(e.target.value, 10));
});

playBtn.addEventListener("click", () = > {
isPlaying = !isPlaying;
playBtn.textContent = isPlaying ? "⏸ Tạm dừng": "▶ Phát Blink";
});

speedSelect.addEventListener("change", startBlinkLoop);

// Nhấp
chuột
trên
bản
đồ
sao
để
trích
xuất
quang
phổ
skyCanvas.addEventListener("click", (e) = > {
const
rect = skyCanvas.getBoundingClientRect();
const
clickX = ((e.clientX - rect.left) / rect.width) * 420;
const
clickY = ((e.clientY - rect.top) / rect.height) * 420;

const
target = PRESETS[currentKey];
const
fovScale = 10 / parseFloat(fovInput.value);
const
tx = 210 + target.dx * currentEpoch * fovScale;
const
ty = 210 + target.dy * currentEpoch * fovScale;

const
dist = Math.hypot(clickX - tx, clickY - ty);
selectedObject = dist < 24 ? "target": "bg_star";
renderSpectrum();
});

// Chia
sẻ
tọa
độ
qua
URL
document.getElementById("shareBtn").addEventListener("click", () = > {
const
url = new
URL(window.location.href);
url.searchParams.set("target", currentKey);
url.searchParams.set("ra", raInput.value);
url.searchParams.set("dec", decInput.value);
navigator.clipboard.writeText(url.toString());
const
btn = document.getElementById("shareBtn");
btn.textContent = "✅ Đã sao chép URL!";
setTimeout(() = > btn.textContent = "🔗 Sao chép URL tọa độ", 2000);
});

// Đọc
URL
parameters
khi
khởi
động
function
initFromURL()
{
    const
params = new
URLSearchParams(window.location.search);
if (params.has("target") & & PRESETS[params.get("target")])
{
currentKey = params.get("target");
presetSelect.value = currentKey;
}
if (params.has("ra")) raInput.value = params.get("ra");
if (params.has("dec")) decInput.value = params.get("dec");
generateField(raInput.value + decInput.value);
updateEpoch(0);
startBlinkLoop();
}

initFromURL();
< / script >
< / body >
< / html >