from lib2 import page
MORE = '<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>\n<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>'
MORECSS = '.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; } @media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }'

# 71 Colour mesh
page(71, 'colour-mesh', 'family=Manrope:wght@400..800', '#0E0B1F', '''
:root { color-scheme: dark; --line: rgb(255 255 255 / 0.18); --focus: #fff; --f-bg: rgb(255 255 255 / 0.12); --f-text: #fff; --f-ph: #D2CCEE; --f-border: 1px solid rgb(255 255 255 / 0.25); --b-bg: #fff; --b-text: #150F33; --note: #D2CCEE; --err: #FFD2CB; --f-radius: 14px; --b-radius: 10px; }
body { background: #0E0B1F; color: #fff; font: 16px/1.55 "Manrope", system-ui, sans-serif; }
::selection { background: #fff; color: #5B2BD9; }
.mesh { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; }
.orb { position: absolute; width: 56vmax; aspect-ratio: 1; border-radius: 50%; filter: blur(70px); opacity: 0.85; }
.o1 { background: #FF4D8D; left: -14vmax; top: -18vmax; } .o2 { background: #5B6CFF; right: -18vmax; top: 6vmax; } .o3 { background: #19D3C5; left: 18vmax; bottom: -32vmax; } .o4 { background: #FFB347; right: 4vmax; bottom: -30vmax; width: 40vmax; }
@media (prefers-reduced-motion: no-preference) { .orb { animation: roam 18s ease-in-out infinite alternate; } .o2 { animation-duration: 23s; animation-delay: -6s; } .o3 { animation-duration: 27s; animation-delay: -12s; } .o4 { animation-duration: 21s; animation-delay: -3s; } @keyframes roam { 0% { translate: 0 0; scale: 1; } 50% { translate: 12vmax 8vmax; scale: 1.2; } 100% { translate: -8vmax 14vmax; scale: 0.9; } } }
.mesh > .wrap { position: relative; z-index: 2; }
.center { display: grid; place-items: center; padding-block: 20px 48px; }
.glass { width: min(100%, 720px); padding: clamp(22px, 4vw, 44px); border-radius: 32px; background: rgb(20 14 46 / 0.42); border: 1px solid rgb(255 255 255 / 0.22); backdrop-filter: blur(22px) saturate(1.3); -webkit-backdrop-filter: blur(22px) saturate(1.3); box-shadow: 0 40px 80px -40px #000; }
.who { display: flex; align-items: center; gap: 14px; margin-bottom: 20px; font-weight: 600; }
.face { width: 60px; height: 60px; border-radius: 18px; background: rgb(255 255 255 / 0.25); }
h1 { font-size: clamp(2rem, 1.2rem + 3.4vw, 3.8rem); font-weight: 800; line-height: 1; letter-spacing: -0.045em; }
.glass p.s { margin: 16px 0 22px; color: #E3DEF7; max-width: 32em; }
''' + MORECSS, '''
<div class="mesh"><i class="orb o1"></i><i class="orb o2"></i><i class="orb o3"></i><i class="orb o4"></i>
	<div class="wrap">{{TOP}}</div>
	<main class="wrap center"><div class="glass" data-reveal="scale"><div class="who"><div class="face">{{IMG}}</div><span>Mostafa Saher · Technical instructor</span></div><h1 data-split data-fx="blur" style="--wait:300ms">{{H}}</h1><p class="s">My newsletter carries what comes up after class.</p>{{FORM}}</div></main>
</div>''' + MORE)

