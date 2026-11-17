from lib2 import page

# 51 Kinetic letters
page(51, 'kinetic-letters', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800', '#F2EFE8', '''
:root { --line: #D9D4C7; --focus: #FF4B1F; --f-bg: #fff; --b-bg: #15140F; --b-text: #fff; --note: #6A665A; --f-radius: 999px; --b-radius: 999px; }
body { background: #F2EFE8; color: #15140F; font: 16px/1.5 "Bricolage Grotesque", system-ui, sans-serif; }
::selection { background: #FF4B1F; color: #fff; }
.hero { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; overflow: hidden; }
h1 { align-self: center; font-size: clamp(4.6rem, 1rem + 19vw, 17rem); font-weight: 800; line-height: 0.8; letter-spacing: -0.06em; --stag: 60ms; --dur: 1100ms; }
h1 span.l2 { display: block; color: #FF4B1F; padding-left: 0.5em; }
.hero figure { position: absolute; right: 3%; bottom: 0; width: min(48%, 430px); z-index: 1; }
.low { position: relative; z-index: 2; display: grid; gap: 16px 40px; padding-bottom: 26px; align-items: end; }
.low p { max-width: 24em; font-size: 1.2rem; font-weight: 500; line-height: 1.25; }
.strip { padding-block: 14px; background: #15140F; color: #F2EFE8; font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em; --dur: 26s; }
.strip i { font-style: normal; color: #FF4B1F; margin-inline: 0.6em; }
.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; }
@media (min-width: 860px) { .low { grid-template-columns: minmax(0, 1fr) 420px minmax(0, 0.9fr); } .more { grid-template-columns: 1fr 1fr; } }
''', '''
<header class="hero"><div class="wrap">{{TOP}}</div>
	<h1 class="wrap" data-split="chars">Mostafa <span class="l2">Saher</span></h1>
	<figure data-wipe style="--wait:500ms">{{IMG}}</figure>
	<div class="wrap low"><p data-reveal style="--wait:700ms">{{H}}</p><div data-reveal style="--wait:850ms">{{FORM}}</div></div>
</header>
<div class="strip" data-marquee>Thoughts<i>✳</i>Opinions<i>✳</i>Resources<i>✳</i>One clear step at a time<i>✳</i></div>
<main class="wrap more"><p data-reveal>{{INTRO}}</p><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></main>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 52 Starfield
page(52, 'starfield', 'family=Sora:wght@300..600', '#000000', '''
:root { color-scheme: dark; --line: #24242C; --focus: #B9C8FF; --f-bg: rgb(255 255 255 / 0.08); --f-text: #fff; --f-ph: #A3A6B8; --f-border: 1px solid rgb(255 255 255 / 0.18); --b-bg: #fff; --b-text: #000; --note: #A3A6B8; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #000; color: #fff; font: 15px/1.6 "Sora", system-ui, sans-serif; }
::selection { background: #B9C8FF; color: #000; }
.space { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; text-align: center; }
.space canvas { position: absolute; inset: 0; color: #DCE4FF; }
.space > * { position: relative; }
.mid { align-self: center; padding-block: 16px 0; }
h1 { max-width: 14em; margin-inline: auto; font-size: clamp(2rem, 1.1rem + 3.6vw, 4rem); font-weight: 300; line-height: 1.08; letter-spacing: -0.035em; --stag: 70ms; --dur: 1300ms; }
h1 em { font-style: normal; font-weight: 600; }
.signup { max-width: 430px; margin: 28px auto 0; text-align: left; } .note { text-align: center; }
.mid figure { width: min(300px, 62%); margin: 28px auto 0; }
.mid img { filter: drop-shadow(0 0 2px rgb(200 215 255 / 0.7)) drop-shadow(0 0 40px rgb(120 150 255 / 0.35)); -webkit-mask-image: linear-gradient(#000 70%, transparent); mask-image: linear-gradient(#000 70%, transparent); }
.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; }
@media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }
''', '''
<div class="space"><canvas data-canvas="stars"></canvas>
	<div class="wrap">{{TOP}}</div>
	<main class="wrap mid">
		<h1 data-split data-fx="blur">I teach <em>AI and cloud</em>, one clear step at a time.</h1>
		<div data-reveal="fade" style="--wait:900ms">{{FORM}}</div>
		<figure data-reveal="scale" style="--wait:1100ms" data-par="14">{{IMG}}</figure>
	</main>
</div>
<section class="wrap more"><div data-reveal><p style="margin-bottom:18px;color:#B5B8C8">{{INTRO}}</p>{{LINKS_INLINE}}</div><div data-reveal style="--i:1">{{TOPICS_UL}}</div></section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 53 Constellation
page(53, 'constellation', 'family=Manrope:wght@400..800', '#080E2B', '''
:root { color-scheme: dark; --line: #1E2A5C; --focus: #7C9BFF; --f-bg: #101A45; --f-text: #F1F4FF; --f-ph: #93A0D1; --f-border: 1px solid #263474; --b-bg: #7C9BFF; --b-text: #060B22; --note: #93A0D1; --err: #FF9B8F; --f-radius: 12px; --b-radius: 8px; }
body { background: #080E2B; color: #F1F4FF; font: 16px/1.6 "Manrope", system-ui, sans-serif; }
::selection { background: #7C9BFF; color: #060B22; }
.net { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; }
.net canvas { position: absolute; inset: 0; color: #6F8CFF; }
.net > * { position: relative; }
.hero { display: grid; gap: 12px 40px; align-items: end; }
.copy { align-self: center; padding-block: 16px 36px; }
h1 { font-size: clamp(2.3rem, 1.2rem + 4vw, 4.6rem); font-weight: 800; line-height: 1; letter-spacing: -0.045em; max-width: 11em; }
.copy p { margin: 18px 0 24px; max-width: 30em; color: #AEB9E6; }
.signup { max-width: 440px; }
.shot { justify-self: center; width: min(320px, 72%); }
.shot img { filter: drop-shadow(0 0 1.5px rgb(170 190 255 / 0.6)); }
.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; }
@media (min-width: 900px) { .hero { grid-template-columns: 1.2fr 0.8fr; } .shot { width: min(100%, 460px); justify-self: end; } .more { grid-template-columns: 1fr 1fr; } }
''', '''
<div class="net"><canvas data-canvas="net"></canvas>
	<div class="wrap">{{TOP}}</div>
	<main class="wrap hero">
		<div class="copy"><h1 data-split>Connecting the dots in AI and cloud.</h1><p data-reveal style="--wait:500ms">I’m Mostafa Saher, a technical instructor. I teach one clear step at a time, and my newsletter carries what comes up after class.</p><div data-reveal style="--wait:650ms">{{FORM}}</div></div>
		<div class="shot" data-reveal="scale" style="--wait:400ms" data-par="-18">{{IMG}}</div>
	</main>
</div>
<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 54 Wave lines
page(54, 'wave-lines', 'family=Figtree:wght@400..800', '#FFFFFF', '''
:root { --blue: #1A56F0; --line: #E3E7F0; --focus: var(--blue); --f-bg: #F2F4F9; --b-bg: var(--blue); --b-text: #fff; --note: #667; --f-radius: 14px; --b-radius: 10px; }
body { background: #fff; color: #0F1320; font: 16px/1.55 "Figtree", system-ui, sans-serif; }
::selection { background: var(--blue); color: #fff; }
.hero { text-align: center; padding-top: clamp(16px, 5vh, 48px); }
h1 { max-width: 12em; margin-inline: auto; font-size: clamp(2.4rem, 1.3rem + 4.4vw, 5rem); font-weight: 800; line-height: 0.98; letter-spacing: -0.045em; }
h1 em { font-style: normal; color: var(--blue); }
.sea { position: relative; height: clamp(320px, 52vh, 520px); margin-top: 8px; }
.sea canvas { position: absolute; inset: 0; color: var(--blue); }
.sea figure { position: absolute; left: 50%; bottom: 0; height: 96%; aspect-ratio: 1100 / 1433; translate: -50% 0; }
.sea figure img { height: 100%; width: auto; max-width: none; }
.ask { position: relative; max-width: 460px; margin: -36px auto 0; padding: 10px; border-radius: 22px; background: #fff; box-shadow: 0 20px 50px -20px rgb(26 86 240 / 0.45); text-align: left; }
.ask .note { text-align: center; padding-bottom: 4px; }
.more { display: grid; gap: 28px 56px; padding-block: 56px 8px; }
@media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }
''', '''
<div class="wrap">{{TOP}}</div>
<main>
	<section class="hero"><h1 class="wrap" data-split data-fx="flip">AI and cloud, in <em>waves</em> you can follow.</h1>
		<div class="sea"><canvas data-canvas="waves"></canvas><figure data-wipe style="--wait:400ms">{{IMG}}</figure></div>
		<div class="wrap"><div class="ask" data-reveal style="--wait:700ms">{{FORM}}</div></div>
	</section>
	<section class="wrap more"><div data-reveal><p style="margin-bottom:18px">I’m Mostafa Saher, a technical instructor. {{INTRO}}</p>{{LINKS_INLINE}}</div><div data-reveal style="--i:1">{{TOPICS_UL}}</div></section>
</main>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 55 Dot grid
page(55, 'dot-grid', 'family=Inter+Tight:wght@400..700', '#ECECEA', '''
:root { --line: #D2D2CE; --focus: #111; --f-bg: #F4F4F2; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 10px; --b-radius: 6px; }
body { background: #ECECEA; color: #111; font: 16px/1.5 "Inter Tight", system-ui, sans-serif; }
::selection { background: #111; color: #ECECEA; }
.field-bg { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; overflow: hidden; }
.field-bg canvas { position: absolute; inset: 0; color: #111; }
.field-bg > * { position: relative; }
h1 { align-self: center; max-width: 9em; font-size: clamp(3rem, 1.4rem + 7.6vw, 8rem); font-weight: 600; line-height: 0.9; letter-spacing: -0.055em; }
.low { display: grid; gap: 16px 40px; align-items: end; padding-bottom: 24px; }
.cardx { max-width: 440px; padding: 18px; border-radius: 18px; background: #fff; box-shadow: 0 20px 44px -22px rgb(0 0 0 / 0.35); }
.cardx p { margin-bottom: 12px; font-weight: 500; }
.low figure { width: min(250px, 60%); justify-self: end; margin-bottom: -24px; }
.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; }
@media (min-width: 860px) { .low { grid-template-columns: 1fr auto; } .low figure { width: 330px; } .more { grid-template-columns: 1fr 1fr; } }
''', '''
<div class="field-bg"><canvas data-canvas="dots"></canvas>
	<div class="wrap">{{TOP}}</div>
	<h1 class="wrap" data-split data-fx="pop">Point by point. Step by step.</h1>
	<div class="wrap low"><div class="cardx" data-reveal style="--wait:600ms"><p>Mostafa Saher teaches AI and cloud, one clear step at a time.</p>{{FORM}}</div><figure data-reveal style="--wait:500ms" data-par="16">{{IMG}}</figure></div>
</div>
<section class="wrap more"><div data-reveal><p style="margin-bottom:18px">{{INTRO}}</p>{{LINKS_INLINE}}</div><div data-reveal style="--i:1">{{TOPICS_UL}}</div></section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 56 Flow field
page(56, 'flow-field', 'family=Young+Serif&family=Geist:wght@400;500', '#0D2A22', '''
:root { color-scheme: dark; --line: #1F4A3D; --focus: #A6E8C9; --f-bg: #12392E; --f-text: #F2EFE3; --f-ph: #8FB5A6; --f-border: 1px solid #25584A; --b-bg: #F2EFE3; --b-text: #0D2A22; --note: #8FB5A6; --err: #FFB3A6; --f-radius: 6px; --b-radius: 3px; --f-pad: 5px; }
body { background: #0D2A22; color: #F2EFE3; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #A6E8C9; color: #0D2A22; }
.stream { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; }
.stream canvas { position: absolute; inset: 0; color: #7FD3AE; }
.stream > * { position: relative; }
.hero { display: grid; gap: 28px 56px; align-items: center; padding-bottom: 36px; }
h1 { font: 400 clamp(2.4rem, 1.3rem + 4vw, 4.8rem)/1.02 "Young Serif", serif; letter-spacing: -0.02em; max-width: 10em; --stag: 80ms; }
.hero p { margin: 20px 0 22px; max-width: 30em; color: #B9D4C8; }
.signup { max-width: 440px; }
.frame { justify-self: center; width: min(320px, 78%); aspect-ratio: 4 / 5; border-radius: 200px 200px 8px 8px; background: #17473A; overflow: hidden; display: flex; align-items: flex-end; justify-content: center; }
.frame img { width: 112%; max-width: none; }
.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; }
@media (min-width: 900px) { .hero { grid-template-columns: 1.2fr 0.8fr; } .frame { width: 380px; justify-self: end; } .more { grid-template-columns: 1fr 1fr; } }
''', '''
<div class="stream"><canvas data-canvas="flow"></canvas>
	<div class="wrap">{{TOP}}</div>
	<main class="wrap hero">
		<div><h1 data-split>Follow the flow of an idea, one clear step at a time.</h1><p data-reveal style="--wait:700ms">I’m Mostafa Saher. I teach AI and cloud, and I write down what comes up after class.</p><div data-reveal style="--wait:850ms">{{FORM}}</div></div>
		<div class="frame" data-wipe style="--wait:300ms">{{IMG}}</div>
	</main>
</div>
<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 57 Marquee bands
page(57, 'marquee-bands', 'family=Archivo:wght@500..900', '#1D3BFF', '''
:root { --line: rgb(255 255 255 / 0.35); --focus: #fff; --f-bg: #fff; --b-bg: #0A0F2E; --b-text: #fff; --note: #D7DDFF; --err: #FFD9D2; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #1D3BFF; color: #fff; font: 16px/1.5 "Archivo", system-ui, sans-serif; }
::selection { background: #fff; color: #1D3BFF; }
.hero { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto auto 1fr auto; overflow: hidden; }
h1 { position: relative; z-index: 3; max-width: 9em; font-size: clamp(2.6rem, 1.4rem + 5vw, 5.6rem); font-weight: 900; line-height: 0.92; letter-spacing: -0.045em; text-transform: uppercase; }
.band { position: absolute; left: -10%; right: -10%; padding-block: 12px; font-size: clamp(1.4rem, 1rem + 2vw, 2.6rem); font-weight: 900; text-transform: uppercase; letter-spacing: -0.02em; }
.band i { font-style: normal; margin-inline: 0.7em; opacity: 0.5; }
.b1 { z-index: 1; top: 52%; background: #fff; color: #1D3BFF; rotate: -7deg; --dur: 24s; }
.b2 { z-index: 4; top: 64%; background: #0A0F2E; color: #fff; rotate: 5deg; --dur: 30s; --dir: reverse; }
.hero figure { position: absolute; z-index: 2; left: 50%; bottom: 0; height: 74%; aspect-ratio: 1100 / 1433; translate: -50% 0; }
.hero figure img { height: 100%; width: auto; max-width: none; }
.ask { position: relative; z-index: 5; max-width: 440px; padding-bottom: 24px; } .field { gap: 0; }
.more { background: #0A0F2E; } .more .inr { display: grid; gap: 28px 56px; padding-block: 48px 8px; }
@media (min-width: 860px) { .hero figure { left: auto; right: 6%; translate: none; height: 86%; } .more .inr { grid-template-columns: 1fr 1fr; } }
''', '''
<header class="hero"><div class="wrap" style="position:relative;z-index:5">{{TOP}}</div>
	<h1 class="wrap" data-split data-fx="drop">AI and cloud, one clear step at a time.</h1>
	<div></div>
	<div class="band b1" data-marquee>Thoughts<i>/</i>Opinions<i>/</i>Resources<i>/</i>After class<i>/</i></div>
	<figure data-reveal style="--wait:300ms">{{IMG}}</figure>
	<div class="band b2" data-marquee>Mostafa Saher<i>/</i>Technical instructor<i>/</i>Newsletter<i>/</i></div>
	<div class="wrap"><div class="ask" data-reveal style="--wait:700ms">{{FORM}}</div></div>
</header>
<section class="more"><div class="wrap inr"><div data-reveal><p style="margin-bottom:18px;color:#C7CEF5">{{INTRO}}</p>{{LINKS_INLINE}}</div><div data-reveal style="--i:1">{{TOPICS_UL}}</div></div><div class="wrap"><footer class="foot">{{FOOT}}</footer></div></section>
''')

# 58 Terminal
page(58, 'terminal', 'family=JetBrains+Mono:wght@400;700', '#0C0E11', '''
:root { color-scheme: dark; --green: #7CF29A; --line: #23272E; --focus: var(--green); --f-bg: #0C0E11; --f-text: #E8EAED; --f-ph: #7D8591; --f-border: 1px solid #2B3038; --b-bg: var(--green); --b-text: #06210E; --note: #7D8591; --err: #FF9B8F; --f-radius: 6px; --b-radius: 3px; --f-pad: 4px; --w: 860px; }
body { background: #0C0E11 radial-gradient(60% 50% at 50% 0%, #17202A, transparent); background-repeat: no-repeat; color: #E8EAED; font: 14px/1.7 "JetBrains Mono", ui-monospace, monospace; }
::selection { background: var(--green); color: #06210E; }
.win { margin-top: clamp(20px, 7vh, 72px); border: 1px solid #2B3038; border-radius: 12px; background: #12151A; box-shadow: 0 40px 80px -30px #000; overflow: hidden; }
.bar { display: flex; align-items: center; gap: 8px; padding: 10px 14px; border-bottom: 1px solid #23272E; color: #7D8591; font-size: 0.8rem; }
.bar i { width: 11px; height: 11px; border-radius: 50%; background: #2F353E; } .bar i:first-child { background: #FF6B5E; } .bar i:nth-child(2) { background: #F5BD4F; } .bar i:nth-child(3) { background: #5FCB5A; }
.bar .face { margin-left: auto; width: 22px; height: 22px; border-radius: 50%; background: #2F353E; }
.out { padding: 18px 18px 22px; min-height: 420px; }
.ln { white-space: pre-wrap; } .ln b { color: var(--green); font-weight: 400; } .ln.cmd::before { content: "$ "; color: #7D8591; } .ln.res { color: #AEB5BF; margin-bottom: 10px; }
.fx:not(.fx-rm) .ln, .fx:not(.fx-rm) .after { opacity: 0; } .fx .ln.show, .fx .after.show { opacity: 1; transition: opacity 250ms ease; }
.after { margin-top: 8px; max-width: 460px; }
.below { display: grid; gap: 28px 56px; padding-block: 44px 8px; }
@media (min-width: 820px) { .below { grid-template-columns: 1fr 1fr; } }
''', '''
<div class="wrap">
	<main class="win">
		<div class="bar"><i></i><i></i><i></i><span>mostafa@classroom: ~</span><div class="face">{{IMG}}</div></div>
		<div class="out" id="out">
			<h1 class="ln cmd" style="font:inherit">whoami</h1><p class="ln res">Mostafa Saher. Technical instructor.</p>
			<p class="ln cmd">cat teaches.txt</p><p class="ln res"><b>AI</b> and <b>cloud</b>, one clear step at a time.</p>
			<p class="ln cmd">tail -n 3 corridor.log</p><p class="ln res">"wait, so why does that work?"
"can you send me that link?"
"this finally makes sense."</p>
			<p class="ln cmd">./subscribe --free</p>
			<div class="after">{{FORM}}</div>
		</div>
	</main>
	<section class="below"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>
	<footer class="foot">{{FOOT}}</footer>
</div>
''', '''
const lines = FX.$$('#out .ln, #out .after'); if (FX.RM) return;
let i = 0; const next = () => { if (i >= lines.length) return; const el = lines[i++]; el.classList.add('show');
	if (el.classList.contains('cmd')) { const full = el.textContent; el.textContent = ''; let k = 0; const t = setInterval(() => { el.textContent = full.slice(0, ++k); if (k >= full.length) { clearInterval(t); setTimeout(next, 260); } }, 38); }
	else setTimeout(next, 340); };
setTimeout(next, 400);
''')

# 59 Word rotator
page(59, 'word-rotator', 'family=Gabarito:wght@400..900', '#F5F4EF', '''
:root { --line: #DCDAD0; --focus: #111; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #6B6A62; --f-radius: 999px; --b-radius: 999px; }
body { background: #F5F4EF; color: #111; font: 16px/1.5 "Gabarito", system-ui, sans-serif; }
::selection { background: #7C5CFF; color: #fff; }
.hero { min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; padding-bottom: 28px; }
h1 { align-self: center; font-size: clamp(3rem, 1.2rem + 9vw, 9rem); font-weight: 800; line-height: 0.95; letter-spacing: -0.05em; }
h1 .slot { display: inline-block; margin-top: 0.08em; padding: 0.02em 0.28em 0.08em; border-radius: 0.22em; background: #7C5CFF; color: #fff; overflow: hidden; vertical-align: bottom; transition: background-color 500ms ease; }
.low { display: grid; gap: 18px 40px; align-items: end; }
.me { display: flex; align-items: center; gap: 14px; max-width: 30em; font-size: 1.1rem; font-weight: 500; line-height: 1.3; }
.face { flex: none; width: 76px; height: 76px; border-radius: 50%; background: #E3DFD2; }
.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; border-top: 1px solid var(--line); }
@media (min-width: 860px) { .low { grid-template-columns: 1fr 440px; } .more { grid-template-columns: 1fr 1fr; } }
''', '''
<div class="wrap">
	<div class="hero">
		{{TOP}}
		<h1 data-reveal>I teach<br><span class="slot" id="slot" data-words="AI|cloud|the why|step by step" data-every="2000">AI</span></h1>
		<div class="low"><div class="me" data-reveal style="--i:2"><div class="face">{{IMG}}</div><p>I’m Mostafa Saher, a technical instructor. My newsletter carries what comes up after class.</p></div><div data-reveal style="--i:3">{{FORM}}</div></div>
	</div>
	<main class="more"><div data-reveal><p style="margin-bottom:18px">{{INTRO}}</p>{{LINKS_INLINE}}</div><div data-reveal style="--i:1">{{TOPICS_UL}}</div></main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''', '''
const slot = document.getElementById('slot'), cs = ['#7C5CFF', '#FF5A36', '#0FA968', '#1A56F0']; let k = 0;
if (!FX.RM) setInterval(() => { slot.style.backgroundColor = cs[++k % cs.length]; }, 2000);
''')

# 60 Decode
page(60, 'decode', 'family=JetBrains+Mono:wght@400;700', '#0A0A0A', '''
:root { color-scheme: dark; --line: #2A2A2A; --focus: #EDEDED; --f-bg: #0A0A0A; --f-text: #EDEDED; --f-ph: #8A8A8A; --f-border: 1px solid #3A3A3A; --b-bg: #EDEDED; --b-text: #0A0A0A; --note: #8A8A8A; --err: #FF9B8F; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #0A0A0A; color: #EDEDED; font: 13px/1.6 "JetBrains Mono", ui-monospace, monospace; text-transform: uppercase; letter-spacing: 0.04em; }
::selection { background: #EDEDED; color: #0A0A0A; }
.sheet { display: grid; grid-template-columns: 1fr; border: 1px solid var(--line); margin-block: 16px; }
.sheet > * { padding: 16px; border-bottom: 1px solid var(--line); }
.sheet > *:last-child { border-bottom: 0; }
.k { display: block; color: #8A8A8A; font-size: 0.72rem; margin-bottom: 8px; }
h1 { font-size: clamp(2rem, 1rem + 7vw, 6.6rem); font-weight: 700; line-height: 0.95; letter-spacing: -0.02em; overflow-wrap: anywhere; }
.pic { display: flex; align-items: flex-end; justify-content: center; min-height: 260px; padding-bottom: 0 !important; background: #111; }
.pic img { width: min(260px, 70%); filter: grayscale(1) contrast(1.15); }
.v { font-size: 1.05rem; }
.signup, .signup input { text-transform: none; letter-spacing: 0; } .field { gap: 0; }
.tp, .links { text-transform: none; letter-spacing: 0; font-size: 14px; }
.dot { display: inline-block; width: 8px; height: 8px; margin-right: 8px; border-radius: 50%; background: #5CF28A; }
@media (min-width: 860px) { .sheet { grid-template-columns: repeat(4, 1fr); } .sheet > * { border-right: 1px solid var(--line); } .s4 { grid-column: span 4; border-right: 0; } .s2 { grid-column: span 2; } .sheet > *:nth-child(5), .sheet > *:nth-child(7), .sheet > *:nth-child(9) { border-right: 0; } .pic { grid-row: span 2; } }
''', '''
<div class="wrap">
	<main class="sheet">
		<div class="s4"><span class="k">Name</span><h1 data-scramble>Mostafa Saher</h1></div>
		<div><span class="k">Role</span><p class="v" data-scramble>Technical instructor</p></div>
		<div><span class="k">Subjects</span><p class="v" data-scramble>AI / Cloud</p></div>
		<div><span class="k">Method</span><p class="v" data-scramble>One clear step</p></div>
		<div><span class="k">Status</span><p class="v"><i class="dot fx-pulse"></i>Writing</p></div>
		<div class="pic s2" data-reveal="fade">{{IMG}}</div>
		<div class="s2"><span class="k">Newsletter</span><div style="max-width:440px">{{FORM}}</div></div>
		<div class="s2"><span class="k">Contents</span>{{TOPICS_UL}}</div>
		<div class="s4"><span class="k">Links</span>{{LINKS_ROWS}}</div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')
print('c1 done')
