from lib2 import page
MORE = '<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>\n<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>'
MORECSS = '.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; } @media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }'
HERO2 = '.hero { display: grid; gap: 24px 48px; align-items: center; min-height: calc(100svh - 70px); padding-bottom: 36px; } @media (min-width: 900px) { .hero { grid-template-columns: 1.1fr 0.9fr; } }'
ME = '<div class="me" data-reveal><div class="face">{{IMG}}</div><p>I’m Mostafa Saher, a technical instructor. My newsletter carries what comes up after class.</p></div>'
MECSS = '.me { display: flex; gap: 14px; align-items: center; max-width: 30em; } .me .face { flex: none; width: 72px; height: 72px; border-radius: 50%; background: var(--facebg, #ddd); }'

# 131 Metro map
page(131, 'metro-map', 'family=Hanken+Grotesk:wght@400..800', '#F7F5EF', '''
:root { --line: #D9D5C8; --focus: #111; --f-bg: #fff; --f-border: 2px solid #111; --b-bg: #E32017; --b-text: #fff; --note: #666; --f-radius: 999px; --b-radius: 999px; }
body { background: #F7F5EF; color: #111; font: 16px/1.5 "Hanken Grotesk", system-ui, sans-serif; }
h1 { margin-top: clamp(10px, 4vh, 40px); font-size: clamp(2.2rem, 1.2rem + 4vw, 4.4rem); font-weight: 800; line-height: 1; letter-spacing: -0.04em; max-width: 12em; }
.map { position: relative; margin-top: 20px; }
.map svg { width: 100%; height: auto; overflow: visible; }
.map path { fill: none; stroke-width: 12; stroke-linecap: round; stroke-linejoin: round; }
.st { position: absolute; left: var(--x); top: var(--y); translate: -50% -50%; display: grid; justify-items: center; gap: 6px; text-align: center; width: 9em; }
.st i { width: 22px; height: 22px; border-radius: 50%; background: #fff; border: 5px solid #111; }
.st b { font-size: clamp(0.8rem, 0.7rem + 0.5vw, 1.05rem); line-height: 1.1; } .st small { color: #666; font-size: 0.8rem; line-height: 1.2; }
.fx:not(.fx-rm) .map:not(.in) .st { scale: 0; } .fx .map.in .st { transition: scale 500ms var(--spring) calc(600ms + var(--k) * 450ms); }
.st.you i { background: #E32017; border-color: #E32017; box-shadow: 0 0 0 6px rgb(227 32 23 / 0.25); }
.low { display: grid; gap: 20px 48px; align-items: end; padding-top: 40px; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } }
@media (max-width: 700px) { .st small { display: none; } .st { width: 6em; } }
''' + MECSS + MORECSS, '''
<div class="wrap">{{TOP}}
	<main>
		<h1 data-split>The AI and cloud line. All stops, one clear step at a time.</h1>
		<div class="map" data-inview data-draw style="--wait:300ms">
			<svg viewBox="0 0 1000 300" aria-hidden="true"><path pathLength="1" stroke="#0019A8" d="M40 230 H300 L400 130 H640 L740 60 H960"/><path pathLength="1" stroke="#00A650" style="--i:2" d="M400 130 V260 H700"/></svg>
			<div class="st" style="--x:4%;--y:77%;--k:0"><i></i><b>Classroom</b><small>where it starts</small></div>
			<div class="st" style="--x:30%;--y:77%;--k:1"><i></i><b>Thoughts</b><small>what students get stuck on</small></div>
			<div class="st" style="--x:40%;--y:43%;--k:2"><i></i><b>Opinions</b><small>where I stand on the hype</small></div>
			<div class="st" style="--x:64%;--y:43%;--k:3"><i></i><b>Resources</b><small>what I’d hand a student</small></div>
			<div class="st you" style="--x:96%;--y:20%;--k:4"><i class="fx-pulse"></i><b>Your inbox</b><small>terminus</small></div>
		</div>
		<div class="low">''' + ME + '''<div data-reveal style="--i:1">{{FORM}}</div></div>
	</main>
</div>''' + MORE)