# 72 Marquee name
page(72, 'marquee-name', 'family=Archivo:wght@400..900', '#F4D03F', '''
:root { --line: rgb(0 0 0 / 0.2); --focus: #141414; --f-bg: #fff; --b-bg: #141414; --b-text: #fff; --note: #DDE6FF; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #EFEDE6; color: #141414; font: 16px/1.5 "Archivo", system-ui, sans-serif; }
::selection { background: #141414; color: #fff; }
.show { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; overflow: hidden; background: #2E6BFF; color: #fff; }
.rows { position: absolute; inset: 12% 0 auto; display: grid; gap: 0; }
.rows p { font-size: clamp(5rem, 24vw, 22rem); font-weight: 900; line-height: 0.82; letter-spacing: -0.06em; text-transform: uppercase; --dur: 30s; }
.rows p + p { --dir: reverse; -webkit-text-stroke: 2px #fff; color: transparent; --dur: 38s; }
.rows span span { padding-right: 0.25em; }
.show figure { position: absolute; left: 50%; bottom: 0; height: 80%; aspect-ratio: 1100 / 1433; margin-left: calc(80svh * 1100 / 1433 / -2); }
.show figure img { height: 100%; width: auto; max-width: none; filter: drop-shadow(0 30px 40px rgb(0 0 60 / 0.45)); }
.show > .wrap { position: relative; z-index: 3; }
.ask { max-width: 440px; padding-bottom: 24px; } .ask p { font-weight: 700; margin-bottom: 10px; font-size: 1.1rem; } .field { gap: 0; }
''' + MORECSS, '''
<div class="show"><div class="wrap">{{TOP}}</div><div></div>
	<div class="rows" aria-hidden="true"><p data-marquee><span>Mostafa Saher</span></p><p data-marquee><span>AI and cloud</span></p></div>
	<h1 class="sr">Mostafa Saher. AI and cloud, one clear step at a time.</h1>
	<figure data-reveal style="--wait:200ms">{{IMG}}</figure>
	<div class="wrap"><div class="ask" data-reveal style="--wait:600ms"><p>{{H}}</p>{{FORM}}</div></div>
</div>''' + MORE)

# 73 Scribble
page(73, 'scribble', 'family=Gochi+Hand&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600', '#FBF7EC', '''
:root { --pen: #E0452B; --line: #E4DCC6; --focus: var(--pen); --f-bg: #fff; --f-border: 1.5px solid #20201C; --b-bg: #20201C; --b-text: #FBF7EC; --note: #6E6956; --f-radius: 10px; --b-radius: 6px; --w: 980px; }
body { background: #FBF7EC; color: #20201C; font: 18px/1.55 "Source Serif 4", Georgia, serif; }
::selection { background: #FFE27A; }
.top b { font: 400 1.5rem "Gochi Hand", cursive; }
.hero { display: grid; gap: 24px 56px; align-items: center; padding-block: clamp(20px, 7vh, 72px) 48px; }
h1 { font-size: clamp(2.3rem, 1.3rem + 3.8vw, 4.4rem); font-weight: 600; line-height: 1.08; letter-spacing: -0.03em; }
.ul, .ci { position: relative; display: inline-block; }
.ul svg { position: absolute; left: -2%; bottom: -0.16em; width: 104%; height: 0.3em; overflow: visible; }
.ci svg { position: absolute; left: -9%; top: -12%; width: 118%; height: 124%; overflow: visible; }
svg path { fill: none; stroke: var(--pen); stroke-width: 3.5; stroke-linecap: round; vector-effect: non-scaling-stroke; }
.note2 { margin-top: 18px; font: 400 1.5rem/1.2 "Gochi Hand", cursive; color: var(--pen); rotate: -2deg; }
.hero p.s { margin: 20px 0 22px; max-width: 30em; }
.signup { max-width: 440px; font-family: system-ui, sans-serif; }
.pol { justify-self: center; width: min(280px, 70%); padding: 12px 12px 6px; background: #fff; box-shadow: 0 16px 34px -18px rgb(0 0 0 / 0.5); rotate: 3deg; }
.pol .ph { aspect-ratio: 1; background: #E9E0C8; overflow: hidden; } .pol img { width: 124%; max-width: none; margin: 6% 0 0 -12%; }
.pol figcaption { padding: 8px 0 6px; text-align: center; font: 400 1.4rem "Gochi Hand", cursive; }
@media (min-width: 880px) { .hero { grid-template-columns: 1.3fr 0.7fr; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div>
			<h1 data-reveal>I teach <span class="ci">AI<svg data-draw viewBox="0 0 100 60" preserveAspectRatio="none"><path pathLength="1" d="M52 4C24 2 4 14 5 31c1 17 24 26 50 24 24-2 42-12 40-28C93 12 70 3 44 6"/></svg></span> and <span class="ci">cloud<svg data-draw style="--i:1" viewBox="0 0 100 60" preserveAspectRatio="none"><path pathLength="1" d="M50 5C22 3 3 15 5 32c2 16 26 24 51 23 25-1 41-13 39-28C93 13 72 4 42 7"/></svg></span>, <span class="ul">one clear step<svg data-draw style="--i:2" viewBox="0 0 100 10" preserveAspectRatio="none"><path pathLength="1" d="M1 6c16-4 32-5 49-3 16 2 33 3 49-1M8 9c28-3 56-4 84-2"/></svg></span> at a time.</h1>
			<p class="note2" data-reveal style="--wait:1400ms">← this part matters</p>
			<p class="s" data-reveal style="--wait:300ms">I’m Mostafa Saher, a technical instructor. My newsletter is where the after-class questions go.</p>
			<div data-reveal style="--wait:450ms">{{FORM}}</div>
		</div>
		<figure class="pol" data-reveal="scale" style="--wait:200ms"><div class="ph">{{IMG}}</div><figcaption>me, after class</figcaption></figure>
	</main>
</div>''' + MORE)

