from lib2 import page
MORE = '<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>\n<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>'
MORECSS = '.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; } @media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }'
HERO2 = '.hero { display: grid; gap: 24px 48px; align-items: center; min-height: calc(100svh - 70px); padding-bottom: 36px; } @media (min-width: 900px) { .hero { grid-template-columns: 1.1fr 0.9fr; } }'

# 141 Weather
page(141, 'forecast', 'family=Manrope:wght@400..800', '#3B82F6', '''
:root { --line: rgb(255 255 255 / 0.3); --focus: #fff; --f-bg: rgb(255 255 255 / 0.18); --f-text: #fff; --f-ph: #E3EEFF; --f-border: 1px solid rgb(255 255 255 / 0.4); --b-bg: #fff; --b-text: #1E4FC2; --note: #E3EEFF; --err: #FFE0DA; --f-radius: 14px; --b-radius: 10px; }
body { background: #8DBCF7 linear-gradient(#2F6FE8, #6CA8F5 520px, #8DBCF7 1100px) no-repeat; color: #fff; font: 15px/1.5 "Manrope", system-ui, sans-serif; }
.app { max-width: 520px; margin-inline: auto; padding: 8px 16px 40px; text-align: center; }
.city { font-size: 1.6rem; font-weight: 600; margin-top: 18px; } .big { font-size: clamp(5rem, 22vw, 8rem); font-weight: 300; line-height: 1; letter-spacing: -0.04em; } .cond { font-size: 1.15rem; font-weight: 600; }
.face { width: 110px; height: 110px; margin: 14px auto 0; border-radius: 50%; background: rgb(255 255 255 / 0.25); }
.sunx { display: inline-block; width: 22px; height: 22px; vertical-align: -4px; margin-right: 6px; border-radius: 50%; background: #FFD166; box-shadow: 0 0 0 4px rgb(255 209 102 / 0.35); }
.card { margin-top: 14px; padding: 14px; border-radius: 20px; background: rgb(255 255 255 / 0.16); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); text-align: left; }
.card h2 { font-size: 0.75rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #E3EEFF; margin-bottom: 10px; padding-bottom: 8px; border-bottom: 1px solid var(--line); }
.hours { display: flex; justify-content: space-between; gap: 8px; text-align: center; } .hours div { display: grid; gap: 6px; font-size: 0.85rem; } .hours b { font-size: 1.1rem; }
.fx:not(.fx-rm) .hours:not(.in) div { opacity: 0; translate: 0 12px; } .fx .hours.in div { transition: opacity 500ms ease calc(var(--k) * 90ms), translate 500ms var(--ease-out) calc(var(--k) * 90ms); }
.days li { display: grid; grid-template-columns: 5.5em 1fr auto; align-items: center; gap: 10px; padding-block: 8px; border-top: 1px solid var(--line); font-weight: 600; } .days li:first-child { border-top: 0; }
.days li i { height: 5px; border-radius: 5px; background: linear-gradient(90deg, #8FD3FF, #FFD166); } .days small { font-weight: 400; color: #E3EEFF; }
.foot { text-align: center; }
''', '''
<main class="app">
	<p class="city" data-reveal>Mostafa Saher</p>
	<p class="big" data-reveal style="--i:1"><span id="deg">100</span>°</p>
	<p class="cond" data-reveal style="--i:2"><span class="sunx fx-pulse"></span>Clear, all day</p>
	<p data-reveal style="--i:2;color:#E3EEFF">Forecast for AI and cloud: one clear step at a time.</p>
	<div class="face" data-reveal="scale" style="--i:3">{{IMG}}</div>
	<h1 class="sr">Mostafa Saher teaches AI and cloud, one clear step at a time</h1>
	<section class="card" data-reveal><h2>Today in class</h2><div class="hours" data-inview><div style="--k:0">9am<b>AI</b>☀</div><div style="--k:1">11am<b>Cloud</b>☀</div><div style="--k:2">1pm<b>Lab</b>⛅</div><div style="--k:3">3pm<b>Q&amp;A</b>☀</div><div style="--k:4">After<b>Notes</b>✉</div></div></section>
	<section class="card" data-reveal><h2>This week’s newsletter</h2><ul class="days"><li>Thoughts<i></i><small>clear</small></li><li>Opinions<i></i><small>hype: low</small></li><li>Resources<i></i><small>tested</small></li></ul></section>
	<section class="card" data-reveal><h2>Get the forecast by email</h2>{{FORM}}</section>
	<section class="card" data-reveal><h2>Elsewhere</h2>{{LINKS_ROWS}}</section>
	<footer class="foot">{{FOOT}}</footer>
</main>
''', '''
const d = document.getElementById('deg'); if (FX.RM) return; let n = 0; const t = setInterval(() => { n += 4; d.textContent = Math.min(n, 100); if (n >= 100) clearInterval(t); }, 24); d.textContent = 0;
''')