# 132 Periodic table
els = [('Ms','Mostafa','#FFD23F'),('Ai','AI','#7FD1FF'),('Cl','Cloud','#B8F2C8'),('Th','Thoughts','#FFB3C7'),('Op','Opinions','#C9B8FF'),('Rs','Resources','#FFC78A'),('St','One step','#E5E5E5'),('Nw','Newsletter','#9FF0E0')]
page(132, 'elements', 'family=Geist:wght@400..700&family=Geist+Mono:wght@400', '#FFFFFF', '''
:root { --line: #E3E3E3; --focus: #111; --f-bg: #F3F3F3; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 8px; --b-radius: 5px; }
body { background: #fff; color: #111; font: 15px/1.5 "Geist", system-ui, sans-serif; }
h1 { margin: clamp(10px, 4vh, 36px) 0 20px; font-size: clamp(2rem, 1.2rem + 3.4vw, 3.8rem); font-weight: 700; line-height: 1; letter-spacing: -0.04em; max-width: 13em; }
.tbl { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; perspective: 900px; }
.el { position: relative; aspect-ratio: 1; padding: 10px; background: var(--c); display: grid; align-content: space-between; transition: transform 500ms var(--ease-out); transform-style: preserve-3d; cursor: default; }
.el small { font: 400 0.72rem "Geist Mono", monospace; } .el b { font-size: clamp(1.8rem, 6vw, 4rem); font-weight: 700; letter-spacing: -0.05em; line-height: 0.9; } .el span { font-size: 0.85rem; font-weight: 500; }
.el.ph { padding: 0; overflow: hidden; } .el.ph img { width: 130%; max-width: none; margin: 6% 0 0 -15%; }
.fx:not(.fx-rm) .tbl:not(.in) .el { transform: rotateY(90deg); opacity: 0; } .fx .tbl.in .el { transition: transform 700ms var(--ease-out) calc(var(--k) * 80ms), opacity 300ms ease calc(var(--k) * 80ms); }
@media (hover: hover) and (pointer: fine) { .tbl.in .el:hover { transform: translateZ(40px) rotateX(8deg); transition-delay: 0ms; z-index: 2; } }
.low { display: grid; gap: 20px 48px; align-items: end; padding-top: 32px; }
@media (min-width: 860px) { .tbl { grid-template-columns: repeat(9, 1fr); } .low { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main>
		<h1 data-split>The elements of a class that makes sense.</h1>
		<div class="tbl" data-inview><div class="el ph" style="--c:#DDE6F5;--k:0">{{IMG}}</div>''' + ''.join(f'<div class="el" style="--c:{c};--k:{k+1}"><small>{k+1}</small><b>{s}</b><span>{n}</span></div>' for k,(s,n,c) in enumerate(els)) + '''</div>
		<div class="low"><p data-reveal style="max-width:30em">I’m Mostafa Saher, a technical instructor. I teach AI and cloud, one clear step at a time, and I write down what comes up after class.</p><div data-reveal style="--i:1">{{FORM}}</div></div>
	</main>
</div>''' + MORE)

# 133 Vinyl
page(133, 'vinyl', 'family=Fraunces:opsz,wght@9..144,400;9..144,700&family=Geist:wght@400;500', '#E8DCC4', '''
:root { --line: #CDBF9F; --focus: #2B1D12; --f-bg: #FBF6EA; --b-bg: #C8452A; --b-text: #fff; --note: #6B5B45; --f-radius: 999px; --b-radius: 999px; }
body { background: #E8DCC4; color: #2B1D12; font: 15px/1.55 "Geist", system-ui, sans-serif; }
''' + HERO2 + '''
h1 { font: 700 clamp(2.4rem, 1.2rem + 4.6vw, 5rem)/0.98 "Fraunces", serif; letter-spacing: -0.03em; }
.hero p.s { margin: 16px 0 22px; max-width: 30em; }
.signup { max-width: 440px; }
.deck { position: relative; justify-self: center; width: min(400px, 86vw); aspect-ratio: 1; cursor: pointer; }
.sleeve { position: absolute; inset: 0 22% 0 0; background: #C8452A; overflow: hidden; display: flex; align-items: flex-end; justify-content: center; box-shadow: 0 20px 40px -20px #000; z-index: 2; } .sleeve img { width: 110%; max-width: none; } .sleeve b { position: absolute; left: 14px; top: 12px; color: #FBF6EA; font: 700 1.5rem/1 "Fraunces", serif; }
.disc { position: absolute; top: 4%; bottom: 4%; right: 0; aspect-ratio: 1; border-radius: 50%; background: repeating-radial-gradient(circle, #111 0 2px, #1E1E1E 2px 4px); transition: translate 900ms var(--ease-out); translate: -30% 0; }
.disc::after { content: "AI + CLOUD"; position: absolute; inset: 34%; border-radius: 50%; background: #F2B84B; display: grid; place-items: center; font-size: 0.6rem; font-weight: 600; letter-spacing: 0.1em; }
.deck.in .disc, .deck.play .disc { translate: 0 0; }
@media (prefers-reduced-motion: no-preference) { .deck.in .disc { animation: fx-spin 3.2s linear infinite; } .deck.paused .disc { animation-play-state: paused; } }
.np { margin-top: 14px; text-align: center; font-size: 0.85rem; }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div><h1 data-split>AI and cloud, on repeat until it clicks.</h1><p class="s" data-reveal style="--wait:500ms">I’m Mostafa Saher. I teach one clear step at a time, and I write down what comes up after class.</p><div data-reveal style="--wait:650ms">{{FORM}}</div></div>
		<div><div class="deck" id="deck" data-inview><div class="disc"></div><div class="sleeve"><b>After class</b>{{IMG}}</div></div><p class="np">Now playing: Side A, “Wait, so why does that work?” (tap the record to pause)</p></div>
	</main>
</div>''' + MORE, "document.getElementById('deck').addEventListener('click', (e) => e.currentTarget.classList.toggle('paused'));")

