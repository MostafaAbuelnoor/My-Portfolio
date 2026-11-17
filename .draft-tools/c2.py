from lib2 import page
MORE = '<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>\n<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>'
MORECSS = '.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; } @media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }'

# 61 Holographic card
page(61, 'holo-card', 'family=Sora:wght@300..700', '#0B0B10', '''
:root { color-scheme: dark; --line: #262633; --focus: #C7B8FF; --f-bg: #15151D; --f-text: #F3F2F8; --f-ph: #9896A8; --f-border: 1px solid #2B2B3A; --b-bg: #F3F2F8; --b-text: #0B0B10; --note: #9896A8; --err: #FF9B8F; --f-radius: 12px; --b-radius: 8px; }
body { background: #0B0B10; color: #F3F2F8; font: 15px/1.6 "Sora", system-ui, sans-serif; }
::selection { background: #C7B8FF; color: #0B0B10; }
.hero { display: grid; gap: 36px 64px; align-items: center; min-height: calc(100svh - 70px); padding-block: 16px 40px; }
.area { display: grid; place-items: center; padding: 20px; }
.card { position: relative; width: min(320px, 84%); aspect-ratio: 5 / 7; border-radius: 24px; overflow: hidden; background: linear-gradient(150deg, #2B2140, #142238 55%, #0F2B2A); box-shadow: 0 40px 80px -30px #000, inset 0 0 0 1px rgb(255 255 255 / 0.12); transform-style: preserve-3d; }
.card::after { content: ""; position: absolute; inset: 0; background: radial-gradient(circle at var(--gx, 30%) var(--gy, 20%), rgb(255 255 255 / 0.5), rgb(190 150 255 / 0.25) 22%, rgb(90 220 220 / 0.18) 40%, transparent 62%); mix-blend-mode: screen; }
.card img { position: absolute; left: 50%; bottom: 0; width: 104%; max-width: none; translate: -50% 0; }
.card .tag { position: absolute; z-index: 2; left: 18px; top: 16px; right: 18px; display: flex; justify-content: space-between; font-size: 0.72rem; letter-spacing: 0.1em; text-transform: uppercase; }
.card .nm { position: absolute; z-index: 2; left: 18px; bottom: 16px; font-size: 1.5rem; font-weight: 700; line-height: 1; letter-spacing: -0.03em; text-shadow: 0 2px 12px #000; }
h1 { font-size: clamp(2.2rem, 1.2rem + 3.6vw, 4.2rem); font-weight: 600; line-height: 1.02; letter-spacing: -0.04em; }
.hero p { margin: 18px 0 24px; max-width: 30em; color: #B4B2C4; }
.signup { max-width: 440px; }
@media (min-width: 900px) { .hero { grid-template-columns: 0.9fr 1.1fr; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div class="area" data-tilt-area data-reveal="scale"><div class="card" data-tilt="16"><div class="tag"><span>Instructor pass</span><span>AI · Cloud</span></div>{{IMG}}<div class="nm">Mostafa<br>Saher</div></div></div>
		<div><h1 data-split data-fx="blur">Your pass to AI and cloud, one clear step at a time.</h1><p data-reveal style="--wait:600ms">Move your cursor over the card. Then leave your email, and I’ll send what comes up after class.</p><div data-reveal style="--wait:750ms">{{FORM}}</div></div>
	</main>
</div>''' + MORE)

