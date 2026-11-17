from lib2 import page
MORE = '<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>\n<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>'
MORECSS = '.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; } @media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }'

# 81 Cursor blob
page(81, 'cursor-blob', 'family=Host+Grotesk:wght@400..800', '#FFFFFF', '''
:root { --line: #111; --focus: #111; --f-bg: #F1F1F1; --b-bg: #111; --b-text: #fff; --note: #555; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #fff; color: #111; font: 16px/1.5 "Host Grotesk", system-ui, sans-serif; }
::selection { background: #111; color: #fff; }
h1 { margin-top: clamp(20px, 6vh, 64px); font-size: clamp(3rem, 1.2rem + 9.4vw, 10rem); font-weight: 800; line-height: 0.86; letter-spacing: -0.06em; }
.row2 { display: grid; gap: 20px 48px; align-items: end; padding-block: 32px 40px; }
.row2 p { max-width: 26em; font-size: 1.2rem; font-weight: 500; line-height: 1.25; } .field { gap: 0; }
.big li { border-top: 2px solid #111; } .big li:last-child { border-bottom: 2px solid #111; }
.big a { display: flex; justify-content: space-between; align-items: center; gap: 16px; padding-block: 0.12em; font-size: clamp(2.2rem, 1rem + 6vw, 6.4rem); font-weight: 800; letter-spacing: -0.05em; line-height: 1.05; transition: padding 400ms var(--ease-out); }
.big small { font-size: 0.9rem; font-weight: 500; letter-spacing: 0; }
.end { display: grid; gap: 28px 56px; align-items: end; padding-block: 44px 0; }
.end figure { width: min(240px, 60%); filter: grayscale(1) contrast(1.1); }
@media (hover: hover) and (pointer: fine) { .big a:hover { padding-left: 0.3em; } }
@media (min-width: 860px) { .row2 { grid-template-columns: 1fr 440px; } .end { grid-template-columns: 240px 1fr; } .end figure { width: 100%; } }
''', '''
<div class="wrap">{{TOP}}
	<main>
		<h1 data-split="chars" style="--stag:18ms">AI and cloud, made clear.</h1>
		<div class="row2"><p data-reveal style="--wait:500ms">Mostafa Saher, technical instructor. One clear step at a time. Move the cursor around.</p><div data-reveal style="--wait:650ms" data-big>{{FORM}}</div></div>
		<ul class="big">
			<li data-reveal><a data-mag="0.08" href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn<small>Mostafa Abuelnoor</small></a></li>
			<li data-reveal style="--i:1"><a data-mag="0.08" href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub<small>@MostafaAbuelnoor</small></a></li>
			<li data-reveal style="--i:2"><a data-mag="0.08" href="mailto:mostafasaher@gmail.com">Email<small>mostafasaher@gmail.com</small></a></li>
		</ul>
		<section class="end"><figure data-reveal>{{IMG}}</figure><div data-reveal style="--i:1">{{TOPICS_UL}}</div></section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''', "document.body.setAttribute('data-cursor', ''); if (FX.FINE && !FX.RM) { const c = document.createElement('div'); c.className = 'fx-cursor'; document.body.append(c); let x = FX.ptr.x, y = FX.ptr.y; addEventListener('pointermove', (e) => { c.classList.add('on'); c.classList.toggle('big', !!e.target.closest('a,button,[data-big]')); }, { passive: true }); FX.onTick(() => { x = FX.lerp(x, FX.ptr.x, 0.2); y = FX.lerp(y, FX.ptr.y, 0.2); c.style.transform = 'translate(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px)'; }); }")