# 134 Timetable
page(134, 'timetable', 'family=Figtree:wght@400..800', '#F4F6FA', '''
:root { --line: #DDE2EC; --focus: #2348E0; --f-bg: #fff; --f-border: 1px solid #D5DBE8; --b-bg: #2348E0; --b-text: #fff; --note: #667; --f-radius: 10px; --b-radius: 7px; }
body { background: #F4F6FA; color: #141A2B; font: 15px/1.5 "Figtree", system-ui, sans-serif; }
h1 { margin: clamp(8px, 3vh, 28px) 0 18px; font-size: clamp(2rem, 1.2rem + 3.2vw, 3.6rem); font-weight: 800; line-height: 1; letter-spacing: -0.04em; max-width: 13em; }
.cal { position: relative; display: grid; grid-template-columns: 44px repeat(5, 1fr); grid-template-rows: 30px repeat(5, 64px); background: #fff; border-radius: 16px; border: 1px solid var(--line); overflow: hidden; }
.cal > span { font-size: 0.72rem; font-weight: 600; color: #7A8296; padding: 8px; border-bottom: 1px solid var(--line); } .cal > span.t { border-bottom: 0; border-right: 1px solid var(--line); grid-column: 1; }
.cal::before { content: ""; position: absolute; left: 44px; right: 0; top: 30px; bottom: 0; background: repeating-linear-gradient(transparent 0 63px, var(--line) 63px 64px); }
.ev { position: relative; margin: 3px; padding: 8px; border-radius: 9px; background: var(--c); font-size: 0.8rem; font-weight: 600; line-height: 1.15; overflow: hidden; grid-column: var(--d); grid-row: var(--r); }
.ev small { display: block; font-weight: 400; opacity: 0.75; }
.fx:not(.fx-rm) .cal:not(.in) .ev { scale: 0.6; opacity: 0; } .fx .cal.in .ev { transition: scale 500ms var(--spring) calc(var(--k) * 110ms), opacity 300ms ease calc(var(--k) * 110ms); }
.now { position: absolute; left: 44px; right: 0; top: calc(30px + var(--t, 0.4) * 320px); height: 2px; background: #E5341D; z-index: 3; } .now::before { content: ""; position: absolute; left: -5px; top: -4px; width: 10px; height: 10px; border-radius: 50%; background: #E5341D; }
.ev.ph { padding: 0; } .ev.ph img { width: 150%; max-width: none; margin: 0 0 0 -25%; }
.low { display: grid; gap: 20px 48px; align-items: end; padding-top: 28px; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } .cal { grid-template-rows: 30px repeat(5, 76px); } .cal::before { background: repeating-linear-gradient(transparent 0 75px, var(--line) 75px 76px); } .now { top: calc(30px + var(--t, 0.4) * 380px); } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main>
		<h1 data-split>My week, and where your inbox fits in.</h1>
		<div class="cal" data-inview aria-hidden="true"><span></span><span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span>
			<span class="t" style="grid-row:2">9</span><span class="t" style="grid-row:3">11</span><span class="t" style="grid-row:4">1</span><span class="t" style="grid-row:5">3</span><span class="t" style="grid-row:6">5</span>
			<div class="ev" style="--d:2;--r:2 / span 2;--c:#CFE0FF;--k:0">AI class<small>one clear step</small></div><div class="ev" style="--d:3;--r:3 / span 2;--c:#C8F2D4;--k:1">Cloud class<small>hands-on lab</small></div>
			<div class="ev ph" style="--d:4;--r:2 / span 2;--c:#E8E2D2;--k:2">{{IMG}}</div><div class="ev" style="--d:5;--r:2;--c:#FFE39B;--k:3">AI class</div><div class="ev" style="--d:6;--r:3 / span 2;--c:#CFE0FF;--k:4">Cloud class</div>
			<div class="ev" style="--d:2;--r:5;--c:#FFD0C8;--k:5">Corridor questions<small>the best part</small></div><div class="ev" style="--d:4;--r:5;--c:#FFD0C8;--k:6">Corridor questions</div>
			<div class="ev" style="--d:5 / span 2;--r:6;--c:#2348E0;color:#fff;--k:7">Write the newsletter<small>→ your inbox</small></div>
			<i class="now" id="now"></i>
		</div>
		<div class="low"><p data-reveal style="max-width:30em">I’m Mostafa Saher, a technical instructor. The best part of every class comes once it’s over, and I write that part down.</p><div data-reveal style="--i:1">{{FORM}}</div></div>
	</main>
</div>''' + MORE, "const n = new Date(), h = n.getHours() + n.getMinutes() / 60; document.getElementById('now').style.setProperty('--t', Math.min(1, Math.max(0, (h - 9) / 10)).toFixed(3));")