# 142 Search box
page(142, 'search', 'family=Inter+Tight:wght@400..700', '#FFFFFF', '''
:root { --line: #E5E5E5; --focus: #1A73E8; --f-bg: #fff; --f-border: 1px solid #DADCE0; --b-bg: #1A73E8; --b-text: #fff; --note: #70757A; --f-radius: 999px; --b-radius: 999px; --w: 760px; }
body { background: #fff; color: #202124; font: 15px/1.5 "Inter Tight", system-ui, sans-serif; }
.home { min-height: calc(100svh - 70px); display: grid; align-content: center; justify-items: center; gap: 22px; text-align: center; padding-bottom: 60px; }
.logo { font-size: clamp(3rem, 10vw, 5.6rem); font-weight: 600; letter-spacing: -0.05em; line-height: 1; } .logo span:nth-child(1) { color: #4285F4; } .logo span:nth-child(2) { color: #EA4335; } .logo span:nth-child(3) { color: #FBBC05; } .logo span:nth-child(4) { color: #4285F4; } .logo span:nth-child(5) { color: #34A853; } .logo span:nth-child(6) { color: #EA4335; } .logo span:nth-child(7) { color: #4285F4; }
.box { display: flex; align-items: center; gap: 12px; width: min(100%, 600px); padding: 12px 18px; border: 1px solid #DADCE0; border-radius: 999px; box-shadow: 0 1px 6px rgb(32 33 36 / 0.18); text-align: left; font-size: 1.05rem; }
.box svg { flex: none; color: #9AA0A6; }
.res { width: min(100%, 600px); text-align: left; display: grid; gap: 22px; }
.r small { color: #4D5156; font-size: 0.85rem; } .r b { display: block; color: #1A0DAB; font-size: 1.25rem; font-weight: 500; margin-block: 2px; } .r p { color: #4D5156; }
.r.card { display: flex; gap: 14px; align-items: center; padding: 14px; border: 1px solid #DADCE0; border-radius: 14px; } .r.card .face { flex: none; width: 76px; height: 76px; border-radius: 12px; background: #E8F0FE; }
.fx:not(.fx-rm) .res:not(.show) .r { opacity: 0; translate: 0 10px; } .fx .res.show .r { transition: opacity 400ms ease calc(var(--k) * 120ms), translate 400ms var(--ease-out) calc(var(--k) * 120ms); }
.signup { width: 100%; }
''', '''
<div class="wrap">{{TOP}}
	<main class="home">
		<p class="logo" aria-hidden="true"><span>M</span><span>o</span><span>s</span><span>t</span><span>a</span><span>f</span><span>a</span></p>
		<h1 class="sr">Mostafa Saher teaches AI and cloud, one clear step at a time</h1>
		<div class="box" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg><span id="q"></span></div>
		<div class="res" id="res">
			<div class="r card" style="--k:0"><div class="face">{{IMG}}</div><div><b style="font-size:1.4rem;color:#202124">Mostafa Saher</b><p>Technical instructor · teaches AI and cloud, one clear step at a time</p></div></div>
			<div class="r" style="--k:1"><small>mostafasaher.com › newsletter</small><b>The newsletter: notes from after class</b><p>Thoughts from the classroom, where I stand on the hype, and the resources I’d hand a student.</p></div>
			<div class="r" style="--k:2">{{FORM}}</div>
			<div class="r" style="--k:3"><small>linkedin.com › in › mostafa-abuelnoor</small><b><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">Mostafa Abuelnoor · LinkedIn</a></b></div>
			<div class="r" style="--k:4"><small>github.com › MostafaAbuelnoor</small><b><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">MostafaAbuelnoor · GitHub</a></b></div>
		</div>
	</main>
	<footer class="foot" style="text-align:center">{{FOOT}}</footer>
</div>
''', '''
const q = document.getElementById('q'), res = document.getElementById('res'), txt = 'who explains AI and cloud clearly?';
if (FX.RM) { q.textContent = txt; res.classList.add('show'); return; } let i = 0; q.classList.add('fx-caret');
const t = setInterval(() => { q.textContent = txt.slice(0, ++i); if (i >= txt.length) { clearInterval(t); setTimeout(() => res.classList.add('show'), 350); } }, 55);
''')

