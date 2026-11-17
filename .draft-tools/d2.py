from lib2 import page
MORE = '<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>\n<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>'
MORECSS = '.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; } @media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }'
HERO2 = '.hero { display: grid; gap: 24px 48px; align-items: center; min-height: calc(100svh - 70px); padding-bottom: 36px; } @media (min-width: 900px) { .hero { grid-template-columns: 1.1fr 0.9fr; } }'

# 111 Loud pop — after Protip Marketing (One Page Love)
page(111, 'loud-pop', 'family=Archivo:wght@500..900&family=Archivo+Narrow:wght@600', '#FF63D8', '''
:root { --line: #111; --focus: #111; --f-bg: #fff; --f-border: 3px solid #111; --b-bg: #111; --b-text: #C8FF3D; --note: #3A0A30; --err: #5A0000; --f-radius: 999px; --b-radius: 999px; }
body { background: #FF63D8; color: #111; font: 600 16px/1.4 "Archivo", system-ui, sans-serif; }
::selection { background: #C8FF3D; }
.top a { padding: 6px 14px; border: 3px solid #111; border-radius: 999px; background: #C8FF3D; }
.hero { position: relative; display: grid; gap: 18px; padding-block: 8px 0; overflow: hidden; }
.pic { position: relative; background: #C8FF3D; border: 4px solid #111; border-radius: 26px; overflow: hidden; display: flex; justify-content: center; align-items: flex-end; min-height: 340px; }
.pic img { width: min(86%, 400px); }
.pill { position: absolute; padding: 6px 14px; border: 3px solid #111; border-radius: 999px; background: #fff; font-weight: 800; rotate: var(--r); left: var(--x); top: var(--y); white-space: nowrap; }
@media (prefers-reduced-motion: no-preference) { .pill { animation: wob 2.6s ease-in-out infinite alternate; animation-delay: var(--d); } @keyframes wob { from { rotate: calc(var(--r) - 5deg); translate: 0 -4px; } to { rotate: calc(var(--r) + 5deg); translate: 0 4px; } } }
h1 { font-size: clamp(2.6rem, 1.2rem + 7vw, 7rem); font-weight: 900; line-height: 0.88; letter-spacing: -0.04em; text-transform: uppercase; }
h1 mark { background: #111; color: #C8FF3D; padding-inline: 0.12em; }
.banner { margin: 22px -6% 0; padding: 10px 0; background: #2A4BFF; color: #fff; border-block: 4px solid #111; rotate: -3deg; font-size: 1.5rem; font-weight: 900; text-transform: uppercase; --dur: 18s; } .banner i { font-style: normal; margin-inline: 0.6em; color: #C8FF3D; }
.cols { display: grid; gap: 14px; padding-block: 44px 8px; }
.box { border: 4px solid #111; border-radius: 22px; padding: 20px; background: var(--c); box-shadow: 6px 6px 0 #111; }
.box h2 { font-size: 1.6rem; font-weight: 900; text-transform: uppercase; letter-spacing: -0.02em; margin-bottom: 10px; }
.box .tp li, .box .li-rows a { border-color: #111; }
@media (min-width: 880px) { .hero { grid-template-columns: 1.1fr 0.9fr; align-items: stretch; } .cols { grid-template-columns: 1fr 1fr 1fr; } }
''', '''
<div class="wrap">{{TOP}}
	<main>
		<section class="hero">
			<div style="align-self:center"><h1 data-split data-fx="pop">AI and cloud people <mark>actually get.</mark></h1><p style="margin:16px 0 18px;max-width:28em" data-reveal style="--wait:500ms">I’m Mostafa Saher, a technical instructor. One clear step at a time.</p><div data-reveal style="--wait:650ms;max-width:460px">{{FORM}}</div></div>
			<div class="pic" data-reveal="scale">{{IMG}}<span class="pill" style="--x:6%;--y:8%;--r:-8deg;--d:0s">Ask me why ↗</span><span class="pill" style="--x:58%;--y:16%;--r:9deg;--d:-1s;background:#2A4BFF;color:#fff">AI</span><span class="pill" style="--x:8%;--y:72%;--r:6deg;--d:-2s;background:#111;color:#C8FF3D">Cloud</span></div>
		</section>
		<div class="banner" data-marquee>Thoughts<i>★</i>Opinions<i>★</i>Resources<i>★</i>After class<i>★</i></div>
		<section class="cols">
			<div class="box" style="--c:#fff" data-reveal><h2>What I write</h2>{{TOPICS_UL}}</div>
			<div class="box" style="--c:#C8FF3D" data-reveal style="--i:1"><h2>Why</h2><p>{{INTRO}}</p></div>
			<div class="box" style="--c:#FFD23F" data-reveal style="--i:2"><h2>Find me</h2>{{LINKS_ROWS}}</div>
		</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 112 Monolith — after Brikken+Co (One Page Love)
page(112, 'monolith', 'family=Inter+Tight:wght@400..700', '#F3F2EF', '''
:root { --line: #D6D4CC; --focus: #2B36FF; --f-bg: #fff; --b-bg: #2B36FF; --b-text: #fff; --note: #666; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #F3F2EF; color: #111; font: 15px/1.5 "Inter Tight", system-ui, sans-serif; }
::selection { background: #2B36FF; color: #fff; }
h1 { font-size: clamp(3rem, 14.6vw, 15rem); font-weight: 500; line-height: 0.86; letter-spacing: -0.065em; white-space: nowrap; padding-top: 6px; } h1 sup { font-size: 0.16em; vertical-align: 3.6em; letter-spacing: 0; }
.scene { position: relative; height: min(64svh, 560px); display: grid; place-items: center; perspective: 1100px; }
.slab { position: relative; width: min(300px, 62vw); aspect-ratio: 3 / 4; transform-style: preserve-3d; transform: rotateX(8deg) rotateY(calc(-24deg + var(--sy, 0) * 80deg)); --d: 70px; }
.slab > * { position: absolute; inset: 0; }
.fr { background: linear-gradient(#D9DCFF, #8D97FF); transform: translateZ(calc(var(--d) / 2)); overflow: hidden; display: flex; align-items: flex-end; justify-content: center; } .fr img { width: 108%; max-width: none; }
.bk { background: #5A63E8; transform: rotateY(180deg) translateZ(calc(var(--d) / 2)); }
.sd { width: var(--d); left: calc(50% - var(--d) / 2); background: linear-gradient(#6E78F5, #2B36FF); } .sd.l { transform: rotateY(-90deg) translateZ(calc(min(300px, 62vw) / 2)); } .sd.r { transform: rotateY(90deg) translateZ(calc(min(300px, 62vw) / 2)); }
.tp2 { height: var(--d); top: calc(50% - var(--d) / 2); background: #B9C0FF; transform: rotateX(90deg) translateZ(calc(min(300px, 62vw) * 2 / 3)); }
.shadow { position: absolute; bottom: 4%; width: min(360px, 70vw); height: 34px; border-radius: 50%; background: radial-gradient(rgb(0 0 0 / 0.35), transparent 70%); }
.low { display: grid; gap: 18px 48px; align-items: end; padding-bottom: 8px; }
.low p { max-width: 26em; font-size: 1.1rem; font-weight: 500; line-height: 1.25; } .field { gap: 0; }
@media (prefers-reduced-motion: no-preference) { .slab { animation: sw 9s ease-in-out infinite alternate; } @keyframes sw { from { rotate: y -10deg; } to { rotate: y 26deg; } } }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">
	<h1 data-split="chars" style="--stag:28ms">Mostafa<sup data-keep>AI+Cloud</sup></h1>
	<main>
		<div class="scene" aria-hidden="true"><div class="shadow"></div><div class="slab"><div class="fr">{{IMG}}</div><div class="bk"></div><div class="sd l"></div><div class="sd r"></div><div class="tp2"></div></div></div>
		<div class="low"><p data-reveal>We teach ambitious ideas into plain understanding. Mostafa Saher, technical instructor: AI and cloud, one clear step at a time.</p><div data-reveal style="--i:1">{{FORM}}</div></div>
	</main>
</div>''' + MORE, "document.documentElement.setAttribute('data-sy', ''); const set = () => document.documentElement.style.setProperty('--sy', (scrollY / Math.max(1, document.documentElement.scrollHeight - innerHeight)).toFixed(4)); addEventListener('scroll', set, { passive: true }); set();")

# 113 Changelog — after Tiny Computer Co. (One Page Love)
page(113, 'changelog', 'family=Newsreader:opsz,wght@6..72,400&family=Geist+Mono:wght@400;500&family=Geist:wght@400;500', '#FFFFFF', '''
:root { --line: #E6E6E2; --focus: #111; --f-bg: #F5F5F2; --b-bg: #111; --b-text: #fff; --note: #777; --f-radius: 6px; --b-radius: 3px; --f-pad: 4px; --w: 760px; }
body { background: #fff; color: #171717; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #111; color: #fff; }
.mono { font: 400 0.78rem/1.6 "Geist Mono", monospace; color: #777; }
h1 { margin-top: clamp(24px, 8vh, 80px); font: 400 clamp(2.4rem, 1.4rem + 3.6vw, 4rem)/1.02 "Newsreader", serif; letter-spacing: -0.025em; }
.sub { margin: 10px 0 0; } .sub .fx-caret::after { height: 1em; }
.shots { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-top: 28px; }
.shots div { aspect-ratio: 1; overflow: hidden; background: var(--c); } .shots img { width: 150%; max-width: none; margin: 4% 0 0 -25%; filter: var(--f, none); }
.intro { margin-top: 24px; max-width: 36em; }
.join { margin-top: 20px; max-width: 460px; }
h2 { margin: 48px 0 6px; font: 500 0.78rem "Geist Mono", monospace; letter-spacing: 0.06em; text-transform: uppercase; color: #777; }
.log li { display: grid; grid-template-columns: 16px minmax(0, 1fr) auto; gap: 10px; align-items: baseline; padding-block: 9px; border-bottom: 1px solid var(--line); }
.log li::before { content: "+"; font-family: "Geist Mono", monospace; color: #1FA971; } .log li.fix::before { content: "~"; color: #D97706; }
.log a { text-decoration: underline; text-decoration-color: #CFCFCB; text-underline-offset: 3px; }
.fx:not(.fx-rm) .log:not(.in) li { opacity: 0; translate: -10px 0; } .fx .log.in li { transition: opacity 500ms ease calc(var(--k) * 70ms), translate 500ms var(--ease-out) calc(var(--k) * 70ms); }
''', '''
<div class="wrap">{{TOP}}
	<main>
		<h1 data-split data-fx="blur">Useful lessons, well explained.</h1>
		<p class="mono sub">A small, independent classroom. <span data-type="AI and cloud, one clear step at a time.|Notes from after class, by email." data-delay="900"></span></p>
		<div class="shots" data-reveal><div style="--c:#E7E3D8">{{IMG}}</div><div style="--c:#111;--f:grayscale(1) contrast(1.2)">{{IMG}}</div><div style="--c:#CFE0FF">{{IMG}}</div><div style="--c:#F2B84B;--f:sepia(0.6)">{{IMG}}</div></div>
		<p class="intro" data-reveal><b>Mostafa Saher</b> is a technical instructor. {{INTRO}}</p>
		<div class="join" data-reveal>{{FORM}}</div>
		<h2>Changelog</h2>
		<ul class="log" data-inview>
			<li style="--k:0"><span>Started writing down the after-class questions</span><span class="mono">v1.0</span></li>
			<li style="--k:1"><span>Added Thoughts: what students get stuck on, and the explanation that made it click</span><span class="mono">notes</span></li>
			<li style="--k:2"><span>Added Opinions: where I stand on new models, cloud services and the hype</span><span class="mono">takes</span></li>
			<li style="--k:3"><span>Added Resources: labs, docs, courses and tools I actually use</span><span class="mono">links</span></li>
			<li class="fix" style="--k:4"><span>Removed filler and recycled press releases</span><span class="mono">fix</span></li>
		</ul>
		<h2>Elsewhere</h2>
		<ul class="log" data-inview>
			<li style="--k:0"><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a><span class="mono">Mostafa Abuelnoor</span></li>
			<li style="--k:1"><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a><span class="mono">@MostafaAbuelnoor</span></li>
			<li style="--k:2"><a href="mailto:mostafasaher@gmail.com">Email</a><span class="mono">mostafasaher@gmail.com</span></li>
		</ul>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 114 Halftone — after OhhMyDesign (One Page Love)
page(114, 'halftone', 'family=Anton&family=Geist:wght@400;500', '#3E8EEA', '''
:root { --line: #D9E3F2; --focus: #E5341D; --f-bg: #fff; --b-bg: #E5341D; --b-text: #fff; --note: #5E6B80; --f-radius: 10px; --b-radius: 6px; }
body { background: #fff; color: #10182B; font: 15px/1.55 "Geist", system-ui, sans-serif; }
::selection { background: #E5341D; color: #fff; }
.sky { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto auto 1fr; overflow: hidden; background: linear-gradient(#2F7FE3, #7DB6F5 70%, #CFE5FB); text-align: center; }
.top { color: #fff; }
h1 { margin: clamp(8px, 3vh, 32px) auto 0; max-width: 8em; font: 400 clamp(3.4rem, 1rem + 14vw, 12rem)/0.86 "Anton", sans-serif; text-transform: uppercase; color: #E5341D; -webkit-mask-image: radial-gradient(circle at center, #000 var(--dot, 46%), transparent calc(var(--dot, 46%) + 6%)); mask-image: radial-gradient(circle at center, #000 var(--dot, 46%), transparent calc(var(--dot, 46%) + 6%)); -webkit-mask-size: 9px 9px; mask-size: 9px 9px; }
@property --dot { syntax: "<percentage>"; inherits: false; initial-value: 46%; }
@media (prefers-reduced-motion: no-preference) { h1 { animation: half 4.5s ease-in-out infinite alternate; } @keyframes half { from { --dot: 22%; } to { --dot: 62%; } } }
.ask { max-width: 440px; margin: 20px auto 0; text-align: left; position: relative; z-index: 3; } .ask .note { text-align: center; color: #10182B; }
.sky figure { position: relative; z-index: 2; align-self: end; justify-self: center; width: min(300px, 66%); margin-top: 16px; }
.frame { position: absolute; z-index: 1; left: 50%; bottom: -2%; width: min(560px, 92%); aspect-ratio: 16 / 9; margin-left: calc(min(560px, 92%) / -2); border: 4px solid #fff; border-radius: 14px; background: #10182B; box-shadow: 0 30px 60px -30px #000; }
''' + MORECSS, '''
<div class="sky"><div class="wrap">{{TOP}}</div>
	<div class="wrap"><h1 data-reveal="scale">Impossible to confuse.</h1><div class="ask" data-reveal style="--wait:500ms">{{FORM}}</div></div>
	<div class="frame" data-par="8"></div><figure data-reveal style="--wait:300ms" data-par="-10">{{IMG}}</figure>
</div>
<section class="wrap more"><div data-reveal><p style="margin-bottom:18px">I’m Mostafa Saher. I teach AI and cloud, one clear step at a time. {{INTRO}}</p>{{LINKS_INLINE}}</div><div data-reveal style="--i:1">{{TOPICS_UL}}</div></section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 115 Sunburst — after Frontend Supply (One Page Love)
page(115, 'sunburst', 'family=Figtree:wght@400..700', '#FFFFFF', '''
:root { --line: #E7E7E7; --focus: #111; --f-bg: #F3F3F3; --b-bg: #111; --b-text: #fff; --note: #777; --f-radius: 999px; --b-radius: 999px; --w: 760px; }
body { background: #fff; color: #111; font: 16px/1.55 "Figtree", system-ui, sans-serif; text-align: center; }
::selection { background: #111; color: #fff; }
.burst { position: relative; width: min(340px, 78vw); aspect-ratio: 1; margin: clamp(10px, 4vh, 40px) auto 0; }
.burst i { position: absolute; left: 50%; top: 50%; width: 3px; height: 50%; margin-left: -1.5px; transform-origin: 50% 0; rotate: calc(var(--k) * 7.5deg); }
.burst i::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: var(--h, 34%); border-radius: 3px; background: #111; opacity: var(--o, 0.2); }
@media (prefers-reduced-motion: no-preference) { .burst i::after { animation: ray 2.4s ease-in-out infinite; animation-delay: calc(var(--k) * -50ms); } @keyframes ray { 0%, 100% { height: 18%; opacity: 0.15; } 50% { height: 58%; opacity: 1; } } }
.burst .face { position: absolute; inset: 31%; border-radius: 50%; background: #EDEDED; }
h1 { margin-top: 20px; font-size: clamp(1.8rem, 1.2rem + 2.4vw, 2.9rem); font-weight: 700; line-height: 1.08; letter-spacing: -0.035em; }
.grey { color: #9A9A9A; }
.signup { max-width: 430px; margin: 22px auto 0; text-align: left; } .note { text-align: center; }
.steps { margin-top: 72px; display: grid; gap: 30px; }
.steps p { font-size: clamp(1.3rem, 1rem + 1.4vw, 2rem); font-weight: 700; letter-spacing: -0.03em; line-height: 1.15; }
.tp { text-align: left; margin-top: 56px; } .li-inline { justify-content: center; margin-top: 30px; font-weight: 600; }
''', '''
<div class="wrap">{{TOP}}
	<main>
		<div class="burst" aria-hidden="true">''' + ''.join(f'<i style="--k:{k}"></i>' for k in range(48)) + '''<div class="face">{{IMG}}</div></div>
		<h1 data-split data-fx="blur">The instructor learners choose <span class="grey">when it has to make sense.</span></h1>
		<div data-reveal style="--wait:500ms">{{FORM}}</div>
		<div class="steps"><p data-reveal><span class="grey">Taught.</span><br>One clear step at a time.</p><p data-reveal><span class="grey">Written down.</span><br>What comes up after class.</p><p data-reveal><span class="grey">Sent.</span><br>By email, free.</p></div>
		{{TOPICS_UL}}
		{{LINKS_INLINE}}
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 116 Arcs — after Mammut Studios (One Page Love)
page(116, 'arcs', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800', '#D9E8FB', '''
:root { --line: #C6D8F0; --focus: #151B2E; --f-bg: #fff; --b-bg: #151B2E; --b-text: #fff; --note: #5C6880; --f-radius: 999px; --b-radius: 999px; }
body { background: #D9E8FB; color: #151B2E; font: 16px/1.55 "Bricolage Grotesque", system-ui, sans-serif; }
::selection { background: #151B2E; color: #D9E8FB; }
.land { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; text-align: center; }
.arc { position: absolute; bottom: -42%; width: 62vmax; aspect-ratio: 1; border-radius: 50%; background: var(--c); left: var(--x); transform-origin: 50% 100%; }
.fx:not(.fx-rm) .land:not(.in) .arc { translate: 0 70%; } .fx .land.in .arc { transition: translate 1400ms var(--ease-out) calc(var(--k) * 160ms); }
.land > .wrap { position: relative; z-index: 3; }
h1 { margin: clamp(10px, 5vh, 56px) auto 0; max-width: 10em; font-size: clamp(2.4rem, 1.2rem + 5vw, 5.4rem); font-weight: 800; line-height: 0.95; letter-spacing: -0.045em; }
.land p.s { max-width: 30em; margin: 16px auto 0; color: #45506A; }
.signup { max-width: 430px; margin: 22px auto 0; text-align: left; } .note { text-align: center; }
.land figure { position: absolute; z-index: 2; left: 50%; bottom: 0; width: min(300px, 62%); margin-left: calc(min(300px, 62%) / -2); }
@media (max-height: 760px) { .land figure { display: none; } }
''' + MORECSS, '''
<div class="land" data-inview><i class="arc" style="--c:#EEF5FE;--x:-22vmax;--k:0"></i><i class="arc" style="--c:#F7FAFF;--x:14vmax;--k:1"></i><i class="arc" style="--c:#fff;--x:52vmax;--k:2"></i>
	<div class="wrap">{{TOP}}</div>
	<main class="wrap"><h1 data-split>Built to explain &amp; designed to stick.</h1><p class="s" data-reveal style="--wait:500ms">I’m Mostafa Saher, a technical instructor. AI and cloud, one clear step at a time.</p><div data-reveal style="--wait:650ms">{{FORM}}</div></main>
	<figure data-reveal style="--wait:800ms">{{IMG}}</figure>
</div>''' + MORE)

# 117 Contact sheet — after Amanda Guo (One Page Love)
page(117, 'contact-sheet', 'family=Geist+Mono:wght@400;500&family=Geist:wght@400..600', '#121212', '''
:root { color-scheme: dark; --line: #2B2B2B; --focus: #FFB000; --f-bg: #1B1B1B; --f-text: #F2F0EA; --f-ph: #99968E; --f-border: 1px solid #333; --b-bg: #FFB000; --b-text: #121212; --note: #99968E; --err: #FF9B8F; --f-radius: 4px; --b-radius: 2px; --f-pad: 4px; }
body { background: #121212; color: #F2F0EA; font: 15px/1.55 "Geist", system-ui, sans-serif; }
::selection { background: #FFB000; color: #121212; }
.mono { font: 500 0.72rem "Geist Mono", monospace; letter-spacing: 0.08em; text-transform: uppercase; color: #FFB000; }
.sheet { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; padding: 26px 10px; background: #0A0A0A repeating-linear-gradient(90deg, #2A2A2A 0 12px, transparent 12px 26px) 0 6px / 100% 12px no-repeat, #0A0A0A; border-block: 1px solid #2B2B2B; position: relative; }
.sheet::after { content: ""; position: absolute; left: 0; right: 0; bottom: 6px; height: 12px; background: repeating-linear-gradient(90deg, #2A2A2A 0 12px, transparent 12px 26px); }
.fr { position: relative; aspect-ratio: 4 / 3; overflow: hidden; background: var(--c, #3A3A3A); outline: 2px solid transparent; transition: outline-color 300ms ease; }
.fr img { position: absolute; width: var(--z, 120%); max-width: none; left: var(--l, -10%); top: var(--t, 2%); filter: var(--f, grayscale(1) contrast(1.1)); transition: filter 400ms ease, scale 600ms var(--ease-out); }
.fr b { position: absolute; left: 6px; bottom: 4px; font: 500 0.68rem "Geist Mono", monospace; color: #FFB000; }
.fr.on { outline-color: #E0241B; } .fr.on img { filter: none; scale: 1.05; }
.fr.on::after { content: ""; position: absolute; inset: 8%; border: 2px solid #E0241B; border-radius: 50%; rotate: -8deg; }
.txt { display: grid; gap: 22px 56px; align-items: end; padding-block: 36px 0; }
h1 { font-size: clamp(2rem, 1.2rem + 3.4vw, 3.8rem); font-weight: 600; line-height: 1; letter-spacing: -0.04em; margin-top: 10px; }
@media (min-width: 860px) { .sheet { grid-template-columns: repeat(6, 1fr); } .txt { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}</div>
<main>
	<div class="sheet" id="sheet" aria-hidden="true">''' + ''.join(f'<div class="fr" style="--z:{z}%;--l:{l}%;--t:{t}%;--c:{c}">{{{{IMG}}}}<b>{n:02d}A</b></div>' for n,(z,l,t,c) in enumerate([(120,-10,2,'#3A3A3A'),(210,-55,-6,'#2E3A4A'),(150,-25,0,'#4A3A2E'),(260,-80,-18,'#333'),(130,-2,4,'#2E4A3A'),(180,-40,-4,'#4A2E3A'),(300,-98,-30,'#3A3A3A'),(140,-30,6,'#2E3A4A'),(230,-66,-10,'#4A3A2E'),(120,-4,0,'#333'),(200,-50,-2,'#2E4A3A'),(160,-30,2,'#4A2E3A')],1)) + '''</div>
	<div class="wrap txt"><div><span class="mono">Roll 01 · Mostafa Saher · technical instructor</span><h1 data-split>{{H}}</h1></div><div data-reveal>{{FORM}}</div></div>
</main>''' + MORE, '''
const fr = FX.$$('#sheet .fr'); let i = 0; fr[0].classList.add('on'); if (FX.RM) return;
setInterval(() => { fr[i].classList.remove('on'); i = (i + 1 + Math.floor(Math.random() * 4)) % fr.length; fr[i].classList.add('on'); }, 1300);
''')

# 118 Title list — after Samuel Räikkönen (One Page Love)
page(118, 'title-list', 'family=Gloock&family=Geist:wght@400;500', '#0D1B2A', '''
:root { --bgc: #0D1B2A; --line: rgb(255 255 255 / 0.22); --focus: #fff; --f-bg: rgb(255 255 255 / 0.1); --f-text: #fff; --f-ph: #C5CBD6; --f-border: 1px solid rgb(255 255 255 / 0.25); --b-bg: #fff; --b-text: #0D1B2A; --note: #C5CBD6; --err: #FFD2CB; --f-radius: 999px; --b-radius: 999px; }
body { background: var(--bgc); color: #fff; font: 15px/1.6 "Geist", system-ui, sans-serif; transition: background-color 700ms ease; text-align: center; }
::selection { background: #fff; color: #0D1B2A; }
.stage { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; overflow: hidden; }
.stage figure { position: absolute; left: 50%; bottom: 0; width: min(420px, 84%); margin-left: calc(min(420px, 84%) / -2); opacity: 0.32; filter: grayscale(1); -webkit-mask-image: linear-gradient(#000 60%, transparent); mask-image: linear-gradient(#000 60%, transparent); }
.stage > .wrap { position: relative; z-index: 2; }
.list { align-self: center; padding-block: 10px; }
.list li { font: 400 clamp(1.9rem, 1.1rem + 4.4vw, 4.6rem)/1.12 "Gloock", serif; letter-spacing: -0.015em; opacity: 0.28; transition: opacity 350ms ease, letter-spacing 500ms var(--ease-out); cursor: default; }
.list li.on { opacity: 1; letter-spacing: 0; }
.cap { min-height: 3.2em; max-width: 30em; margin: 10px auto 0; color: #D5DAE3; }
.signup { max-width: 430px; margin: 0 auto 26px; text-align: left; } .note { text-align: center; }
''' + MORECSS, '''
<div class="stage"><div class="wrap">{{TOP}}</div>
	<figure>{{IMG}}</figure>
	<main class="wrap list">
		<h1 class="sr">Mostafa Saher teaches AI and cloud, one clear step at a time</h1>
		<ul id="list">
			<li data-c="#0D1B2A" data-t="Mostafa Saher. Technical instructor.">The instructor</li>
			<li data-c="#3A1D5C" data-t="AI and cloud, one clear step at a time.">The subjects</li>
			<li data-c="#7A2E1F" data-t="Notes from the classroom: what students get stuck on, and the explanation that made it click.">Thoughts</li>
			<li data-c="#14523F" data-t="Where I stand on new models, cloud services and the hype around them.">Opinions</li>
			<li data-c="#1B3F8A" data-t="The labs, docs, courses and tools I actually use, each with a line on why.">Resources</li>
			<li data-c="#5A4A12" data-t="All of it, by email. Sign up below.">The newsletter</li>
		</ul>
		<p class="cap" id="cap" aria-live="polite"></p>
	</main>
	<div class="wrap" data-reveal>{{FORM}}</div>
</div>''' + MORE, '''
const items = FX.$$('#list li'), cap = document.getElementById('cap'); let cur = -1, auto = true, timer;
const show = (i) => { if (i === cur) return; cur = i; items.forEach((el, k) => el.classList.toggle('on', k === i)); document.documentElement.style.setProperty('--bgc', items[i].dataset.c); cap.textContent = items[i].dataset.t; };
items.forEach((el, i) => { el.addEventListener('pointerenter', () => { auto = false; show(i); }); el.addEventListener('click', () => { auto = false; show(i); }); });
show(0); if (!FX.RM) timer = setInterval(() => { if (auto) show((cur + 1) % items.length); }, 2400);
''')

# 119 Conveyor — after Scout Graphics (One Page Love)
page(119, 'conveyor', 'family=Young+Serif&family=Geist:wght@400;500', '#F4F1EA', '''
:root { --line: #DDD8CA; --focus: #1E1D19; --f-bg: #fff; --f-border: 1px solid #D5CFBF; --b-bg: #1E1D19; --b-text: #fff; --note: #726E60; --f-radius: 999px; --b-radius: 999px; }
body { background: #F4F1EA; color: #1E1D19; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #1E1D19; color: #F4F1EA; }
.stage { min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; overflow: hidden; }
.mid { align-self: center; text-align: center; padding-block: 16px; }
.face { width: 74px; height: 74px; margin: 0 auto 18px; border: 1.5px solid #1E1D19; background: #E8E2D2; }
h1 { max-width: 14em; margin-inline: auto; font: 400 clamp(1.7rem, 1.1rem + 2.2vw, 2.8rem)/1.2 "Young Serif", serif; }
.signup { max-width: 430px; margin: 22px auto 0; text-align: left; } .note { text-align: center; }
.belt { padding-block: 24px 0; --dur: 40s; }
.belt .cd { flex: none; width: clamp(150px, 20vw, 240px); aspect-ratio: 4 / 5; margin-inline: 10px; background: var(--c); overflow: hidden; display: flex; align-items: flex-end; justify-content: center; rotate: var(--r); translate: 0 var(--y); position: relative; }
.belt .cd img { width: 116%; max-width: none; filter: var(--f, none); }
.belt .cd.tx { align-items: center; padding: 16px; font: 400 clamp(1.2rem, 1rem + 1vw, 1.8rem)/1.1 "Young Serif", serif; white-space: normal; text-align: center; }
.belt:hover .fx-track { animation-play-state: paused; }
''' + MORECSS, '''
<div class="stage"><div class="wrap">{{TOP}}</div>
	<main class="wrap mid"><div class="face" data-reveal="scale">{{IMG}}</div><h1 data-split data-fx="blur">Mostafa Saher is an independent instructor teaching AI and cloud, one clear step at a time.</h1><div data-reveal style="--wait:600ms">{{FORM}}</div></main>
	<div class="belt" data-marquee aria-hidden="true">
		<div class="cd" style="--c:#C9D9F2;--r:-3deg;--y:12px">{{IMG}}</div><div class="cd tx" style="--c:#F2B84B;--r:2deg;--y:30px">Thoughts</div><div class="cd" style="--c:#1E1D19;--r:4deg;--y:4px;--f:grayscale(1)">{{IMG}}</div><div class="cd tx" style="--c:#B8E6C8;--r:-2deg;--y:22px">Opinions</div><div class="cd" style="--c:#F4A6A0;--r:-4deg;--y:34px;--f:sepia(0.4)">{{IMG}}</div><div class="cd tx" style="--c:#fff;--r:3deg;--y:8px">Resources</div>
	</div>
</div>''' + MORE)

# 120 Catch me — after READYMAGIC / Rmc.Studio (One Page Love)
page(120, 'catch-me', 'family=Host+Grotesk:wght@400..800', '#161616', '''
:root { color-scheme: dark; --line: #2C2C2C; --focus: #FF8CF0; --f-bg: #222; --f-text: #F5F5F5; --f-ph: #9B9B9B; --f-border: 1px solid #353535; --b-bg: #FF8CF0; --b-text: #161616; --note: #9B9B9B; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #161616; color: #F5F5F5; font: 16px/1.5 "Host Grotesk", system-ui, sans-serif; }
::selection { background: #FF8CF0; color: #161616; }
.play { position: relative; min-height: calc(100svh - 70px); display: grid; align-content: center; gap: 26px; padding-block: 16px 40px; }
h1 { font-size: clamp(2.3rem, 1.2rem + 5.2vw, 5.6rem); font-weight: 500; line-height: 0.98; letter-spacing: -0.045em; max-width: 12em; }
h1 .hd { display: inline-block; vertical-align: -0.12em; width: 0.9em; height: 0.9em; border-radius: 50%; background: #3A3A3A; overflow: hidden; margin-inline: 0.06em; rotate: var(--r); } h1 .hd img { width: 170%; max-width: none; margin: 4% 0 0 -36%; }
.h2 { padding-left: clamp(0px, 8vw, 140px); }
.runner { position: absolute; left: 62%; top: 16%; z-index: 4; padding: 10px 18px; border: 0; border-radius: 999px; background: #FF8CF0; color: #161616; font: inherit; font-weight: 700; cursor: pointer; rotate: -6deg; transition: translate 450ms var(--spring), rotate 450ms var(--spring); white-space: nowrap; }
.row2 { display: grid; gap: 18px 48px; align-items: end; }
.row2 p { max-width: 28em; color: #B8B8B8; }
.tally { font-variant-numeric: tabular-nums; color: #FF8CF0; font-weight: 600; }
@media (min-width: 860px) { .row2 { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="play" id="play">
		<button class="runner" id="runner" type="button">Catch me :)</button>
		<h1><span data-split>I’m <span class="hd" style="--r:-8deg" data-keep>{{IMG}}</span> Mostafa, an AI and cloud instructor.</span><br><span class="h2" data-split style="--wait:400ms;display:block">I teach <span class="hd" style="--r:10deg" data-keep>{{IMG}}</span> one clear step at a time.</span></h1>
		<div class="row2"><p data-reveal>The pink button runs away from your cursor (tap it on a phone). The sign-up stays put. <span class="tally" id="tally">Caught 0 times.</span></p><div data-reveal style="--i:1">{{FORM}}</div></div>
	</main>
</div>''' + MORE, '''
const btn = document.getElementById('runner'), play = document.getElementById('play'), tally = document.getElementById('tally'); let x = 0, y = 0, n = 0;
const jump = () => { const r = play.getBoundingClientRect(), b = btn.getBoundingClientRect(); const bx = b.left - x - r.left, by = b.top - y - r.top; x = Math.random() * (r.width - b.width) - bx; y = Math.random() * (r.height * 0.6) - by; btn.style.translate = x.toFixed(0) + 'px ' + y.toFixed(0) + 'px'; btn.style.rotate = (Math.random() * 30 - 15).toFixed(0) + 'deg'; };
if (FX.FINE && !FX.RM) FX.onTick(() => { const b = btn.getBoundingClientRect(); if (FX.ptr.moved && Math.hypot(FX.ptr.x - (b.left + b.width / 2), FX.ptr.y - (b.top + b.height / 2)) < 110) jump(); });
btn.addEventListener('click', () => { n++; tally.textContent = 'Caught ' + n + (n === 1 ? ' time.' : ' times.'); btn.textContent = ['Nice!', 'Again?', 'Too slow :)', 'Okay, okay', 'Catch me :)'][n % 5]; jump(); });
''')
print('d2 done')