# 82 Live clock
page(82, 'live-clock', 'family=Geist:wght@400..600&family=Geist+Mono:wght@400;500', '#F4F4F1', '''
:root { --red: #E5341D; --line: #1A1A1A; --focus: #1A1A1A; --f-bg: #fff; --b-bg: #1A1A1A; --b-text: #fff; --note: #5E5E5A; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #F4F4F1; color: #1A1A1A; font: 15px/1.5 "Geist", system-ui, sans-serif; }
::selection { background: var(--red); color: #fff; }
.mono { font-family: "Geist Mono", monospace; font-variant-numeric: tabular-nums; }
.grid { display: grid; grid-template-columns: 1fr; border-top: 1.5px solid #1A1A1A; margin-top: 4px; }
.cell { padding: 18px 0; border-bottom: 1.5px solid #1A1A1A; }
.k { display: block; font-size: 0.72rem; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 10px; }
.time { font-size: clamp(3.4rem, 1rem + 13vw, 12rem); font-weight: 500; line-height: 0.85; letter-spacing: -0.06em; }
.time i { font-style: normal; color: var(--red); }
.dial { position: relative; width: min(220px, 60%); aspect-ratio: 1; border: 1.5px solid #1A1A1A; border-radius: 50%; }
.dial b { position: absolute; left: 50%; bottom: 50%; width: 2px; margin-left: -1px; background: #1A1A1A; transform-origin: 50% 100%; rotate: calc(var(--a) * 1deg); }
.dial .h { height: 28%; } .dial .m { height: 40%; } .dial .s { height: 44%; width: 1px; background: var(--red); transition: rotate 300ms var(--spring); }
.dial::after { content: ""; position: absolute; left: 50%; top: 50%; width: 8px; height: 8px; margin: -4px; border-radius: 50%; background: var(--red); }
h1 { font-size: clamp(1.8rem, 1.2rem + 2.2vw, 2.8rem); font-weight: 600; line-height: 1.05; letter-spacing: -0.035em; max-width: 13em; }
.status { display: inline-flex; align-items: center; gap: 8px; font-weight: 500; } .status::before { content: ""; width: 9px; height: 9px; border-radius: 50%; background: var(--red); }
.pic { width: min(200px, 56%); filter: grayscale(1) contrast(1.08); } .field { gap: 0; }
@media (min-width: 860px) { .grid { grid-template-columns: repeat(4, 1fr); } .cell { padding: 20px 20px 20px 0; } .cell + .cell { padding-left: 20px; border-left: 1.5px solid #1A1A1A; } .s4 { grid-column: span 4; border-left: 0 !important; padding-left: 0 !important; } .s2 { grid-column: span 2; } .cell:nth-child(2), .cell:nth-child(6), .cell:nth-child(8) { border-left: 0; padding-left: 0; } }
''', '''
<div class="wrap">{{TOP}}
	<main class="grid">
		<div class="cell s4"><span class="k">Local time, live</span><p class="time mono" id="time" aria-live="off">00<i>:</i>00<i>:</i>00</p></div>
		<div class="cell"><span class="k">Dial</span><div class="dial" id="dial" aria-hidden="true"><b class="h" style="--a:0"></b><b class="m" style="--a:0"></b><b class="s" style="--a:0"></b></div></div>
		<div class="cell"><span class="k">Status</span><p class="status fx-pulse" id="status">Class in session</p><p class="mono" id="date" style="margin-top:10px"></p></div>
		<div class="cell s2"><span class="k">Instructor</span><h1 data-split>{{H}}</h1></div>
		<div class="cell"><span class="k">Portrait</span><figure class="pic" data-reveal>{{IMG}}</figure></div>
		<div class="cell s2"><span class="k">Newsletter</span><p style="margin-bottom:14px;max-width:32em">{{INTRO}}</p><div style="max-width:440px">{{FORM}}</div></div>
		<div class="cell"><span class="k">Elsewhere</span>{{LINKS_INLINE}}</div>
		<div class="cell s4"><span class="k">Contents</span>{{TOPICS_UL}}</div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''', '''
const t = document.getElementById('time'), d = document.getElementById('dial'), st = document.getElementById('status'), pad = (n) => String(n).padStart(2, '0');
const hs = d.children; let turns = 0, lastS = -1;
const tick = () => { const n = new Date(), h = n.getHours(), m = n.getMinutes(), s = n.getSeconds();
	t.innerHTML = pad(h) + '<i>:</i>' + pad(m) + '<i>:</i>' + pad(s);
	if (s < lastS) turns++; lastS = s;
	hs[0].style.setProperty('--a', (h % 12) * 30 + m / 2); hs[1].style.setProperty('--a', m * 6 + s / 10); hs[2].style.setProperty('--a', turns * 360 + s * 6);
	st.textContent = (h >= 8 && h < 17) ? 'Class in session' : 'After class: writing'; };
document.getElementById('date').textContent = new Date().toLocaleDateString(undefined, { weekday: 'long', day: 'numeric', month: 'long' });
tick(); setInterval(tick, 1000);
''')

