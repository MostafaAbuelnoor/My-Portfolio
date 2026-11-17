from lib2 import page
MORE = '<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>\n<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>'
MORECSS = '.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; } @media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }'
HERO2 = '.hero { display: grid; gap: 24px 48px; align-items: center; min-height: calc(100svh - 70px); padding-bottom: 36px; } @media (min-width: 900px) { .hero { grid-template-columns: 1.1fr 0.9fr; } }'

# 101 Date poster — after Petrillo.studio (One Page Love)
page(101, 'date-poster', 'family=Anton&family=Geist:wght@400;500', '#F0201A', '''
:root { --line: rgb(0 0 0 / 0.3); --focus: #0A0A0A; --f-bg: #0A0A0A; --f-text: #fff; --f-ph: #B9B9B9; --b-bg: #F0201A; --b-text: #0A0A0A; --note: #2A0504; --err: #3A0000; --f-radius: 0; --b-radius: 0; --f-pad: 4px; }
body { background: #F0201A; color: #0A0A0A; font: 15px/1.5 "Geist", system-ui, sans-serif; }
::selection { background: #0A0A0A; color: #F0201A; }
.poster { position: relative; min-height: 100svh; display: grid; grid-template: auto 1fr auto / 1fr 1fr; overflow: hidden; }
.n { font: 400 clamp(5rem, 24vw, 21rem)/0.78 "Anton", sans-serif; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; padding: 0 clamp(10px, 2vw, 28px); }
.n.r { text-align: right; } .n.b { align-self: end; }
.sun { grid-column: 1 / -1; grid-row: 2; justify-self: center; align-self: center; position: relative; width: min(46vmin, 380px); aspect-ratio: 1; border-radius: 50%; background: radial-gradient(circle, #0A0A0A 52%, rgb(10 10 10 / 0) 72%); }
.sun b { position: absolute; left: 50%; bottom: 50%; width: 3px; margin-left: -1.5px; background: #F0201A; transform-origin: 50% 100%; rotate: calc(var(--a) * 1deg); border-radius: 3px; } .sun .h { height: 24%; } .sun .m { height: 36%; } .sun .s { height: 40%; width: 1px; background: #fff; transition: rotate 300ms cubic-bezier(0.34, 1.56, 0.64, 1); }
.tag { position: absolute; left: 50%; top: 18px; translate: -50% 0; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.78rem; white-space: nowrap; }
.below { background: #0A0A0A; color: #F4F0EA; --line: #2A2A2A; --note: #A9A49B; --f-bg: #1A1A1A; --f-border: 1px solid #333; --focus: #F0201A; }
.below .inr { display: grid; gap: 28px 56px; padding-block: 48px 8px; }
h1 { font: 400 clamp(2.4rem, 1.2rem + 5vw, 5.4rem)/0.92 "Anton", sans-serif; text-transform: uppercase; margin-bottom: 18px; }
.who { display: flex; gap: 14px; align-items: center; margin-bottom: 18px; } .face { flex: none; width: 70px; height: 70px; background: #F0201A; }
@media (min-width: 860px) { .below .inr { grid-template-columns: 1.2fr 0.8fr; } }
''', '''
<div class="poster" aria-hidden="true"><span class="tag">Mostafa Saher · class is on</span>
	<span class="n" id="dd">17</span><span class="n r" id="hh">09</span>
	<div class="sun"><b class="h" style="--a:0"></b><b class="m" style="--a:0"></b><b class="s" style="--a:0"></b></div>
	<span class="n b" id="mo">NOV</span><span class="n r b" id="mm">03</span>
</div>
<main class="below"><div class="wrap inr">
	<div><h1 data-split>{{H}}</h1><div class="who" data-reveal><div class="face">{{IMG}}</div><p>Mostafa Saher, technical instructor. The poster above is today, live.</p></div><div data-reveal style="max-width:460px">{{FORM}}</div></div>
	<div data-reveal style="--i:1">{{TOPICS_UL}}<div style="margin-top:22px">{{LINKS_INLINE}}</div></div>
</div><div class="wrap"><footer class="foot">{{FOOT}}</footer></div></main>
''', '''
const $ = (i) => document.getElementById(i), pad = (n) => String(n).padStart(2, '0'), hs = document.querySelectorAll('.sun b'); let turns = 0, last = -1;
const tick = () => { const n = new Date(), h = n.getHours(), m = n.getMinutes(), s = n.getSeconds(); $('dd').textContent = pad(n.getDate()); $('hh').textContent = pad(h); $('mm').textContent = pad(m); $('mo').textContent = n.toLocaleString('en', { month: 'short' }).toUpperCase();
	if (s < last) turns++; last = s; hs[0].style.setProperty('--a', (h % 12) * 30 + m / 2); hs[1].style.setProperty('--a', m * 6); hs[2].style.setProperty('--a', turns * 360 + s * 6); };
tick(); setInterval(tick, 1000);
''')