# 62 Inverting lens
page(62, 'lens', 'family=Host+Grotesk:wght@400..800', '#000000', '''
:root { color-scheme: dark; --line: #2A2A2A; --focus: #fff; --f-bg: #111; --f-text: #fff; --f-ph: #999; --f-border: 1px solid #333; --b-bg: #fff; --b-text: #000; --note: #999; --err: #FF9B8F; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #000; color: #fff; font: 16px/1.5 "Host Grotesk", system-ui, sans-serif; }
.stage { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; overflow: hidden; isolation: isolate; }
h1 { align-self: center; font-size: clamp(3rem, 1.2rem + 9vw, 9.4rem); font-weight: 800; line-height: 0.88; letter-spacing: -0.055em; }
.lens { position: absolute; z-index: 5; left: 0; top: 0; width: min(46vw, 380px); aspect-ratio: 1; margin: calc(min(46vw, 380px) / -2) 0 0 calc(min(46vw, 380px) / -2); border-radius: 50%; background: #fff; mix-blend-mode: difference; pointer-events: none; translate: 68vw 42vh; }
.low { position: relative; display: grid; gap: 16px 40px; align-items: end; padding-bottom: 24px; }
.low p { max-width: 24em; font-size: 1.15rem; font-weight: 500; line-height: 1.25; } .field { gap: 0; }
.pic { position: relative; z-index: 6; display: grid; gap: 28px 56px; align-items: end; padding-block: 48px 0; }
.pic figure { width: min(260px, 60%); filter: grayscale(1) contrast(1.1); }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } .pic { grid-template-columns: 260px 1fr 1fr; } .pic figure { width: 100%; } }
@media (prefers-reduced-motion: no-preference) and (hover: none) { .lens { animation: drift 14s ease-in-out infinite alternate; } @keyframes drift { 0% { translate: 70vw 30vh; } 50% { translate: 25vw 55vh; } 100% { translate: 60vw 75vh; } } }
''', '''
<div class="stage" id="stage"><div class="wrap">{{TOP}}</div>
	<h1 class="wrap" data-split="chars" data-fx="rise" style="--stag:22ms">See AI and cloud in a new light.</h1>
	<div class="wrap low"><p data-reveal style="--wait:600ms">Mostafa Saher, technical instructor. One clear step at a time.</p><div data-reveal style="--wait:750ms">{{FORM}}</div></div>
	<div class="lens" id="lens"></div>
</div>
<section class="wrap pic"><figure data-reveal>{{IMG}}</figure><div data-reveal style="--i:1">{{TOPICS_UL}}</div><div data-reveal style="--i:2">{{LINKS_ROWS}}</div></section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''', '''
if (!FX.FINE || FX.RM) return;
const lens = document.getElementById('lens'), stage = document.getElementById('stage'); let x = innerWidth * 0.68, y = innerHeight * 0.42;
FX.onTick(() => { const r = stage.getBoundingClientRect(); const tx = FX.ptr.moved ? FX.ptr.x - r.left : x, ty = FX.ptr.moved ? FX.ptr.y - r.top : y; x = FX.lerp(x, tx, 0.14); y = FX.lerp(y, ty, 0.14); lens.style.translate = x.toFixed(1) + 'px ' + y.toFixed(1) + 'px'; });
''')

# 63 Depth
page(63, 'depth', 'family=Unbounded:wght@500;800&family=Hanken+Grotesk:wght@400..600', '#FF7A45', '''
:root { --line: rgb(255 255 255 / 0.35); --focus: #2B0F3A; --f-bg: #fff; --b-bg: #2B0F3A; --b-text: #fff; --note: #5B4A63; --f-radius: 14px; --b-radius: 10px; }
body { background: #2B0F3A; color: #fff; font: 16px/1.55 "Hanken Grotesk", system-ui, sans-serif; }
::selection { background: #fff; color: #FF7A45; }
.sun { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; overflow: hidden; background: linear-gradient(180deg, #FFB25C 0%, #FF7A45 38%, #D64578 72%, #5B2A86 100%); }
.back { position: absolute; left: 0; right: 0; top: 16%; text-align: center; font: 800 clamp(4.4rem, 22vw, 20rem)/0.8 "Unbounded", sans-serif; letter-spacing: -0.06em; text-transform: uppercase; white-space: nowrap; color: rgb(255 255 255 / 0.9); }
.orb { position: absolute; left: 50%; top: 20%; width: min(60vw, 520px); aspect-ratio: 1; margin-left: calc(min(60vw, 520px) / -2); border-radius: 50%; background: radial-gradient(circle at 50% 40%, #FFF3C4, #FFD27A 60%, rgb(255 210 122 / 0)); }
.sun figure { position: absolute; left: 50%; bottom: 0; height: 78%; aspect-ratio: 1100 / 1433; margin-left: calc(78svh * 1100 / 1433 / -2); }
.sun figure img { height: 100%; width: auto; max-width: none; }
.sun > .wrap { position: relative; z-index: 3; }
.cardx { position: relative; z-index: 4; max-width: 430px; margin: 0 0 24px; padding: 18px; border-radius: 22px; background: #fff; color: #2B0F3A; box-shadow: 0 30px 60px -24px rgb(43 15 58 / 0.7); }
.cardx h1 { font-size: 1.35rem; font-weight: 600; line-height: 1.15; letter-spacing: -0.02em; margin-bottom: 12px; }
''' + MORECSS, '''
<div class="sun"><div class="wrap">{{TOP}}</div><div></div>
	<div class="orb" data-par="10"></div>
	<p class="back" aria-hidden="true" data-par="38">Mostafa</p>
	<figure data-par="-16" data-reveal style="--wait:200ms">{{IMG}}</figure>
	<div class="wrap"><div class="cardx" data-par="8" data-reveal style="--wait:600ms"><h1>{{H}}</h1>{{FORM}}</div></div>
</div>''' + MORE)