# 143 Map pin
page(143, 'map-pin', 'family=Figtree:wght@400..800', '#E9EEE6', '''
:root { --line: #D3DACE; --focus: #E5341D; --f-bg: #fff; --b-bg: #E5341D; --b-text: #fff; --note: #66705F; --f-radius: 12px; --b-radius: 8px; }
body { background: #E9EEE6; color: #1F2A1B; font: 15px/1.5 "Figtree", system-ui, sans-serif; }
.map { position: relative; height: min(84svh, 760px); overflow: hidden; background: #E9EEE6; }
.map svg.roads { position: absolute; inset: -10%; width: 120%; height: 120%; }
.roads path { fill: none; stroke: #fff; stroke-linecap: round; } .roads .w { stroke: #F7D774; } .roads .r { stroke: #9CC6E8; }
.park { position: absolute; border-radius: 40% 60% 55% 45%; background: #C6E3B5; }
.pin { position: absolute; left: 56%; top: 46%; translate: -50% -100%; display: grid; justify-items: center; }
.pin .hd { width: 86px; height: 86px; border-radius: 50% 50% 50% 0; rotate: -45deg; background: #E5341D; display: grid; place-items: center; box-shadow: 0 10px 20px -8px rgb(0 0 0 / 0.5); }
.pin .face { width: 70px; height: 70px; rotate: 45deg; border-radius: 50%; background: #fff; }
.fx:not(.fx-rm) .pin { animation: drop 900ms cubic-bezier(0.3, 1.4, 0.5, 1) 300ms backwards; } @keyframes drop { from { translate: -50% -260%; opacity: 0; } }
.pin::after { content: ""; position: absolute; bottom: -10px; width: 30px; height: 10px; border-radius: 50%; background: rgb(0 0 0 / 0.2); }
.pulse { position: absolute; left: 56%; top: 46%; width: 20px; height: 20px; margin: -10px; border-radius: 50%; border: 2px solid #E5341D; }
@media (prefers-reduced-motion: no-preference) { .pulse { animation: ping 2s ease-out 1.2s infinite; } @keyframes ping { from { scale: 1; opacity: 1; } to { scale: 8; opacity: 0; } } }
.sheet { position: absolute; left: 50%; bottom: 16px; translate: -50% 0; width: min(94%, 520px); padding: 18px; border-radius: 22px; background: #fff; box-shadow: 0 20px 50px -20px rgb(0 0 0 / 0.45); }
.sheet h1 { font-size: 1.4rem; font-weight: 800; letter-spacing: -0.02em; line-height: 1.1; } .sheet .meta { color: #66705F; margin: 4px 0 12px; } .sheet .meta b { color: #1F8A3A; }
.lab { position: absolute; font-size: 0.75rem; font-weight: 600; color: #66705F; letter-spacing: 0.04em; text-transform: uppercase; }
''' + MORECSS, '''
<div class="wrap">{{TOP}}</div>
<main class="map">
	<svg class="roads" viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><path class="r" stroke-width="40" d="M-50 620 C300 560 500 700 1250 600"/><path stroke-width="14" d="M0 200 H1200 M0 420 H1200 M180 0 V800 M520 0 V800 M880 0 V800"/><path class="w" stroke-width="22" d="M-40 760 L640 300 L1260 120"/><path stroke-width="8" d="M0 300 H520 M880 520 H1200 M340 0 V420 M700 420 V800"/></svg>
	<i class="park" style="left:6%;top:10%;width:22%;height:24%"></i><i class="park" style="left:72%;top:58%;width:20%;height:22%"></i>
	<span class="lab" style="left:8%;top:40%">AI district</span><span class="lab" style="left:76%;top:30%">Cloud quarter</span><span class="lab" style="left:30%;top:72%">The corridor</span>
	<i class="pulse"></i><div class="pin"><div class="hd"><div class="face">{{IMG}}</div></div></div>
	<div class="sheet" data-reveal style="--wait:900ms"><h1>Mostafa Saher · Technical instructor</h1><p class="meta"><b>Open now</b> · AI and cloud, one clear step at a time</p>{{FORM}}</div>
</main>''' + MORE)