# 102 Shelf — after JUNGLE / Yann Do (One Page Love)
page(102, 'shelf', 'family=Archivo:wght@500..900', '#F2EFE9', '''
:root { --line: #D5D0C4; --focus: #171717; --f-bg: #fff; --b-bg: #171717; --b-text: #fff; --note: #6B675C; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #F2EFE9; color: #171717; font: 16px/1.5 "Archivo", system-ui, sans-serif; }
::selection { background: #171717; color: #F2EFE9; }
.room { min-height: calc(100svh - 70px); display: grid; align-content: center; gap: clamp(26px, 6vh, 60px); padding-block: 20px 36px; overflow: hidden; }
.shelf { position: relative; display: flex; align-items: flex-end; gap: 0.02em; padding-bottom: 6px; border-bottom: 5px solid #171717; font-size: clamp(3.4rem, 15vw, 13rem); font-weight: 900; line-height: 0.78; letter-spacing: -0.04em; text-transform: uppercase; transform-origin: 50% 100%; rotate: calc(var(--tilt, 0) * 1deg); will-change: rotate; width: fit-content; }
.shelf.s2 { margin-left: auto; font-size: clamp(2rem, 8vw, 7rem); border-bottom-width: 4px; }
.shelf.s3 { font-size: clamp(1.1rem, 2.4vw, 1.8rem); letter-spacing: -0.02em; font-weight: 700; text-transform: none; border-bottom-width: 3px; gap: 0.3em; }
.shelf i { display: inline-block; font-style: normal; translate: calc(var(--tilt, 0) * var(--w, 1) * 3px) 0; will-change: translate; }
.shelf .ball { width: 0.62em; height: 0.62em; border-radius: 50%; background: #FF4B1F; align-self: flex-end; margin-inline: 0.04em; }
.low { display: grid; gap: 22px 48px; align-items: end; }
.me { display: flex; gap: 14px; align-items: center; max-width: 30em; font-weight: 500; } .face { flex: none; width: 76px; height: 76px; background: #DDD7C8; } .field { gap: 0; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="room" id="room">
		<h1 class="sr">Mostafa Saher teaches AI and cloud, one clear step at a time</h1>
		<div class="shelf" aria-hidden="true"><i style="--w:0.6">M</i><i style="--w:1.4">o</i><i style="--w:0.9">s</i><i style="--w:1.8">t</i><i style="--w:1.1">a</i><i style="--w:2.2">f</i><i style="--w:1.5">a</i><i class="ball" style="--w:6"></i></div>
		<div class="shelf s2" aria-hidden="true"><i class="ball" style="--w:7"></i><i style="--w:1">A</i><i style="--w:1.6">I</i><i style="--w:0.4">&nbsp;</i><i style="--w:2">+</i><i style="--w:0.4">&nbsp;</i><i style="--w:1.2">c</i><i style="--w:1.9">l</i><i style="--w:0.8">o</i><i style="--w:1.5">u</i><i style="--w:2.3">d</i></div>
		<div class="shelf s3" aria-hidden="true"><i style="--w:1">one</i><i style="--w:2">clear</i><i style="--w:3">step</i><i style="--w:4">at</i><i style="--w:5">a</i><i style="--w:6">time</i></div>
		<div class="low"><div class="me" data-reveal><div class="face">{{IMG}}</div><p>Technical instructor. Tilt the shelves with your cursor. My newsletter carries what comes up after class.</p></div><div data-reveal style="--i:1">{{FORM}}</div></div>
	</main>
</div>''' + MORE, '''
const room = document.getElementById('room'), shelves = FX.$$('.shelf'); if (FX.RM) return; const cur = shelves.map(() => 0);
FX.onTick((t) => { shelves.forEach((s, i) => { const target = FX.FINE && FX.ptr.moved ? FX.ptr.nx * (i % 2 ? -7 : 7) : Math.sin(t / 1400 + i * 1.7) * 3.2; cur[i] = FX.lerp(cur[i], target, 0.06); s.style.setProperty('--tilt', cur[i].toFixed(3)); }); });
''')