# 74 Split flap
page(74, 'split-flap', 'family=Oswald:wght@500;600&family=Geist:wght@400;500', '#141414', '''
:root { color-scheme: dark; --amber: #FFC83D; --line: #2C2C2C; --focus: var(--amber); --f-bg: #1E1E1E; --f-text: #F2F2F2; --f-ph: #9A9A9A; --f-border: 1px solid #333; --b-bg: var(--amber); --b-text: #141414; --note: #9A9A9A; --err: #FF9B8F; --f-radius: 6px; --b-radius: 3px; --f-pad: 4px; }
body { background: #141414; color: #F2F2F2; font: 15px/1.55 "Geist", system-ui, sans-serif; }
::selection { background: var(--amber); color: #141414; }
.board { margin-top: clamp(16px, 5vh, 48px); padding: clamp(14px, 3vw, 28px); border-radius: 14px; background: #0B0B0B; border: 1px solid #2C2C2C; }
.rowx { display: grid; grid-template-columns: repeat(13, 1fr); gap: clamp(2px, 0.5vw, 6px); }
.rowx + .rowx { margin-top: clamp(4px, 0.8vw, 10px); }
.rowx i { position: relative; aspect-ratio: 5 / 7; display: grid; place-items: center; border-radius: 4px; background: #1F1F1F; color: #F2F2F2; font: 600 clamp(0.9rem, 4.2vw, 3.4rem)/1 "Oswald", sans-serif; font-style: normal; overflow: hidden; }
.rowx i::after { content: ""; position: absolute; left: 0; right: 0; top: 50%; height: 1px; background: #0B0B0B; }
.rowx i.hl { color: var(--amber); }
.rowx i.tick { animation: tick 90ms ease-in; } @keyframes tick { from { transform: rotateX(-70deg); } }
.lbl { display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.72rem; letter-spacing: 0.12em; text-transform: uppercase; color: #9A9A9A; }
.under { display: grid; gap: 28px 56px; align-items: end; padding-block: 36px 0; }
.under p { max-width: 30em; color: #BDBDBD; margin-bottom: 18px; }
.under figure { width: min(240px, 60%); filter: grayscale(1) contrast(1.1); }
@media (min-width: 880px) { .under { grid-template-columns: 240px 1fr 1fr; } .under figure { width: 100%; } }
''', '''
<div class="wrap">{{TOP}}
	<main>
		<h1 class="sr">Mostafa Saher teaches AI and cloud, one clear step at a time</h1>
		<div class="board" aria-hidden="true"><div class="lbl"><span>Departures</span><span>Classroom 01</span></div>
			<div class="rowx" data-flap="MOSTAFA SAHER" data-hl="1"></div><div class="rowx" data-flap=" TEACHES AI  "></div><div class="rowx" data-flap="  AND CLOUD  "></div><div class="rowx" data-flap="ONE CLEARSTEP" data-hl="1"></div>
		</div>
		<section class="under"><figure data-reveal>{{IMG}}</figure><div data-reveal style="--i:1"><p>{{INTRO}}</p>{{FORM}}</div><div data-reveal style="--i:2">{{TOPICS_UL}}<div style="margin-top:20px">{{LINKS_INLINE}}</div></div></section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''', '''
const pool = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ';
FX.$$('[data-flap]').forEach((row, r) => { const txt = row.dataset.flap.padEnd(13).slice(0, 13);
	Array.from(txt).forEach((ch, c) => { const cell = document.createElement('i'); if (row.dataset.hl) cell.className = 'hl'; row.append(cell);
		if (FX.RM) { cell.textContent = ch; return; }
		let n = 6 + r * 4 + c * 2; const t = setInterval(() => { n--; cell.textContent = n <= 0 ? ch : pool[Math.random() * pool.length | 0]; cell.classList.remove('tick'); void cell.offsetWidth; cell.classList.add('tick'); if (n <= 0) clearInterval(t); }, 70); }); });
''')