# 144 Bookshelf spines
spines = [('Thoughts','#E86A33',2.1),('Opinions','#2F5BFF',1.6),('Resources','#1FA971',2.4),('AI basics','#F2B84B',1.4),('Cloud 101','#7B5BFF',1.9),('After class','#111',2.6),('One step','#E0452B',1.3),('Labs','#9EE6C2',1.7)]
page(144, 'bookshelf', 'family=Oswald:wght@500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600', '#F2ECDF', '''
:root { --line: #DDD3BE; --focus: #2A2117; --f-bg: #fff; --b-bg: #2A2117; --b-text: #fff; --note: #6E6250; --f-radius: 6px; --b-radius: 3px; --f-pad: 4px; }
body { background: #F2ECDF; color: #2A2117; font: 17px/1.55 "Source Serif 4", Georgia, serif; }
h1 { margin-top: clamp(10px, 4vh, 40px); font-size: clamp(2.2rem, 1.2rem + 4vw, 4.4rem); font-weight: 600; line-height: 1; letter-spacing: -0.025em; max-width: 12em; }
.shelf { display: flex; align-items: flex-end; gap: 4px; margin-top: 28px; padding: 0 12px; height: clamp(220px, 36vw, 320px); border-bottom: 14px solid #7A5634; box-shadow: 0 10px 0 -2px #5B3E24; overflow-x: auto; overflow-y: hidden; scrollbar-width: none; }
.sp { flex: none; width: calc(var(--w) * 22px); height: var(--h); border-radius: 3px 3px 0 0; background: var(--c); color: #fff; display: grid; place-items: center; writing-mode: vertical-rl; rotate: 180deg; font: 600 clamp(0.85rem, 0.7rem + 0.6vw, 1.1rem) "Oswald", sans-serif; letter-spacing: 0.08em; text-transform: uppercase; transform-origin: 50% 50%; transition: translate 400ms var(--spring), rotate 400ms var(--spring); box-shadow: inset -4px 0 0 rgb(0 0 0 / 0.15); }
.sp.lean { rotate: 172deg; margin-left: 10px; }
.sp.book { writing-mode: horizontal-tb; rotate: 0deg; width: 150px; padding: 0; overflow: hidden; background: #DDE6F5; place-items: end center; } .sp.book img { width: 120%; max-width: none; }
.fx:not(.fx-rm) .shelf:not(.in) .sp { translate: 0 110%; } .fx .shelf.in .sp { transition: translate 700ms var(--spring) calc(var(--k) * 80ms); }
@media (hover: hover) and (pointer: fine) { .shelf.in .sp:not(.book):hover { translate: 0 -18px; transition-delay: 0ms; } }
.low { display: grid; gap: 20px 48px; align-items: end; padding-top: 36px; } .low p { max-width: 30em; }
.signup { font-family: system-ui, sans-serif; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main>
		<h1 data-split>A shelf of things worth knowing about AI and cloud.</h1>
		<div class="shelf" data-inview aria-hidden="true"><div class="sp book" style="--h:96%;--k:0">{{IMG}}</div>''' + ''.join(f'<div class="sp{" lean" if k==5 else ""}" style="--c:{c};--w:{w};--h:{62+((k*13)%34)}%;--k:{k+1}">{t}</div>' for k,(t,c,w) in enumerate(spines)) + '''</div>
		<div class="low"><p data-reveal>I’m Mostafa Saher, a technical instructor. Each issue of my newsletter is one more spine on the shelf: what comes up after class, explained one clear step at a time.</p><div data-reveal style="--i:1">{{FORM}}</div></div>
	</main>
</div>''' + MORE)

# 145 Highlight reel / scratch card
page(145, 'scratch-card', 'family=Gabarito:wght@400..900', '#1C1530', '''
:root { color-scheme: dark; --line: #2F2650; --focus: #FFD23F; --f-bg: #261D42; --f-text: #F5F2FF; --f-ph: #A49BC7; --f-border: 1px solid #3A2F60; --b-bg: #FFD23F; --b-text: #1C1530; --note: #A49BC7; --err: #FF9B8F; --f-radius: 12px; --b-radius: 8px; }
body { background: #1C1530; color: #F5F2FF; font: 16px/1.5 "Gabarito", system-ui, sans-serif; }
''' + HERO2 + '''
h1 { font-size: clamp(2.3rem, 1.2rem + 4.4vw, 5rem); font-weight: 900; line-height: 0.95; letter-spacing: -0.045em; } h1 em { font-style: normal; color: #FFD23F; }
.hero p.s { margin: 16px 0 22px; max-width: 30em; color: #C9C2E6; }
.signup { max-width: 440px; }
.tk { position: relative; justify-self: center; width: min(360px, 84vw); aspect-ratio: 4 / 5; border-radius: 22px; overflow: hidden; background: linear-gradient(160deg, #FF6FB5, #7B5BFF); box-shadow: 0 30px 60px -30px #000; touch-action: none; }
.tk .prize { position: absolute; inset: 0; display: grid; align-content: end; justify-items: center; text-align: center; }
.tk .prize b { position: absolute; top: 16px; left: 0; right: 0; font-size: 1.6rem; font-weight: 900; letter-spacing: -0.03em; color: #fff; }
.tk .prize img { width: 90%; }
.tk canvas { position: absolute; inset: 0; width: 100%; height: 100%; cursor: crosshair; }
.hint2 { text-align: center; margin-top: 10px; color: #A49BC7; font-size: 0.9rem; }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div><h1 data-split>Scratch to reveal <em>your instructor.</em></h1><p class="s" data-reveal style="--wait:500ms">Every ticket wins: AI and cloud, one clear step at a time. I’m Mostafa Saher, and I write down what comes up after class.</p><div data-reveal style="--wait:650ms">{{FORM}}</div></div>
		<div><div class="tk" data-reveal="scale"><div class="prize"><b>You won: Mostafa!</b>{{IMG}}</div><canvas id="sc" aria-label="Scratch card covering the portrait"></canvas></div><p class="hint2">Drag across the card to scratch it.</p></div>
	</main>
</div>''' + MORE, '''
const cv = document.getElementById('sc'), ctx = cv.getContext('2d'); let w, h, down = false, last = null;
const paint = () => { const r = cv.getBoundingClientRect(), dpr = Math.min(devicePixelRatio || 1, 2); w = r.width; h = r.height; cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
	const g = ctx.createLinearGradient(0, 0, w, h); g.addColorStop(0, '#C9C9D6'); g.addColorStop(0.5, '#F2F2F7'); g.addColorStop(1, '#A9A9BA'); ctx.globalCompositeOperation = 'source-over'; ctx.fillStyle = g; ctx.fillRect(0, 0, w, h);
	ctx.fillStyle = '#6B6B80'; ctx.font = '900 ' + Math.round(w / 9) + 'px Gabarito, sans-serif'; ctx.textAlign = 'center'; ctx.fillText('SCRATCH', w / 2, h / 2); ctx.font = '600 ' + Math.round(w / 22) + 'px Gabarito, sans-serif'; ctx.fillText('to reveal', w / 2, h / 2 + w / 12); };
const at = (e) => { const r = cv.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; };
const scratch = (p) => { ctx.globalCompositeOperation = 'destination-out'; ctx.lineWidth = 46; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(...(last || p)); ctx.lineTo(...p); ctx.stroke(); last = p; };
cv.addEventListener('pointerdown', (e) => { down = true; last = null; cv.setPointerCapture(e.pointerId); scratch(at(e)); }); cv.addEventListener('pointermove', (e) => { if (down) scratch(at(e)); }); ['pointerup', 'pointercancel'].forEach((n) => cv.addEventListener(n, () => { down = false; }));
paint(); if (FX.RM) { ctx.clearRect(0, 0, w, h); return; }
setTimeout(() => { let t = 0; const demo = () => { t += 0.05; scratch([w * (0.2 + 0.6 * (t % 1)), h * (0.3 + 0.12 * Math.floor(t))]); if (t < 3) requestAnimationFrame(demo); else last = null; }; demo(); }, 1200);
''')

