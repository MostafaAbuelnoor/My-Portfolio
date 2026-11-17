from lib import page

# 21 after Roman Caseres
page(21, 'scattered-words', 'family=Unbounded:wght@500;700&family=Hanken+Grotesk:wght@400..600', '#EFEBE2', '''
:root { --line: #D6D0C2; --focus: #111; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #6B665A; --f-radius: 8px; --b-radius: 4px; }
body { background: #EFEBE2; color: #111; font: 15px/1.55 "Hanken Grotesk", system-ui, sans-serif; }
::selection { background: #111; color: #EFEBE2; }
.big { font-family: "Unbounded", sans-serif; font-weight: 700; text-transform: uppercase; line-height: 0.95; letter-spacing: -0.04em; font-size: clamp(1.7rem, 0.8rem + 4.2vw, 4rem); }
.board { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; align-items: start; padding-block: 12px 40px; }
.w1 { grid-column: 1 / -1; } .w2 { grid-column: 1 / -1; text-align: right; }
.pic { aspect-ratio: 4 / 3; background: #DCD6C8; overflow: hidden; display: flex; justify-content: center; align-items: flex-end; }
.pic img { height: 96%; width: auto; max-width: none; }
.txt p { margin-bottom: 14px; }
.w3 { grid-column: 1 / -1; font-size: clamp(2rem, 1rem + 6vw, 6rem); display: flex; flex-wrap: wrap; gap: 0 0.3em; }
.w3 i { font-style: normal; color: #A39C8B; }
.join { grid-column: 1 / -1; max-width: 440px; }
@media (min-width: 860px) { .w1 { grid-column: 1; } .w2 { grid-column: 2; grid-row: 2; align-self: end; } .pic { grid-row: 2; } .txt { grid-row: 1; grid-column: 2; max-width: 30em; justify-self: end; } }
''', '''
<div class="wrap">
	{{TOP}}
	<main class="board">
		<h1 class="big w1" data-in>Technical instructor</h1>
		<div class="txt" data-in style="--i:1"><p>{{INTRO}}</p>{{LINKS_INLINE}}</div>
		<div class="pic" data-in style="--i:1">{{IMG}}</div>
		<p class="big w2" data-in style="--i:2">Mostafa<br>Saher</p>
		<p class="big w3" aria-label="AI and cloud and clarity"><span>AI</span><i>&amp;</i><span>Cloud</span><i>&amp;</i><span>Clarity</span></p>
		<div class="join">{{FORM}}</div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 22 after Jha Sundaram
page(22, 'heavy-caps', 'family=Anton&family=Geist:wght@400;500', '#D9D9D6', '''
:root { --line: #BDBDB9; --focus: #111; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #555; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #D9D9D6; color: #111; font: 14px/1.5 "Geist", system-ui, sans-serif; }
::selection { background: #111; color: #D9D9D6; }
.screen { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; padding-block: 16px 20px; overflow: hidden; }
.head { display: flex; justify-content: space-between; gap: 20px; align-items: flex-start; }
h1 { font: 400 clamp(3rem, 1rem + 8.4vw, 7.4rem)/0.9 "Anton", sans-serif; text-transform: uppercase; letter-spacing: -0.01em; }
.metas { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.04em; text-align: right; }
.metas li::before { content: "■ "; }
.mid { display: grid; place-items: end center; }
.mid figure { width: min(330px, 74%); margin-bottom: -20px; }
.low { position: relative; display: grid; gap: 16px; background: #D9D9D6; padding-top: 16px; border-top: 1px solid #111; }
.low p { max-width: 30em; font-weight: 500; }
.field { gap: 0; }
@media (min-width: 860px) { .low { grid-template-columns: minmax(0, 1fr) 420px; align-items: end; } .mid figure { width: 360px; } }
''', '''
<div class="wrap">
	<main class="screen">
		<div class="head"><h1 data-in>AI &amp;<br>Cloud</h1><ul class="metas"><li>Mostafa Saher</li><li>Technical instructor</li><li>Newsletter</li></ul></div>
		<div class="mid" data-in style="--i:1"><figure>{{IMG}}</figure></div>
		<div class="low" data-in style="--i:2"><div><p>Teaching the edges of what’s next, one clear step at a time. From new models to cloud services, explained the way I explain them in class.</p><div style="margin-top:12px">{{LINKS_INLINE}}</div></div>{{FORM}}</div>
	</main>
</div>
''')

# 23 after Ramy Adel
page(23, 'badge', 'family=Wix+Madefor+Display:wght@400..800', '#FFFFFF', '''
:root { --blue: #1757F5; --line: #E7E9EE; --focus: var(--blue); --f-bg: #fff; --f-border: 1px solid #D5D9E2; --b-bg: var(--blue); --b-text: #fff; --note: #667; --f-radius: 12px; --b-radius: 8px; }
body { background: #fff linear-gradient(#EEF0F4 1px, transparent 1px) 0 0 / 100% 48px; color: #10131A; font: 16px/1.55 "Wix Madefor Display", system-ui, sans-serif; }
::selection { background: var(--blue); color: #fff; }
.top a { padding: 7px 14px; border-radius: 999px; background: #10131A; color: #fff; font-size: 0.9rem; font-weight: 600; }
.hero { display: grid; gap: 40px; align-items: center; padding-block: clamp(24px, 6vh, 64px) 56px; }
h1 { font-size: clamp(2.3rem, 1.3rem + 3.6vw, 3.9rem); font-weight: 800; line-height: 1.02; letter-spacing: -0.04em; }
h1 span { display: block; color: var(--blue); }
.hero p { margin: 16px 0 22px; max-width: 30em; color: #4A5060; }
.signup { max-width: 440px; }
.card { justify-self: center; width: min(300px, 82%); padding: 14px 14px 18px; border-radius: 22px; background: #10131A; color: #fff; transform: rotate(5deg); box-shadow: 0 30px 50px -24px rgb(16 19 26 / 0.55); }
.card::before { content: ""; display: block; width: 46px; height: 8px; margin: 0 auto 12px; border-radius: 999px; background: #fff; }
.card .ph { aspect-ratio: 1; border-radius: 12px; background: #C9D8FF; overflow: hidden; }
.card .ph img { width: 124%; max-width: none; margin: 6% 0 0 -12%; }
.card b { display: block; margin-top: 14px; font-size: 1.3rem; letter-spacing: -0.02em; }
.card span { color: #A9B0C2; font-size: 0.9rem; }
.rest { display: grid; gap: 28px 56px; padding-block: 36px 8px; background: #fff; border-top: 1px solid var(--line); }
@media (min-width: 880px) { .hero { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); } .rest { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
@media (prefers-reduced-motion: no-preference) { .card { animation: swing 1100ms var(--ease-out) 150ms backwards; transform-origin: 50% 0; } @keyframes swing { from { transform: rotate(-9deg); opacity: 0; } } }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<section class="hero">
			<div data-in><h1>Built for people, <span>then for exams.</span></h1><p>I’m Mostafa Saher, a technical instructor. I teach AI and cloud, one clear step at a time, and write down what comes up after class.</p>{{FORM}}</div>
			<div class="card"><div class="ph">{{IMG}}</div><b>Mostafa Saher</b><span>Instructor · AI and cloud</span></div>
		</section>
		<section class="rest">{{TOPICS_UL}}{{LINKS_ROWS}}</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 24 after Vanmassenhove Sen
page(24, 'side-box', 'family=Lexend:wght@300..600', '#E8E8E5', '''
:root { --blue: #3E4BDB; --line: #CFCFCB; --focus: var(--blue); --f-bg: #fff; --b-bg: var(--blue); --b-text: #fff; --note: #5E5E5A; --f-radius: 6px; --b-radius: 3px; }
body { background: #E8E8E5; color: #17171A; font: 300 15px/1.6 "Lexend", system-ui, sans-serif; }
::selection { background: var(--blue); color: #fff; }
.top b { font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; font-size: 0.85rem; }
.hero { position: relative; display: grid; align-items: end; min-height: min(84svh, 760px); overflow: hidden; }
.hero figure { justify-self: center; width: min(86%, 400px); }
.box { position: relative; z-index: 1; margin-top: -90px; padding: 24px; background: rgb(255 255 255 / 0.92); border: 1px solid var(--line); }
h1 { font-size: clamp(1.6rem, 1.2rem + 1.4vw, 2.2rem); font-weight: 500; line-height: 1.15; letter-spacing: -0.02em; }
.box p { margin: 12px 0 18px; color: #4B4B50; }
.strip { display: grid; gap: 28px 56px; padding-block: 40px 8px; }
.strip h2 { font-size: 0.85rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 10px; }
@media (min-width: 880px) { .hero { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); } .box { grid-column: 1; grid-row: 1; align-self: center; margin: 0; padding: 32px; } .hero figure { grid-column: 2; grid-row: 1; width: min(100%, 520px); } .strip { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<section class="hero">
			<figure data-in style="--i:1">{{IMG}}</figure>
			<div class="box" data-in><h1>Bridging complex ideas with real-world understanding.</h1><p>I’m Mostafa Saher, a technical instructor. I teach AI and cloud, one clear step at a time. My newsletter carries what comes up after class.</p>{{FORM}}</div>
		</section>
		<section class="strip"><div><h2>My writing</h2>{{TOPICS_UL}}</div><div><h2>Elsewhere</h2>{{LINKS_ROWS}}</div></section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 25 after Antonio Pires
page(25, 'sparse', 'family=Funnel+Display:wght@300..500', '#F5F4F0', '''
:root { --line: #DDDBD3; --focus: #18181A; --f-bg: transparent; --f-border: 0; --b-bg: transparent; --b-text: #18181A; --note: #77756C; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #F5F4F0; color: #18181A; font: 14px/1.6 "Funnel Display", system-ui, sans-serif; }
::selection { background: #18181A; color: #F5F4F0; }
.screen { min-height: 100svh; display: grid; gap: 40px; align-content: center; padding-block: 48px; }
.left { max-width: 22em; color: #5F5D55; font-size: 0.86rem; }
.face { width: 34px; height: 34px; border-radius: 50%; background: #DDDBD3; margin-bottom: 14px; }
h1 { font-size: clamp(1.7rem, 1.2rem + 2vw, 2.6rem); font-weight: 400; line-height: 1.18; letter-spacing: -0.03em; max-width: 15em; }
.field { border-bottom: 1px solid #18181A; margin-top: 28px; max-width: 420px; }
.field:focus-within { box-shadow: 0 2px 0 #18181A; }
.field input { padding-left: 0; } .btn { padding-right: 0; }
.left .li-inline { margin-top: 16px; color: #18181A; }
@media (min-width: 860px) { .screen { grid-template-columns: 1fr 1.6fr; align-items: center; gap: 80px; } }
''', '''
<div class="wrap">
	<main class="screen">
		<div class="left" data-in style="--i:1"><div class="face">{{IMG}}</div><p>Mostafa Saher is a technical instructor. The best part of every class comes once it’s over, and his newsletter is where that goes now.</p>{{LINKS_INLINE}}</div>
		<div data-in><h1>Teaching AI and cloud, one clear step at a time. Currently writing it all down.</h1>{{FORM}}</div>
	</main>
</div>
''')

# 26 after Grega Cuderman
page(26, 'asterisk', 'family=Young+Serif&family=Geist:wght@400;500', '#FFFFFF', '''
:root { --green: #1E9E5A; --line: #E8E8E4; --focus: var(--green); --f-bg: #F4F4F1; --b-bg: #121212; --b-text: #fff; --note: #666; --f-radius: 999px; --b-radius: 999px; }
body { background: #fff; color: #121212; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: var(--green); color: #fff; }
.top a { padding: 6px 14px; border-radius: 999px; background: #121212; color: #fff; font-size: 0.88rem; }
h1 { max-width: 13em; margin: clamp(32px, 9vh, 88px) auto 26px; font: 400 clamp(2rem, 1.3rem + 2.6vw, 3.2rem)/1.15 "Young Serif", serif; letter-spacing: -0.02em; text-wrap: balance; }
h1 i { font-style: normal; color: var(--green); display: inline-block; }
.signup { max-width: 430px; margin-inline: auto; } .note { text-align: center; }
.frame { position: relative; margin-top: 56px; border-radius: 20px; background: #1F6B46; overflow: hidden; display: grid; align-items: end; min-height: 380px; color: #fff; }
.frame figure { justify-self: center; width: min(74%, 380px); }
.frame p { position: absolute; left: 22px; top: 20px; right: 22px; max-width: 16em; font: 400 1.5rem/1.15 "Young Serif", serif; }
.cols { display: grid; gap: 28px 56px; padding-block: 48px 8px; }
@media (min-width: 860px) { .cols { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } .frame { min-height: 480px; } .frame p { font-size: 2.2rem; left: 36px; top: 32px; } .frame figure { justify-self: end; margin-right: 8%; } }
@media (prefers-reduced-motion: no-preference) { h1 i { animation: spin 1400ms var(--ease-out) 300ms backwards; } @keyframes spin { from { transform: rotate(-180deg) scale(0.6); opacity: 0; } } }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<h1 data-in>I teach AI &amp; cloud for people who want to <i>✳</i> understand.</h1>
		<div data-in style="--i:1">{{FORM}}</div>
		<div class="frame" data-in style="--i:2"><p>Class notes from the heart of the corridor.</p><figure>{{IMG}}</figure></div>
		<section class="cols"><div><p style="margin-bottom:18px">I’m Mostafa Saher, a technical instructor. {{INTRO}}</p>{{LINKS_INLINE}}</div>{{TOPICS_UL}}</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 27 after Christoph Mandl
page(27, 'two-colour', 'family=Gabarito:wght@400..900', '#A9AE7C', '''
:root { --red: #E5231B; --line: #8F9465; --focus: #1A1B10; --f-bg: #C3C79C; --f-text: #1A1B10; --f-ph: #4F5233; --b-bg: var(--red); --b-text: #fff; --note: #3C3F25; --err: #6E0D08; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #A9AE7C; color: #1A1B10; font: 16px/1.5 "Gabarito", system-ui, sans-serif; }
::selection { background: var(--red); color: #fff; }
.screen { min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; padding-block: 0 24px; }
.logo { align-self: center; display: flex; align-items: flex-start; gap: 0.12em; color: var(--red); font-weight: 900; font-size: clamp(4.4rem, 1rem + 19vw, 15rem); line-height: 0.8; letter-spacing: -0.06em; }
.logo small { font-size: 0.2em; line-height: 0.98; letter-spacing: -0.02em; padding-top: 0.5em; }
.low { display: grid; gap: 20px 48px; align-items: end; }
.low p { max-width: 30em; font-size: 1.08rem; font-weight: 500; }
.field { gap: 0; }
.more { display: grid; gap: 28px 56px; padding-block: 44px 8px; border-top: 2px solid var(--red); }
.shot { background: #969B69; display: flex; justify-content: center; align-items: flex-end; aspect-ratio: 4 / 3; overflow: hidden; }
.shot img { height: 96%; width: auto; max-width: none; }
@media (min-width: 860px) { .low { grid-template-columns: minmax(0, 1fr) 430px; } .more { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
''', '''
<div class="wrap">
	<div class="screen">
		{{TOP}}
		<h1 class="logo" data-in aria-label="Mostafa Saher">mostafa<small>Sa<br>he<br>r</small></h1>
		<div class="low" data-in style="--i:1"><p>{{H}}</p>{{FORM}}</div>
	</div>
	<main class="more">
		<div class="shot">{{IMG}}</div>
		<div><p style="margin-bottom:20px">{{INTRO}}</p>{{TOPICS_UL}}<div style="margin-top:22px;font-weight:600">{{LINKS_INLINE}}</div></div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 28 after Made by Igor
page(28, 'teal-serif', 'family=Gloock&family=Geist:wght@400;500', '#3FA892', '''
:root { --line: #2B7B6A; --focus: #0D231E; --f-bg: #0D231E; --f-text: #EAF6F2; --f-ph: #8FBDB1; --b-bg: #EAF6F2; --b-text: #0D231E; --note: #0D231E; --err: #5A0A05; --f-radius: 4px; --b-radius: 2px; --f-pad: 4px; }
body { background: #3FA892; color: #0D231E; font: 13px/1.5 "Geist", system-ui, sans-serif; }
::selection { background: #0D231E; color: #3FA892; }
.screen { position: relative; min-height: 100svh; display: grid; grid-template-columns: minmax(0, 1fr); grid-template-rows: auto 1fr auto; overflow: hidden; background: radial-gradient(60% 50% at 62% 46%, #E0586F 0%, rgb(224 88 111 / 0) 60%); }
.bits { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px; align-content: center; padding-block: 16px; }
.bits p { max-width: 18em; }
.bits .join { grid-column: 1 / -1; max-width: 400px; }
.giant { font: 400 clamp(2.6rem, 9.4vw, 9rem)/0.86 "Gloock", serif; text-transform: uppercase; letter-spacing: -0.02em; white-space: nowrap; margin: 0 -0.04em -0.06em; }
.more { background: #0D231E; color: #EAF6F2; --line: #244A40; --focus: #EAF6F2; }
.more .in { display: grid; gap: 28px 56px; padding-block: 48px 8px; }
.more figure { width: min(240px, 60%); }
@media (min-width: 860px) { .bits { grid-template-columns: repeat(4, minmax(0, 1fr)); } .bits .join { grid-column: 2 / span 2; justify-self: center; width: 100%; } .more .in { grid-template-columns: 240px minmax(0, 1fr) minmax(0, 1fr); align-items: end; } }
''', '''
<div class="screen"><div class="wrap" style="display:contents">
	<div class="wrap">{{TOP}}</div>
	<main class="wrap bits">
		<p data-in>Mostafa Saher<br>Technical instructor</p><p data-in style="--i:1">Teaching AI and cloud, one clear step at a time.</p>
		<p data-in style="--i:2">Newsletter: notes from the classroom, where I stand on the hype, resources I’d hand a student.</p><p data-in style="--i:3">LinkedIn, GitHub and email below.</p>
		<div class="join" data-in style="--i:2">{{FORM}}</div>
	</main>
	<h1 class="giant wrap">Cloud instructor</h1>
</div></div>
<section class="more"><div class="wrap in"><figure>{{IMG}}</figure>{{TOPICS_UL}}{{LINKS_ROWS}}</div><div class="wrap"><footer class="foot">{{FOOT}}</footer></div></section>
''')

# 29 after Marina Rachello
page(29, 'hello', 'family=Zilla+Slab:wght@400;500;600&family=Geist:wght@400;500', '#EE3B1F', '''
:root { --line: #3A3A3A; --focus: #fff; --f-bg: #333; --f-text: #F3F1EC; --f-ph: #A6A39B; --b-bg: #EE3B1F; --b-text: #160502; --note: #A6A39B; --err: #FFB3A6; --f-radius: 4px; --b-radius: 2px; --f-pad: 4px; }
body { background: #242424; color: #F3F1EC; font: 15px/1.55 "Geist", system-ui, sans-serif; }
::selection { background: #fff; color: #EE3B1F; }
.red { background: #EE3B1F; color: #160502; min-height: 72svh; display: grid; grid-template-rows: auto 1fr auto; grid-template-columns: minmax(0, 1fr); padding-bottom: 76px; }
h1 { align-self: start; margin-top: 8px; font: 500 clamp(3.2rem, 1rem + 10vw, 8.6rem)/0.92 "Zilla Slab", serif; letter-spacing: -0.03em; }
h1 span { color: #FFF3E6; }
.red p { justify-self: end; max-width: 24em; text-align: right; font-weight: 500; }
.dark { display: grid; grid-template-columns: minmax(0, 1fr); gap: 28px 56px; padding-block: 36px 8px; }
.shot { background: #303030; display: flex; justify-content: center; align-items: flex-end; aspect-ratio: 16 / 10; overflow: hidden; margin-top: -84px; }
.shot img { height: 100%; width: auto; max-width: none; }
.dark h2 { font: 500 1.7rem/1.1 "Zilla Slab", serif; margin-bottom: 14px; }
@media (min-width: 860px) { .dark { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } .shot { margin-top: -150px; } .red { padding-bottom: 150px; } }
''', '''
<header class="red"><div class="wrap">{{TOP}}</div>
	<h1 class="wrap" data-in>Mostafa Sa-<br><span>hello!</span></h1>
	<div class="wrap" style="display:grid"><p data-in style="--i:1">I am a technical instructor. I teach AI and cloud, one clear step at a time, and I write down what comes up after class.</p></div>
</header>
<main class="wrap dark">
	<div><div class="shot" data-in style="--i:2">{{IMG}}</div><div style="margin-top:22px">{{LINKS_ROWS}}</div></div>
	<div><h2>Get the newsletter</h2><p style="color:#B9B6AE;margin-bottom:16px">{{INTRO}}</p>{{FORM}}<div style="margin-top:28px">{{TOPICS_UL}}</div></div>
</main>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 30 after Specia1ne
page(30, 'blue-bar', 'family=Familjen+Grotesk:wght@400..700', '#FFFFFF', '''
:root { --blue: #1B3BFF; --line: #5C73FF; --focus: #fff; --f-bg: #fff; --b-bg: #0B0E1F; --b-text: #fff; --note: #D3D9FF; --err: #FFD2CB; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #fff; color: #0B0E1F; font: 16px/1.5 "Familjen Grotesk", system-ui, sans-serif; }
::selection { background: var(--blue); color: #fff; }
.hero { position: relative; padding-block: 8px 48px; overflow: hidden; }
.hero::after { content: ""; position: absolute; top: 0; bottom: 0; left: 62%; width: clamp(28px, 6vw, 64px); background: var(--blue); mix-blend-mode: multiply; }
h1 { margin-top: clamp(28px, 8vh, 80px); max-width: 13em; font-size: clamp(2.3rem, 1.2rem + 4.4vw, 4.6rem); font-weight: 700; line-height: 0.98; letter-spacing: -0.04em; }
.hero p { margin-top: 20px; max-width: 30em; color: #555A70; }
.blue { background: var(--blue); color: #fff; padding-block: 40px 8px; }
.blue .in { display: grid; gap: 32px 56px; }
.blue h2 { font-size: 1.5rem; font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 16px; }
.field { gap: 0; }
.blue .tp b { font-size: 1.2rem; }
.close { display: grid; gap: 20px 56px; align-items: end; padding-block: 36px 0; }
.close figure { width: 180px; }
.close p { font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; max-width: 14em; padding-bottom: 20px; }
@media (min-width: 860px) { .blue .in { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } .blue .right { text-align: right; } .blue .right .li-rows a { flex-direction: row-reverse; } .blue .right .l-meta { margin: 0 auto 0 0; } .close { grid-template-columns: 180px minmax(0, 1fr); } }
''', '''
<header class="hero"><div class="wrap">{{TOP}}
	<h1 data-in>AI, cloud and the systems behind them, taught from first idea to working form.</h1>
	<p data-in style="--i:1">Mostafa Saher. Technical instructor.</p>
</div></header>
<main>
	<section class="blue"><div class="wrap in">
		<div data-in style="--i:2"><h2>Selected notes, sent by email.</h2>{{FORM}}</div>
		<div class="right">{{TOPICS_UL}}<div style="margin-top:24px">{{LINKS_ROWS}}</div></div>
	</div></section>
	<section class="wrap close"><figure>{{IMG}}</figure><p>Hype is what people see. Understanding is what makes it work.</p></section>
</main>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')
print('batch 2 done')