# 75 Weight wave
page(75, 'weight-wave', 'family=Bricolage+Grotesque:opsz,wght@12..96,200..800', '#111318', '''
:root { color-scheme: dark; --mint: #8CFFC9; --line: #272B35; --focus: var(--mint); --f-bg: #1A1D25; --f-text: #F3F5F8; --f-ph: #9299A8; --f-border: 1px solid #2C313D; --b-bg: var(--mint); --b-text: #0B1A13; --note: #9299A8; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #111318; color: #F3F5F8; font: 16px/1.55 "Bricolage Grotesque", system-ui, sans-serif; }
::selection { background: var(--mint); color: #0B1A13; }
.hero { min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; padding-bottom: 28px; }
h1 { align-self: center; font-size: clamp(3.6rem, 1rem + 16vw, 15rem); font-weight: 200; line-height: 0.84; letter-spacing: -0.05em; }
h1 .c { transition: none !important; }
@media (prefers-reduced-motion: no-preference) { h1 .c { animation: wv 2.6s ease-in-out infinite; animation-delay: calc(var(--n) * 110ms); } @keyframes wv { 0%, 100% { font-weight: 200; color: #F3F5F8; } 50% { font-weight: 800; color: var(--mint); } } }
.low { display: grid; gap: 18px 40px; align-items: end; }
.me { display: flex; gap: 14px; align-items: center; max-width: 30em; font-size: 1.1rem; }
.face { flex: none; width: 76px; height: 76px; border-radius: 50%; background: #272B35; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">
	<div class="hero">{{TOP}}
		<h1 data-split="chars" data-fx="fade">Mostafa<br>Saher</h1>
		<div class="low"><div class="me" data-reveal><div class="face">{{IMG}}</div><p>I teach AI and cloud, one clear step at a time. My newsletter carries what comes up after class.</p></div><div data-reveal style="--i:1">{{FORM}}</div></div>
	</div>
</div>''' + MORE)