# 146 Spotlight stage
page(146, 'stage-lights', 'family=Bodoni+Moda:opsz,wght@6..96,500;6..96,700&family=Geist:wght@400;500', '#0B0606', '''
:root { color-scheme: dark; --line: #2A1A1A; --focus: #FFD9A8; --f-bg: #1A1010; --f-text: #F8EFE6; --f-ph: #A99A8E; --f-border: 1px solid #3A2626; --b-bg: #C8102E; --b-text: #fff; --note: #A99A8E; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #0B0606; color: #F8EFE6; font: 15px/1.55 "Geist", system-ui, sans-serif; }
.theatre { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; text-align: center; }
.cur { position: absolute; top: 0; bottom: 0; width: 18%; background: repeating-linear-gradient(90deg, #6E0B17 0 18px, #8E1222 18px 30px, #5A0812 30px 40px); box-shadow: inset -20px 0 40px #000; z-index: 3; } .cur.l { left: 0; } .cur.r { right: 0; transform: scaleX(-1); }
.val { position: absolute; left: 0; right: 0; top: 0; height: 64px; z-index: 4; background: repeating-linear-gradient(90deg, #8E1222 0 40px, #6E0B17 40px 80px); border-radius: 0 0 50% 50% / 0 0 30px 30px; }
.beam { position: absolute; top: -10%; width: 40vw; height: 130%; background: linear-gradient(rgb(255 236 200 / 0.4), rgb(255 236 200 / 0)); clip-path: polygon(45% 0, 55% 0, 100% 100%, 0 100%); transform-origin: 50% 0; mix-blend-mode: screen; z-index: 1; }
.b1 { left: 10%; rotate: -14deg; } .b2 { right: 10%; rotate: 14deg; }
@media (prefers-reduced-motion: no-preference) { .b1 { animation: sweep 6s ease-in-out infinite alternate; } .b2 { animation: sweep 7s ease-in-out infinite alternate-reverse; } @keyframes sweep { from { rotate: -20deg; } to { rotate: 14deg; } } }
.theatre > .wrap { position: relative; z-index: 5; }
.mid { align-self: end; padding-bottom: 0; }
h1 { font: 700 clamp(2.4rem, 1.2rem + 5vw, 5.6rem)/0.95 "Bodoni Moda", serif; letter-spacing: -0.02em; }
.mid p.s { max-width: 30em; margin: 12px auto 18px; color: #D8C9BC; }
.signup { max-width: 430px; margin-inline: auto; text-align: left; } .note { text-align: center; }
.mid figure { width: min(280px, 56%); margin: 18px auto 0; filter: drop-shadow(0 0 30px rgb(255 220 170 / 0.35)); }
.floorx { height: 50px; background: linear-gradient(#3A1F12, #1A0E08); position: relative; z-index: 5; }
''' + MORECSS, '''
<div class="theatre"><i class="beam b1"></i><i class="beam b2"></i><i class="cur l"></i><i class="cur r"></i><i class="val"></i>
	<div class="wrap" style="padding-top:64px">{{TOP}}</div>
	<main class="wrap mid"><h1 data-split data-fx="blur">Now presenting: AI and cloud, made clear.</h1><p class="s" data-reveal style="--wait:700ms">Starring Mostafa Saher, technical instructor. One clear step at a time.</p><div data-reveal style="--wait:850ms">{{FORM}}</div><figure data-reveal style="--wait:400ms">{{IMG}}</figure></main>
</div><div class="floorx"></div>''' + MORE)