# 103 Spheres — after Angelo (One Page Love)
page(103, 'spheres', 'family=Sora:wght@300..700', '#FFFFFF', '''
:root { --line: #E7E7EC; --focus: #6C3DF4; --f-bg: #F3F3F7; --b-bg: #15151F; --b-text: #fff; --note: #6B6B7B; --f-radius: 999px; --b-radius: 999px; }
body { background: #fff; color: #15151F; font: 15px/1.6 "Sora", system-ui, sans-serif; }
::selection { background: #6C3DF4; color: #fff; }
.orbs { position: relative; height: min(74svh, 620px); margin-top: 4px; }
.o { position: absolute; left: var(--x); top: var(--y); width: var(--s); aspect-ratio: 1; margin: calc(var(--s) / -2); border-radius: 50%; display: grid; place-items: center; color: #fff; font-weight: 700; font-size: calc(var(--s) * 0.17); letter-spacing: -0.02em; text-align: center; box-shadow: inset -0.12em -0.16em 0.5em rgb(0 0 0 / 0.45), inset 0.1em 0.12em 0.4em rgb(255 255 255 / 0.5), 0 0.4em 0.9em -0.3em rgb(0 0 0 / 0.5); background: radial-gradient(circle at 32% 26%, #fff 0 6%, var(--c1) 22%, var(--c2) 70%, #0B0B14 115%); overflow: hidden; transition: scale 400ms var(--spring); }
.o.pic img { width: 132%; max-width: none; margin: 10% 0 0 0; } .o.pic { background: radial-gradient(circle at 32% 26%, #fff 0 4%, #C9B8FF 30%, #6C3DF4 100%); place-items: start center; }
.o.big { --s: clamp(150px, 26vw, 250px); } .o.mid { --s: clamp(96px, 15vw, 150px); } .o.sm { --s: clamp(64px, 9vw, 96px); }
@media (hover: hover) and (pointer: fine) { .o:hover { scale: 1.12; } }
.txt { text-align: center; padding-block: 8px 0; }
h1 { max-width: 15em; margin-inline: auto; font-size: clamp(1.7rem, 1.1rem + 2.4vw, 3rem); font-weight: 600; line-height: 1.08; letter-spacing: -0.035em; }
.signup { max-width: 430px; margin: 22px auto 0; text-align: left; } .note { text-align: center; }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main>
		<div class="orbs" aria-hidden="true">
			<div class="o big pic fx-float" style="--x:50%;--y:50%;--dur:7s" data-par="10">{{IMG}}</div>
			<div class="o mid fx-float" style="--x:22%;--y:30%;--c1:#7FE7FF;--c2:#1667E0;--dur:5.5s" data-par="34">AI</div>
			<div class="o mid fx-float" style="--x:79%;--y:28%;--c1:#FFD08A;--c2:#F2542D;--dur:6.5s" data-par="-28">Cloud</div>
			<div class="o sm fx-float" style="--x:16%;--y:72%;--c1:#B9FFB0;--c2:#0E9F6E;--dur:4.8s" data-par="-40">Notes</div>
			<div class="o sm fx-float" style="--x:84%;--y:70%;--c1:#FFB3E6;--c2:#C2189A;--dur:6s" data-par="46">Takes</div>
			<div class="o sm fx-float" style="--x:36%;--y:88%;--c1:#E8E8F0;--c2:#3B3B52;--dur:5.2s" data-par="22">Links</div>
			<div class="o sm fx-float" style="--x:66%;--y:10%;--c1:#FFF3A6;--c2:#E0A100;--dur:7.4s" data-par="-18">Steps</div>
		</div>
		<div class="txt"><h1 data-split data-fx="blur">{{H}}</h1><div data-reveal style="--wait:600ms">{{FORM}}</div></div>
	</main>
</div>''' + MORE)

# 104 Panorama — after Mathias Adolfsson (One Page Love)
page(104, 'panorama', 'family=Familjen+Grotesk:wght@400..700', '#0B0B0D', '''
:root { color-scheme: dark; --line: #25252B; --focus: #FFB347; --f-bg: #17171B; --f-text: #F3F2EE; --f-ph: #9A988F; --f-border: 1px solid #2D2D34; --b-bg: #FFB347; --b-text: #0B0B0D; --note: #9A988F; --err: #FF9B8F; --f-radius: 10px; --b-radius: 6px; }
body { background: #0B0B0D; color: #F3F2EE; font: 16px/1.5 "Familjen Grotesk", system-ui, sans-serif; }
::selection { background: #FFB347; color: #0B0B0D; }
.stage { --w: min(74vw, 520px); --r: calc(var(--w) * 0.9); height: min(66svh, 520px); display: grid; place-items: center; perspective: 1200px; overflow: hidden; cursor: grab; touch-action: pan-y; user-select: none; }
.ring { position: relative; width: var(--w); height: 78%; transform-style: preserve-3d; transform: translateZ(calc(var(--r) * -1)) rotateY(calc(var(--ry, 0) * 1deg)); }
.pn { position: absolute; inset: 0; border-radius: 18px; padding: 24px; display: grid; align-content: space-between; overflow: hidden; backface-visibility: hidden; transform: rotateY(calc(var(--k) * 60deg)) translateZ(var(--r)); }
.pn b { font-size: clamp(1.5rem, 1rem + 2.4vw, 2.8rem); font-weight: 700; line-height: 0.98; letter-spacing: -0.04em; } .pn span { font-size: 0.95rem; max-width: 22em; }
.p0 { background: #FFB347; color: #0B0B0D; } .p1 { background: #2A6BFF; } .p2 { background: #F3F2EE; color: #0B0B0D; } .p3 { background: #E0413A; } .p4 { background: #1FA971; } .p5 { background: #7B5BFF; }
.p0 img { position: absolute; right: -4%; bottom: 0; height: 92%; width: auto; max-width: none; } .p0 b { position: relative; max-width: 5em; }
.under { display: grid; gap: 20px 48px; align-items: end; padding-block: 8px 0; }
h1 { font-size: clamp(1.8rem, 1.2rem + 2.4vw, 3rem); font-weight: 700; line-height: 1; letter-spacing: -0.04em; max-width: 13em; }
@media (min-width: 860px) { .under { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}</div>
<main>
	<div class="stage" id="stage" aria-hidden="true"><div class="ring" id="ring">
		<div class="pn p0" style="--k:0"><b>Mostafa Saher</b><span>Technical instructor</span>{{IMG}}</div>
		<div class="pn p1" style="--k:1"><b>AI and cloud.</b><span>One clear step at a time.</span></div>
		<div class="pn p2" style="--k:2"><b>Thoughts</b><span>Notes from the classroom: what students get stuck on.</span></div>
		<div class="pn p3" style="--k:3"><b>Opinions</b><span>Where I stand on new models, cloud services and the hype.</span></div>
		<div class="pn p4" style="--k:4"><b>Resources</b><span>The labs, docs, courses and tools I actually use.</span></div>
		<div class="pn p5" style="--k:5"><b>By email.</b><span>Subscribe below. Drag to keep turning.</span></div>
	</div></div>
	<div class="wrap under"><h1 data-split>{{H}}</h1><div data-reveal>{{FORM}}</div></div>
</main>''' + MORE, '''
const st = document.getElementById('stage'), ring = document.getElementById('ring'); let ry = 0, v = -0.12, drag = false, lx = 0;
st.addEventListener('pointerdown', (e) => { drag = true; lx = e.clientX; st.setPointerCapture(e.pointerId); st.style.cursor = 'grabbing'; });
st.addEventListener('pointermove', (e) => { if (!drag) return; v = (e.clientX - lx) * 0.28; lx = e.clientX; });
['pointerup', 'pointercancel'].forEach((n) => st.addEventListener(n, () => { drag = false; st.style.cursor = 'grab'; }));
FX.onTick(() => { ry += v; if (!drag) v = FX.lerp(v, -0.12, 0.03); ring.style.setProperty('--ry', ry.toFixed(2)); });
''')

