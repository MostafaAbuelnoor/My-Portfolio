from lib2 import page
MORE = '<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>\n<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>'
MORECSS = '.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; } @media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }'
HERO2 = '.hero { display: grid; gap: 24px 48px; align-items: center; min-height: calc(100svh - 70px); padding-bottom: 36px; } @media (min-width: 900px) { .hero { grid-template-columns: 1.1fr 0.9fr; } }'

# 121 Arch text — after Gatzara (Portfolio Project)
page(121, 'arch-text', 'family=Archivo:wght@500..900', '#FF2A12', '''
:root { --line: rgb(0 0 0 / 0.3); --focus: #0C0C0C; --f-bg: #0C0C0C; --f-text: #fff; --f-ph: #BDBDBD; --b-bg: #FF2A12; --b-text: #0C0C0C; --note: #3A0703; --err: #2A0000; --f-radius: 0; --b-radius: 0; --f-pad: 4px; }
body { background: #FF2A12; color: #0C0C0C; font: 600 15px/1.45 "Archivo", system-ui, sans-serif; }
::selection { background: #0C0C0C; color: #FF2A12; }
.tick { border-block: 2px solid #0C0C0C; padding-block: 5px; font-size: 0.75rem; letter-spacing: 0.08em; text-transform: uppercase; --dur: 30s; } .tick i { font-style: normal; margin-inline: 1.4em; }
.stage { position: relative; height: min(82svh, 720px); overflow: hidden; }
.stage svg { position: absolute; left: 50%; top: 6%; width: max(118vw, 900px); translate: -50% 0; overflow: visible; }
.stage text { font: 900 104px "Archivo", sans-serif; letter-spacing: -2px; text-transform: uppercase; fill: #0C0C0C; }
.gate { position: absolute; left: 50%; bottom: 0; width: min(330px, 70vw); height: 50%; margin-left: calc(min(330px, 70vw) / -2); border-radius: 999px 999px 0 0; background: #0C0C0C; overflow: hidden; display: flex; align-items: flex-end; justify-content: center; }
.gate img { width: 108%; max-width: none; filter: grayscale(1) contrast(1.15); }
.mid { position: absolute; left: 0; right: 0; top: 28%; text-align: center; font-size: clamp(1rem, 0.8rem + 1vw, 1.5rem); font-weight: 800; letter-spacing: -0.01em; padding-inline: 20px; }
.low { display: grid; gap: 18px 48px; align-items: end; padding-block: 26px 0; }
h1 { font-size: clamp(1.8rem, 1.2rem + 2.6vw, 3.2rem); font-weight: 900; line-height: 0.95; letter-spacing: -0.04em; text-transform: uppercase; max-width: 12em; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="tick" data-marquee aria-hidden="true">Class is in session<i>◆</i>AI and cloud<i>◆</i>One clear step at a time<i>◆</i>Mostafa Saher<i>◆</i></div>
<div class="wrap">{{TOP}}</div>
<main>
	<div class="stage" aria-hidden="true">
		<svg viewBox="0 0 1200 700"><defs><path id="arc" d="M-300,470 A1400,1400 0 0,1 1500,470"/></defs><text><textPath href="#arc" id="tp" startOffset="0">AI &amp; cloud teaching ✳ one clear step at a time ✳ AI &amp; cloud teaching ✳ one clear step at a time ✳ AI &amp; cloud teaching ✳ one clear step at a time ✳</textPath></text></svg>
		<p class="mid">A one-person classroom<br>explaining AI and cloud<br>through clear lessons.</p>
		<div class="gate">{{IMG}}</div>
	</div>
	<div class="wrap low"><h1 data-split>{{H}}</h1><div data-reveal>{{FORM}}</div></div>
</main>''' + MORE, '''
const tp = document.getElementById('tp'); if (FX.RM) return; let o = 0; FX.onTick(() => { o = (o - 1.1) % 1570; tp.setAttribute('startOffset', o.toFixed(1)); });
''')