# 83 Chat
page(83, 'chat', 'family=Figtree:wght@400..700', '#EEF1F5', '''
:root { --blue: #1D7CF2; --line: #DDE2EA; --focus: var(--blue); --f-bg: #fff; --f-border: 1px solid #D5DBE5; --b-bg: var(--blue); --b-text: #fff; --note: #6B7482; --f-radius: 999px; --b-radius: 999px; --w: 640px; }
body { background: #EEF1F5; color: #111827; font: 16px/1.45 "Figtree", system-ui, sans-serif; }
::selection { background: var(--blue); color: #fff; }
.head { position: sticky; top: 0; z-index: 3; display: flex; align-items: center; gap: 12px; padding-block: 14px; background: rgb(238 241 245 / 0.92); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }
.face { width: 46px; height: 46px; border-radius: 50%; background: #CFE0FF; }
.head small { display: block; color: #16A34A; font-weight: 600; }
.log { display: flex; flex-direction: column; gap: 8px; padding-block: 22px 12px; min-height: 60svh; }
.b { max-width: 82%; padding: 10px 15px; border-radius: 20px; font-size: 1.04rem; }
.them { align-self: flex-start; background: #fff; border-bottom-left-radius: 6px; } .me { align-self: flex-end; background: var(--blue); color: #fff; border-bottom-right-radius: 6px; }
.b.pic { padding: 6px; } .b.pic .ph { width: 190px; aspect-ratio: 1; border-radius: 15px; background: #CFE0FF; overflow: hidden; } .b.pic img { width: 124%; max-width: none; margin: 6% 0 0 -12%; }
.stamp { align-self: center; font-size: 0.78rem; color: #6B7482; margin-block: 6px; }
.fx:not(.fx-rm) .log > * { display: none; } .fx .log > .on { display: block; animation: msg 380ms var(--spring) backwards; }
@keyframes msg { from { opacity: 0; transform: translateY(14px) scale(0.92); } }
.typing { align-self: flex-start; display: none; gap: 5px; padding: 14px 16px; border-radius: 20px; background: #fff; } .typing.on { display: inline-flex !important; }
.typing i { width: 7px; height: 7px; border-radius: 50%; background: #9AA3B2; animation: dotb 1s ease-in-out infinite; } .typing i:nth-child(2) { animation-delay: 150ms; } .typing i:nth-child(3) { animation-delay: 300ms; }
@keyframes dotb { 30% { transform: translateY(-5px); opacity: 0.5; } }
.compose { position: sticky; bottom: 0; padding-block: 12px max(14px, env(safe-area-inset-bottom)); background: linear-gradient(transparent, #EEF1F5 30%); }
.links2 { padding-block: 8px 0; } .li-inline { justify-content: center; font-weight: 600; color: var(--blue); }
.foot { text-align: center; }
''', '''
<div class="wrap">
	<header class="head"><div class="face">{{IMG}}</div><div><b>Mostafa Saher</b><small>● online · AI and cloud instructor</small></div></header>
	<main>
		<h1 class="sr">Mostafa Saher teaches AI and cloud, one clear step at a time</h1>
		<div class="log" id="log">
			<p class="stamp">After class</p>
			<p class="b me">wait, so why does that work?</p>
			<p class="b them">Good question. That’s the best part of every class: the ones that come once it’s over.</p>
			<p class="b them">I’m Mostafa. I teach AI and cloud, one clear step at a time.</p>
			<div class="b them pic"><div class="ph">{{IMG}}</div></div>
			<p class="b me">can you send me that link?</p>
			<p class="b them">Better: I write it all down now. Thoughts from the classroom, where I stand on the hype, and the resources I’d hand a student.</p>
			<p class="b them">Leave your email below and I’ll send it. 👇</p>
		</div>
		<div class="typing" id="typing" aria-hidden="true"><i></i><i></i><i></i></div>
		<div class="compose">{{FORM}}</div>
		<div class="links2">{{LINKS_INLINE}}</div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''', '''
const items = FX.$$('#log > *'), typing = document.getElementById('typing'), log = document.getElementById('log'); if (FX.RM) return;
log.after(typing); let i = 0;
const next = () => { if (i >= items.length) { typing.classList.remove('on'); return; } const el = items[i++]; const them = el.classList.contains('them');
	const show = () => { typing.classList.remove('on'); el.classList.add('on'); setTimeout(next, el.classList.contains('stamp') ? 300 : 650); };
	if (them) { typing.classList.add('on'); setTimeout(show, 900); } else show(); };
setTimeout(next, 500);
''')