# 105 Eyes — after Abdullah (One Page Love)
page(105, 'eyes', 'family=Gabarito:wght@400..900', '#FFFFFF', '''
:root { --line: #E5E5E5; --focus: #111; --f-bg: #F2F2F2; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 999px; --b-radius: 999px; }
body { background: #fff; color: #111; font: 16px/1.5 "Gabarito", system-ui, sans-serif; }
::selection { background: #FFD23F; }
.stage { position: relative; min-height: calc(100svh - 70px); display: grid; align-content: center; justify-items: center; gap: 22px; text-align: center; padding-block: 12px 150px; overflow: hidden; }
h1 { max-width: 12em; font-size: clamp(2.4rem, 1.2rem + 5vw, 5.6rem); font-weight: 800; line-height: 0.95; letter-spacing: -0.045em; }
.chip { display: inline-flex; align-items: center; gap: 8px; padding: 6px 14px; border-radius: 999px; border: 1.5px solid #111; font-weight: 600; }
.chip .face { width: 28px; height: 28px; border-radius: 50%; background: #E9E9E9; }
.signup { width: 100%; max-width: 430px; text-align: left; } .note { text-align: center; }
.tagx { position: absolute; left: var(--x); top: var(--y); padding: 5px 12px; border-radius: 999px; font-weight: 700; font-size: 0.9rem; background: var(--c); color: #111; rotate: var(--r); }
.eyes { position: absolute; left: 50%; bottom: -70px; translate: -50% 0; display: flex; gap: 14px; }
.eye { position: relative; width: clamp(120px, 20vw, 190px); aspect-ratio: 1; border-radius: 50%; background: #fff; border: 5px solid #111; overflow: hidden; }
.eye i { position: absolute; left: 50%; top: 50%; width: 44%; aspect-ratio: 1; margin: -22%; border-radius: 50%; background: #111; translate: var(--px, 0) var(--py, -18%); }
.eye i::after { content: ""; position: absolute; left: 18%; top: 16%; width: 26%; aspect-ratio: 1; border-radius: 50%; background: #fff; }
.eye::after { content: ""; position: absolute; inset: 0; background: #111; transform: translateY(-101%); }
@media (prefers-reduced-motion: no-preference) { .eye::after { animation: blink 5.5s ease-in-out infinite; } @keyframes blink { 0%, 93%, 100% { transform: translateY(-101%); } 96% { transform: translateY(0); } } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="stage">
		<span class="tagx fx-float" style="--x:6%;--y:12%;--c:#FFD23F;--r:-8deg;--dur:5s">AI</span><span class="tagx fx-float" style="--x:84%;--y:16%;--c:#8FD3FF;--r:7deg;--dur:6.4s">Cloud</span><span class="tagx fx-float" style="--x:10%;--y:58%;--c:#B8F2C8;--r:5deg;--dur:5.6s">Thoughts</span><span class="tagx fx-float" style="--x:80%;--y:56%;--c:#FFB3D1;--r:-6deg;--dur:7s">Resources</span>
		<span class="chip" data-reveal><span class="face">{{IMG}}</span>Mostafa Saher · instructor</span>
		<h1 data-split data-fx="pop">I keep an eye on AI and cloud, so you can keep up.</h1>
		<div data-reveal style="--wait:600ms;width:100%;display:grid;justify-items:center">{{FORM}}</div>
		<div class="eyes" aria-hidden="true"><div class="eye"><i></i></div><div class="eye"><i></i></div></div>
	</main>
</div>''' + MORE, '''
const eyes = FX.$$('.eye'); if (FX.RM) return;
FX.onTick((t) => { eyes.forEach((e) => { const r = e.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height / 2; let dx, dy;
	if (FX.ptr.moved && FX.FINE) { dx = FX.ptr.x - cx; dy = FX.ptr.y - cy; } else { dx = Math.sin(t / 900) * 200; dy = -200 + Math.cos(t / 1300) * 60; }
	const d = Math.hypot(dx, dy) || 1, m = Math.min(1, d / 220) * 24; e.firstElementChild.style.setProperty('--px', (dx / d * m) + '%'); e.firstElementChild.style.setProperty('--py', (dy / d * m) + '%'); }); });
''')