# 64 Sticky stack
page(64, 'sticky-stack', 'family=Rethink+Sans:wght@400..800', '#111111', '''
:root { --line: rgb(0 0 0 / 0.15); --focus: #111; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #333; --f-radius: 14px; --b-radius: 10px; }
body { background: #111; color: #111; font: 16px/1.5 "Rethink Sans", system-ui, sans-serif; }
::selection { background: #111; color: #fff; }
.top { color: #fff; }
.stack { display: grid; gap: 16px; padding-bottom: 20svh; }
.sc { position: sticky; top: calc(12px + var(--k) * 14px); min-height: 72svh; border-radius: 28px; padding: clamp(22px, 4vw, 48px); display: grid; align-content: space-between; gap: 24px; overflow: hidden; box-shadow: 0 -10px 30px -18px rgb(0 0 0 / 0.5); }
.sc small { font-size: 0.85rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; }
.sc h2, .sc h1 { font-size: clamp(2rem, 1.2rem + 4.4vw, 5rem); font-weight: 800; line-height: 0.95; letter-spacing: -0.045em; max-width: 11em; }
.sc p { max-width: 32em; font-size: 1.15rem; font-weight: 500; line-height: 1.3; }
.c1 { background: #F4F0E6; } .c2 { background: #FFCC3D; } .c3 { background: #FF8A5B; } .c4 { background: #9EE6C2; } .c5 { background: #B9B2FF; } .c6 { background: #fff; }
.c2 h2 { max-width: 6em; position: relative; z-index: 1; } .c2 figure { position: absolute; right: 4%; bottom: 0; height: 88%; aspect-ratio: 1100 / 1433; } .c2 img { height: 100%; width: auto; max-width: none; }
.c6 .signup { max-width: 460px; }
.foot { color: #fff; }
''', '''
<div class="wrap">{{TOP}}
	<main class="stack">
		<section class="sc c1" style="--k:0"><small>Mostafa Saher</small><h1 data-split>{{H}}</h1><p>Scroll. Each card is one step.</p></section>
		<section class="sc c2" style="--k:1"><small>The instructor</small><h2>Technical instructor. AI and cloud.</h2><p style="max-width:16em">I teach it for a living.</p><figure>{{IMG}}</figure></section>
		<section class="sc c3" style="--k:2"><small>Thoughts</small><h2>Notes from the classroom.</h2><p>What students get stuck on, and the explanation that finally made it click.</p></section>
		<section class="sc c4" style="--k:3"><small>Opinions</small><h2>Where I stand on the hype.</h2><p>New models and cloud services, said plainly.</p></section>
		<section class="sc c5" style="--k:4"><small>Resources</small><h2>What I’d hand a student.</h2><p>The labs, docs, courses and tools I actually use, each with a line on why.</p></section>
		<section class="sc c6" style="--k:5"><small>Newsletter</small><h2>Get all of it by email.</h2><div>{{FORM}}<div style="margin-top:22px">{{LINKS_INLINE}}</div></div></section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 65 Sideways
page(65, 'sideways', 'family=Epilogue:wght@400..800', '#0F0F12', '''
:root { --line: rgb(255 255 255 / 0.25); --focus: #fff; --f-bg: #fff; --b-bg: #0F0F12; --b-text: #fff; --note: inherit; --f-radius: 12px; --b-radius: 8px; }
html, body { height: 100%; }
body { background: #0F0F12; color: #fff; font: 16px/1.5 "Epilogue", system-ui, sans-serif; overflow: hidden; }
.rail { display: flex; height: 100svh; overflow-x: auto; overflow-y: hidden; scroll-snap-type: x mandatory; scrollbar-width: none; }
.rail::-webkit-scrollbar { display: none; }
.pn { flex: 0 0 100vw; scroll-snap-align: start; position: relative; display: grid; align-content: center; gap: 22px; padding: 72px clamp(20px, 7vw, 110px) 96px; overflow: hidden; }
.pn h1, .pn h2 { font-size: clamp(2.4rem, 1.2rem + 6vw, 6.4rem); font-weight: 800; line-height: 0.92; letter-spacing: -0.05em; max-width: 10em; }
.pn p { max-width: 30em; font-size: 1.2rem; line-height: 1.35; }
.p1 { background: #0F0F12; } .p2 { background: #2F5BFF; } .p3 { background: #FF5A3C; } .p4 { background: #F2EEE3; color: #0F0F12; --line: rgb(0 0 0 / 0.2); } .p5 { background: #12B886; color: #062018; --line: rgb(0 0 0 / 0.25); }
.pn figure { position: absolute; right: 4%; bottom: 0; height: 76%; aspect-ratio: 1100 / 1433; opacity: 0.98; } .pn figure img { height: 100%; width: auto; max-width: none; }
.p2 h2, .p2 p { position: relative; z-index: 1; max-width: 8em; } .p2 p { max-width: 16em; }
.hud { position: fixed; z-index: 5; left: 0; right: 0; bottom: 0; display: flex; align-items: center; gap: 14px; padding: 16px clamp(20px, 7vw, 110px) max(18px, env(safe-area-inset-bottom)); mix-blend-mode: difference; }
.hud button { width: 46px; height: 46px; border: 1.5px solid #fff; border-radius: 50%; background: none; color: #fff; font-size: 1.1rem; cursor: pointer; transition: transform 140ms var(--ease-out); } .hud button:active { transform: scale(0.94); }
.barx { flex: 1; height: 2px; background: rgb(255 255 255 / 0.3); } .barx i { display: block; height: 100%; width: 20%; background: #fff; transform-origin: 0 50%; transition: transform 500ms var(--ease-out); }
.name { position: fixed; z-index: 5; left: clamp(20px, 7vw, 110px); top: 20px; font-weight: 700; mix-blend-mode: difference; }
.p5 .signup { max-width: 460px; }
''', '''
<b class="name">Mostafa Saher</b>
<main class="rail" id="rail">
	<section class="pn p1"><h1 data-split>{{H}}</h1><p data-reveal style="--wait:500ms">Swipe, scroll or use the arrows.</p></section>
	<section class="pn p2"><h2>Technical instructor.</h2><p>I teach AI and cloud for a living.</p><figure>{{IMG}}</figure></section>
	<section class="pn p3"><h2>The best part comes after class.</h2><p>The questions in the corridor, the “wait, so why does that work?”, the links I send people afterwards.</p></section>
	<section class="pn p4"><h2>So I write it down.</h2>{{TOPICS_UL}}</section>
	<section class="pn p5"><h2>Get it by email.</h2>{{FORM}}{{LINKS_INLINE}}</section>
</main>
<div class="hud"><button id="pv" aria-label="Previous panel">←</button><div class="barx"><i id="pg"></i></div><button id="nx" aria-label="Next panel">→</button></div>
''', '''
const rail = document.getElementById('rail'), pg = document.getElementById('pg'), n = rail.children.length;
const idx = () => Math.round(rail.scrollLeft / rail.clientWidth);
const go = (i) => rail.scrollTo({ left: Math.max(0, Math.min(n - 1, i)) * rail.clientWidth, behavior: FX.RM ? 'auto' : 'smooth' });
const upd = () => { pg.style.transform = 'translateX(' + (idx() * 100) + '%)'; };
rail.addEventListener('scroll', upd, { passive: true });
document.getElementById('pv').onclick = () => go(idx() - 1); document.getElementById('nx').onclick = () => go(idx() + 1);
addEventListener('keydown', (e) => { if (e.target.matches('input')) return; if (e.key === 'ArrowRight') go(idx() + 1); if (e.key === 'ArrowLeft') go(idx() - 1); });
let lock = 0; rail.addEventListener('wheel', (e) => { if (Math.abs(e.deltaY) < Math.abs(e.deltaX)) return; e.preventDefault(); const now = Date.now(); if (now - lock < 650 || Math.abs(e.deltaY) < 12) return; lock = now; go(idx() + (e.deltaY > 0 ? 1 : -1)); }, { passive: false });
''')

# 66 Scroll zoom
page(66, 'scroll-zoom', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800', '#F3F1EA', '''
:root { --line: #D8D4C6; --focus: #15140F; --f-bg: #fff; --b-bg: #15140F; --b-text: #fff; --note: #6A665A; --f-radius: 999px; --b-radius: 999px; }
body { background: #F3F1EA; color: #15140F; font: 16px/1.5 "Bricolage Grotesque", system-ui, sans-serif; }
::selection { background: #15140F; color: #F3F1EA; }
.fixedtop { position: fixed; z-index: 5; left: 0; right: 0; top: 0; mix-blend-mode: difference; color: #fff; }
.pin { height: 260vh; }
.view { position: sticky; top: 0; height: 100svh; overflow: hidden; display: grid; place-items: center; }
.word { position: absolute; top: 50%; font-size: clamp(3.4rem, 15vw, 15rem); font-weight: 800; line-height: 0.8; letter-spacing: -0.06em; white-space: nowrap; }
.w-l { right: 50%; translate: calc(var(--p, 0) * -42vw - 0.1em) -50%; } .w-r { left: 50%; translate: calc(var(--p, 0) * 42vw + 0.1em) -50%; }
.win { position: relative; width: 100%; height: 100%; background: #2D5BFF; clip-path: inset(calc((1 - var(--p, 0)) * 34%) calc((1 - var(--p, 0)) * 41%) round calc((1 - var(--p, 0)) * 200px)); display: flex; justify-content: center; align-items: flex-end; }
.win img { height: 86%; width: auto; max-width: none; scale: calc(0.6 + var(--p, 0) * 0.4); transform-origin: 50% 100%; }
.cap { position: absolute; left: 0; right: 0; bottom: 6%; text-align: center; color: #fff; font-size: clamp(1.2rem, 1rem + 1.4vw, 2rem); font-weight: 700; letter-spacing: -0.02em; opacity: calc((var(--p, 0) - 0.7) * 3.4); padding-inline: 20px; }
.hint { position: absolute; bottom: 20px; left: 50%; translate: -50% 0; font-size: 0.85rem; opacity: calc(1 - var(--p, 0) * 6); }
.after { display: grid; gap: 28px 56px; padding-block: 64px 8px; }
.after h2 { font-size: clamp(2rem, 1.2rem + 3vw, 3.6rem); font-weight: 800; line-height: 0.98; letter-spacing: -0.04em; margin-bottom: 18px; }
@media (min-width: 860px) { .after { grid-template-columns: 1fr 1fr; } }
''', '''
<div class="fixedtop"><div class="wrap">{{TOP}}</div></div>
<main>
	<section class="pin" data-progress="pin"><div class="view">
		<span class="word w-l" aria-hidden="true">AI &amp;</span><span class="word w-r" aria-hidden="true">cloud</span>
		<h1 class="sr">AI and cloud, one clear step at a time</h1>
		<div class="win">{{IMG}}</div>
		<p class="cap">Mostafa Saher. One clear step at a time.</p><span class="hint">Scroll</span>
	</div></section>
	<section class="wrap after"><div data-reveal><h2>Get the newsletter.</h2><p style="margin-bottom:18px;max-width:32em">{{INTRO}}</p>{{FORM}}</div><div data-reveal style="--i:1">{{TOPICS_UL}}<div style="margin-top:24px">{{LINKS_INLINE}}</div></div></section>
</main>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 67 Blinds
page(67, 'blinds', 'family=Albert+Sans:wght@400..800', '#101B3A', '''
:root { color-scheme: dark; --line: #24336B; --focus: #FFD166; --f-bg: #172554; --f-text: #F4F6FF; --f-ph: #98A4D4; --f-border: 1px solid #2C3D80; --b-bg: #FFD166; --b-text: #101B3A; --note: #98A4D4; --err: #FF9B8F; --f-radius: 10px; --b-radius: 6px; }
body { background: #101B3A; color: #F4F6FF; font: 16px/1.55 "Albert Sans", system-ui, sans-serif; }
::selection { background: #FFD166; color: #101B3A; }
.room { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; background: linear-gradient(180deg, #1B2B63, #101B3A); }
.slats { position: absolute; inset: 0; z-index: 6; display: grid; grid-template-rows: repeat(10, 1fr); pointer-events: none; }
.slats i { background: #22346F; border-bottom: 2px solid #101B3A; transform-origin: 50% 0; }
.fx:not(.fx-rm) .slats i { animation: slat 900ms var(--ease-io) forwards; animation-delay: calc(350ms + var(--k) * 70ms); }
.fx-rm .slats, html:not(.fx) .slats { display: none; }
@keyframes slat { to { transform: scaleY(0.04); background: #3A56B8; opacity: 0.3; } }
.hero { display: grid; gap: 20px 48px; align-items: end; }
.copy { align-self: center; padding-block: 12px 36px; }
h1 { font-size: clamp(2.3rem, 1.2rem + 4.2vw, 4.8rem); font-weight: 800; line-height: 0.98; letter-spacing: -0.045em; max-width: 10em; --wait: 1100ms; }
.copy p { margin: 18px 0 22px; max-width: 30em; color: #B6C0E8; }
.signup { max-width: 440px; }
.shot { justify-self: center; width: min(320px, 74%); }
@media (min-width: 900px) { .hero { grid-template-columns: 1.15fr 0.85fr; } .shot { width: min(100%, 470px); justify-self: end; } }
''' + MORECSS, '''
<div class="room"><div class="slats" aria-hidden="true">''' + ''.join(f'<i style="--k:{k}"></i>' for k in range(10)) + '''</div>
	<div class="wrap">{{TOP}}</div>
	<main class="wrap hero">
		<div class="copy"><h1 data-split>Let some light in on AI and cloud.</h1><p data-reveal style="--wait:1500ms">I’m Mostafa Saher, a technical instructor. I teach one clear step at a time, and I write down what comes up after class.</p><div data-reveal style="--wait:1650ms">{{FORM}}</div></div>
		<div class="shot" data-par="-14">{{IMG}}</div>
	</main>
</div>''' + MORE)

# 68 Curtains
page(68, 'curtains', 'family=Anton&family=Geist:wght@400;500', '#F4F1EA', '''
:root { --red: #C8102E; --line: #DAD5C7; --focus: var(--red); --f-bg: #fff; --b-bg: var(--red); --b-text: #fff; --note: #6B675B; --f-radius: 6px; --b-radius: 3px; --f-pad: 5px; }
body { background: #F4F1EA; color: #17150F; font: 16px/1.55 "Geist", system-ui, sans-serif; }
::selection { background: var(--red); color: #fff; }
.cur { position: fixed; z-index: 20; top: 0; bottom: 0; width: 50.5%; background: var(--red); color: #fff; display: grid; align-items: center; font: 400 clamp(4rem, 17vw, 16rem)/0.8 "Anton", sans-serif; text-transform: uppercase; overflow: hidden; pointer-events: none; }
.cur.l { left: 0; justify-items: end; } .cur.r { right: 0; justify-items: start; }
.fx:not(.fx-rm) .cur { animation: open 1100ms var(--ease-io) 900ms forwards; }
.fx:not(.fx-rm) .cur.l { --to: -101%; } .fx:not(.fx-rm) .cur.r { --to: 101%; }
.fx-rm .cur, html:not(.fx) .cur { display: none; }
@keyframes open { to { transform: translateX(var(--to)); } }
.hero { display: grid; gap: 20px 48px; align-items: end; min-height: calc(100svh - 70px); }
.copy { align-self: center; padding-block: 12px 36px; }
h1 { font: 400 clamp(3.2rem, 1.4rem + 8vw, 8.4rem)/0.88 "Anton", sans-serif; text-transform: uppercase; --wait: 1700ms; }
h1 em { font-style: normal; color: var(--red); }
.copy p { margin: 18px 0 22px; max-width: 30em; }
.signup { max-width: 440px; }
.shot { justify-self: center; width: min(320px, 74%); }
@media (min-width: 900px) { .hero { grid-template-columns: 1.15fr 0.85fr; } .shot { width: min(100%, 460px); justify-self: end; } }
''' + MORECSS, '''
<div class="cur l" aria-hidden="true"><span>Mos</span></div><div class="cur r" aria-hidden="true"><span>tafa</span></div>
<div class="wrap">{{TOP}}
	<main class="hero">
		<div class="copy"><h1 data-split>Class is <em>in session.</em></h1><p data-reveal style="--wait:2100ms">I’m Mostafa Saher. I teach AI and cloud, one clear step at a time, and I write down what comes up after class.</p><div data-reveal style="--wait:2250ms">{{FORM}}</div></div>
		<div class="shot" data-reveal style="--wait:1900ms">{{IMG}}</div>
	</main>
</div>''' + MORE)

# 69 Orbit
page(69, 'orbit', 'family=Figtree:wght@400..800', '#F7F7FB', '''
:root { --violet: #5B3DF5; --line: #E0E0EC; --focus: var(--violet); --f-bg: #fff; --f-border: 1px solid #DADAE8; --b-bg: var(--violet); --b-text: #fff; --note: #666680; --f-radius: 999px; --b-radius: 999px; }
body { background: #F7F7FB; color: #14142B; font: 16px/1.55 "Figtree", system-ui, sans-serif; }
::selection { background: var(--violet); color: #fff; }
.hero { display: grid; gap: 28px 56px; align-items: center; min-height: calc(100svh - 70px); padding-bottom: 36px; }
.sys { position: relative; justify-self: center; width: min(400px, 88vw); aspect-ratio: 1; }
.ring { position: absolute; inset: 0; border: 1.5px dashed #C9C6EE; border-radius: 50%; --dur: 26s; }
.ring.r2 { inset: 17%; --dur: 18s; animation-direction: reverse; border-style: solid; border-color: #E3E1F7; }
.sat { position: absolute; left: 50%; top: 0; translate: -50% -50%; }
.sat a { display: block; padding: 8px 14px; border-radius: 999px; background: #fff; box-shadow: 0 8px 20px -8px rgb(91 61 245 / 0.45); font-weight: 700; font-size: 0.92rem; --dur: 26s; animation-direction: reverse; }
.s2 { top: 75%; left: 6.7%; } .s3 { top: 75%; left: 93.3%; }
.r2 .dot { position: absolute; left: 50%; top: 0; width: 14px; height: 14px; margin: -7px; border-radius: 50%; background: var(--violet); }
.core { position: absolute; inset: 24%; border-radius: 50%; background: #DCD6FF; overflow: hidden; }
.core img { width: 132%; max-width: none; margin: 6% 0 0 -16%; }
.sys:hover .fx-spin { animation-play-state: paused; }
h1 { font-size: clamp(2.3rem, 1.2rem + 3.8vw, 4.4rem); font-weight: 800; line-height: 1; letter-spacing: -0.04em; max-width: 11em; }
.hero p { margin: 16px 0 22px; max-width: 30em; color: #50506B; }
.signup { max-width: 440px; }
@media (min-width: 900px) { .hero { grid-template-columns: 1.1fr 0.9fr; } }
''' + MORECSS.replace('1fr 1fr', '1fr'), '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div><h1 data-split data-fx="pop">Everything I do revolves around making it click.</h1><p data-reveal style="--wait:600ms">I’m Mostafa Saher. I teach AI and cloud, one clear step at a time. The links are in orbit; hover to catch one.</p><div data-reveal style="--wait:750ms">{{FORM}}</div></div>
		<div class="sys" data-reveal="scale">
			<div class="ring fx-spin"><span class="sat"><a class="fx-spin" href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a></span><span class="sat s2"><a class="fx-spin" href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a></span><span class="sat s3"><a class="fx-spin" href="mailto:mostafasaher@gmail.com">Email</a></span></div>
			<div class="ring r2 fx-spin"><i class="dot"></i></div>
			<div class="core">{{IMG}}</div>
		</div>
	</main>
	<section class="more"><div data-reveal>{{TOPICS_UL}}</div></section>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 70 Signal
page(70, 'signal', 'family=Chivo+Mono:wght@400;500&family=Chivo:wght@400..800', '#06110B', '''
:root { color-scheme: dark; --green: #5CF2A0; --line: #143024; --focus: var(--green); --f-bg: #0B1D14; --f-text: #EAF7EF; --f-ph: #7FA890; --f-border: 1px solid #1B4030; --b-bg: var(--green); --b-text: #06110B; --note: #7FA890; --err: #FF9B8F; --f-radius: 4px; --b-radius: 2px; --f-pad: 4px; }
body { background: #06110B; color: #EAF7EF; font: 16px/1.55 "Chivo", system-ui, sans-serif; }
::selection { background: var(--green); color: #06110B; }
.air { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; }
.air canvas { position: absolute; inset: 0; color: var(--green); }
.air > * { position: relative; }
.mono { font: 500 0.78rem "Chivo Mono", monospace; letter-spacing: 0.08em; text-transform: uppercase; color: var(--green); }
.hero { display: grid; gap: 16px 48px; align-items: end; }
.copy { align-self: center; padding-block: 12px 36px; }
h1 { margin-top: 12px; font-size: clamp(2.3rem, 1.2rem + 4.2vw, 4.8rem); font-weight: 800; line-height: 0.98; letter-spacing: -0.04em; max-width: 10em; }
.copy p.s { margin: 18px 0 22px; max-width: 30em; color: #A9CDB8; }
.signup { max-width: 440px; }
.shot { justify-self: center; width: min(300px, 70%); }
.shot img { filter: drop-shadow(0 0 1.5px rgb(92 242 160 / 0.8)); }
@media (min-width: 900px) { .hero { grid-template-columns: 1.15fr 0.85fr; } .shot { width: min(100%, 440px); justify-self: center; } }
''' + MORECSS, '''
<div class="air"><canvas data-canvas="rings" data-cx="0.72" data-cy="0.62"></canvas>
	<div class="wrap">{{TOP}}</div>
	<main class="wrap hero">
		<div class="copy"><p class="mono"><span class="fx-pulse">●</span> On air</p><h1 data-split>Broadcasting from the classroom.</h1><p class="s" data-reveal style="--wait:600ms">I’m Mostafa Saher. I teach AI and cloud, one clear step at a time. Tune in by email.</p><div data-reveal style="--wait:750ms">{{FORM}}</div></div>
		<div class="shot" data-reveal="scale" style="--wait:300ms">{{IMG}}</div>
	</main>
</div>''' + MORE)
print('c2 done')