# 147 Bento grid with hover reveal
page(147, 'hover-grid', 'family=Familjen+Grotesk:wght@400..700', '#0F0F10', '''
:root { color-scheme: dark; --line: #2A2A2E; --focus: #9EE6C2; --f-bg: #1A1A1D; --f-text: #F2F2F2; --f-ph: #8E8E94; --f-border: 1px solid #2E2E33; --b-bg: #9EE6C2; --b-text: #0F0F10; --note: #8E8E94; --err: #FF9B8F; --f-radius: 12px; --b-radius: 8px; }
body { background: #0F0F10; color: #F2F2F2; font: 15px/1.5 "Familjen Grotesk", system-ui, sans-serif; }
.grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; padding-block: 6px 12px; }
.cell { position: relative; min-height: 180px; border-radius: 20px; background: #19191C; border: 1px solid #26262B; padding: 18px; overflow: hidden; display: grid; align-content: end; }
.cell::before { content: ""; position: absolute; inset: 0; background: radial-gradient(260px circle at var(--mx, -300px) var(--my, -300px), rgb(158 230 194 / 0.22), transparent 70%); pointer-events: none; }
.cell b { font-size: 1.3rem; letter-spacing: -0.02em; } .cell span { color: #A6A6AD; }
.cell.big { grid-column: span 2; min-height: 300px; } .cell.big h1 { font-size: clamp(1.9rem, 1.2rem + 3vw, 3.6rem); font-weight: 700; line-height: 1; letter-spacing: -0.04em; max-width: 11em; }
.cell.pic { padding: 0; place-items: end center; background: #22302A; } .cell.pic img { width: 92%; }
.cell.form { grid-column: span 2; }
.cell .reveal { position: absolute; inset: 0; padding: 18px; background: #9EE6C2; color: #0F0F10; display: grid; align-content: end; clip-path: circle(0 at var(--ox, 100%) var(--oy, 100%)); transition: clip-path 550ms var(--ease-out); }
@media (hover: hover) and (pointer: fine) { .cell:hover .reveal { clip-path: circle(150% at var(--ox, 100%) var(--oy, 100%)); } }
@media (hover: none) { .cell .reveal { display: none; } }
@media (min-width: 900px) { .grid { grid-template-columns: repeat(4, 1fr); grid-auto-rows: 200px; } .cell.big { grid-row: span 2; } .cell.pic { grid-row: span 2; } .cell.form { grid-column: span 2; } }
''', '''
<div class="wrap">{{TOP}}
	<main class="grid" id="grid">
		<section class="cell big" data-reveal><h1 data-split>{{H}}</h1><span>Mostafa Saher · technical instructor</span></section>
		<div class="cell pic" data-reveal style="--i:1">{{IMG}}</div>
		<div class="cell" data-reveal style="--i:2"><b>Thoughts</b><span>What students get stuck on.</span><div class="reveal"><b>Notes from the classroom</b><span style="color:#0F0F10">and the explanation that finally made it click.</span></div></div>
		<div class="cell" data-reveal style="--i:3"><b>Opinions</b><span>On the hype.</span><div class="reveal"><b>Plainly said</b><span style="color:#0F0F10">Where I stand on new models and cloud services.</span></div></div>
		<div class="cell" data-reveal style="--i:4"><b>Resources</b><span>Tested first.</span><div class="reveal"><b>Labs, docs, tools</b><span style="color:#0F0F10">The ones I actually use, each with a line on why.</span></div></div>
		<div class="cell" data-reveal style="--i:5"><b>Elsewhere</b>{{LINKS_INLINE}}</div>
		<section class="cell form" data-reveal style="--i:6"><b style="margin-bottom:12px">Get it by email</b>{{FORM}}</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''', '''
FX.$$('#grid .cell').forEach((c) => { c.addEventListener('pointermove', (e) => { const r = c.getBoundingClientRect(); c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px'); }); c.addEventListener('pointerenter', (e) => { const r = c.getBoundingClientRect(); c.style.setProperty('--ox', (e.clientX - r.left) + 'px'); c.style.setProperty('--oy', (e.clientY - r.top) + 'px'); }); });
''')