# 84 Chalkboard
page(84, 'chalkboard', 'family=Schoolbell&family=Hanken+Grotesk:wght@400..600', '#23473B', '''
:root { --chalk: #F4F1E6; --line: rgb(244 241 230 / 0.3); --focus: #FFE27A; --f-bg: rgb(244 241 230 / 0.1); --f-text: #F4F1E6; --f-ph: #B9CCC2; --f-border: 2px dashed rgb(244 241 230 / 0.55); --b-bg: #F4F1E6; --b-text: #1E3D33; --note: #B9CCC2; --err: #FFD2CB; --f-radius: 8px; --b-radius: 4px; --f-pad: 5px; }
body { background: #3A2A1C; color: var(--chalk); font: 16px/1.55 "Hanken Grotesk", system-ui, sans-serif; }
::selection { background: #FFE27A; color: #1E3D33; }
.frame { margin: clamp(10px, 2vw, 24px); border: clamp(10px, 1.6vw, 20px) solid #6B4A2C; border-radius: 10px; background: #23473B radial-gradient(120% 90% at 30% 20%, #2C5747, #1E3D33); box-shadow: inset 0 0 80px rgb(0 0 0 / 0.35), 0 20px 40px -20px #000; }
.chalk { font-family: "Schoolbell", "Gochi Hand", cursive; }
.board { display: grid; gap: 24px 48px; align-items: end; min-height: calc(100svh - 150px); padding-block: 8px 28px; }
h1 { font: 400 clamp(2.6rem, 1.2rem + 6.4vw, 6.6rem)/1 "Schoolbell", cursive; }
h1 span { display: block; width: fit-content; } h1 .y { color: #FFE27A; } h1 .p { color: #FFB3C7; }
.tip { margin-top: 18px; font: 400 1.5rem/1.2 "Schoolbell", cursive; color: #BFE3F2; rotate: -1.5deg; }
.board p.s { margin: 18px 0 20px; max-width: 30em; color: #D4E2DA; }
.signup { max-width: 440px; }
.pinup { justify-self: center; width: min(250px, 66%); padding: 10px 10px 4px; background: #FBF8EF; color: #23473B; rotate: 3deg; box-shadow: 0 14px 28px -14px #000; }
.pinup .ph { aspect-ratio: 1; background: #DDE8DC; overflow: hidden; } .pinup img { width: 124%; max-width: none; margin: 6% 0 0 -12%; } .pinup figcaption { text-align: center; font: 400 1.4rem/1.8 "Schoolbell", cursive; }
.tray { height: 14px; margin-inline: 8%; background: #6B4A2C; border-radius: 0 0 6px 6px; position: relative; } .tray::before, .tray::after { content: ""; position: absolute; top: -7px; height: 7px; border-radius: 2px; } .tray::before { left: 12%; width: 54px; background: #F4F1E6; } .tray::after { left: 26%; width: 34px; background: #FFE27A; }
@media (min-width: 900px) { .board { grid-template-columns: 1.3fr 0.7fr; } }
''' + MORECSS, '''
<div class="frame"><div class="wrap">{{TOP}}
	<main class="board">
		<div>
			<h1 aria-label="Today: AI and cloud, one clear step at a time"><span data-wipe="right">Today:</span><span class="y" data-wipe="right" style="--i:5">AI + cloud,</span><span data-wipe="right" style="--i:11">one clear step</span><span class="p" data-wipe="right" style="--i:17">at a time.</span></h1>
			<p class="tip" data-reveal style="--wait:2400ms">(homework: subscribe ↓)</p>
			<p class="s" data-reveal style="--wait:400ms">I’m Mostafa Saher, a technical instructor. My newsletter carries what comes up after class.</p>
			<div data-reveal style="--wait:550ms">{{FORM}}</div>
		</div>
		<figure class="pinup" data-reveal="scale" style="--wait:300ms"><div class="ph">{{IMG}}</div><figcaption>your instructor</figcaption></figure>
	</main>
	<div class="more" style="padding-top:8px">''' + '<div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></div><footer class="foot">{{FOOT}}</footer></div><div class="tray"></div></div>')

# 85 Slide deck
page(85, 'slide-deck', 'family=Albert+Sans:wght@400..800', '#111318', '''
:root { --line: rgb(0 0 0 / 0.18); --focus: #111318; --f-bg: #fff; --b-bg: #111318; --b-text: #fff; --note: #454a57; --f-radius: 12px; --b-radius: 8px; }
html { scroll-snap-type: y mandatory; }
body { background: #111318; color: #111318; font: 16px/1.5 "Albert Sans", system-ui, sans-serif; }
::selection { background: #111318; color: #fff; }
.sl { position: relative; min-height: 100svh; scroll-snap-align: start; display: grid; align-content: center; gap: 22px; padding: 76px clamp(20px, 8vw, 130px) 90px; overflow: hidden; }
.sl h1, .sl h2 { font-size: clamp(2.3rem, 1.2rem + 5.4vw, 6rem); font-weight: 800; line-height: 0.95; letter-spacing: -0.045em; max-width: 11em; }
.sl p { max-width: 30em; font-size: 1.25rem; line-height: 1.35; }
.sl .n { position: absolute; left: clamp(20px, 8vw, 130px); top: 26px; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.08em; text-transform: uppercase; }
.s1 { background: #F5F2EA; } .s2 { background: #FFD84D; } .s3 { background: #8ED1FC; } .s4 { background: #B8F2C8; } .s5 { background: #fff; }
.s2 figure { position: absolute; right: 5%; bottom: 0; height: 80%; aspect-ratio: 1100 / 1433; } .s2 img { height: 100%; width: auto; max-width: none; } .s2 h2 { max-width: 6em; position: relative; z-index: 1; } .s2 p { max-width: 14em; position: relative; z-index: 1; }
.bul li { font-size: clamp(1.2rem, 1rem + 1.2vw, 1.9rem); font-weight: 600; letter-spacing: -0.02em; padding-block: 8px; border-top: 2px solid #111318; max-width: 24em; }
.hud { position: fixed; z-index: 5; right: clamp(16px, 4vw, 40px); bottom: max(18px, env(safe-area-inset-bottom)); display: flex; align-items: center; gap: 12px; padding: 8px 14px; border-radius: 999px; background: #111318; color: #fff; font-weight: 700; font-variant-numeric: tabular-nums; }
.hud span { width: 90px; height: 3px; background: rgb(255 255 255 / 0.25); } .hud i { display: block; height: 100%; background: #fff; transform-origin: 0 50%; transform: scaleX(calc(0.2 + var(--sy, 0) * 0.8)); }
.s5 .signup { max-width: 460px; }
@media (max-width: 700px) { .s2 { align-content: start; padding-top: 96px; } .s2 figure { height: 58%; right: -4%; } }
''', '''
<main>
	<section class="sl s1"><span class="n">Mostafa Saher · Lesson 1</span><h1 data-split>{{H}}</h1><p data-reveal style="--wait:500ms">Scroll to go to the next slide.</p></section>
	<section class="sl s2"><span class="n">Slide 2 · Your instructor</span><h2 data-split>Technical instructor.</h2><p data-reveal style="--i:2">I teach AI and cloud for a living.</p><figure data-reveal="right">{{IMG}}</figure></section>
	<section class="sl s3"><span class="n">Slide 3 · The problem</span><h2 data-split>The best part of class happens after it ends.</h2><p data-reveal style="--i:2">The questions in the corridor, the “wait, so why does that work?”, the links I send people afterwards.</p></section>
	<section class="sl s4"><span class="n">Slide 4 · The answer</span><h2 data-split>I write it down.</h2><ul class="bul"><li data-reveal style="--i:2">Thoughts from the classroom</li><li data-reveal style="--i:3">Opinions on new models and cloud services</li><li data-reveal style="--i:4">Resources I’d hand a student</li></ul></section>
	<section class="sl s5"><span class="n">Slide 5 · Homework</span><h2 data-split>Subscribe.</h2><div data-reveal style="--i:2">{{FORM}}</div>{{LINKS_INLINE}}<p style="font-size:0.85rem;opacity:0.65">{{FOOT}}</p></section>
</main>
<div class="hud" aria-hidden="true"><b id="cnt">1 / 5</b><span><i></i></span></div>
''', '''
document.documentElement.setAttribute('data-sy', ''); const cnt = document.getElementById('cnt');
const set = () => { const max = Math.max(1, document.documentElement.scrollHeight - innerHeight); document.documentElement.style.setProperty('--sy', (scrollY / max).toFixed(4)); cnt.textContent = (Math.round(scrollY / innerHeight) + 1) + ' / 5'; };
addEventListener('scroll', set, { passive: true }); set();
''')