# 106 Charm row — after Melike Turgut (One Page Love)
page(106, 'charm-row', 'family=Bricolage+Grotesque:opsz,wght@12..96,300..800', '#E4E2D5', '''
:root { --line: #C9C6B4; --focus: #23351A; --f-bg: #F3F2EA; --b-bg: #23351A; --b-text: #fff; --note: #5F6350; --f-radius: 999px; --b-radius: 999px; }
body { background: #E4E2D5; color: #23351A; font: 16px/1.5 "Bricolage Grotesque", system-ui, sans-serif; }
::selection { background: #23351A; color: #E4E2D5; }
.stage { min-height: calc(100svh - 70px); display: grid; grid-template-rows: 1fr auto; padding-bottom: 28px; }
h1 { align-self: center; display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 0.08em 0.14em; font-size: clamp(3rem, 1rem + 11vw, 10.5rem); font-weight: 300; line-height: 0.9; letter-spacing: -0.05em; }
.ch { display: inline-flex; gap: 0.04em; }
.ch i { width: 0.56em; aspect-ratio: 1; display: inline-block; transition: rotate 700ms var(--spring), scale 400ms var(--spring); }
.fx:not(.fx-rm) h1:not(.in) .ch i { scale: 0; rotate: -180deg; } .fx h1.in .ch i { transition-delay: calc(400ms + var(--k) * 90ms); }
.c1 { border-radius: 50%; background: #E0452B; } .c2 { background: #F2B705; clip-path: polygon(50% 0, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%); }
.c3 { background: #7B4BD9; border-radius: 50% 50% 50% 50% / 30% 30% 70% 70%; } .c4 { background: #1C8FD6; border-radius: 12% 50% 12% 50%; } .c5 { background: #F28A2E; border-radius: 50% 50% 0 50%; rotate: 45deg; } .c6 { background: #1FA971; border-radius: 0 50% 50% 50%; }
@media (hover: hover) and (pointer: fine) { .ch i:hover { rotate: 220deg; scale: 1.25; transition-delay: 0ms !important; } }
@media (prefers-reduced-motion: no-preference) { h1.in .ch i { animation: bob 3s ease-in-out calc(1.6s + var(--k) * 160ms) infinite; } @keyframes bob { 50% { translate: 0 -0.08em; } } }
.low { display: grid; gap: 20px 48px; align-items: end; }
.me { display: flex; gap: 14px; align-items: center; max-width: 30em; } .face { flex: none; width: 72px; height: 72px; border-radius: 50%; background: #CFCDBD; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="stage">
		<h1 data-inview aria-label="AI, cloud, clear">AI <span class="ch" aria-hidden="true"><i class="c1" style="--k:0"></i><i class="c2" style="--k:1"></i><i class="c3" style="--k:2"></i><i class="c4" style="--k:3"></i><i class="c5" style="--k:4"></i><i class="c6" style="--k:5"></i></span> cloud</h1>
		<div class="low"><div class="me" data-reveal><div class="face">{{IMG}}</div><p>I’m Mostafa Saher. I’ve spent my time teaching the bits in between, one clear step at a time.</p></div><div data-reveal style="--i:1">{{FORM}}</div></div>
	</main>
</div>''' + MORE)