# 148 Origami fold
page(148, 'fold', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800', '#F4F0E8', '''
:root { --line: #DCD5C5; --focus: #1E1B16; --f-bg: #fff; --b-bg: #1E1B16; --b-text: #fff; --note: #6E685A; --f-radius: 999px; --b-radius: 999px; }
body { background: #F4F0E8; color: #1E1B16; font: 16px/1.5 "Bricolage Grotesque", system-ui, sans-serif; }
.stage { min-height: calc(100svh - 70px); display: grid; align-content: center; justify-items: center; gap: 24px; padding-block: 12px 40px; perspective: 1600px; }
.paper { width: min(100%, 720px); display: grid; transform-style: preserve-3d; }
.leaf { padding: clamp(18px, 3vw, 30px); background: var(--c); transform-origin: 50% 0; transform-style: preserve-3d; backface-visibility: hidden; box-shadow: 0 1px 0 rgb(0 0 0 / 0.06); }
.leaf:first-child { transform-origin: 50% 100%; }
.fx:not(.fx-rm) .paper:not(.in) .leaf:nth-child(2) { transform: rotateX(-178deg); } .fx:not(.fx-rm) .paper:not(.in) .leaf:nth-child(3) { transform: rotateX(178deg); opacity: 0; } .fx:not(.fx-rm) .paper:not(.in) .leaf:nth-child(4) { transform: rotateX(-178deg); opacity: 0; }
.fx .paper.in .leaf { transition: transform 1000ms var(--ease-io), opacity 200ms ease; } .fx .paper.in .leaf:nth-child(2) { transition-delay: 300ms; } .fx .paper.in .leaf:nth-child(3) { transition-delay: 1000ms, 1000ms; } .fx .paper.in .leaf:nth-child(4) { transition-delay: 1700ms, 1700ms; }
.leaf:nth-child(odd) { background-image: linear-gradient(rgb(0 0 0 / 0.03), transparent 40%); } .leaf:nth-child(even) { background-image: linear-gradient(transparent 60%, rgb(0 0 0 / 0.05)); }
h1 { font-size: clamp(2rem, 1.2rem + 3.6vw, 4rem); font-weight: 800; line-height: 0.98; letter-spacing: -0.045em; }
.row { display: flex; gap: 16px; align-items: center; } .row .face { flex: none; width: 90px; height: 90px; border-radius: 50%; background: #E6DFCF; }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="stage">
		<div class="paper" data-inview>
			<div class="leaf" style="--c:#FFFDF7"><h1>AI and cloud, unfolded one clear step at a time.</h1></div>
			<div class="leaf" style="--c:#FFE39B"><div class="row"><div class="face">{{IMG}}</div><p>I’m Mostafa Saher, a technical instructor. Each fold opens the next step.</p></div></div>
			<div class="leaf" style="--c:#CFE6FF"><p>The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?”. My newsletter is where that goes now.</p></div>
			<div class="leaf" style="--c:#FFFDF7">{{FORM}}</div>
		</div>
	</main>
</div>''' + MORE)

# 149 Gradient name follow
page(149, 'paint-name', 'family=Unbounded:wght@800&family=Geist:wght@400;500', '#F2F2EE', '''
:root { --line: #D9D9D3; --focus: #111; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 999px; --b-radius: 999px; }
body { background: #F2F2EE; color: #111; font: 15px/1.5 "Geist", system-ui, sans-serif; }
.stage { position: relative; min-height: calc(100svh - 70px); display: grid; grid-template-rows: 1fr auto; padding-bottom: 28px; }
.name { align-self: center; font: 800 clamp(3.4rem, 15vw, 14rem)/0.86 "Unbounded", sans-serif; letter-spacing: -0.06em; text-transform: uppercase; color: transparent; -webkit-text-stroke: 1.5px #111; background: radial-gradient(circle clamp(120px, 20vw, 300px) at var(--mx, 30%) var(--my, 40%), #FF5A36 0%, #FFB02E 35%, #7B5BFF 60%, transparent 61%) no-repeat; -webkit-background-clip: text; background-clip: text; }
.low { display: grid; gap: 18px 48px; align-items: end; }
.me { display: flex; gap: 14px; align-items: center; max-width: 30em; } .me .face { flex: none; width: 72px; height: 72px; border-radius: 50%; background: #E2E2DC; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="stage" id="stage">
		<h1 class="name" id="name" aria-label="Mostafa Saher">Mostafa<br>Saher</h1>
		<div class="low"><div class="me" data-reveal><div class="face">{{IMG}}</div><p>Move your cursor over the name to paint it. I teach AI and cloud, one clear step at a time.</p></div><div data-reveal style="--i:1">{{FORM}}</div></div>
	</main>
</div>''' + MORE, '''
const n = document.getElementById('name'); let x = 0.3, y = 0.4, tx = x, ty = y, used = false;
document.getElementById('stage').addEventListener('pointermove', (e) => { const r = n.getBoundingClientRect(); tx = (e.clientX - r.left) / r.width; ty = (e.clientY - r.top) / r.height; used = true; }, { passive: true });
if (FX.RM) return; FX.onTick((t) => { if (!used) { tx = 0.5 + Math.cos(t / 1500) * 0.4; ty = 0.5 + Math.sin(t / 1100) * 0.35; } x = FX.lerp(x, tx, 0.1); y = FX.lerp(y, ty, 0.1); n.style.setProperty('--mx', (x * 100).toFixed(2) + '%'); n.style.setProperty('--my', (y * 100).toFixed(2) + '%'); });
''')

# 150 Credits roll
page(150, 'credits', 'family=Cormorant+Garamond:wght@500;700&family=Geist:wght@400;500', '#000000', '''
:root { color-scheme: dark; --line: #222; --focus: #fff; --f-bg: #111; --f-text: #F2F2F2; --f-ph: #8E8E8E; --f-border: 1px solid #2E2E2E; --b-bg: #F2F2F2; --b-text: #000; --note: #8E8E8E; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #000; color: #F2F2F2; font: 15px/1.6 "Geist", system-ui, sans-serif; }
.screen { position: relative; height: 100svh; overflow: hidden; text-align: center; -webkit-mask-image: linear-gradient(transparent, #000 18%, #000 82%, transparent); mask-image: linear-gradient(transparent, #000 18%, #000 82%, transparent); }
.roll { position: absolute; left: 0; right: 0; top: 45%; display: grid; gap: 46px; padding-inline: 20px; }
.fx:not(.fx-rm) .roll { animation: credits 30s linear 400ms forwards; } .fx-rm .roll, html:not(.fx) .roll { position: static; padding-top: 40px; }
@keyframes credits { to { transform: translateY(calc(-100% - 20svh)); } }
.screen:hover .roll { animation-play-state: paused; }
.roll h1 { font: 700 clamp(2.6rem, 1.4rem + 6vw, 6rem)/0.95 "Cormorant Garamond", serif; }
.role { font: 400 0.75rem "Geist", sans-serif; letter-spacing: 0.2em; text-transform: uppercase; color: #8E8E8E; } .nm { font: 500 clamp(1.4rem, 1rem + 1.6vw, 2.2rem)/1.15 "Cormorant Garamond", serif; }
.roll figure { width: min(230px, 50%); margin-inline: auto; filter: grayscale(1) contrast(1.1); }
.roll .signup { max-width: 430px; margin-inline: auto; text-align: left; } .roll .note { text-align: center; }
.skip { position: absolute; right: 16px; bottom: 16px; z-index: 3; padding: 8px 14px; border: 1px solid #444; border-radius: 999px; background: #000; color: #ccc; font: inherit; cursor: pointer; }
.after { min-height: 50svh; display: grid; place-items: center; text-align: center; padding: 40px 20px; } .after .signup { max-width: 430px; width: 100%; text-align: left; } .after .note { text-align: center; }
''', '''
<main>
	<div class="screen" id="screen">
		<div class="roll">
			<p class="role">A one-person classroom presents</p><h1>AI and Cloud,<br>One Clear Step at a Time</h1>
			<figure>{{IMG}}</figure>
			<div><p class="role">Taught by</p><p class="nm">Mostafa Saher</p></div>
			<div><p class="role">Thoughts</p><p class="nm">What students get stuck on</p></div>
			<div><p class="role">Opinions</p><p class="nm">Where I stand on the hype</p></div>
			<div><p class="role">Resources</p><p class="nm">Labs, docs and tools I actually use</p></div>
			<div><p class="role">Filmed on location</p><p class="nm">The corridor, after class</p></div>
			<div><p class="role">No filler was harmed in the making of this newsletter</p></div>
			<div><p class="role">Stay after the credits</p></div>
		</div>
		<button class="skip" id="skip" type="button">Skip credits</button>
	</div>
	<section class="after" id="after"><div style="width:100%;max-width:520px"><p class="role" style="margin-bottom:10px">Post-credits scene</p><p class="nm" style="margin-bottom:18px">Get the next one by email.</p>{{FORM}}<div style="margin-top:22px;display:flex;justify-content:center">{{LINKS_INLINE}}</div><p style="margin-top:18px;color:#8E8E8E;font-size:0.85rem">{{FOOT}}</p></div></section>
</main>
''', "document.getElementById('skip').addEventListener('click', () => document.getElementById('after').scrollIntoView({ behavior: FX.RM ? 'auto' : 'smooth' }));")
print('d5 done')