# 122 Portal — after Jarcos (Portfolio Project)
page(122, 'portal', 'family=Inter+Tight:wght@400..700', '#FFFFFF', '''
:root { --line: #E4E4E4; --focus: #1437FF; --f-bg: #F2F2F2; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #fff; color: #111; font: 14px/1.5 "Inter Tight", system-ui, sans-serif; }
::selection { background: #1437FF; color: #fff; }
.screen { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; }
.metas { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; padding-block: 16px; font-size: 0.85rem; } .metas a { text-decoration: underline; text-underline-offset: 3px; }
.door { position: absolute; z-index: 1; left: 50%; bottom: 9vw; width: min(300px, 46vw); aspect-ratio: 3 / 4.2; margin-left: calc(min(300px, 46vw) / -2); background: #1437FF; overflow: hidden; }
.door::before { content: ""; position: absolute; inset: 14% 14% 0; background: linear-gradient(#FFB703 0%, #FB5607 45%, #FF006E 100%); }
.door::after { content: ""; position: absolute; inset: 14% 14% 0; background: linear-gradient(90deg, rgb(0 0 0 / 0.35), transparent 30%); }
.door img { position: absolute; z-index: 2; left: 50%; bottom: 0; width: 96%; translate: -50% 0; }
@media (prefers-reduced-motion: no-preference) { .door::before { animation: hue 9s linear infinite; } @keyframes hue { to { filter: hue-rotate(360deg); } } }
.giant { position: absolute; left: 0; right: 0; bottom: -0.17em; text-align: center; font-size: 22vw; font-weight: 600; line-height: 0.8; letter-spacing: -0.06em; white-space: nowrap; }
.giant.front { z-index: 2; clip-path: inset(0 0 0 50%); } .giant.back { z-index: 0; }
.ask { position: relative; z-index: 3; max-width: 400px; margin-top: clamp(8px, 4vh, 40px); font-size: 15px; } .ask p { font-weight: 600; margin-bottom: 12px; } .field { gap: 0; }
@media (min-width: 860px) { .metas { grid-template-columns: repeat(4, 1fr); } }
''' + MORECSS, '''
<div class="screen">
	<div class="wrap">
		<div class="metas"><p>Mostafa Saher<br>Technical instructor</p><p>AI and cloud<br>One clear step at a time</p><p><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a><br><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a></p><p><a href="mailto:mostafasaher@gmail.com">Email</a><br><a href="#email" data-focus-signup>Newsletter</a></p></div>
		<main class="ask" data-reveal><p>Step through. Notes from after class, by email.</p>{{FORM}}</main>
	</div>
	<h1 class="giant back">MOSTAFA</h1>
	<div class="door" data-wipe style="--wait:300ms">{{IMG}}</div>
	<p class="giant front" aria-hidden="true">MOSTAFA</p>
</div>
<section class="wrap more"><div data-reveal><p style="margin-bottom:18px;font-size:16px">{{INTRO}}</p></div><div data-reveal style="--i:1">{{TOPICS_UL}}</div></section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 123 Pastel gothic — after Chenice Taylor (Portfolio Project)
page(123, 'pastel-gothic', 'family=UnifrakturCook:wght@700&family=Geist+Mono:wght@400&family=Geist:wght@400;500', '#E9D5F2', '''
:root { --line: rgb(40 20 60 / 0.2); --focus: #2B1B3F; --f-bg: rgb(255 255 255 / 0.7); --b-bg: #2B1B3F; --b-text: #fff; --note: #5B4A6E; --f-radius: 999px; --b-radius: 999px; }
body { background: #F1E7F6; color: #2B1B3F; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #2B1B3F; color: #F1E7F6; }
.dream { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; text-align: center; background: linear-gradient(120deg, #CDB4F6, #F9C6D8 35%, #FDE7C2 60%, #BFE6F5); background-size: 240% 240%; }
@media (prefers-reduced-motion: no-preference) { .dream { animation: drift 16s ease-in-out infinite alternate; } @keyframes drift { to { background-position: 100% 100%; } } }
.bow { position: absolute; right: -18%; top: 8%; width: 90vmin; aspect-ratio: 1; border-radius: 50%; border: 5vmin solid transparent; background: conic-gradient(from 200deg, #FF9AA2, #FFDAC1, #E2F0CB, #B5EAD7, #C7CEEA, #FF9AA2) border-box; -webkit-mask: linear-gradient(#000 0 0) padding-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor; mask: linear-gradient(#000 0 0) padding-box exclude, linear-gradient(#000 0 0); opacity: 0.55; filter: blur(6px); }
.pillnav { display: flex; justify-content: center; flex-wrap: wrap; gap: 8px; padding-block: 18px; } .pillnav a, .pillnav span { padding: 5px 14px; border: 1px solid #2B1B3F; border-radius: 999px; font: 400 0.72rem "Geist Mono", monospace; letter-spacing: 0.08em; text-transform: uppercase; }
.dream > .wrap { position: relative; z-index: 2; }
.mid { align-self: center; padding-block: 8px 30px; }
h1 { font: 700 clamp(3.2rem, 1.4rem + 9vw, 8.6rem)/0.95 "UnifrakturCook", serif; --stag: 40ms; }
.mid p.s { max-width: 34em; margin: 14px auto 6px; }
.mono { font: 400 0.75rem "Geist Mono", monospace; letter-spacing: 0.08em; text-transform: uppercase; }
.face { width: 84px; height: 84px; margin: 18px auto 0; border-radius: 50%; background: rgb(255 255 255 / 0.6); border: 1px solid #2B1B3F; }
.signup { max-width: 430px; margin: 20px auto 0; text-align: left; } .note { text-align: center; }
''' + MORECSS, '''
<div class="dream"><i class="bow" data-par="18"></i>
	<div class="wrap"><nav class="pillnav" aria-label="Sections"><span>Home</span><a href="#email" data-focus-signup>Newsletter</a><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a></nav></div>
	<main class="wrap mid">
		<h1 data-split="chars" data-fx="blur">Mostafa Saher</h1>
		<p class="s" data-reveal="fade" style="--wait:700ms">A technical instructor teaching at the intersection of AI, cloud and people.</p>
		<p class="mono" data-reveal="fade" style="--wait:800ms">Instructor + newsletter writer · one clear step at a time</p>
		<div class="face fx-float" data-reveal="scale" style="--wait:900ms">{{IMG}}</div>
		<div data-reveal="fade" style="--wait:1000ms">{{FORM}}</div>
	</main>
</div>''' + MORE)

# 124 Twin panels — after Daniel D (Portfolio Project)
page(124, 'twin-panels', 'family=Manrope:wght@400..800', '#FFFFFF', '''
:root { --line: rgb(255 255 255 / 0.3); --focus: #fff; --f-bg: rgb(255 255 255 / 0.16); --f-text: #fff; --f-ph: #E6EEF5; --f-border: 1px solid rgb(255 255 255 / 0.4); --b-bg: #fff; --b-text: #0B2A3A; --note: #E6EEF5; --err: #FFE0DA; --f-radius: 14px; --b-radius: 10px; }
body { background: #fff; color: #10151C; font: 16px/1.55 "Manrope", system-ui, sans-serif; }
::selection { background: #0F6B7A; color: #fff; }
.pair { display: grid; gap: 14px; padding-bottom: 14px; }
.pnl { position: relative; min-height: min(78svh, 640px); border-radius: 30px; overflow: hidden; color: #fff; display: grid; align-content: end; padding: clamp(20px, 3vw, 36px); isolation: isolate; }
.pnl canvas { position: absolute; inset: 0; z-index: -1; }
.sea { background: linear-gradient(160deg, #0B4F6C, #01303F); } .sea canvas { color: #BDF3FF; }
.glow { background: #FF6B3D; }
.glow::before { content: ""; position: absolute; inset: -30%; z-index: -1; background: radial-gradient(40% 40% at 30% 30%, #FFD166, transparent 70%), radial-gradient(45% 45% at 75% 35%, #EF476F, transparent 70%), radial-gradient(50% 50% at 55% 80%, #3A86FF, transparent 70%); filter: blur(30px); }
@media (prefers-reduced-motion: no-preference) { .glow::before { animation: turn 22s linear infinite; } @keyframes turn { to { rotate: 360deg; } } }
.glass { padding: 18px; border-radius: 20px; background: rgb(255 255 255 / 0.14); border: 1px solid rgb(255 255 255 / 0.35); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); }
h1 { font-size: clamp(1.6rem, 1.1rem + 1.8vw, 2.5rem); font-weight: 700; line-height: 1.08; letter-spacing: -0.035em; margin-bottom: 8px; }
.glow figure { position: absolute; z-index: -1; left: 50%; bottom: 0; width: min(320px, 76%); translate: -50% 0; }
.glow .row { display: flex; justify-content: space-between; align-items: center; gap: 12px; } .glow .row b { font-size: 1.1rem; }
.glow a.go { display: grid; place-items: center; width: 46px; height: 46px; border-radius: 50%; background: #fff; color: #10151C; font-size: 1.2rem; }
@media (min-width: 860px) { .pair { grid-template-columns: 1fr 1fr; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="pair">
		<section class="pnl sea" data-reveal><canvas data-canvas="waves" data-rows="18"></canvas><div class="glass"><h1>Mostafa is an AI and cloud instructor, writer and note-taker.</h1><p style="margin-bottom:14px;color:#E6EEF5">One clear step at a time. Get the newsletter:</p>{{FORM}}</div></section>
		<section class="pnl glow" data-reveal style="--i:1"><figure>{{IMG}}</figure><div class="glass row"><b>Learn about him</b><a class="go" href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener" aria-label="LinkedIn">↗</a></div></section>
	</main>
</div>''' + MORE)

# 125 Rising block — after Paul Macgregor (Portfolio Project)
page(125, 'rising-block', 'family=Host+Grotesk:wght@400..700', '#FFFFFF', '''
:root { --line: rgb(255 255 255 / 0.4); --focus: #fff; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #FFE3DC; --err: #3A0000; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #fff; color: #111; font: 15px/1.5 "Host Grotesk", system-ui, sans-serif; }
::selection { background: #FF3B1D; color: #fff; }
.fixedtop { position: fixed; z-index: 6; left: 0; right: 0; top: 0; mix-blend-mode: difference; color: #fff; }
.pin { height: 240vh; }
.view { position: sticky; top: 0; height: 100svh; overflow: hidden; }
.say { position: absolute; right: clamp(18px, 6vw, 90px); top: 18%; max-width: 20em; font-size: clamp(1rem, 0.9rem + 0.6vw, 1.35rem); font-weight: 500; line-height: 1.25; }
.blk { position: absolute; left: 0; right: 0; bottom: 0; background: #FF3B1D; height: calc(18% + var(--p, 0) * 82%); margin-inline: calc((1 - var(--p, 0)) * 12%); display: grid; align-content: center; overflow: hidden; }
.blk .inr { opacity: calc((var(--p, 0) - 0.55) * 3); color: #fff; display: grid; gap: 18px; }
.blk h1 { font-size: clamp(2.2rem, 1.2rem + 5vw, 5.6rem); font-weight: 700; line-height: 0.95; letter-spacing: -0.045em; max-width: 10em; }
.dot { position: absolute; right: 22px; bottom: 22px; width: 40px; height: 40px; border-radius: 50%; background: #111; scale: calc(1 - var(--p, 0)); }
.view figure { position: absolute; left: clamp(18px, 6vw, 90px); bottom: calc(18% + var(--p, 0) * 82%); width: min(210px, 40vw); margin-bottom: -2px; opacity: calc(1 - var(--p, 0) * 2.2); }
.after { background: #FF3B1D; color: #fff; } .after .inr { display: grid; gap: 28px 56px; padding-block: 8px 8px; }
@media (min-width: 860px) { .after .inr { grid-template-columns: 1fr 1fr; } }
''', '''
<div class="fixedtop"><div class="wrap">{{TOP}}</div></div>
<main>
	<section class="pin" data-progress="pin"><div class="view">
		<p class="say">A selection of recent-ish notes by instructor Mostafa Saher. Currently teaching AI and cloud. Scroll.</p>
		<figure>{{IMG}}</figure>
		<div class="blk"><div class="wrap inr"><h1>{{H}}</h1><div style="max-width:460px">{{FORM}}</div></div><i class="dot"></i></div>
	</div></section>
	<section class="after"><div class="wrap inr"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}<footer class="foot">{{FOOT}}</footer></div></div></section>
</main>
''')

# 126 Card rail — after David McGillivray (Portfolio Project)
page(126, 'card-rail', 'family=Familjen+Grotesk:wght@400..700', '#FFFFFF', '''
:root { --line: rgb(0 0 0 / 0.16); --focus: #111; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #555; --f-radius: 12px; --b-radius: 8px; }
body { background: #fff; color: #111; font: 16px/1.5 "Familjen Grotesk", system-ui, sans-serif; }
::selection { background: #111; color: #fff; }
.head { padding-block: 8px 20px; }
h1 { font-size: clamp(1.5rem, 1.1rem + 1.6vw, 2.3rem); font-weight: 600; letter-spacing: -0.03em; line-height: 1.1; } h1 span { display: block; color: #9A9A9A; }
.rail { display: flex; gap: 14px; overflow-x: auto; padding: 4px max(18px, calc((100vw - 1160px) / 2 + 36px)) 26px; cursor: grab; scrollbar-width: none; user-select: none; } .rail::-webkit-scrollbar { display: none; } .rail.drag { cursor: grabbing; }
.cd { position: relative; flex: 0 0 min(78vw, 360px); aspect-ratio: 3 / 4.3; border-radius: 22px; background: var(--c); color: var(--t, #111); overflow: hidden; padding: 20px; display: grid; align-content: space-between; transition: scale 400ms var(--ease-out); }
.cd b { font-size: clamp(1.8rem, 1.3rem + 1.6vw, 2.6rem); font-weight: 700; letter-spacing: -0.04em; line-height: 0.98; } .cd small { font-size: 0.8rem; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; }
.cd img { position: absolute; left: 50%; bottom: 0; width: 104%; max-width: none; translate: -50% 0; pointer-events: none; }
.cd .tagr { display: inline-block; margin-top: 8px; padding: 3px 10px; border: 1.5px solid currentColor; border-radius: 999px; font-size: 0.8rem; }
.fx:not(.fx-rm) .rail:not(.in) .cd { translate: 60vw 0; } .fx .rail.in .cd { transition: translate 1000ms var(--ease-out) calc(var(--k) * 90ms), scale 400ms var(--ease-out); }
.hintx { padding-inline: max(18px, calc((100vw - 1160px) / 2 + 36px)); color: #9A9A9A; font-size: 0.9rem; }
''' + MORECSS, '''
<div class="wrap">{{TOP}}<div class="head"><h1>The Teaching Office of Mostafa Saher <span>AI and cloud, one clear step at a time</span></h1></div></div>
<main>
	<div class="rail" id="rail" data-inview>
		<div class="cd" style="--c:#E86A33;--t:#fff;--k:0"><small>The instructor</small>{{IMG}}</div>
		<div class="cd" style="--c:#ECECEC;--k:1"><small>01</small><div><b>Thoughts</b><p>Notes from the classroom: what students get stuck on.</p><span class="tagr">Notes</span></div></div>
		<div class="cd" style="--c:#E9E2B8;--k:2"><small>02</small><div><b>Opinions</b><p>Where I stand on new models, cloud services and the hype.</p><span class="tagr">Takes</span></div></div>
		<div class="cd" style="--c:#1B1B1F;--t:#fff;--k:3"><small>03</small><div><b>Resources</b><p>The labs, docs, courses and tools I actually use.</p><span class="tagr">Links</span></div></div>
		<div class="cd" style="--c:#3D63FF;--t:#fff;--k:4;--line:rgb(255 255 255 / 0.3);--note:#DCE3FF;--focus:#fff"><small>Newsletter</small><div><b style="display:block;margin-bottom:14px">Get it by email.</b>{{FORM}}</div></div>
		<div class="cd" style="--c:#C8F2D4;--k:5"><small>Elsewhere</small><div>{{LINKS_ROWS}}</div></div>
	</div>
	<p class="hintx">Drag sideways →</p>
</main>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''', '''
const rail = document.getElementById('rail'); let down = false, sx = 0, sl = 0, v = 0, lx = 0, moved = false;
rail.addEventListener('pointerdown', (e) => { if (e.pointerType !== 'mouse' || e.target.closest('input,button,a')) return; down = true; moved = false; sx = lx = e.clientX; sl = rail.scrollLeft; rail.classList.add('drag'); });
addEventListener('pointermove', (e) => { if (!down) return; rail.scrollLeft = sl - (e.clientX - sx); v = lx - e.clientX; lx = e.clientX; if (Math.abs(e.clientX - sx) > 5) moved = true; });
addEventListener('pointerup', () => { if (!down) return; down = false; rail.classList.remove('drag'); if (FX.RM) return; const glide = () => { if (down || Math.abs(v) < 0.4) return; rail.scrollLeft += v; v *= 0.94; requestAnimationFrame(glide); }; glide(); });
rail.addEventListener('click', (e) => { if (moved) e.preventDefault(); }, true);
''')

# 127 LED matrix — after Ramy Baiche's dot map (Portfolio Project)
page(127, 'led-matrix', 'family=Geist+Mono:wght@400;500&family=Geist:wght@400..600', '#0A0A0A', '''
:root { color-scheme: dark; --amber: #FFB000; --line: #262626; --focus: var(--amber); --f-bg: #151515; --f-text: #F2F2F2; --f-ph: #8E8E8E; --f-border: 1px solid #2E2E2E; --b-bg: var(--amber); --b-text: #0A0A0A; --note: #8E8E8E; --err: #FF9B8F; --f-radius: 6px; --b-radius: 3px; --f-pad: 4px; }
body { background: #0A0A0A; color: #F2F2F2; font: 15px/1.55 "Geist", system-ui, sans-serif; }
::selection { background: var(--amber); color: #0A0A0A; }
.sign { margin-top: 6px; padding: 14px; border-radius: 14px; background: #111; border: 1px solid #262626; box-shadow: inset 0 0 40px #000; }
.sign canvas { display: block; width: 100%; height: clamp(120px, 24vw, 230px); }
.cap { display: flex; justify-content: space-between; gap: 12px; margin-top: 10px; font: 400 0.72rem "Geist Mono", monospace; letter-spacing: 0.08em; text-transform: uppercase; color: #8E8E8E; } .cap b { color: var(--amber); font-weight: 500; }
.under { display: grid; gap: 28px 56px; align-items: end; padding-block: 36px 0; }
h1 { font-size: clamp(1.9rem, 1.2rem + 2.8vw, 3.4rem); font-weight: 600; line-height: 1.02; letter-spacing: -0.04em; margin-bottom: 14px; }
.under p { color: #B5B5B5; max-width: 32em; margin-bottom: 18px; }
.under figure { width: min(230px, 60%); filter: grayscale(1) contrast(1.1); }
@media (min-width: 880px) { .under { grid-template-columns: 230px 1fr 0.9fr; } .under figure { width: 100%; } }
''', '''
<div class="wrap">{{TOP}}
	<main>
		<div class="sign"><canvas id="led" role="img" aria-label="Scrolling sign: Mostafa Saher teaches AI and cloud, one clear step at a time"></canvas><div class="cap"><span>Platform 1 · Classroom</span><b class="fx-pulse">● Live</b></div></div>
		<section class="under"><figure data-reveal>{{IMG}}</figure><div data-reveal style="--i:1"><h1>{{H}}</h1><p>{{INTRO}}</p>{{FORM}}</div><div data-reveal style="--i:2">{{TOPICS_UL}}<div style="margin-top:20px">{{LINKS_INLINE}}</div></div></section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''', '''
const cv = document.getElementById('led'), ctx = cv.getContext('2d'), off = document.createElement('canvas'), octx = off.getContext('2d');
const msg = '  MOSTAFA SAHER  ●  AI + CLOUD  ●  ONE CLEAR STEP AT A TIME  ●  NEXT: YOUR INBOX  ●'; const ROWS = 15; let cols = 0, cell = 0, w = 0, h = 0, data = null, tw = 0, x = 0;
const build = () => { const dpr = Math.min(devicePixelRatio || 1, 2), r = cv.getBoundingClientRect(); w = r.width; h = r.height; cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); cell = h / ROWS; cols = Math.ceil(w / cell);
	octx.font = '700 ' + ROWS + 'px monospace'; tw = Math.ceil(octx.measureText(msg).width); off.width = tw; off.height = ROWS; octx.font = '700 ' + ROWS + 'px monospace'; octx.textBaseline = 'middle'; octx.fillStyle = '#fff'; octx.fillText(msg, 0, ROWS / 2 + 1); data = octx.getImageData(0, 0, tw, ROWS).data; };
const draw = () => { ctx.clearRect(0, 0, w, h); const ox = Math.floor(x); for (let c = 0; c < cols; c++) { const sx = (ox + c) % tw; for (let r = 0; r < ROWS; r++) { const on = data[(r * tw + sx) * 4 + 3] > 110; ctx.fillStyle = on ? '#FFB000' : '#1E1A12'; if (on) { ctx.shadowColor = '#FFB000'; ctx.shadowBlur = cell * 0.9; } else ctx.shadowBlur = 0; ctx.beginPath(); ctx.arc(c * cell + cell / 2, r * cell + cell / 2, cell * 0.36, 0, 6.3); ctx.fill(); } } };
build(); draw(); new ResizeObserver(() => { build(); draw(); }).observe(cv); if (FX.RM) return; FX.onTick(() => { x += 0.35; draw(); });
''')

# 128 Sunrise — after Dharmesh Nayak (Wall of Portfolios)
page(128, 'sunrise', 'family=Young+Serif&family=Geist:wght@400;500', '#120A0F', '''
:root { color-scheme: dark; --line: rgb(255 255 255 / 0.2); --focus: #FFD9C4; --f-bg: rgb(255 255 255 / 0.1); --f-text: #fff; --f-ph: #D9C7C0; --f-border: 1px solid rgb(255 255 255 / 0.25); --b-bg: #fff; --b-text: #2A0E12; --note: #D9C7C0; --err: #FFD2CB; --f-radius: 999px; --b-radius: 999px; }
@property --up { syntax: "<number>"; inherits: true; initial-value: 1; }
body { background: #120A0F; color: #fff; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #FF3D2E; color: #fff; }
.dawn { --up: 1; position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; text-align: center; background: linear-gradient(180deg, color-mix(in srgb, #2A0E1A calc(var(--up) * 100%), #0B0508), color-mix(in srgb, #7A1F1F calc(var(--up) * 100%), #120A0F) 70%, #120A0F); }
.fx:not(.fx-rm) .dawn { animation: rise 3200ms cubic-bezier(0.2, 0.7, 0.2, 1) both; } @keyframes rise { from { --up: 0; } to { --up: 1; } }
.sunx { position: absolute; left: 50%; top: calc(64% - var(--up) * 92%); width: min(88vmin, 720px); aspect-ratio: 1; margin-left: calc(min(88vmin, 720px) / -2); border-radius: 50%; background: radial-gradient(circle, #FF5A3C 0%, #FF2D2D 55%, #C4122B 100%); box-shadow: 0 0 120px 20px rgb(255 60 50 / 0.45); }
.dawn > .wrap { position: relative; z-index: 2; }
.mid { align-self: center; padding-block: 12px 30px; opacity: calc(var(--up) * 1.6 - 0.6); translate: 0 calc((1 - var(--up)) * 30px); }
h1 { font: 400 clamp(2.6rem, 1.3rem + 6vw, 6rem)/1.02 "Young Serif", serif; letter-spacing: -0.02em; }
.mid p.s { max-width: 32em; margin: 16px auto 0; color: #F0DDD5; }
.signup { max-width: 430px; margin: 22px auto 0; text-align: left; } .note { text-align: center; }
.mid figure { width: min(250px, 56%); margin: 26px auto 0; -webkit-mask-image: linear-gradient(#000 70%, transparent); mask-image: linear-gradient(#000 70%, transparent); }
''' + MORECSS, '''
<div class="dawn"><i class="sunx"></i>
	<div class="wrap">{{TOP}}</div>
	<main class="wrap mid"><h1>Hi there,<br>I am Mostafa</h1><p class="s">A technical instructor. I teach AI and cloud, one clear step at a time, and I write down what comes up after class.</p>{{FORM}}<figure>{{IMG}}</figure></main>
</div>''' + MORE)

# 129 Collage — after Sudarvel K (Wall of Portfolios)
page(129, 'collage', 'family=Zilla+Slab:ital,wght@0,600;1,600&family=Gochi+Hand&family=Geist:wght@400;500', '#6FB7EE', '''
:root { --line: #D7D2C2; --focus: #1B1B1B; --f-bg: #fff; --f-border: 2px solid #1B1B1B; --b-bg: #1B1B1B; --b-text: #fff; --note: #55524A; --f-radius: 0; --b-radius: 0; --f-pad: 3px; }
body { background: #F5F1E6; color: #1B1B1B; font: 15px/1.55 "Geist", system-ui, sans-serif; }
::selection { background: #FFE14D; }
.sky { position: relative; min-height: 100svh; overflow: hidden; background: linear-gradient(#4E9FE6, #A9D6F7 70%, #E8F4FC); }
.sky .wrap { position: relative; z-index: 5; } .top { color: #fff; }
.pc { position: absolute; left: var(--x); top: var(--y); rotate: var(--r, 0deg); z-index: var(--z, 2); }
.fx:not(.fx-rm) .sky:not(.in) .pc { scale: 0; rotate: calc(var(--r, 0deg) - 60deg); } .fx .sky.in .pc { transition: scale 700ms var(--spring) calc(var(--k) * 130ms), rotate 900ms var(--ease-out) calc(var(--k) * 130ms); }
.word { font: 600 clamp(2.6rem, 9vw, 7.4rem)/0.9 "Zilla Slab", serif; color: #fff; text-shadow: 3px 3px 0 #1B1B1B; } .word.it { font-style: italic; color: #FFE14D; }
.photo { width: clamp(200px, 30vw, 380px); } .photo img { filter: drop-shadow(8px 8px 0 #1B1B1B); }
.tape { padding: 4px 12px; background: #FFE14D; font: 400 1.25rem "Gochi Hand", cursive; box-shadow: 2px 2px 0 rgb(0 0 0 / 0.25); }
.tape.g { background: #B8F2B0; } .tape.p { background: #FFB3D1; }
.cloud { width: clamp(120px, 18vw, 240px); height: clamp(40px, 6vw, 78px); border-radius: 999px; background: #fff; } .cloud::before { content: ""; position: absolute; left: 22%; top: -60%; width: 46%; height: 150%; border-radius: 50%; background: #fff; }
.tv { width: clamp(150px, 20vw, 250px); padding: 12px 12px 26px; background: #D9D2BC; border: 3px solid #1B1B1B; border-radius: 14px; box-shadow: 6px 6px 0 #1B1B1B; } .tv div { aspect-ratio: 4 / 3; border: 3px solid #1B1B1B; border-radius: 10px; background: #1B3A2A; color: #8CFFB5; display: grid; place-items: center; text-align: center; font: 400 1.2rem/1.1 "Gochi Hand", cursive; padding: 6px; }
.note2 { width: min(86vw, 400px); padding: 18px; background: #fff; border: 3px solid #1B1B1B; box-shadow: 6px 6px 0 #1B1B1B; }
.note2 p { font-weight: 500; margin-bottom: 12px; }
@media (prefers-reduced-motion: no-preference) { .sky.in .cloud { animation: fx-float 7s ease-in-out infinite alternate; } }
@media (max-width: 760px) { .sky { min-height: 124svh; } .tv { display: none; } }
''' + MORECSS, '''
<div class="sky" data-inview><div class="wrap">{{TOP}}</div>
	<h1 class="sr">Teach. Explain. Tell stories. Mostafa Saher, AI and cloud instructor.</h1>
	<i class="pc cloud" style="--x:6%;--y:14%;--k:0;--z:1"></i><i class="pc cloud" style="--x:70%;--y:9%;--k:1;--z:1"></i>
	<span class="pc word" style="--x:6%;--y:20%;--r:-4deg;--k:1" aria-hidden="true">Teach.</span>
	<span class="pc word it" style="--x:34%;--y:30%;--r:3deg;--k:2;--z:4" aria-hidden="true">Explain.</span>
	<span class="pc word" style="--x:10%;--y:43%;--r:-2deg;--k:3" aria-hidden="true">Tell stories.</span>
	<figure class="pc photo" style="--x:56%;--y:22%;--r:4deg;--k:2;--z:3" data-par="-10">{{IMG}}</figure>
	<span class="pc tape" style="--x:60%;--y:17%;--r:-7deg;--k:4;--z:6">AI + cloud</span><span class="pc tape g" style="--x:8%;--y:58%;--r:5deg;--k:5;--z:6">one clear step at a time</span><span class="pc tape p" style="--x:80%;--y:60%;--r:8deg;--k:6;--z:6">after class</span>
	<div class="pc tv" style="--x:74%;--y:66%;--r:-5deg;--k:5;--z:4"><div>wait, so why does that work?</div></div>
	<div class="pc note2" style="--x:max(18px, 8%);--y:68%;--r:-1.5deg;--k:6;--z:7"><p>Mostafa Saher, technical instructor. Get my notes from after class:</p>{{FORM}}</div>
</div>''' + MORE)

# 130 Receipt — after Shabnam Raghavan (Wall of Portfolios)
page(130, 'receipt', 'family=Courier+Prime:wght@400;700&family=Archivo:wght@600..900', '#C8371F', '''
:root { --line: #1B1B1B; --focus: #1B1B1B; --f-bg: #fff; --f-border: 1.5px dashed #1B1B1B; --b-bg: #1B1B1B; --b-text: #fff; --note: #555; --f-radius: 0; --b-radius: 0; --f-pad: 3px; }
body { background: #C8371F; color: #FBF3E6; font: 600 16px/1.5 "Archivo", system-ui, sans-serif; }
::selection { background: #1B1B1B; color: #FBF3E6; }
''' + HERO2 + '''
.hero { align-items: start; padding-top: 12px; }
h1 { font-size: clamp(2.6rem, 1.3rem + 6vw, 6.2rem); font-weight: 900; line-height: 0.9; letter-spacing: -0.045em; text-transform: uppercase; }
.hero p.s { margin: 16px 0 0; max-width: 28em; font-weight: 500; color: #FFE1D6; }
.hero figure { width: min(220px, 52%); margin-top: 22px; filter: drop-shadow(6px 6px 0 #7A1D0E); }
.printer { justify-self: center; width: min(100%, 380px); }
.slot { position: relative; z-index: 2; height: 26px; border-radius: 10px; background: #1B1B1B; box-shadow: inset 0 -6px 0 #3A3A3A; }
.roll { overflow: hidden; margin: -10px 14px 0; }
.rc { color: #1B1B1B; background: #FBF7EC; padding: 26px 18px 34px; font: 400 14px/1.5 "Courier Prime", monospace; -webkit-mask: conic-gradient(from -45deg at bottom, #0000, #000 1deg 89deg, #0000 90deg) bottom / 16px 100%; mask: conic-gradient(from -45deg at bottom, #0000, #000 1deg 89deg, #0000 90deg) bottom / 16px 100%; }
.fx:not(.fx-rm) .printer:not(.in) .rc { translate: 0 -102%; } .fx .printer.in .rc { transition: translate 2600ms steps(26, end) 400ms; }
.rc h2 { text-align: center; font: 700 1.2rem "Courier Prime", monospace; letter-spacing: 0.1em; } .rc .c { text-align: center; }
.rc hr { border: 0; border-top: 1.5px dashed #1B1B1B; margin: 12px 0; }
.rc dl { display: grid; grid-template-columns: 1fr auto; gap: 4px 12px; margin: 0; } .rc dd { margin: 0; text-align: right; } .rc dt small { display: block; color: #555; font-size: 12px; }
.rc .tot { font-weight: 700; font-size: 1.15rem; }
.rc .signup { margin-top: 12px; font-family: system-ui, sans-serif; } .rc .btn { padding-inline: 12px; } .rc .btn svg { display: none; }
.bars { height: 44px; margin-top: 14px; background: repeating-linear-gradient(90deg, #1B1B1B 0 2px, transparent 2px 5px, #1B1B1B 5px 9px, transparent 9px 11px, #1B1B1B 11px 12px, transparent 12px 16px); }
.more { color: #FBF3E6; --line: rgb(255 255 255 / 0.35); }
''' + MORECSS.replace('1fr 1fr', '1fr'), '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div><h1 data-split data-fx="drop">Your order: AI and cloud, explained.</h1><p class="s" data-reveal style="--wait:500ms">Mostafa Saher, technical instructor. One clear step at a time. Your receipt is printing.</p><figure data-reveal style="--wait:700ms">{{IMG}}</figure></div>
		<div class="printer" data-inview><div class="slot"></div><div class="roll"><div class="rc">
			<h2>AFTER CLASS</h2><p class="c">Mostafa Saher · Classroom 01</p><hr>
			<dl><dt>1 × Thoughts<small>notes from the classroom</small></dt><dd>0.00</dd><dt>1 × Opinions<small>where I stand on the hype</small></dt><dd>0.00</dd><dt>1 × Resources<small>labs, docs, tools I use</small></dt><dd>0.00</dd></dl><hr>
			<dl class="tot"><dt>TOTAL</dt><dd>FREE</dd></dl><hr>
			<p class="c">Deliver to:</p>{{FORM}}
			<div class="bars" aria-hidden="true"></div><p class="c" style="margin-top:8px">THANK YOU · COME AGAIN</p>
		</div></div></div>
	</main>
	<section class="more"><div data-reveal>{{LINKS_ROWS}}</div></section>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')
print('d3 done')
