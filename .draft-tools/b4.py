from lib import page

# 41 after Linda Jolly
page(41, 'staggered-name', 'family=Inter+Tight:wght@400..600', '#E3E4DF', '''
:root { --line: #C9CAC4; --focus: #111; --f-bg: #F4F4F1; --b-bg: #111; --b-text: #fff; --note: #5C5D57; --f-radius: 999px; --b-radius: 999px; }
body { background: #E3E4DF; color: #111; font: 15px/1.55 "Inter Tight", system-ui, sans-serif; }
::selection { background: #111; color: #E3E4DF; }
.top { font-size: 0.78rem; letter-spacing: 0.06em; text-transform: uppercase; }
.screen { min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; padding-bottom: 28px; }
.name { align-self: center; justify-self: center; position: relative; font-size: clamp(4.6rem, 1rem + 17vw, 13rem); font-weight: 500; line-height: 0.8; letter-spacing: -0.07em; }
.name span { display: block; } .name span + span { margin-left: 0.62em; }
.name small { position: absolute; left: 100%; top: 0.5em; margin-left: 0.4em; width: 9em; font-size: 0.085em; line-height: 1.25; letter-spacing: 0; font-weight: 500; }
.ask { justify-self: center; width: 100%; max-width: 430px; } .note { text-align: center; }
.more { display: grid; gap: 28px 56px; padding-block: 44px 8px; border-top: 1px solid var(--line); }
.more figure { width: min(220px, 60%); filter: grayscale(1); }
@media (max-width: 700px) { .name small { position: static; display: block; margin: 1.6em 0 0 0.3em; font-size: 0.16em; width: auto; } }
@media (min-width: 860px) { .more { grid-template-columns: 220px minmax(0, 1fr) minmax(0, 1fr); align-items: end; } }
''', '''
<div class="wrap">
	<div class="screen">
		{{TOP}}
		<h1 class="name" data-in><span>Mostafa</span><span>Saher</span><small>Technical instructor teaching AI and cloud</small></h1>
		<div class="ask" data-in style="--i:1">{{FORM}}</div>
	</div>
	<main class="more"><figure>{{IMG}}</figure><div><p style="margin-bottom:18px">{{INTRO}}</p>{{LINKS_INLINE}}</div>{{TOPICS_UL}}</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 42 after Oliver Gareis
page(42, 'cropped-name', 'family=Schibsted+Grotesk:wght@400..700', '#FFFFFF', '''
:root { --line: #E5E5E5; --focus: #111; --f-bg: #F2F2F2; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #fff; color: #111; font: 13px/1.5 "Schibsted Grotesk", system-ui, sans-serif; }
::selection { background: #111; color: #fff; }
.screen { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; }
.metas { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; padding-block: 16px; }
.metas a { text-decoration: underline; text-underline-offset: 3px; }
.mid { position: relative; z-index: 2; align-self: start; margin-top: clamp(16px, 6vh, 64px); max-width: 420px; font-size: 15px; }
.mid p { margin-bottom: 14px; font-weight: 500; } .field { gap: 0; }
.screen figure { position: absolute; z-index: 0; right: 4%; bottom: 9vw; width: min(52%, 360px); }
.giant { position: absolute; z-index: 1; left: 0; right: 0; bottom: -0.2em; text-align: center; font-size: 21.5vw; font-weight: 600; line-height: 0.8; letter-spacing: -0.05em; white-space: nowrap; }
.more { display: grid; gap: 28px 56px; padding-block: 44px 8px; font-size: 15px; }
@media (min-width: 860px) { .metas { grid-template-columns: repeat(4, minmax(0, 1fr)); } .more { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } .screen figure { right: 12%; } }
@media (prefers-reduced-motion: no-preference) { .giant { animation: lift 1100ms var(--ease-out) 200ms backwards; } @keyframes lift { from { transform: translateY(40%); } } }
''', '''
<div class="screen">
	<div class="wrap">
		<div class="metas"><p>Mostafa Saher<br>Technical instructor</p><p>AI and cloud<br>One clear step at a time</p><p><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a><br><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a></p><p><a href="mailto:mostafasaher@gmail.com">Email</a><br><a href="#email" data-focus-signup>Newsletter</a></p></div>
		<main class="mid" data-in><p>Classroom-based instructor, specialising in AI and cloud. Notes from class, sent by email.</p>{{FORM}}</main>
	</div>
	<figure data-in style="--i:1">{{IMG}}</figure>
	<h1 class="giant">MOSTAFA</h1>
</div>
<section class="wrap more"><div><p style="margin-bottom:18px">{{INTRO}}</p></div>{{TOPICS_UL}}</section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 43 after Daniel White
page(43, 'plain-text', 'family=JetBrains+Mono:wght@400;700', '#FBF8F1', '''
:root { --line: #E3DDCE; --focus: #1B1A17; --f-bg: #fff; --f-border: 1px solid #1B1A17; --b-bg: #1B1A17; --b-text: #FBF8F1; --note: #7A7566; --f-radius: 0; --b-radius: 0; --f-pad: 3px; --w: 720px; }
body { background: #FBF8F1; color: #1B1A17; font: 14px/1.7 "JetBrains Mono", ui-monospace, monospace; }
::selection { background: #FFE27A; }
h1, h2 { font-size: inherit; font-weight: 700; } h1 { padding-top: clamp(32px, 9vh, 88px); }
h1::before { content: "# "; color: #A59F8D; } h2::before { content: "## "; color: #A59F8D; }
h2 { margin: 36px 0 10px; }
p + p { margin-top: 12px; }
mark { padding: 0 3px; color: inherit; } .m1 { background: #FFE27A; } .m2 { background: #BFE6FF; } .m3 { background: #CFF2C9; }
.list li::before { content: "- "; color: #A59F8D; } .list a { text-decoration: underline; text-underline-offset: 3px; }
.signup { max-width: 460px; font-family: inherit; }
.strip { margin-top: 44px; height: 170px; background: #EDE6D4; display: flex; justify-content: center; overflow: hidden; }
.strip img { width: 240px; max-width: none; height: auto; align-self: flex-start; margin-top: 6px; }
''', '''
<div class="wrap">
	<main>
		<h1 data-in>Mostafa Saher</h1>
		<p data-in style="--i:1">I’m a <mark class="m1">technical instructor</mark>. I teach <mark class="m2">AI</mark> and <mark class="m3">cloud</mark>, one clear step at a time.</p>
		<p data-in style="--i:1">{{INTRO}}</p>
		<h2>newsletter</h2>
		<div data-in style="--i:2">{{FORM}}</div>
		<h2>writing</h2>
		<ul class="list"><li><b>thoughts</b>: what students get stuck on, and the explanation that finally made it click.</li><li><b>opinions</b>: where I stand on new models, cloud services and the hype.</li><li><b>resources</b>: the labs, docs, courses and tools I actually use.</li></ul>
		<h2>elsewhere</h2>
		<ul class="list"><li><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">linkedin</a></li><li><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">github</a></li><li><a href="mailto:mostafasaher@gmail.com">mostafasaher@gmail.com</a></li></ul>
		<div class="strip">{{IMG}}</div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 44 after Polywork
page(44, 'arch', 'family=Gilda+Display&family=Albert+Sans:wght@400..600', '#7A6EDB', '''
:root { --line: rgb(255 255 255 / 0.35); --focus: #fff; --f-bg: #fff; --b-bg: #2A2170; --b-text: #fff; --note: #E4E0FF; --err: #FFE0DA; --f-radius: 6px; --b-radius: 3px; --f-pad: 5px; }
body { background: #7A6EDB; color: #fff; font: 15px/1.6 "Albert Sans", system-ui, sans-serif; }
::selection { background: #fff; color: #7A6EDB; }
.top a { padding: 7px 14px; background: #fff; color: #2A2170; border-radius: 4px; font-size: 0.85rem; font-weight: 600; }
.hero { display: grid; gap: 28px 56px; align-items: start; padding-block: 16px 56px; }
.arch { justify-self: center; width: min(340px, 82%); aspect-ratio: 3 / 4.4; border-radius: 999px 999px 0 0; background: #B9B1F2; overflow: hidden; display: flex; align-items: flex-end; justify-content: center; }
.arch img { width: 112%; max-width: none; }
h1 { font: 400 clamp(3.4rem, 2rem + 6vw, 6.4rem)/0.95 "Gilda Display", serif; }
.hero p { margin: 22px 0; max-width: 28em; }
.signup { max-width: 430px; }
.rule { width: 1px; height: 90px; background: #fff; margin-top: 28px; }
.more { display: grid; gap: 28px 56px; padding-block: 8px 16px; }
.more h2 { font-size: 1.15rem; font-weight: 600; margin-bottom: 10px; }
@media (min-width: 860px) { .hero { grid-template-columns: 340px minmax(0, 1fr); padding-top: 32px; } .arch { width: 100%; } .more { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
@media (prefers-reduced-motion: no-preference) { .arch { animation: arch 1000ms var(--ease-out) backwards; } @keyframes arch { from { clip-path: inset(100% 0 0 0 round 999px 999px 0 0); } to { clip-path: inset(0 0 0 0 round 999px 999px 0 0); } } }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<section class="hero">
			<div class="arch">{{IMG}}</div>
			<div data-in style="--i:1"><h1>Mostafa<br>Saher</h1><p>I’m a technical instructor teaching AI and cloud, one clear step at a time. My newsletter carries what comes up after class.</p>{{FORM}}<div class="rule"></div></div>
		</section>
		<section class="more"><div><h2>What I write</h2>{{TOPICS_UL}}</div><div><h2>Elsewhere</h2>{{LINKS_ROWS}}</div></section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 45 after Headspace
page(45, 'circles', 'family=Rubik:wght@400..600', '#FFFFFF', '''
:root { --orange: #F47D31; --line: #E8E8E8; --focus: #2D2C2B; --f-bg: #F4F3F1; --b-bg: #2D2C2B; --b-text: #fff; --note: #6B6966; --f-radius: 999px; --b-radius: 999px; }
body { background: #fff; color: #2D2C2B; font: 16px/1.6 "Rubik", system-ui, sans-serif; }
::selection { background: var(--orange); color: #fff; }
.top a { padding: 7px 16px; border-radius: 999px; background: #2D2C2B; color: #fff; font-size: 0.88rem; }
.story { display: grid; gap: 40px 64px; align-items: center; padding-block: clamp(24px, 6vh, 64px) 56px; }
.pic { position: relative; justify-self: center; width: min(360px, 78%); }
.pic::before, .pic::after { content: ""; position: absolute; border-radius: 50%; }
.pic::before { width: 44%; aspect-ratio: 1; right: 6%; top: -9%; background: #F0B63A; }
.pic::after { width: 32%; aspect-ratio: 1; left: -14%; bottom: 4%; background: var(--orange); z-index: 2; }
.pic .ph { position: relative; z-index: 1; aspect-ratio: 4 / 5; background: #DCDAD6; overflow: hidden; display: flex; align-items: flex-end; justify-content: center; }
.pic img { width: 116%; max-width: none; filter: grayscale(1) contrast(1.05); }
h1 { font-size: clamp(2.2rem, 1.5rem + 2.4vw, 3.2rem); font-weight: 600; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 14px; }
.story p { margin-bottom: 22px; max-width: 32em; color: #4A4846; }
.signup { max-width: 440px; }
.more { display: grid; gap: 28px 56px; padding-block: 36px 8px; border-top: 1px solid var(--line); }
@media (min-width: 860px) { .story { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); } .more { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
@media (prefers-reduced-motion: no-preference) { .pic::before, .pic::after { animation: dot 900ms var(--ease-out) 250ms backwards; } @keyframes dot { from { transform: scale(0.6); opacity: 0; } } }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<section class="story">
			<div class="pic" data-in><div class="ph">{{IMG}}</div></div>
			<div data-in style="--i:1"><h1>My story</h1><p>I teach AI and cloud for a living, one clear step at a time. {{INTRO}}</p>{{FORM}}</div>
		</section>
		<section class="more">{{TOPICS_UL}}{{LINKS_ROWS}}</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 46 after Rauno Freiberg
page(46, 'canvas-card', 'family=Inter+Tight:wght@400;500', '#E6E6E6', '''
:root { --line: #E2E2E2; --focus: #111; --f-bg: #F1F1F1; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #E6E6E6; color: #111; font: 15px/1.5 "Inter Tight", system-ui, sans-serif; }
::selection { background: #FFF200; }
.board { display: grid; gap: 12px; padding: 44px 12px 12px; max-width: 1500px; margin-inline: auto; }
.card { position: relative; background: #fff; padding: clamp(20px, 3vw, 36px); overflow: hidden; min-height: 300px; }
.card > small { position: absolute; left: 0; bottom: 100%; padding-bottom: 6px; font-size: 0.7rem; color: #777; }
.lead h1 { position: relative; z-index: 1; font-size: clamp(1.9rem, 1.1rem + 2.8vw, 3.3rem); font-weight: 400; line-height: 1.16; letter-spacing: -0.03em; mix-blend-mode: multiply; }
.lead h1 span { display: block; } .lead h1 span:nth-child(even) { padding-left: 0.6em; }
.lead::after { content: ""; position: absolute; right: -6%; top: 50%; width: min(62%, 420px); aspect-ratio: 1; border-radius: 50%; background: #FFF200; transform: translateY(-50%); }
.photo { background: #111; padding: 0; display: flex; align-items: flex-end; justify-content: center; }
.photo img { width: 86%; filter: grayscale(1) contrast(1.1); }
.photo::before { content: ""; position: absolute; inset: 12% 14% 0; background: radial-gradient(closest-side, #555, transparent); }
.photo img { position: relative; }
.field { gap: 0; }
.card h2 { font-size: 1.4rem; font-weight: 500; letter-spacing: -0.02em; margin-bottom: 14px; }
.card.pad { padding-top: 44px; margin-top: 0; }
.board .gap { margin-top: 28px; }
@media (min-width: 900px) { .board { grid-template-columns: 1.5fr 0.8fr 1fr; padding: 56px 20px 20px; } .card { min-height: 420px; } .board .gap { margin-top: 0; } .wide { grid-column: span 2; } }
@media (prefers-reduced-motion: no-preference) { .lead::after { animation: sun 1200ms var(--ease-out) 200ms backwards; } @keyframes sun { from { transform: translateY(-50%) scale(0.2); } } }
''', '''
<main class="board">
	<section class="card lead" data-in><small>Mostafa Saher</small><h1><span>Mostafa Saher</span><span>is a technical</span><span>instructor</span><span>teaching AI</span><span>and cloud</span></h1></section>
	<section class="card photo gap" data-in style="--i:1"><small>Portrait</small>{{IMG}}</section>
	<section class="card gap" data-in style="--i:2"><small>Newsletter</small><h2>One clear step at a time, by email.</h2><p style="margin-bottom:16px;color:#555">{{INTRO}}</p>{{FORM}}</section>
	<section class="card wide gap" style="min-height:0"><small>Writing</small>{{TOPICS_UL}}</section>
	<section class="card gap" style="min-height:0"><small>Elsewhere</small>{{LINKS_ROWS}}<p class="foot" style="padding-bottom:0">{{FOOT}}</p></section>
</main>
''')

# 47 after Dan Martell
page(47, 'condensed', 'family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600', '#060C16', '''
:root { color-scheme: dark; --cyan: #19B5FE; --line: #1C2738; --focus: var(--cyan); --f-bg: #0F1826; --f-text: #F3F6FA; --f-ph: #8996A8; --f-border: 1px solid #22304A; --b-bg: var(--cyan); --b-text: #04121E; --note: #8996A8; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #060C16; color: #F3F6FA; font: 16px/1.55 "Barlow", system-ui, sans-serif; }
::selection { background: var(--cyan); color: #04121E; }
.top a { padding: 8px 16px; border-radius: 999px; background: var(--cyan); color: #04121E; font-size: 0.9rem; font-weight: 600; }
.hero { display: grid; gap: 28px 48px; align-items: end; padding-block: clamp(16px, 5vh, 56px) 40px; }
h1 { font: 700 clamp(3.6rem, 1.6rem + 9vw, 8.6rem)/0.86 "Barlow Condensed", sans-serif; text-transform: uppercase; letter-spacing: -0.01em; }
h1 span { color: var(--cyan); display: block; }
.hero p { margin: 20px 0 22px; max-width: 30em; color: #B3BECC; }
.signup { max-width: 440px; }
.frame { justify-self: center; width: min(400px, 88%); aspect-ratio: 4 / 4.6; overflow: hidden; background: linear-gradient(160deg, #24364F, #0B1422); display: flex; justify-content: center; align-items: flex-end; }
.frame img { width: 104%; max-width: none; }
.stats { display: grid; gap: 0; border-top: 1px solid var(--line); }
.stats li { padding: 22px 0; border-bottom: 1px solid var(--line); }
.stats b { display: block; font: 700 2rem/1 "Barlow Condensed", sans-serif; text-transform: uppercase; margin-bottom: 6px; } .stats span { color: #B3BECC; font-size: 0.95rem; }
.li-inline { margin-top: 28px; font-weight: 600; }
@media (min-width: 880px) { .hero { grid-template-columns: minmax(0, 1.25fr) minmax(0, 0.75fr); } .stats { grid-template-columns: repeat(3, 1fr); } .stats li { padding: 26px 24px 26px 0; border-bottom: 0; } .stats li + li { padding-left: 24px; border-left: 1px solid var(--line); } }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<section class="hero">
			<div data-in><h1>AI and cloud, <span>made clear.</span></h1><p>You can understand this. I’m Mostafa Saher, a technical instructor, and I teach it one clear step at a time.</p>{{FORM}}</div>
			<div class="frame" data-in style="--i:1">{{IMG}}</div>
		</section>
		<ul class="stats">
	{{TOPICS}}
		</ul>
		{{LINKS_INLINE}}
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 48 after Lee Robinson
page(48, 'tall-card', 'family=Source+Serif+4:opsz,wght@8..60,400;8..60,700&family=Geist:wght@400;500', '#FFFFFF', '''
:root { --line: #E5E5E5; --focus: #222; --f-bg: #fff; --f-border: 1px solid #D4D4D4; --b-bg: #222; --b-text: #fff; --note: #6B6B6B; --f-radius: 8px; --b-radius: 4px; --f-pad: 4px; }
body { background: #fff; color: #222; font: 400 18px/1.55 "Source Serif 4", Georgia, serif; }
::selection { background: #222; color: #fff; }
.lay { display: grid; gap: 32px 72px; padding-block: 36px 24px; }
h1 { font-size: 2.6rem; font-weight: 700; letter-spacing: -0.03em; line-height: 1; }
.tabs { display: flex; justify-content: space-between; margin: 34px 0 20px; padding-bottom: 10px; border-bottom: 1px solid var(--line); font: 400 0.8rem "Geist", sans-serif; color: #6B6B6B; }
.tabs b { color: #222; font-weight: 500; }
.bio p + p { margin-top: 1em; }
h2 { margin: 44px 0 14px; font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em; }
.notes { display: grid; gap: 6px 32px; } .notes li::before { content: "▪ "; color: #999; }
.blog li { display: flex; justify-content: space-between; gap: 16px; padding-block: 12px; border-top: 1px solid var(--line); }
.blog a { text-decoration: none; } .blog span { font: 400 0.8rem "Geist", sans-serif; color: #6B6B6B; white-space: nowrap; align-self: center; }
.signup { font-family: "Geist", sans-serif; max-width: 460px; }
.card { border-radius: 14px; border: 1px solid var(--line); overflow: hidden; background: linear-gradient(#8FC3EE, #D9ECFA 60%, #F3E7C8); display: flex; align-items: flex-end; justify-content: center; height: 420px; }
.card img { width: 96%; }
.foot { font-family: "Geist", sans-serif; }
@media (min-width: 900px) { .lay { grid-template-columns: minmax(0, 1.25fr) minmax(0, 0.75fr); } .notes { grid-template-columns: 1fr 1fr; } .card { position: sticky; top: 36px; height: calc(100svh - 72px); max-height: 760px; } }
''', '''
<div class="wrap">
	<div class="lay">
		<main>
			<h1 data-in>@mostafa</h1>
			<div class="tabs"><span>Bio</span><b>Default</b></div>
			<div class="bio" data-in style="--i:1"><p>I’m an instructor and writer. I teach AI and cloud, one clear step at a time.</p><p>{{INTRO}}</p></div>
			<h2>Newsletter</h2>
			{{FORM}}
			<h2>Notes</h2>
			<ul class="notes"><li>Thoughts from the classroom</li><li>Opinions on the hype</li><li>Resources I’d hand a student</li><li>Explanations that made it click</li></ul>
			<h2>Elsewhere</h2>
			<ul class="blog"><li><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a><span>Mostafa Abuelnoor</span></li><li><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a><span>@MostafaAbuelnoor</span></li><li><a href="mailto:mostafasaher@gmail.com">Email</a><span>mostafasaher@gmail.com</span></li></ul>
			<footer class="foot">{{FOOT}}</footer>
		</main>
		<aside class="card" data-in style="--i:2">{{IMG}}</aside>
	</div>
</div>
''')

# 49 after Nick Saraev
page(49, 'ink-portrait', 'family=Instrument+Serif&family=Schibsted+Grotesk:wght@400;500', '#FFFFFF', '''
:root { --green: #55703A; --line: #E7E7E2; --focus: var(--green); --f-bg: #fff; --f-border: 1px solid #DAD9D2; --b-bg: var(--green); --b-text: #fff; --note: #6D6D66; --f-radius: 999px; --b-radius: 999px; --w: 660px; }
body { background: #fff; color: #1C1C1A; font: 17px/1.65 "Schibsted Grotesk", system-ui, sans-serif; }
::selection { background: #DDE7CF; }
.top b { font: 400 1.6rem "Instrument Serif", serif; } .top a { font-size: 0.92rem; color: #55554F; }
.ink { width: min(330px, 78%); margin: 20px auto 8px; }
.ink img { filter: grayscale(1) contrast(1.9) brightness(1.12); -webkit-mask-image: radial-gradient(closest-side at 50% 46%, #000 62%, transparent 100%); mask-image: radial-gradient(closest-side at 50% 46%, #000 62%, transparent 100%); }
.bio p + p { margin-top: 1em; }
.bio a, .rows a span:first-child { text-decoration: underline; text-decoration-color: #B9C7A6; text-underline-offset: 4px; }
h2 { margin: 48px 0 8px; font: 400 1.5rem "Instrument Serif", serif; }
.rows li { display: flex; justify-content: space-between; gap: 16px; align-items: baseline; padding-block: 5px; }
.rows a { display: contents; } .rows small { font-size: 0.8rem; color: #6D6D66; white-space: nowrap; }
.box { margin-top: 56px; padding: 22px; border: 1px solid var(--line); border-radius: 12px; background: #F8F8F4; }
.box h2 { margin: 0 0 4px; } .box p.lead { color: #6D6D66; font-size: 0.92rem; margin-bottom: 14px; }
.foot { margin-top: 40px; border-top: 1px solid var(--line); }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<div class="ink" data-in>{{IMG}}</div>
		<div class="bio" data-in style="--i:1"><p>Mostafa Saher teaches people AI and cloud, one clear step at a time. He is a technical instructor.</p><p>The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?”, the links he sends people afterwards. His <a href="#email" data-focus-signup>newsletter</a> is where that goes now.</p></div>
		<h2>Writing</h2>
		<ul class="rows"><li><span>Thoughts from the classroom</span><small>notes</small></li><li><span>Opinions on new models and cloud services</span><small>takes</small></li><li><span>Resources I’d hand a student</span><small>links</small></li></ul>
		<h2>Elsewhere</h2>
		<ul class="rows"><li><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener"><span>LinkedIn</span><small>Mostafa Abuelnoor</small></a></li><li><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener"><span>GitHub</span><small>@MostafaAbuelnoor</small></a></li><li><a href="mailto:mostafasaher@gmail.com"><span>Email</span><small>mostafasaher@gmail.com</small></a></li></ul>
		<section class="box"><h2>Newsletter</h2><p class="lead">Mostafa writes down what comes up after class. Get it by email.</p>{{FORM}}</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 50 after Zacchi
page(50, 'midnight', 'family=Manrope:wght@300..700', '#070B1E', '''
:root { color-scheme: dark; --line: #1D2647; --focus: #9DB4FF; --f-bg: rgb(255 255 255 / 0.07); --f-text: #F2F4FF; --f-ph: #97A0C4; --f-border: 1px solid rgb(255 255 255 / 0.14); --b-bg: #F2F4FF; --b-text: #070B1E; --note: #97A0C4; --err: #FF9B8F; --f-radius: 10px; --b-radius: 6px; --f-pad: 5px; }
body { background: #070B1E; color: #F2F4FF; font: 16px/1.6 "Manrope", system-ui, sans-serif; }
::selection { background: #9DB4FF; color: #070B1E; }
.night { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; overflow: hidden; background: radial-gradient(70% 60% at 85% 20%, #24347E 0%, transparent 60%), radial-gradient(60% 50% at 10% 100%, #3A1F6B 0%, transparent 60%); }
.hero { display: grid; gap: 8px 40px; align-items: end; }
.copy { align-self: center; padding-block: 24px 40px; }
.who { font-size: 1.5rem; font-weight: 500; letter-spacing: -0.02em; margin-bottom: 10px; }
h1 { font-size: clamp(1.7rem, 1.2rem + 2.1vw, 2.8rem); font-weight: 300; line-height: 1.2; letter-spacing: -0.03em; max-width: 17em; }
h1 em { font-style: normal; color: #9DB4FF; }
.copy p.sub { margin: 16px 0 24px; max-width: 32em; color: #A9B1D3; }
.signup { max-width: 440px; }
.shot { justify-self: center; width: min(330px, 74%); }
.shot img { filter: drop-shadow(0 0 1.5px rgb(190 205 255 / 0.5)); -webkit-mask-image: linear-gradient(#000 76%, transparent); mask-image: linear-gradient(#000 76%, transparent); }
.more { display: grid; gap: 28px 56px; padding-block: 44px 8px; }
@media (min-width: 900px) { .hero { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); } .shot { width: min(100%, 470px); justify-self: end; } .more { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
''', '''
<div class="night"><div class="wrap">{{TOP}}</div>
	<main class="wrap hero">
		<div class="copy"><p class="who" data-in>Mostafa Saher</p><h1 data-in style="--i:1">Technical instructor turning <em>complexity into understandable ideas</em> for AI and cloud.</h1><p class="sub" data-in style="--i:2">One clear step at a time. My newsletter carries what comes up after class.</p><div data-in style="--i:3">{{FORM}}</div></div>
		<div class="shot" data-in style="--i:2">{{IMG}}</div>
	</main>
</div>
<section class="wrap more">{{TOPICS_UL}}{{LINKS_ROWS}}</section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')
print('batch 4 done')