# 107 File tabs — after Medium Rare (One Page Love)
page(107, 'file-tabs', 'family=Barlow+Condensed:wght@500;700&family=Barlow:wght@400;500', '#FFFFFF', '''
:root { --line: rgb(0 0 0 / 0.2); --focus: #111; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #333; --f-radius: 6px; --b-radius: 3px; --f-pad: 4px; --w: 760px; }
body { background: #fff; color: #111; font: 16px/1.5 "Barlow", system-ui, sans-serif; }
::selection { background: #111; color: #fff; }
h1 { margin: clamp(8px, 3vh, 28px) 0 12px; font: 700 clamp(4rem, 1rem + 17vw, 9.6rem)/0.84 "Barlow Condensed", sans-serif; text-transform: uppercase; letter-spacing: -0.01em; text-align: center; }
.tabs { display: grid; }
.tab { position: relative; border-radius: 10px 10px 0 0; background: var(--c); margin-top: -8px; box-shadow: 0 -6px 12px -8px rgb(0 0 0 / 0.35); transition: translate 350ms var(--ease-out); }
.tab summary { list-style: none; cursor: pointer; padding: 12px 18px 16px; font: 700 clamp(1.6rem, 1.2rem + 1.6vw, 2.3rem)/1 "Barlow Condensed", sans-serif; display: flex; justify-content: space-between; align-items: center; } .tab summary::-webkit-details-marker { display: none; }
.tab summary small { font: 500 0.8rem "Barlow", sans-serif; letter-spacing: 0.06em; text-transform: uppercase; }
.tab .body { display: grid; grid-template-rows: 0fr; transition: grid-template-rows 450ms var(--ease-out); } .tab[open] .body { grid-template-rows: 1fr; } .tab .body > div { overflow: hidden; padding-inline: 18px; } .tab[open] .body > div { padding-bottom: 26px; }
.tab p { max-width: 34em; font-size: 1.05rem; }
.tab .pic { display: flex; gap: 16px; align-items: flex-end; } .tab .pic figure { flex: none; width: 130px; margin-bottom: -26px; }
@media (hover: hover) and (pointer: fine) { .tab:not([open]):hover { translate: 0 -8px; } }
.fx:not(.fx-rm) .tabs:not(.in) .tab { translate: 0 60px; opacity: 0; } .fx .tabs.in .tab { transition: translate 700ms var(--ease-out) calc(var(--k) * 70ms), opacity 500ms ease calc(var(--k) * 70ms); }
.foot { text-align: center; }
''', '''
<div class="wrap">{{TOP}}
	<main>
		<h1 data-split="chars" style="--stag:25ms">Mostafa</h1>
		<div class="tabs" data-inview>
			<details class="tab" name="f" style="--c:#F2F2F2;--k:0"><summary>Instructor<small>Open</small></summary><div class="body"><div class="pic"><figure>{{IMG}}</figure><p>Mostafa Saher. I teach AI and cloud, one clear step at a time.</p></div></div></details>
			<details class="tab" name="f" style="--c:#C9B8FF;--k:1"><summary>After class<small>01</small></summary><div class="body"><div><p>{{INTRO}}</p></div></div></details>
			<details class="tab" name="f" style="--c:#FFF27A;--k:2"><summary>Thoughts<small>02</small></summary><div class="body"><div><p>Notes from the classroom: what students get stuck on, and the explanation that finally made it click.</p></div></div></details>
			<details class="tab" name="f" style="--c:#9BF29B;--k:3"><summary>Opinions<small>03</small></summary><div class="body"><div><p>Where I stand on new models, cloud services and the hype around them.</p></div></div></details>
			<details class="tab" name="f" style="--c:#F6D9B8;--k:4"><summary>Resources<small>04</small></summary><div class="body"><div><p>The labs, docs, courses and tools I actually use, each with a line on why.</p></div></div></details>
			<details class="tab" name="f" open style="--c:#7FE3F5;--k:5"><summary>Newsletter<small>Subscribe</small></summary><div class="body"><div><div style="max-width:440px">{{FORM}}</div></div></div></details>
			<details class="tab" name="f" style="--c:#FFB3C7;--k:6"><summary>Elsewhere<small>Links</small></summary><div class="body"><div>{{LINKS_ROWS}}</div></div></details>
		</div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 108 Comic — after Tiago Fragoso (One Page Love)
page(108, 'comic', 'family=Bangers&family=Comic+Neue:wght@400;700', '#FFFFFF', '''
:root { --line: #111; --focus: #111; --f-bg: #fff; --f-border: 3px solid #111; --b-bg: #FFD400; --b-text: #111; --note: #333; --f-radius: 0; --b-radius: 0; --f-pad: 3px; }
body { background: #F4F1E8; color: #111; font: 700 17px/1.35 "Comic Neue", "Comic Sans MS", cursive; }
::selection { background: #FFD400; }
.strip { display: grid; gap: 12px; padding-block: 4px 12px; }
.pn { position: relative; border: 4px solid #111; background: var(--bg, #fff); min-height: 300px; overflow: hidden; padding: 16px; }
.pn.dots { background-image: radial-gradient(#0002 22%, transparent 24%); background-size: 12px 12px; background-color: var(--bg); }
.cap { display: inline-block; padding: 4px 10px; background: #FFD400; border: 3px solid #111; font: 400 1.1rem "Bangers", cursive; letter-spacing: 0.06em; }
.bub { position: absolute; max-width: 62%; padding: 12px 16px; background: #fff; border: 3px solid #111; border-radius: 28px; }
.bub::after { content: ""; position: absolute; width: 22px; height: 22px; background: #fff; border: solid #111; border-width: 0 3px 3px 0; bottom: -13px; left: var(--tl, 28px); transform: skew(18deg) rotate(45deg); }
.fx:not(.fx-rm) .pn:not(.in) .bub, .fx:not(.fx-rm) .pn:not(.in) .pow { scale: 0; } .fx .pn.in .bub, .fx .pn.in .pow { transition: scale 500ms var(--spring) calc(300ms + var(--k, 0) * 350ms); }
.pn figure { position: absolute; right: 2%; bottom: 0; height: 84%; aspect-ratio: 1100 / 1433; } .pn figure img { height: 100%; width: auto; max-width: none; }
h1 { font: 400 clamp(2.6rem, 1.4rem + 5vw, 5.4rem)/0.95 "Bangers", cursive; letter-spacing: 0.02em; }
.pow { position: absolute; right: 8%; top: 14%; font: 400 clamp(2rem, 5vw, 3.6rem) "Bangers", cursive; color: #E0241B; rotate: 10deg; -webkit-text-stroke: 2px #111; }
@media (max-width: 700px) { .pn figure { height: 62%; right: -6%; } .bub { max-width: 54%; font-size: 0.92rem; } }
.pn .signup { max-width: 440px; font-family: system-ui, sans-serif; font-weight: 400; margin-top: 14px; } .pn .tp { font-weight: 400; margin-top: 10px; }
@media (min-width: 860px) { .strip { grid-template-columns: 1.2fr 0.8fr; } .w2 { grid-column: 1 / -1; } .pn { min-height: 340px; } }
''', '''
<div class="wrap">{{TOP}}
	<main class="strip">
		<section class="pn dots" style="--bg:#8FD3FF" data-inview><span class="cap">Meanwhile, after class…</span><p class="bub" style="left:5%;top:26%;--k:0">Wait, so why does that work?</p><p class="bub" style="left:12%;top:56%;--tl:70%;--k:1">Good question. That’s the best part of every class.</p><figure>{{IMG}}</figure></section>
		<section class="pn" style="--bg:#FFD400" data-inview><span class="cap">Our hero</span><h1 style="margin-top:14px">Mostafa Saher!</h1><p style="margin-top:8px;max-width:16em">Technical instructor. Teaches AI and cloud, one clear step at a time.</p><span class="pow">CLICK!</span></section>
		<section class="pn" style="--bg:#fff" data-inview><span class="cap">The plan</span><p style="margin-top:12px">He writes it all down and sends it by email:</p>{{TOPICS_UL}}</section>
		<section class="pn dots" style="--bg:#FFB3C7" data-inview><span class="cap">Your move</span><p class="bub" style="position:relative;max-width:none;margin-top:14px;--k:0">Leave your email and I’ll send the next one.</p>{{FORM}}<div style="margin-top:14px">{{LINKS_INLINE}}</div></section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 109 Cutting mat — after davesocozy (One Page Love)
page(109, 'cutting-mat', 'family=Courier+Prime:wght@400;700&family=Gochi+Hand', '#1F5C3B', '''
:root { --line: #D8D2BE; --focus: #1B1B1B; --f-bg: #fff; --f-border: 1.5px solid #1B1B1B; --b-bg: #1B1B1B; --b-text: #fff; --note: #5B5848; --f-radius: 0; --b-radius: 0; --f-pad: 3px; }
body { background: #3B2C1E; color: #1B1B1B; font: 15px/1.5 "Courier Prime", ui-monospace, monospace; }
::selection { background: #FFE66D; }
.mat { position: relative; margin: clamp(8px, 2vw, 22px); border-radius: 14px; min-height: calc(100svh - 44px); padding: 16px clamp(16px, 3vw, 40px) 40px; background-color: #1F6B45; background-image: linear-gradient(rgb(255 255 255 / 0.28) 1px, transparent 1px), linear-gradient(90deg, rgb(255 255 255 / 0.28) 1px, transparent 1px), linear-gradient(rgb(255 255 255 / 0.1) 1px, transparent 1px), linear-gradient(90deg, rgb(255 255 255 / 0.1) 1px, transparent 1px); background-size: 100px 100px, 100px 100px, 20px 20px, 20px 20px; box-shadow: inset 0 0 0 3px rgb(255 255 255 / 0.5), inset 0 0 80px rgb(0 0 0 / 0.3); overflow: hidden; }
.top { color: #EAF5EC; }
.items { display: grid; gap: 26px; padding-top: 8px; }
.it { background: #fff; padding: 18px; box-shadow: 0 14px 26px -12px rgb(0 0 0 / 0.6); rotate: var(--r, 0deg); }
.fx:not(.fx-rm) .items:not(.in) .it { translate: 0 -120vh; rotate: calc(var(--r, 0deg) * 6); } .fx .items.in .it { transition: translate 900ms cubic-bezier(0.3, 1.25, 0.5, 1) calc(var(--k) * 180ms), rotate 900ms var(--ease-out) calc(var(--k) * 180ms); }
.note1 { background: #FFE66D; --r: -3deg; } .note1 h1 { font: 400 clamp(1.9rem, 1.3rem + 2.4vw, 3rem)/1.05 "Gochi Hand", cursive; }
.photo { --r: 4deg; padding: 12px 12px 6px; width: min(260px, 70%); justify-self: center; position: relative; } .photo .ph { aspect-ratio: 1; background: #DCE8E0; overflow: hidden; } .photo img { width: 124%; max-width: none; margin: 6% 0 0 -12%; } .photo figcaption { font: 400 1.3rem/1.9 "Gochi Hand", cursive; text-align: center; }
.photo::before { content: ""; position: absolute; left: 50%; top: -14px; width: 90px; height: 28px; margin-left: -45px; background: rgb(255 240 190 / 0.85); rotate: -4deg; }
.card { --r: 1.5deg; background: #FBF8EE linear-gradient(#E0452B 0 0) 0 38px / 100% 1.5px no-repeat; } .card b { display: block; margin-bottom: 20px; letter-spacing: 0.08em; text-transform: uppercase; }
.slip { --r: -2deg; background: #F2F2F2; }
@media (min-width: 900px) { .items { grid-template-columns: 1.1fr 0.7fr 1fr; align-items: start; } .card { grid-column: 1 / span 2; max-width: 520px; } .slip { grid-column: 3; grid-row: 1 / span 2; align-self: end; } }
''', '''
<div class="mat"><div class="wrap" style="padding:0">{{TOP}}
	<main class="items" data-inview>
		<div class="it note1" style="--k:0"><h1>Hey, I’m Mostafa. I teach AI + cloud, one clear step at a time.</h1></div>
		<figure class="it photo" style="--k:1"><div class="ph">{{IMG}}</div><figcaption>the instructor</figcaption></figure>
		<div class="it slip" style="--k:3"><b>What I write</b>{{TOPICS_UL}}<div style="margin-top:16px">{{LINKS_INLINE}}</div></div>
		<div class="it card" style="--k:2"><b>Index card · newsletter</b><p style="margin-bottom:12px">Everything that used to stay in the corridor after class, by email.</p>{{FORM}}</div>
	</main>
	<footer class="foot" style="color:#EAF5EC">{{FOOT}}</footer>
</div></div>
''')

# 110 Torn paper — after Teardwn (One Page Love)
page(110, 'torn-paper', 'family=Zilla+Slab:wght@500;700&family=Geist:wght@400;500', '#2A7FD9', '''
:root { --line: rgb(0 0 0 / 0.18); --focus: #1A1A1A; --f-bg: #fff; --f-border: 1.5px solid #1A1A1A; --b-bg: #1A1A1A; --b-text: #fff; --note: #4C4A42; --f-radius: 4px; --b-radius: 2px; --f-pad: 4px; }
body { background: #2A7FD9; color: #1A1A1A; font: 16px/1.55 "Geist", system-ui, sans-serif; }
::selection { background: #1A1A1A; color: #fff; }
.top { color: #fff; }
.sky { min-height: 46svh; display: grid; align-content: end; padding-bottom: 60px; color: #fff; }
h1 { font: 700 clamp(2.6rem, 1.3rem + 6vw, 6.4rem)/0.92 "Zilla Slab", serif; letter-spacing: -0.03em; max-width: 9em; }
.layer { position: relative; margin-top: -34px; padding: 64px 0 70px; background: var(--c); -webkit-mask: conic-gradient(from -45deg at 50% 22px, #000 90deg, #0000 0) 0 0 / 34px 100%, linear-gradient(#000 0 0) 0 21px / 100% 100% no-repeat; mask: conic-gradient(from -45deg at 50% 22px, #000 90deg, #0000 0) 0 0 / 34px 100%, linear-gradient(#000 0 0) 0 21px / 100% 100% no-repeat; filter: drop-shadow(0 -6px 6px rgb(0 0 0 / 0.25)); }
.layer .inr { display: grid; gap: 24px 56px; align-items: end; }
.layer h2 { font: 700 clamp(1.8rem, 1.2rem + 2.4vw, 3rem)/1 "Zilla Slab", serif; letter-spacing: -0.02em; margin-bottom: 12px; }
.l1 { --c: #F3EBD8; } .l2 { --c: #F2B84B; } .l3 { --c: #fff; } .l4 { --c: #1F1F1F; color: #F3EBD8; --line: #3A3A3A; --note: #B9B3A3; padding-bottom: 20px; }
.l1 figure { width: min(250px, 62%); margin-bottom: -70px; }
@media (min-width: 860px) { .layer .inr { grid-template-columns: 1fr 1fr; } .l1 .inr { grid-template-columns: 250px 1fr; } }
''', '''
<div class="wrap">{{TOP}}<div class="sky"><h1 data-split data-fx="drop">Tearing AI and cloud down to the basics.</h1></div></div>
<main>
	<section class="layer l1"><div class="wrap inr"><figure data-reveal>{{IMG}}</figure><div data-reveal style="--i:1"><h2>Mostafa Saher, technical instructor.</h2><p style="max-width:32em">{{INTRO}}</p></div></div></section>
	<section class="layer l2"><div class="wrap inr"><h2 data-reveal>What’s under each layer.</h2><div data-reveal style="--i:1">{{TOPICS_UL}}</div></div></section>
	<section class="layer l3"><div class="wrap inr"><h2 data-reveal>Get the next one by email.</h2><div data-reveal style="--i:1;max-width:460px">{{FORM}}</div></div></section>
	<section class="layer l4"><div class="wrap inr"><div data-reveal>{{LINKS_ROWS}}</div><footer class="foot">{{FOOT}}</footer></div></section>
</main>
''')
print('d1 done')