# 76 Breathing type
page(76, 'breathing-type', 'family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800', '#FF5B2E', '''
:root { --line: rgb(0 0 0 / 0.25); --focus: #1A0A04; --f-bg: #fff; --b-bg: #1A0A04; --b-text: #fff; --note: #4A1B09; --err: #5A0A05; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #FF5B2E; color: #1A0A04; font: 16px/1.5 "Bricolage Grotesque", system-ui, sans-serif; }
::selection { background: #1A0A04; color: #FF5B2E; }
.hero { min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; overflow: hidden; padding-bottom: 24px; }
h1 { align-self: center; font-size: clamp(3rem, 1rem + 12.5vw, 12.5rem); font-weight: 800; line-height: 0.82; letter-spacing: -0.04em; text-transform: uppercase; }
h1 span { display: block; font-stretch: 100%; transform-origin: 0 50%; }
@media (prefers-reduced-motion: no-preference) { h1 span { animation: br 4.2s ease-in-out infinite alternate; } h1 span:nth-child(2) { animation-delay: -1.4s; } h1 span:nth-child(3) { animation-delay: -2.8s; } @keyframes br { from { font-stretch: 75%; font-weight: 300; } to { font-stretch: 100%; font-weight: 800; } } }
.low { position: relative; display: grid; gap: 16px 40px; align-items: end; }
.low p { max-width: 24em; font-size: 1.2rem; font-weight: 600; line-height: 1.2; } .field { gap: 0; }
.hero figure { position: absolute; right: 2%; bottom: 0; width: min(42%, 400px); pointer-events: none; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px 1fr; } }
@media (max-width: 859px) { .hero { grid-template-rows: auto auto auto auto; align-content: space-between; } .hero figure { position: relative; right: auto; width: 62%; margin: 8px auto -8px; } }
''' + MORECSS, '''
<div class="hero" style="position:relative"><div class="wrap">{{TOP}}</div>
	<h1 class="wrap" aria-label="AI and cloud made clear"><span>AI and</span><span>cloud,</span><span>made clear</span></h1>
	<figure data-reveal style="--wait:300ms">{{IMG}}</figure>
	<div class="wrap low"><p data-reveal>Mostafa Saher, technical instructor. One clear step at a time.</p><div data-reveal style="--i:1">{{FORM}}</div></div>
</div>''' + MORE)