# 86 Notebook
page(86, 'notebook', 'family=Gochi+Hand&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600', '#FDFBF3', '''
:root { --line: #C9D7EE; --focus: #2A3A5E; --f-bg: #fff; --f-border: 1.5px solid #2A3A5E; --b-bg: #2A3A5E; --b-text: #fff; --note: #5E6B86; --f-radius: 8px; --b-radius: 4px; --w: 900px; }
body { background: #E9E4D6; color: #1F2A44; font: 18px/36px "Source Serif 4", Georgia, serif; }
::selection { background: #FFE66D; }
.paper { position: relative; margin: clamp(10px, 3vw, 36px) auto; max-width: 980px; background: #FDFBF3 repeating-linear-gradient(transparent 0 35px, #C9D7EE 35px 36px); box-shadow: 0 20px 50px -24px rgb(0 0 0 / 0.5); padding: 36px clamp(18px, 4vw, 48px) 36px clamp(54px, 9vw, 110px); }
.paper::before { content: ""; position: absolute; top: 0; bottom: 0; left: clamp(40px, 7vw, 84px); width: 2px; background: #F2A0A0; }
.holes { position: absolute; left: clamp(10px, 2vw, 26px); top: 0; bottom: 0; display: grid; align-content: space-around; } .holes i { width: 16px; height: 16px; border-radius: 50%; background: #E9E4D6; box-shadow: inset 0 2px 3px rgb(0 0 0 / 0.25); }
.top { padding-block: 0; height: 36px; font-family: "Gochi Hand", cursive; font-size: 1.3rem; }
h1 { margin-top: 36px; font-size: clamp(1.9rem, 1.2rem + 2.8vw, 3.1rem); font-weight: 600; line-height: 72px; letter-spacing: -0.02em; }
mark { background: linear-gradient(#FFE66D, #FFE66D) 0 60% / 100% 62% no-repeat; color: inherit; padding-inline: 2px; } mark.g { background-image: linear-gradient(#B6F2C9, #B6F2C9); } mark.p { background-image: linear-gradient(#FFC2DD, #FFC2DD); }
.fx:not(.fx-rm) mark { background-size: 0% 62%; transition: background-size 900ms var(--ease-io); transition-delay: calc(700ms + var(--i, 0) * 450ms); } .fx .in mark { background-size: 100% 62%; }
.pp { margin-top: 36px; max-width: 34em; }
.margin { position: absolute; left: 6px; width: clamp(44px, 7vw, 76px); font: 400 0.95rem/1.1 "Gochi Hand", cursive; color: #D2452D; text-align: center; rotate: -8deg; }
.rowp { position: relative; }
.join { margin-top: 36px; max-width: 460px; font-family: system-ui, sans-serif; line-height: 1.4; }
.join .note { line-height: 26px; margin-top: 10px; }
.clip { float: right; width: 170px; margin: 0 0 0 20px; padding: 8px 8px 0; background: #fff; box-shadow: 0 10px 22px -12px rgb(0 0 0 / 0.5); rotate: 4deg; shape-outside: margin-box; } .clip .ph { aspect-ratio: 1; overflow: hidden; background: #DDE6F5; } .clip img { width: 124%; max-width: none; margin: 6% 0 0 -12%; } .clip figcaption { font: 400 1.1rem/36px "Gochi Hand", cursive; text-align: center; }
.tp li { border: 0; padding-block: 0; } .tp b { display: inline; } .tp b::after { content: ": "; }
.li-inline { margin-top: 36px; } .li-inline a { text-decoration: underline; text-underline-offset: 4px; }
.foot { padding-block: 0; margin-top: 36px; line-height: 36px; }
@media (max-width: 600px) { .clip { float: none; margin: 36px auto 0; } .margin { display: none; } }
''', '''
<div class="paper"><div class="holes" aria-hidden="true"><i></i><i></i><i></i></div>
	{{TOP}}
	<main>
		<figure class="clip" data-reveal="scale" style="--wait:300ms"><div class="ph">{{IMG}}</div><figcaption>me</figcaption></figure>
		<h1 data-inview>I teach <mark>AI and cloud</mark>, <mark class="g" style="--i:1">one clear step</mark> at a time.</h1>
		<div class="rowp" data-inview><span class="margin">key idea!</span><p class="pp">The best part of every class comes once it’s over: <mark class="p">the questions in the corridor</mark>, the “wait, so why does that work?”, the links I send people afterwards. My newsletter is where that goes now.</p></div>
		<div class="join" data-reveal>{{FORM}}</div>
		<div style="margin-top:36px">{{TOPICS_UL}}</div>
		{{LINKS_INLINE}}
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 87 Staircase
page(87, 'staircase', 'family=Rethink+Sans:wght@400..800', '#0F1A2E', '''
:root { color-scheme: dark; --gold: #FFC857; --line: #25344F; --focus: var(--gold); --f-bg: #16243D; --f-text: #F3F6FB; --f-ph: #97A5BF; --f-border: 1px solid #2B3D5C; --b-bg: var(--gold); --b-text: #0F1A2E; --note: #97A5BF; --err: #FF9B8F; --f-radius: 10px; --b-radius: 6px; }
body { background: #0F1A2E; color: #F3F6FB; font: 16px/1.5 "Rethink Sans", system-ui, sans-serif; }
::selection { background: var(--gold); color: #0F1A2E; }
h1 { margin-top: clamp(12px, 4vh, 40px); font-size: clamp(2.2rem, 1.2rem + 4vw, 4.6rem); font-weight: 800; line-height: 0.98; letter-spacing: -0.045em; max-width: 12em; }
.stairs { display: grid; grid-template-columns: 1fr; gap: 10px; margin-top: 32px; align-items: end; }
.step { position: relative; padding: 18px; border-radius: 14px 14px 0 0; background: #16243D; border-top: 4px solid #2B3D5C; min-height: var(--h); display: grid; align-content: start; gap: 6px; }
.step b { font-size: 1.3rem; letter-spacing: -0.02em; } .step span { color: #A9B6CE; font-size: 0.95rem; } .step small { font-weight: 700; color: var(--gold); letter-spacing: 0.08em; }
.fx:not(.fx-rm) .step { transition: transform 800ms var(--ease-out), opacity 800ms ease, border-color 600ms ease 400ms; transition-delay: calc(500ms + var(--k) * 260ms); } .fx:not(.fx-rm) .stairs:not(.in) .step { transform: translateY(60px); opacity: 0; }
.stairs.in .step, html:not(.fx) .step { border-top-color: var(--gold); }
.step.last { background: var(--gold); color: #0F1A2E; --note: #5A4310; --f-bg: #fff; --f-text: #0F1A2E; --f-ph: #6B6B6B; --f-border: 0; --b-bg: #0F1A2E; --b-text: #fff; --focus: #0F1A2E; } .step.last small, .step.last span { color: #5A4310; }
.step figure { position: absolute; right: 8px; bottom: 100%; width: 120px; margin-bottom: -4px; }
.floor { height: 6px; background: #2B3D5C; }
@media (min-width: 900px) { .stairs { grid-template-columns: repeat(3, 1fr) 1.5fr; margin-top: 150px; } .step { --h: calc(120px + var(--k) * 90px); } .step figure { width: 170px; right: 20px; } }
@media (max-width: 899px) { .step figure { position: static; width: 130px; margin: 0 0 -18px auto; order: 3; } }
.more2 { padding-block: 36px 8px; }
''', '''
<div class="wrap">{{TOP}}
	<main>
		<h1 data-split>One clear step at a time.</h1>
		<div class="stairs" data-inview>
			<div class="step" style="--k:0"><small>STEP 1</small><b>Thoughts</b><span>Notes from the classroom: what students get stuck on.</span></div>
			<div class="step" style="--k:1"><small>STEP 2</small><b>Opinions</b><span>Where I stand on new models, cloud services and the hype.</span></div>
			<div class="step" style="--k:2"><small>STEP 3</small><b>Resources</b><span>The labs, docs, courses and tools I actually use.</span></div>
			<div class="step last" style="--k:3"><figure>{{IMG}}</figure><small>STEP 4</small><b>Get it by email</b><span style="margin-bottom:10px">I’m Mostafa Saher. I teach AI and cloud.</span>{{FORM}}</div>
		</div>
		<div class="floor"></div>
		<section class="more2" data-reveal>{{LINKS_ROWS}}</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 88 Boot loader
page(88, 'loader', 'family=Inter+Tight:wght@400..800', '#F3F2EE', '''
:root { --line: #D7D5CC; --focus: #111; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 999px; --b-radius: 999px; }
body { background: #F3F2EE; color: #111; font: 16px/1.5 "Inter Tight", system-ui, sans-serif; }
::selection { background: #111; color: #F3F2EE; }
.load { position: fixed; inset: 0; z-index: 30; background: #111; color: #F3F2EE; display: grid; align-content: end; padding: clamp(18px, 4vw, 40px); transition: clip-path 900ms var(--ease-io); clip-path: inset(0); }
.load.done { clip-path: inset(0 0 100% 0); }
.load b { font-size: clamp(5rem, 26vw, 22rem); font-weight: 800; line-height: 0.8; letter-spacing: -0.06em; font-variant-numeric: tabular-nums; }
.load span { display: block; height: 3px; margin-top: 18px; background: rgb(255 255 255 / 0.2); } .load i { display: block; height: 100%; background: #F3F2EE; transform-origin: 0 50%; transform: scaleX(var(--v, 0)); }
.load small { display: block; margin-bottom: 8px; letter-spacing: 0.08em; text-transform: uppercase; }
html:not(.fx) .load, .fx-rm .load { display: none; }
.hero { display: grid; gap: 20px 48px; align-items: end; min-height: calc(100svh - 70px); }
.copy { align-self: center; padding-block: 12px 36px; }
h1 { font-size: clamp(2.6rem, 1.2rem + 6vw, 6.4rem); font-weight: 800; line-height: 0.92; letter-spacing: -0.05em; max-width: 9em; --wait: 1500ms; }
.copy p { margin: 18px 0 22px; max-width: 30em; font-size: 1.1rem; }
.signup { max-width: 440px; }
.shot { justify-self: center; width: min(320px, 74%); }
@media (min-width: 900px) { .hero { grid-template-columns: 1.15fr 0.85fr; } .shot { width: min(100%, 460px); justify-self: end; } }
''' + MORECSS, '''
<div class="load" id="load" aria-hidden="true"><small>Loading class</small><b id="num">0</b><span><i></i></span></div>
<div class="wrap">{{TOP}}
	<main class="hero">
		<div class="copy"><h1 data-split="chars" style="--stag:20ms">Ready when you are.</h1><p data-reveal style="--wait:2000ms">I’m Mostafa Saher. I teach AI and cloud, one clear step at a time, and I write down what comes up after class.</p><div data-reveal style="--wait:2150ms">{{FORM}}</div></div>
		<div class="shot" data-wipe style="--wait:1500ms">{{IMG}}</div>
	</main>
</div>''' + MORE, '''
const load = document.getElementById('load'), num = document.getElementById('num'); if (FX.RM) return;
const t0 = performance.now(), dur = 1250; const run = (t) => { const k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3); num.textContent = Math.round(e * 100); load.style.setProperty('--v', e); if (k < 1) requestAnimationFrame(run); else load.classList.add('done'); };
requestAnimationFrame(run);
''')

# 89 Day and night
page(89, 'day-night', 'family=Sora:wght@300..700', '#F6F2E7', '''
:root { --bg: #F6F2E7; --fg: #1B1A17; --soft: #6E6A5E; --acc: #F28C28; --panel: #fff; --line: #DCD6C6; --focus: var(--fg); --f-bg: var(--panel); --f-text: var(--fg); --f-ph: var(--soft); --f-border: 1px solid var(--line); --b-bg: var(--fg); --b-text: var(--bg); --note: var(--soft); --f-radius: 999px; --b-radius: 999px; }
:root.night { --bg: #0B1026; --fg: #EEF1FF; --soft: #9AA4CF; --acc: #8FB0FF; --panel: #151C3D; --line: #253064; --err: #FF9B8F; color-scheme: dark; }
body { background: var(--bg); color: var(--fg); font: 16px/1.55 "Sora", system-ui, sans-serif; }
::selection { background: var(--acc); color: var(--bg); }
.tog { position: relative; width: 64px; height: 34px; border: 0; border-radius: 999px; background: var(--fg); cursor: pointer; }
.tog i { position: absolute; left: 4px; top: 4px; width: 26px; height: 26px; border-radius: 50%; background: var(--acc); transition: translate 400ms var(--spring); } .night .tog i { translate: 30px 0; box-shadow: inset -7px -2px 0 0 var(--fg); }
.hero { display: grid; gap: 20px 48px; align-items: end; min-height: calc(100svh - 70px); }
.copy { align-self: center; padding-block: 12px 36px; }
h1 { font-size: clamp(2.3rem, 1.2rem + 4.4vw, 5rem); font-weight: 700; line-height: 0.98; letter-spacing: -0.045em; max-width: 10em; }
h1 em { font-style: normal; color: var(--acc); }
.copy p { margin: 18px 0 22px; max-width: 30em; color: var(--soft); }
.signup { max-width: 440px; }
.sky { position: relative; justify-self: center; width: min(330px, 76%); }
.sky::before { content: ""; position: absolute; left: 50%; top: 2%; width: 78%; aspect-ratio: 1; margin-left: -39%; border-radius: 50%; background: var(--acc); opacity: 0.9; transition: translate 900ms var(--ease-out); } .night .sky::before { translate: 18% -6%; }
.sky img { position: relative; }
::view-transition-old(root), ::view-transition-new(root) { animation: none; mix-blend-mode: normal; }
::view-transition-new(root) { animation: iris 900ms cubic-bezier(0.77, 0, 0.175, 1); }
@keyframes iris { from { clip-path: circle(0 at var(--ix, 90%) var(--iy, 5%)); } to { clip-path: circle(150vmax at var(--ix, 90%) var(--iy, 5%)); } }
@media (min-width: 900px) { .hero { grid-template-columns: 1.15fr 0.85fr; } .sky { width: min(100%, 460px); justify-self: end; } }
''' + MORECSS, '''
<div class="wrap">
	<header class="top"><b>Mostafa Saher</b><button class="tog" id="tog" type="button" aria-label="Switch between day and night" aria-pressed="false"><i></i></button></header>
	<main class="hero">
		<div class="copy"><h1 data-split>Class by day. <em>Notes by night.</em></h1><p data-reveal style="--wait:500ms">I’m Mostafa Saher. I teach AI and cloud, one clear step at a time, and I write down what comes up after class. Try the switch in the corner.</p><div data-reveal style="--wait:650ms">{{FORM}}</div></div>
		<div class="sky" data-reveal="scale" style="--wait:300ms">{{IMG}}</div>
	</main>
</div>''' + MORE, '''
const tog = document.getElementById('tog'), root = document.documentElement;
tog.addEventListener('click', (e) => { const r = tog.getBoundingClientRect(); root.style.setProperty('--ix', (r.left + r.width / 2) + 'px'); root.style.setProperty('--iy', (r.top + r.height / 2) + 'px');
	const flip = () => { const on = root.classList.toggle('night'); tog.setAttribute('aria-pressed', on); };
	if (document.startViewTransition && !FX.RM) document.startViewTransition(flip); else flip(); });
''')

# 90 Aurora
page(90, 'aurora', 'family=Gloock&family=Geist:wght@400;500', '#050B14', '''
:root { color-scheme: dark; --line: #1B2A3D; --focus: #9FF5D0; --f-bg: rgb(255 255 255 / 0.08); --f-text: #F2F7F5; --f-ph: #A3B8B8; --f-border: 1px solid rgb(255 255 255 / 0.2); --b-bg: #F2F7F5; --b-text: #050B14; --note: #A3B8B8; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #050B14; color: #F2F7F5; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #9FF5D0; color: #050B14; }
.north { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; text-align: center; }
.north canvas { position: absolute; inset: -10% -10% 20%; width: 120%; height: 90%; filter: blur(46px) saturate(1.4); opacity: 0.85; }
.north::after { content: ""; position: absolute; inset: 55% 0 0; background: linear-gradient(transparent, #050B14 70%); }
.north > .wrap { position: relative; z-index: 2; }
.mid { align-self: center; padding-block: 16px 0; }
h1 { max-width: 12em; margin-inline: auto; font: 400 clamp(2.4rem, 1.2rem + 5vw, 5.4rem)/1.02 "Gloock", serif; letter-spacing: -0.02em; --stag: 80ms; --dur: 1300ms; }
.mid p { max-width: 30em; margin: 18px auto 24px; color: #C9D8D6; }
.signup { max-width: 430px; margin-inline: auto; text-align: left; } .note { text-align: center; }
.mid figure { width: min(280px, 60%); margin: 26px auto 0; } .mid img { -webkit-mask-image: linear-gradient(#000 72%, transparent); mask-image: linear-gradient(#000 72%, transparent); filter: drop-shadow(0 0 1.5px rgb(190 255 230 / 0.6)); }
''' + MORECSS, '''
<div class="north"><canvas data-canvas="aurora" data-colors="#19F0A0,#3B8BFF,#B45CFF"></canvas>
	<div class="wrap">{{TOP}}</div>
	<main class="wrap mid">
		<h1 data-split data-fx="blur">Clear skies over AI and cloud.</h1>
		<p data-reveal="fade" style="--wait:800ms">I’m Mostafa Saher. I teach one clear step at a time, and I write down what comes up after class.</p>
		<div data-reveal="fade" style="--wait:950ms">{{FORM}}</div>
		<figure data-reveal="scale" style="--wait:1100ms">{{IMG}}</figure>
	</main>
</div>''' + MORE)
print('c4 done')