# 135 Keyboard
rows = ['QWERTYUIOP','ASDFGHJKL','ZXCVBNM']
kb = ''.join('<div class="kr">' + ''.join(f'<i data-k="{ch}">{ch}</i>' for ch in r) + '</div>' for r in rows) + '<div class="kr"><i data-k=" " class="sp"></i></div>'
page(135, 'keyboard', 'family=Geist+Mono:wght@400;500&family=Geist:wght@400..600', '#E9E7E1', '''
:root { --line: #CFCBC0; --focus: #111; --f-bg: #fff; --b-bg: #FF6A2B; --b-text: #111; --note: #666; --f-radius: 10px; --b-radius: 7px; }
body { background: #E9E7E1; color: #111; font: 15px/1.5 "Geist", system-ui, sans-serif; }
.stage { min-height: calc(100svh - 70px); display: grid; align-content: center; justify-items: center; gap: 22px; padding-block: 12px 36px; text-align: center; }
.screen { width: min(100%, 720px); min-height: 3.4em; padding: 16px 20px; border-radius: 14px; background: #111; color: #8CFFB5; font: 500 clamp(1rem, 0.8rem + 1.4vw, 1.7rem)/1.3 "Geist Mono", monospace; text-align: left; }
.kb { display: grid; gap: 6px; padding: 14px; border-radius: 18px; background: #D4D1C8; box-shadow: 0 16px 30px -18px #000, inset 0 -4px 0 #B9B5AA; width: min(100%, 720px); }
.kr { display: flex; justify-content: center; gap: 6px; }
.kr i { flex: 1 1 0; max-width: 60px; aspect-ratio: 1; display: grid; place-items: center; border-radius: 8px; background: #FAF9F5; font: 500 clamp(0.7rem, 2.2vw, 1rem) "Geist Mono", monospace; font-style: normal; box-shadow: 0 4px 0 #B9B5AA; transition: translate 80ms ease, box-shadow 80ms ease, background-color 200ms ease; user-select: none; }
.kr i.sp { max-width: 46%; aspect-ratio: auto; height: 44px; flex-basis: 46%; }
.kr i.dn { translate: 0 4px; box-shadow: 0 0 0 #B9B5AA; background: #FF6A2B; }
.signup { width: 100%; max-width: 440px; text-align: left; } .note { text-align: center; }
''' + MECSS + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="stage">
		<h1 class="sr">Mostafa Saher teaches AI and cloud, one clear step at a time</h1>
		<p class="screen" aria-hidden="true">&gt; <span id="out"></span><span class="fx-caret"></span></p>
		<div class="kb" id="kb" aria-hidden="true">''' + kb + '''</div>
		''' + ME + '''
		<div data-reveal style="width:100%;display:grid;justify-items:center">{{FORM}}</div>
	</main>
</div>''' + MORE, '''
const out = document.getElementById('out'), keys = {}; FX.$$('#kb i').forEach((k) => { keys[k.dataset.k] = k; });
const press = (ch) => { const k = keys[ch.toUpperCase()]; if (!k) return; k.classList.add('dn'); setTimeout(() => k.classList.remove('dn'), 110); };
const lines = ['I teach AI and cloud', 'one clear step at a time', 'wait so why does that work']; if (FX.RM) { out.textContent = lines[0]; return; }
let l = 0, i = 0, del = false; const step = () => { const s = lines[l]; if (!del) { i++; press(s[i - 1]); } else i--; out.textContent = s.slice(0, i); let d = del ? 28 : 95; if (!del && i === s.length) { del = true; d = 1500; } else if (del && i === 0) { del = false; l = (l + 1) % lines.length; d = 350; } setTimeout(step, d); }; setTimeout(step, 600);
addEventListener('keydown', (e) => { if (!e.target.matches('input')) press(e.key); });
''')

# 136 Blueprint
page(136, 'blueprint', 'family=Chivo+Mono:wght@400;500&family=Chivo:wght@400..800', '#0E3A8A', '''
:root { color-scheme: dark; --ink: #DCE9FF; --line: rgb(220 233 255 / 0.35); --focus: #fff; --f-bg: rgb(255 255 255 / 0.08); --f-text: #fff; --f-ph: #B5C8EE; --f-border: 1.5px dashed rgb(220 233 255 / 0.7); --b-bg: #DCE9FF; --b-text: #0E3A8A; --note: #B5C8EE; --err: #FFD2CB; --f-radius: 0; --b-radius: 0; --f-pad: 4px; }
body { background-color: #0E3A8A; background-image: linear-gradient(rgb(255 255 255 / 0.1) 1px, transparent 1px), linear-gradient(90deg, rgb(255 255 255 / 0.1) 1px, transparent 1px); background-size: 28px 28px; color: var(--ink); font: 15px/1.55 "Chivo", system-ui, sans-serif; }
.mono, .top { font-family: "Chivo Mono", monospace; font-size: 0.78rem; letter-spacing: 0.06em; text-transform: uppercase; }
''' + HERO2 + '''
h1 { font-size: clamp(2.2rem, 1.2rem + 4vw, 4.6rem); font-weight: 800; line-height: 0.98; letter-spacing: -0.035em; }
.hero p.s { margin: 16px 0 22px; max-width: 30em; color: #C4D5F5; }
.signup { max-width: 440px; }
.plan { position: relative; justify-self: center; width: min(360px, 80vw); margin: 34px 40px 34px 0; }
.plan .bx { position: relative; border: 1.5px solid var(--ink); aspect-ratio: 1100 / 1433; }
.plan img { width: 100%; filter: grayscale(1) brightness(1.5) contrast(1.2); mix-blend-mode: screen; opacity: 0.9; }
.dim { position: absolute; color: var(--ink); font: 400 0.7rem "Chivo Mono", monospace; white-space: nowrap; }
.dim.h { left: 0; right: 0; top: -26px; text-align: center; border-top: 1px solid var(--ink); padding-top: 3px; } .dim.h::before, .dim.h::after, .dim.v::before, .dim.v::after { content: ""; position: absolute; background: var(--ink); }
.dim.h::before, .dim.h::after { top: -5px; width: 1px; height: 9px; } .dim.h::before { left: 0; } .dim.h::after { right: 0; }
.dim.v { top: 0; bottom: 0; right: -30px; writing-mode: vertical-rl; text-align: center; border-left: 1px solid var(--ink); padding-left: 3px; } .dim.v::before, .dim.v::after { left: -5px; height: 1px; width: 9px; } .dim.v::before { top: 0; } .dim.v::after { bottom: 0; }
.tagl { position: absolute; left: var(--x); top: var(--y); font: 400 0.7rem "Chivo Mono", monospace; padding-left: 34px; } .tagl::before { content: ""; position: absolute; left: 0; top: 50%; width: 28px; height: 1px; background: var(--ink); } .tagl::after { content: ""; position: absolute; left: -3px; top: calc(50% - 3px); width: 7px; height: 7px; border-radius: 50%; background: var(--ink); }
.fx:not(.fx-rm) .plan:not(.in) .bx { clip-path: inset(0 100% 0 0); } .fx .plan .bx { transition: clip-path 1400ms var(--ease-io); clip-path: inset(-40px -60px); } .fx:not(.fx-rm) .plan:not(.in) .tagl { opacity: 0; } .fx .plan.in .tagl { transition: opacity 400ms ease calc(1200ms + var(--k) * 250ms); }
.stamp { margin-top: 12px; display: inline-block; padding: 4px 10px; border: 1.5px solid var(--ink); }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div><p class="mono" style="margin-bottom:12px">Drawing no. 01 · scale 1:1</p><h1 data-split>How an AI and cloud class is built.</h1><p class="s" data-reveal style="--wait:500ms">I’m Mostafa Saher, a technical instructor. One clear step at a time, drawn up and sent by email.</p><div data-reveal style="--wait:650ms">{{FORM}}</div></div>
		<div class="plan" data-inview><div class="bx">{{IMG}}<span class="dim h">1 instructor</span><span class="dim v">patience: plenty</span>
			<span class="tagl" style="--x:62%;--y:16%;--k:0">explains twice</span><span class="tagl" style="--x:70%;--y:52%;--k:1">arms: crossed</span><span class="tagl" style="--x:58%;--y:80%;--k:2">notes: taken</span></div><span class="mono stamp">Approved for learning</span></div>
	</main>
</div>''' + MORE)

# 137 Flip postcard
page(137, 'postcard', 'family=Kalam:wght@400;700&family=Archivo:wght@500..800', '#D7E7E4', '''
:root { --line: #B9CFCB; --focus: #1D3B36; --f-bg: #fff; --f-border: 1.5px solid #1D3B36; --b-bg: #1D3B36; --b-text: #fff; --note: #5B7570; --f-radius: 6px; --b-radius: 3px; --f-pad: 4px; }
body { background: #D7E7E4; color: #1D3B36; font: 15px/1.5 "Archivo", system-ui, sans-serif; }
.stage { min-height: calc(100svh - 70px); display: grid; align-content: center; justify-items: center; gap: 20px; padding-block: 12px 36px; perspective: 1600px; }
.card { position: relative; width: min(100%, 680px); aspect-ratio: 3 / 2; transform-style: preserve-3d; transition: transform 1100ms var(--ease-io); }
.card.flip { transform: rotateY(180deg); }
.fc { position: absolute; inset: 0; backface-visibility: hidden; border-radius: 10px; overflow: hidden; box-shadow: 0 30px 50px -28px #000; }
.fr { background: linear-gradient(#57B6E8, #BFE6F7 60%, #F6E2B3); display: flex; align-items: flex-end; justify-content: flex-end; }
.fr img { height: 92%; width: auto; max-width: none; margin-right: 4%; }
.fr h1 { position: absolute; left: 5%; top: 8%; font-size: clamp(1.8rem, 6vw, 4rem); font-weight: 800; line-height: 0.92; letter-spacing: -0.04em; text-transform: uppercase; color: #fff; text-shadow: 3px 3px 0 #1D3B36; max-width: 7em; }
.bk { transform: rotateY(180deg); background: #FBF8EE; display: grid; grid-template-columns: 1.1fr 1fr; gap: 0; padding: 5%; }
.msg { font: 400 clamp(0.85rem, 2.4vw, 1.25rem)/1.35 "Kalam", cursive; padding-right: 5%; border-right: 1.5px solid #1D3B36; overflow: hidden; }
.addr { padding-left: 6%; display: grid; align-content: space-between; }
.stampx { justify-self: end; width: 22%; min-width: 46px; aspect-ratio: 4 / 5; border: 2px dashed #1D3B36; background: #F2B84B; overflow: hidden; } .stampx img { width: 150%; max-width: none; margin-left: -25%; }
.addr .signup { font-size: 14px; } .addr .btn { padding-inline: 10px; } .addr .btn svg { display: none; } .addr .note { font-size: 0.75rem; }
.flipbtn { padding: 10px 18px; border: 1.5px solid #1D3B36; border-radius: 999px; background: none; color: inherit; font: inherit; font-weight: 600; cursor: pointer; }
@media (max-width: 600px) { .card { aspect-ratio: 3 / 4; } .bk { grid-template-columns: 1fr; grid-template-rows: auto 1fr; } .msg { border-right: 0; border-bottom: 1.5px solid #1D3B36; padding: 0 0 4%; } .addr { padding: 4% 0 0; } .stampx { display: none; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="stage">
		<div class="card" id="card"><div class="fc fr"><h1>Greetings from the classroom</h1>{{IMG}}</div>
			<div class="fc bk"><p class="msg">Hi! I’m Mostafa. I teach AI and cloud, one clear step at a time. The best part of every class comes once it’s over, so I write it down and post it to you. Wish you were here!</p><div class="addr"><div class="stampx">{{IMG}}</div><div><p style="margin-bottom:8px;font-weight:600">Send to:</p>{{FORM}}</div></div></div></div>
		<button class="flipbtn" id="flipbtn" type="button">Turn the card over</button>
	</main>
</div>''' + MORE, '''
const card = document.getElementById('card'), btn = document.getElementById('flipbtn'); const set = (on) => { card.classList.toggle('flip', on); btn.textContent = on ? 'See the front' : 'Turn the card over'; };
btn.addEventListener('click', () => set(!card.classList.contains('flip'))); setTimeout(() => set(true), FX.RM ? 0 : 1800);
''')

# 138 Elevator
page(138, 'elevator', 'family=Oswald:wght@400;600&family=Geist:wght@400;500', '#1A1A1D', '''
:root { --line: rgb(0 0 0 / 0.18); --focus: #111; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #444; --f-radius: 8px; --b-radius: 5px; }
body { background: #1A1A1D; color: #111; font: 16px/1.5 "Geist", system-ui, sans-serif; }
.panel { position: fixed; z-index: 8; right: max(12px, env(safe-area-inset-right)); top: 50%; translate: 0 -50%; display: grid; gap: 6px; padding: 10px 8px; border-radius: 14px; background: #2A2A2F; box-shadow: 0 10px 30px -10px #000; }
.panel b { display: grid; place-items: center; width: 34px; height: 34px; border-radius: 50%; border: 2px solid #55555E; color: #B9B9C2; font: 600 0.9rem "Oswald", sans-serif; transition: background-color 250ms ease, color 250ms ease, border-color 250ms ease; }
.panel b.on { background: #FFB000; border-color: #FFB000; color: #111; }
.disp { text-align: center; color: #FFB000; font: 600 1.3rem "Oswald", sans-serif; padding-bottom: 4px; border-bottom: 1px solid #44444C; margin-bottom: 2px; }
.fl { position: relative; min-height: 100svh; display: grid; align-content: center; gap: 18px; padding: 60px clamp(20px, 8vw, 120px); padding-right: clamp(70px, 12vw, 160px); background: var(--c); overflow: hidden; }
.fl .no { position: absolute; right: 8%; bottom: -0.2em; font: 600 clamp(12rem, 44vw, 34rem)/0.8 "Oswald", sans-serif; opacity: 0.12; }
.fl h1, .fl h2 { position: relative; font: 600 clamp(2.4rem, 1.2rem + 6vw, 6rem)/0.95 "Oswald", sans-serif; text-transform: uppercase; max-width: 10em; }
.fl p { position: relative; max-width: 28em; font-size: 1.15rem; }
.fl figure { position: absolute; right: 12%; bottom: 0; height: 70%; aspect-ratio: 1100 / 1433; } .fl figure img { height: 100%; width: auto; max-width: none; }
.fl .signup { position: relative; max-width: 440px; }
@media (max-width: 700px) { .fl figure { height: 46%; right: 14%; } }
''', '''
<nav class="panel" aria-hidden="true"><div class="disp" id="disp">4</div><b>4</b><b>3</b><b>2</b><b>1</b><b>G</b></nav>
<main id="floors">
	<section class="fl" style="--c:#F2EEE3"><span class="no">4</span><h1 data-split>Going down? AI and cloud, floor by floor.</h1><p data-reveal>Mostafa Saher, technical instructor. Scroll to ride the lift.</p></section>
	<section class="fl" style="--c:#FFCE4A"><span class="no">3</span><h2 data-split>The instructor.</h2><p data-reveal>I teach one clear step at a time.</p><figure data-reveal="right">{{IMG}}</figure></section>
	<section class="fl" style="--c:#9AD4F5"><span class="no">2</span><h2 data-split>Thoughts and opinions.</h2><p data-reveal>What students get stuck on, and where I stand on the hype.</p></section>
	<section class="fl" style="--c:#B8F0C4"><span class="no">1</span><h2 data-split>Resources.</h2><p data-reveal>The labs, docs, courses and tools I actually use.</p></section>
	<section class="fl" style="--c:#fff"><span class="no">G</span><h2 data-split>Ground floor: your inbox.</h2><div data-reveal>{{FORM}}</div>{{LINKS_INLINE}}<p style="font-size:0.85rem;opacity:0.65">{{FOOT}}</p></section>
</main>
''', '''
const fl = FX.$$('#floors .fl'), bs = FX.$$('.panel b'), disp = document.getElementById('disp'), names = ['4', '3', '2', '1', 'G']; let cur = -1;
const upd = () => { const i = Math.max(0, Math.min(4, Math.round(scrollY / innerHeight))); if (i === cur) return; cur = i; bs.forEach((b, k) => b.classList.toggle('on', k === i)); disp.textContent = names[i]; }; addEventListener('scroll', upd, { passive: true }); upd();
''')

# 139 Flashlight
page(139, 'flashlight', 'family=Unbounded:wght@500;800&family=Geist:wght@400;500', '#050505', '''
:root { color-scheme: dark; --line: #2A2A2A; --focus: #FFE9A8; --f-bg: #151515; --f-text: #F4F1E6; --f-ph: #99958A; --f-border: 1px solid #333; --b-bg: #FFE9A8; --b-text: #111; --note: #99958A; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #050505; color: #F4F1E6; font: 15px/1.55 "Geist", system-ui, sans-serif; }
.dark { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; overflow: hidden; --mx: 70%; --my: 40%; }
.lit { position: absolute; inset: 0; background: #F4F1E6; color: #111; display: grid; align-content: center; padding-inline: clamp(18px, 6vw, 80px); -webkit-mask-image: radial-gradient(circle clamp(120px, 22vmin, 240px) at var(--mx) var(--my), #000 60%, transparent 100%); mask-image: radial-gradient(circle clamp(120px, 22vmin, 240px) at var(--mx) var(--my), #000 60%, transparent 100%); }
.lit h1, .ghost { font: 800 clamp(2.6rem, 1.2rem + 8vw, 8rem)/0.9 "Unbounded", sans-serif; letter-spacing: -0.05em; text-transform: uppercase; }
.lit figure { position: absolute; right: 6%; bottom: 0; height: 74%; aspect-ratio: 1100 / 1433; } .lit figure img { height: 100%; width: auto; max-width: none; }
.ghostwrap { align-self: center; padding-inline: clamp(18px, 6vw, 80px); } .ghost { color: transparent; -webkit-text-stroke: 1px #2E2E2E; }
.dark > .wrap { position: relative; z-index: 3; }
.low { display: grid; gap: 14px 48px; align-items: end; padding-bottom: 24px; } .low p { color: #B9B5A8; max-width: 28em; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="dark" id="dark"><div class="wrap">{{TOP}}</div>
	<div class="ghostwrap" aria-hidden="true"><p class="ghost">Shining a light on AI and cloud.</p></div>
	<div class="lit"><h1>Shining a light on AI and cloud.</h1><figure>{{IMG}}</figure></div>
	<div class="wrap low"><p>Mostafa Saher, technical instructor. Move your cursor (or finger) to look around.</p><div>{{FORM}}</div></div>
</div>''' + MORE, '''
const d = document.getElementById('dark'); let x = 0.7, y = 0.4, tx = x, ty = y, used = false;
d.addEventListener('pointermove', (e) => { const r = d.getBoundingClientRect(); tx = (e.clientX - r.left) / r.width; ty = (e.clientY - r.top) / r.height; used = true; }, { passive: true });
if (FX.RM) return; FX.onTick((t) => { if (!used) { tx = 0.5 + Math.cos(t / 1700) * 0.32; ty = 0.45 + Math.sin(t / 1300) * 0.2; } x = FX.lerp(x, tx, 0.12); y = FX.lerp(y, ty, 0.12); d.style.setProperty('--mx', (x * 100).toFixed(2) + '%'); d.style.setProperty('--my', (y * 100).toFixed(2) + '%'); });
''')

# 140 Equaliser
page(140, 'equaliser', 'family=Sora:wght@300..700', '#0C0B14', '''
:root { color-scheme: dark; --line: #262436; --focus: #B7A6FF; --f-bg: #17152A; --f-text: #F3F1FF; --f-ph: #9D98BD; --f-border: 1px solid #2E2B47; --b-bg: #B7A6FF; --b-text: #0C0B14; --note: #9D98BD; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #0C0B14; color: #F3F1FF; font: 15px/1.6 "Sora", system-ui, sans-serif; }
.stage { min-height: calc(100svh - 70px); display: grid; align-content: center; gap: 26px; padding-block: 12px 36px; }
.player { display: grid; gap: 18px; padding: clamp(16px, 3vw, 28px); border-radius: 26px; background: linear-gradient(140deg, #1D1A38, #121024); border: 1px solid #2E2B47; }
.rowp { display: flex; gap: 16px; align-items: center; } .art { flex: none; width: clamp(84px, 16vw, 150px); aspect-ratio: 1; border-radius: 16px; background: linear-gradient(#7B5BFF, #FF6FB5); overflow: hidden; } .art img { width: 130%; max-width: none; margin: 8% 0 0 -15%; }
h1 { font-size: clamp(1.5rem, 1rem + 2.6vw, 3rem); font-weight: 600; line-height: 1.05; letter-spacing: -0.035em; } .rowp small { color: #9D98BD; }
.eq { display: flex; align-items: flex-end; gap: clamp(2px, 0.6vw, 6px); height: clamp(90px, 18vw, 170px); }
.eq i { flex: 1; border-radius: 4px 4px 0 0; background: linear-gradient(#FF6FB5, #7B5BFF); height: 20%; transform-origin: 50% 100%; }
@media (prefers-reduced-motion: no-preference) { .eq i { animation: eq var(--d) ease-in-out infinite alternate; animation-delay: var(--dl); } .player.paused .eq i { animation-play-state: paused; } @keyframes eq { from { height: 12%; } to { height: var(--h); } } }
.ctl { display: flex; align-items: center; gap: 14px; } .ctl button { width: 54px; height: 54px; border: 0; border-radius: 50%; background: #F3F1FF; color: #0C0B14; font-size: 1.1rem; cursor: pointer; } .bar2 { flex: 1; height: 4px; border-radius: 4px; background: #2E2B47; overflow: hidden; } .bar2 i { display: block; height: 100%; width: 0; background: #B7A6FF; }
.low { display: grid; gap: 16px 48px; align-items: end; } .low p { color: #BDB8DA; max-width: 30em; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="stage">
		<div class="player" id="player"><div class="rowp"><div class="art">{{IMG}}</div><div><small>Now explaining · Mostafa Saher</small><h1>AI and cloud, one clear step at a time</h1></div></div>
			<div class="eq" aria-hidden="true">''' + ''.join(f'<i style="--h:{30+((k*37)%65)}%;--d:{420+((k*53)%500)}ms;--dl:-{(k*91)%700}ms"></i>' for k in range(40)) + '''</div>
			<div class="ctl"><button id="pp" type="button" aria-label="Pause or play the animation">❚❚</button><div class="bar2"><i id="prog"></i></div><small id="tm">0:00</small></div></div>
		<div class="low"><p data-reveal>The best part of every class comes once it’s over. I write that part down and send it by email.</p><div data-reveal style="--i:1">{{FORM}}</div></div>
	</main>
</div>''' + MORE, '''
const pl = document.getElementById('player'), pp = document.getElementById('pp'), prog = document.getElementById('prog'), tm = document.getElementById('tm'); let t = 0, on = true;
pp.addEventListener('click', () => { on = !on; pl.classList.toggle('paused', !on); pp.textContent = on ? '❚❚' : '▶'; });
setInterval(() => { if (!on) return; t = (t + 1) % 180; prog.style.width = (t / 180 * 100) + '%'; tm.textContent = Math.floor(t / 60) + ':' + String(t % 60).padStart(2, '0'); }, 1000);
''')
print('d4 done')