# 77 Counter columns
page(77, 'counter-columns', 'family=Familjen+Grotesk:wght@400..700', '#EDEAE2', '''
:root { --line: #D3CEC0; --focus: #1B1A16; --f-bg: #fff; --b-bg: #1B1A16; --b-text: #fff; --note: #6C6859; --f-radius: 12px; --b-radius: 8px; }
body { background: #EDEAE2; color: #1B1A16; font: 16px/1.5 "Familjen Grotesk", system-ui, sans-serif; }
::selection { background: #1B1A16; color: #EDEAE2; }
.cols { display: grid; grid-template-columns: 1fr; gap: 14px; padding-block: 8px 40px; }
.colx { display: grid; gap: 14px; align-content: start; }
.t { border-radius: 22px; padding: clamp(20px, 3vw, 34px); min-height: 300px; display: grid; align-content: space-between; gap: 20px; overflow: hidden; position: relative; }
.t h1, .t h2 { font-size: clamp(2rem, 1.2rem + 3vw, 3.6rem); font-weight: 700; line-height: 0.95; letter-spacing: -0.04em; }
.t p { max-width: 26em; font-size: 1.08rem; }
.ta { background: #1B1A16; color: #EDEAE2; --line: #3A382F; } .tb { background: #FFB02E; } .tc { background: #fff; } .td { background: #3E63F5; color: #fff; --line: rgb(255 255 255 / 0.3); --note: #DDE4FF; --focus: #fff; } .te { background: #C9F2DC; } .tf { background: #F4C6D8; }
.tb figure { position: absolute; right: 0; bottom: 0; height: 92%; aspect-ratio: 1100 / 1433; } .tb img { height: 100%; width: auto; max-width: none; }
.tb { min-height: 420px; }
@media (min-width: 860px) { .cols { grid-template-columns: 1fr 1fr; padding-bottom: 14vh; } .colx.l { translate: 0 calc(var(--sy, 0) * -90px); } .colx.r { translate: 0 calc(110px - var(--sy, 0) * 190px); } .colx { will-change: translate; } }
''', '''
<div class="wrap">{{TOP}}
	<main class="cols">
		<div class="colx l">
			<section class="t ta"><h1 data-split>{{H}}</h1><p>Scroll and watch the two columns pass each other.</p></section>
			<section class="t tc"><h2>Thoughts</h2><p>Notes from the classroom: what students get stuck on, and the explanation that finally made it click.</p></section>
			<section class="t te"><h2>Resources</h2><p>The labs, docs, courses and tools I actually use, each with a line on why.</p></section>
		</div>
		<div class="colx r">
			<section class="t tb"><h2 style="max-width:5em;position:relative;z-index:1">Mostafa Saher</h2><p style="max-width:10em;position:relative;z-index:1">Technical instructor</p><figure>{{IMG}}</figure></section>
			<section class="t tf"><h2>Opinions</h2><p>Where I stand on new models, cloud services and the hype around them.</p></section>
			<section class="t td"><h2>Get it by email.</h2><div>{{FORM}}<div style="margin-top:20px">{{LINKS_INLINE}}</div></div></section>
		</div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 78 Scroll reading
page(78, 'scroll-reading', 'family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500', '#0F0F0E', '''
:root { color-scheme: dark; --line: #2A2A27; --focus: #F1EEE4; --f-bg: #1A1A18; --f-text: #F1EEE4; --f-ph: #99968B; --f-border: 1px solid #33332F; --b-bg: #F1EEE4; --b-text: #0F0F0E; --note: #99968B; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #0F0F0E; color: #F1EEE4; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #F1EEE4; color: #0F0F0E; }
.fixedtop { position: fixed; z-index: 5; left: 0; right: 0; top: 0; background: linear-gradient(#0F0F0E, transparent); }
.pin { height: 320vh; }
.view { position: sticky; top: 0; height: 100svh; display: grid; align-content: center; gap: 28px; }
.read { font: 400 clamp(1.9rem, 1.1rem + 3.6vw, 4.4rem)/1.08 "Instrument Serif", serif; letter-spacing: -0.02em; max-width: 17em; }
.read .w { transition: opacity 300ms ease, color 300ms ease; } .fx:not(.fx-rm) .read .w { opacity: 0.16; } .fx .read .w.lit { opacity: 1; }
.read em { color: #FFB36B; }
.meter { width: 120px; height: 2px; background: #2A2A27; } .meter i { display: block; height: 100%; background: #F1EEE4; transform-origin: 0 50%; transform: scaleX(var(--p, 0)); }
.end { display: grid; gap: 28px 56px; align-items: end; padding-block: 24px 8px; }
.end h2 { font: 400 clamp(2.2rem, 1.4rem + 3vw, 3.8rem)/1 "Instrument Serif", serif; margin-bottom: 18px; }
.end figure { width: min(240px, 60%); }
@media (min-width: 880px) { .end { grid-template-columns: 240px 1fr 1fr; } .end figure { width: 100%; } }
''', '''
<div class="fixedtop"><div class="wrap">{{TOP}}</div></div>
<main>
	<section class="pin" id="pin" data-progress="pin"><div class="view wrap">
		<h1 class="read" id="read" data-split data-fx="none">I teach <em>AI and cloud</em> for a living. The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?”, the links I send people afterwards. <em>My newsletter is where that goes now.</em></h1>
		<div class="meter"><i></i></div>
	</div></section>
	<section class="wrap end"><figure data-reveal>{{IMG}}</figure><div data-reveal style="--i:1"><h2>Keep reading by email.</h2>{{FORM}}</div><div data-reveal style="--i:2">{{TOPICS_UL}}<div style="margin-top:20px">{{LINKS_INLINE}}</div></div></section>
</main>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''', '''
const pin = document.getElementById('pin'), ws = FX.$$('#read .w'); if (FX.RM) { ws.forEach((w) => w.classList.add('lit')); return; }
let last = -1; FX.onTick(() => { const p = parseFloat(pin.style.getPropertyValue('--p')) || 0; const k = Math.round(FX.clamp(p * 1.15) * ws.length); if (k === last) return; last = k; ws.forEach((w, i) => w.classList.toggle('lit', i < Math.max(3, k))); });
''')

# 79 Polaroids
page(79, 'polaroids', 'family=Gochi+Hand&family=Hanken+Grotesk:wght@400..700', '#2B4C3F', '''
:root { --line: rgb(255 255 255 / 0.25); --focus: #FFE9A8; --f-bg: #fff; --b-bg: #FFE9A8; --b-text: #21382F; --note: #CFE0D8; --err: #FFD2CB; --f-radius: 10px; --b-radius: 6px; }
body { background: #2B4C3F; color: #F5F1E6; font: 16px/1.55 "Hanken Grotesk", system-ui, sans-serif; }
::selection { background: #FFE9A8; color: #21382F; }
.hero { display: grid; gap: 28px 56px; align-items: center; min-height: calc(100svh - 70px); padding-bottom: 36px; }
.fan { position: relative; justify-self: center; width: min(300px, 74vw); aspect-ratio: 4 / 5; margin-block: 30px; }
.pol { position: absolute; inset: 0; padding: 12px 12px 0; background: #FBF8EF; color: #21382F; box-shadow: 0 18px 36px -16px rgb(0 0 0 / 0.6); transition: transform 700ms var(--spring); transform: rotate(var(--r0)); }
.fan.in .pol, html:not(.fx) .pol, .fx-rm .pol { transform: translate(var(--x), var(--y)) rotate(var(--r)); }
.pol .ph { aspect-ratio: 1; overflow: hidden; background: var(--bg); } .pol img { width: 124%; max-width: none; margin: 6% 0 0 -12%; filter: var(--f, none); }
.pol p { text-align: center; font: 400 1.45rem/2.1 "Gochi Hand", cursive; }
.p1 { --r0: -2deg; --x: -34%; --y: 4%; --r: -11deg; --bg: #C9D6C9; --f: grayscale(1) contrast(1.05); } .p2 { --r0: 2deg; --x: 34%; --y: 6%; --r: 10deg; --bg: #F3C9A8; --f: sepia(0.5) saturate(1.2); transition-delay: 80ms; } .p3 { --r0: 0deg; --x: 0%; --y: -3%; --r: -2deg; --bg: #BFD4F2; transition-delay: 160ms; }
@media (hover: hover) and (pointer: fine) { .fan:hover .p1 { transform: translate(-48%, 2%) rotate(-16deg); } .fan:hover .p2 { transform: translate(48%, 4%) rotate(15deg); } .fan:hover .p3 { transform: translate(0, -9%) rotate(0deg); } }
h1 { font-size: clamp(2.2rem, 1.2rem + 3.6vw, 4.2rem); font-weight: 700; line-height: 1; letter-spacing: -0.04em; max-width: 11em; }
.hero p.s { margin: 16px 0 22px; max-width: 30em; color: #D5E2DB; }
.signup { max-width: 440px; }
@media (min-width: 900px) { .hero { grid-template-columns: 1fr 1fr; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div class="fan" data-inview><figure class="pol p1"><div class="ph">{{IMG}}</div><p>before class</p></figure><figure class="pol p2"><div class="ph">{{IMG}}</div><p>during</p></figure><figure class="pol p3"><div class="ph">{{IMG}}</div><p>after class ✓</p></figure></div>
		<div><h1 data-split>Snapshots from an AI and cloud classroom.</h1><p class="s" data-reveal style="--wait:500ms">I’m Mostafa Saher. I teach one clear step at a time, and I write down what comes up after class.</p><div data-reveal style="--wait:650ms">{{FORM}}</div></div>
	</main>
</div>''' + MORE)

# 80 Stickers
page(80, 'stickers', 'family=Gabarito:wght@400..900', '#F2F0E9', '''
:root { --line: #D9D5C8; --focus: #151515; --f-bg: #F2F0E9; --b-bg: #151515; --b-text: #fff; --note: #6A675C; --f-radius: 12px; --b-radius: 8px; }
body { background: #F2F0E9; color: #151515; font: 16px/1.5 "Gabarito", system-ui, sans-serif; }
::selection { background: #151515; color: #F2F0E9; }
.board { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; }
.mid { display: grid; place-items: center; padding: 20px; }
.cardx { position: relative; z-index: 1; width: min(100%, 470px); padding: 24px; border-radius: 26px; background: #fff; box-shadow: 0 30px 60px -30px rgb(0 0 0 / 0.4); text-align: center; }
.cardx h1 { font-size: clamp(1.7rem, 1.2rem + 1.8vw, 2.4rem); font-weight: 800; line-height: 1.02; letter-spacing: -0.035em; margin-bottom: 8px; }
.cardx p.s { color: #5C594F; margin-bottom: 16px; } .signup { text-align: left; } .note { text-align: center; }
.st { position: absolute; z-index: 2; left: var(--x); top: var(--y); padding: 10px 16px; border-radius: 999px; font-weight: 800; font-size: clamp(0.95rem, 0.8rem + 0.8vw, 1.5rem); letter-spacing: -0.02em; rotate: var(--r); cursor: grab; user-select: none; touch-action: none; box-shadow: 0 8px 18px -8px rgb(0 0 0 / 0.45); transition: scale 200ms var(--spring), box-shadow 200ms ease; white-space: nowrap; }
.st.drag { cursor: grabbing; scale: 1.08; box-shadow: 0 22px 36px -14px rgb(0 0 0 / 0.5); z-index: 9; }
.st a { text-decoration: underline; text-underline-offset: 3px; }
.s1 { background: #FF5A36; color: #fff; } .s2 { background: #2E6BFF; color: #fff; } .s3 { background: #FFD23F; } .s4 { background: #12B886; color: #fff; } .s5 { background: #151515; color: #fff; } .s6 { background: #F4A6C6; } .s7 { background: #fff; }
.st.photo { padding: 0; width: clamp(110px, 16vw, 190px); aspect-ratio: 1; border-radius: 50%; background: #CFE0FF; overflow: hidden; border: 5px solid #fff; } .st.photo img { width: 132%; max-width: none; margin: 6% 0 0 -16%; pointer-events: none; }
.hint { position: absolute; left: 0; right: 0; top: 64px; text-align: center; font-size: 0.9rem; color: #6A675C; }
''', '''
<div class="board" id="board"><div class="wrap">{{TOP}}</div>
	<main class="mid"><div class="cardx" data-reveal="scale"><h1>{{H}}</h1><p class="s">Mostafa Saher, technical instructor.</p>{{FORM}}</div></main>
	<div class="st photo" style="--x:8%;--y:14%;--r:-6deg">{{IMG}}</div>
	<span class="st s1" style="--x:66%;--y:12%;--r:7deg">AI</span><span class="st s2" style="--x:78%;--y:30%;--r:-8deg">Cloud</span><span class="st s3" style="--x:4%;--y:70%;--r:5deg">Thoughts</span><span class="st s4" style="--x:70%;--y:73%;--r:-4deg">Opinions</span><span class="st s6" style="--x:14%;--y:82%;--r:-9deg">Resources</span>
	<span class="st s5" style="--x:58%;--y:88%;--r:4deg"><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a></span><span class="st s7" style="--x:30%;--y:91%;--r:-3deg"><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a></span>
	<p class="hint">Drag the stickers around.</p>
</div>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''', '''
FX.$$('.st').forEach((el, i) => { let ox = 0, oy = 0, sx = 0, sy = 0, moved = false;
	if (!FX.RM) { el.animate([{ transform: 'translateY(-120vh) rotate(40deg)' }, { transform: 'none' }], { duration: 900 + i * 90, easing: 'cubic-bezier(0.34, 1.3, 0.64, 1)', fill: 'backwards', delay: 200 + i * 70 }); }
	el.addEventListener('pointerdown', (e) => { el.setPointerCapture(e.pointerId); sx = e.clientX - ox; sy = e.clientY - oy; moved = false; el.classList.add('drag'); });
	el.addEventListener('pointermove', (e) => { if (!el.hasPointerCapture(e.pointerId)) return; ox = e.clientX - sx; oy = e.clientY - sy; if (Math.abs(ox) + Math.abs(oy) > 4) moved = true; el.style.translate = ox + 'px ' + oy + 'px'; });
	const up = (e) => { el.classList.remove('drag'); };
	el.addEventListener('pointerup', up); el.addEventListener('pointercancel', up);
	el.addEventListener('click', (e) => { if (moved) e.preventDefault(); }, true); });
''')
print('c3 done')
