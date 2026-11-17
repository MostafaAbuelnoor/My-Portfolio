import os
OUT = '/home/user/My-Portfolio/v2/drafts/pf'

ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
GO = '<svg class="l-go" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8"/></svg>'
TICK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

FORM = f'''<form class="signup" name="newsletter" method="POST" action="/" data-netlify="true" netlify-honeypot="company" novalidate>
	<input type="hidden" name="form-name" value="newsletter">
	<p class="sr"><label>Leave this empty <input name="company" tabindex="-1" autocomplete="off"></label></p>
	<div class="signup__stack">
		<div class="field">
			<label class="sr" for="email">Email address</label>
			<input id="email" name="email" type="email" inputmode="email" autocomplete="email" placeholder="you@example.com" required aria-describedby="note">
			<button class="btn" type="submit"><span>Subscribe</span>{ARROW}</button>
		</div>
		<p class="done" aria-hidden="true"><span class="done__tick">{TICK}</span><span>You’re on the list. I’ll write when there’s something worth reading.</span></p>
	</div>
	<p class="note" id="note" role="status">Free. Leave whenever you like.</p>
</form>'''

LINKS = f'''<ul class="links">
	<li><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener"><span class="l-name">LinkedIn</span><span class="l-meta">Mostafa Abuelnoor</span>{GO}</a></li>
	<li><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener"><span class="l-name">GitHub</span><span class="l-meta">@MostafaAbuelnoor</span>{GO}</a></li>
	<li><a href="mailto:mostafasaher@gmail.com"><span class="l-name">Email</span><span class="l-meta">mostafasaher@gmail.com</span>{GO}</a></li>
</ul>'''

TOPICS = '''<li><b>Thoughts</b><span>Notes from the classroom: what students get stuck on, and the explanation that finally made it click.</span></li>
	<li><b>Opinions</b><span>Where I stand on new models, cloud services and the hype around them.</span></li>
	<li><b>Resources</b><span>The labs, docs, courses and tools I actually use, each with a line on why.</span></li>'''

IMG = '<img src="../assets/mostafa-cutout.webp" width="1100" height="1433" alt="Mostafa Saher, smiling, arms crossed">'
FOOT = '© <span data-year>2026</span> Mostafa Saher'

def page(n, slug, fonts, theme, css, body):
    html = f'''<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<meta name="theme-color" content="{theme}">
<title>Mostafa Saher</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="base.css">
<style>
{css.strip()}
</style>
</head>

<body>
{body.strip()}
<script src="signup.js" defer></script>
</body>

</html>
'''
    html = html.replace('{{FORM}}', FORM).replace('{{LINKS}}', LINKS).replace('{{TOPICS}}', TOPICS).replace('{{IMG}}', IMG).replace('{{FOOT}}', FOOT)
    open(os.path.join(OUT, f'{n:02d}-{slug}.html'), 'w').write(html)

# 01 Spotlight — after Divesh Borse
page(1, 'spotlight', 'family=Geist:wght@400..600&family=Libre+Caslon+Text:ital@1', '#0B0B0C', '''
:root { color-scheme: dark; --focus: #fff; --f-bg: #1A1A1D; --f-text: #F2F2F3; --f-ph: #9A9AA1; --f-border: 1px solid #2E2E33; --b-bg: #F2F2F3; --b-text: #0B0B0C; --note: #9A9AA1; --err: #FF9B8F; }
body { background: #0B0B0C; color: #F2F2F3; font-family: "Geist", system-ui, sans-serif; font-size: 16px; line-height: 1.6; text-align: center; }
::selection { background: #F2F2F3; color: #0B0B0C; }
.page { max-width: 1040px; margin-inline: auto; padding: 0 20px 56px; }
.top { display: flex; justify-content: space-between; align-items: center; padding-block: 20px; font-weight: 500; }
.cta { padding: 8px 14px; border: 1px solid #2E2E33; border-radius: 999px; font-size: 0.9rem; }
h1 { margin-top: clamp(24px, 6vh, 56px); font-size: clamp(2rem, 1.2rem + 3.4vw, 3.4rem); font-weight: 500; line-height: 1.08; letter-spacing: -0.03em; }
h1 em { display: block; font-family: "Libre Caslon Text", Georgia, serif; font-weight: 400; letter-spacing: -0.01em; color: #B7B7BD; }
.stage { position: relative; width: min(540px, 100%); margin: 28px auto 0; }
.stage::before { content: ""; position: absolute; inset: 4% -14% 10%; background: radial-gradient(closest-side, #3A3A42, rgb(58 58 66 / 0) 72%); }
.stage img { position: relative; width: 100%; -webkit-mask-image: linear-gradient(#000 58%, transparent 96%); mask-image: linear-gradient(#000 58%, transparent 96%); }
.card { position: relative; max-width: 460px; margin: -120px auto 0; text-align: left; }
.card .lead { margin-bottom: 14px; text-align: center; font-size: 1.05rem; }
.note { text-align: center; }
.say { max-width: 26ch; margin: 0.5em auto 0; font-size: clamp(1.25rem, 1rem + 1vw, 1.6rem); line-height: 1.3; letter-spacing: -0.02em; color: #7C7C84; text-wrap: balance; }
.say:first-of-type { margin-top: clamp(64px, 12vh, 120px); }
.say:last-of-type { color: #F2F2F3; }
.links { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px 28px; margin-top: clamp(56px, 10vh, 96px); }
.links a { display: inline-flex; align-items: center; gap: 6px; padding-block: 6px; font-weight: 500; }
.l-meta { display: none; } .l-go { color: #7C7C84; transition: transform 200ms var(--ease-out); }
.foot { margin-top: 40px; color: #7C7C84; font-size: 0.875rem; }
@media (hover: hover) and (pointer: fine) { .links a:hover .l-go { transform: translate(2px, -2px); color: #fff; } .cta:hover { background: #1A1A1D; } }
''', '''
<div class="page">
	<header class="top"><span>Mostafa Saher</span><a class="cta" href="#email" data-focus-signup>Subscribe</a></header>
	<main>
		<h1 data-in>Hi, I’m Mostafa <em>AI &amp; Cloud Instructor</em></h1>
		<div class="stage" data-in style="--i:1">{{IMG}}</div>
		<div class="card" data-in style="--i:2">
			<p class="lead">I teach AI and cloud, one clear step at a time.</p>
			{{FORM}}
		</div>
		<p class="say">The best part of every class comes once it’s over.</p>
		<p class="say">The questions in the corridor. The “wait, so why does that work?”</p>
		<p class="say">My newsletter is where that goes now.</p>
		{{LINKS}}
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 02 Poster — after Cristian Rus
page(2, 'poster', 'family=Archivo:wght@400..800', '#E8452C', '''
:root { --red: #E8452C; --ink: #170A07; --focus: #fff; --f-bg: #fff; --b-bg: var(--red); --b-text: #170A07; --note: #B9AEA8; --err: #FFB3A6; --f-radius: 4px; --b-radius: 2px; }
body { background: #151312; color: #F4EFEA; font-family: "Archivo", system-ui, sans-serif; font-size: 16px; line-height: 1.55; }
::selection { background: #fff; color: var(--red); }
.poster { position: relative; min-height: 100svh; overflow: hidden; background: var(--red); color: var(--ink); }
.meta { position: relative; z-index: 2; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; padding: 18px 20px; font-size: 0.82rem; line-height: 1.35; }
.meta b { display: block; font-weight: 600; }
.meta a { text-decoration: underline; text-underline-offset: 3px; }
.poster img { position: absolute; left: 50%; bottom: 0; height: 74%; width: auto; max-width: none; transform: translateX(-50%); }
.name { position: absolute; z-index: 1; left: 16px; bottom: -0.06em; color: #fff; font-size: 23vw; font-weight: 800; line-height: 0.8; letter-spacing: -0.055em; }
.below { display: grid; gap: 32px 64px; max-width: 1200px; margin-inline: auto; padding: clamp(48px, 8vw, 104px) 20px; }
h2 { font-size: clamp(2rem, 1.2rem + 3.2vw, 3.6rem); font-weight: 700; line-height: 1; letter-spacing: -0.035em; text-wrap: balance; }
.below p.intro { color: #B9AEA8; margin-bottom: 24px; max-width: 34em; }
.links { margin-top: 36px; border-top: 1px solid #2E2A28; }
.links a { display: flex; align-items: baseline; gap: 12px; padding-block: 14px; border-bottom: 1px solid #2E2A28; font-weight: 600; }
.l-meta { margin-left: auto; color: #B9AEA8; font-weight: 400; font-size: 0.9rem; } .l-go { align-self: center; color: var(--red); transition: transform 200ms var(--ease-out); }
.foot { padding: 0 20px 32px; max-width: 1200px; margin-inline: auto; color: #8C827C; font-size: 0.85rem; }
@media (hover: hover) and (pointer: fine) { .links a:hover .l-go { transform: translate(2px, -2px); } }
@media (min-width: 800px) {
	.meta { grid-template-columns: repeat(4, minmax(0, 1fr)); padding: 22px 32px; }
	.poster img { height: 86%; }
	.name { left: 28px; font-size: 19vw; }
	.below { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); padding-inline: 32px; }
	.foot { padding-inline: 32px; }
}
@media (prefers-reduced-motion: no-preference) { .name { animation: up 900ms var(--ease-out) 200ms backwards; } @keyframes up { from { transform: translateY(30%); opacity: 0; } } }
''', '''
<header class="poster">
	<div class="meta">
		<p><b>Mostafa Saher</b>Technical instructor</p>
		<p><b>Teaching</b>AI and cloud</p>
		<p><b>Newsletter</b><a href="#email" data-focus-signup>Subscribe</a></p>
		<p><b>Elsewhere</b><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a>, <a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a></p>
	</div>
	{{IMG}}
	<h1 class="name">Mostafa</h1>
</header>
<main class="below">
	<h2>I teach AI and cloud, one clear step at a time.</h2>
	<div>
		<p class="intro">The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?”, the links I send people afterwards. My newsletter is where that goes now.</p>
		{{FORM}}
		{{LINKS}}
	</div>
</main>
<footer class="foot">{{FOOT}}</footer>
''')

# 03 Flanked portrait — after Alexander Lehmann
page(3, 'flanked', 'family=Instrument+Serif&family=Geist:wght@400..600', '#F3F2EE', '''
:root { --focus: #1D4ED8; --f-bg: #fff; --f-border: 1px solid #DCDAD2; --f-radius: 999px; --b-radius: 999px; --b-bg: #1D4ED8; --b-text: #fff; --note: #6A685F; }
body { background: #F3F2EE; color: #151513; font-family: "Geist", system-ui, sans-serif; font-size: 16px; line-height: 1.6; }
::selection { background: #151513; color: #F3F2EE; }
.page { max-width: 1240px; margin-inline: auto; padding: 0 20px 56px; }
.top { display: flex; justify-content: space-between; align-items: center; padding-block: 20px; font-weight: 500; }
.top a { font-size: 0.92rem; text-decoration: underline; text-underline-offset: 4px; }
.hero { display: grid; grid-template-columns: minmax(0, 1fr); justify-items: center; text-align: center; margin-top: 12px; }
h1 { display: contents; font-family: "Instrument Serif", Georgia, serif; font-weight: 400; }
h1 span { font-family: inherit; font-size: clamp(3rem, 1.4rem + 7vw, 6rem); line-height: 0.95; letter-spacing: -0.025em; }
.l { order: 1; } figure { order: 2; width: min(360px, 78%); margin-block: 8px; } .r { order: 3; }
figure img { width: 100%; filter: grayscale(1) contrast(1.06); -webkit-mask-image: linear-gradient(#000 70%, transparent); mask-image: linear-gradient(#000 70%, transparent); }
.ask { position: relative; max-width: 460px; margin: 20px auto 0; }
.ask .note { text-align: center; }
.two { display: grid; gap: 20px 64px; margin-top: clamp(64px, 10vw, 120px); padding-top: 28px; border-top: 1px solid #DCDAD2; }
h2 { font-family: "Instrument Serif", Georgia, serif; font-size: 2.2rem; font-weight: 400; line-height: 1.05; letter-spacing: -0.02em; }
.two p { color: #55534B; max-width: 36em; font-size: 1.05rem; }
.topics li { display: grid; gap: 2px; padding-block: 16px; border-bottom: 1px solid #DCDAD2; }
.topics li:first-child { padding-top: 0; }
.topics b { font-family: "Instrument Serif", Georgia, serif; font-weight: 400; font-size: 1.7rem; line-height: 1.1; }
.topics span { color: #55534B; }
.links { display: flex; flex-wrap: wrap; gap: 8px 28px; }
.links a { display: inline-flex; align-items: center; gap: 6px; font-weight: 500; text-decoration: underline; text-decoration-color: #C9C6BB; text-underline-offset: 4px; }
.l-meta { display: none; } .l-go { color: #8A877C; transition: transform 200ms var(--ease-out); }
.foot { margin-top: 56px; color: #6A685F; font-size: 0.875rem; }
@media (hover: hover) and (pointer: fine) { .links a:hover .l-go { transform: translate(2px, -2px); } }
@media (min-width: 860px) {
	.hero { grid-template-columns: minmax(0, 1fr) minmax(280px, 31%) minmax(0, 1fr); align-items: start; column-gap: 8px; }
	.l { text-align: right; padding-top: 19%; margin-right: -6%; position: relative; z-index: 1; }
	.r { text-align: left; padding-top: 19%; margin-left: -6%; position: relative; z-index: 1; }
	figure { width: 100%; margin: 0; }
	.ask { margin-top: -56px; }
	.two { grid-template-columns: 300px minmax(0, 1fr); }
}
''', '''
<div class="page">
	<header class="top"><span>Mostafa Saher</span><a href="#email" data-focus-signup>Newsletter</a></header>
	<main>
		<div class="hero">
			<h1><span class="l" data-in>AI and cloud,</span> <span class="r" data-in style="--i:2">made clear.</span></h1>
			<figure data-in style="--i:1">{{IMG}}</figure>
		</div>
		<div class="ask" data-in style="--i:3">{{FORM}}</div>
		<section class="two">
			<h2>After class</h2>
			<p>I’m Mostafa, a technical instructor. The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?”, the links I send people afterwards. My newsletter is where that goes now.</p>
		</section>
		<section class="two">
			<h2>What I write about</h2>
			<ul class="topics">
	{{TOPICS}}
			</ul>
		</section>
		<section class="two">
			<h2>Elsewhere</h2>
			{{LINKS}}
		</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 04 Swiss wordmark — after Łukasz Żydek
page(4, 'wordmark', 'family=Host+Grotesk:wght@400..600', '#FFFFFF', '''
:root { --focus: #000; --f-bg: #F0F0EE; --f-radius: 0; --b-radius: 0; --b-bg: #000; --b-text: #fff; --note: #666; --f-pad: 0; }
body { background: #fff; color: #000; font-family: "Host Grotesk", system-ui, sans-serif; font-size: 15px; line-height: 1.4; }
::selection { background: #000; color: #fff; }
.page { min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto auto; gap: 28px; padding: 16px; overflow: hidden; }
.top { display: grid; grid-template-columns: minmax(0, 1fr) clamp(96px, 26vw, 200px); gap: 20px; align-items: start; }
h1 { max-width: 19em; font-size: clamp(1.25rem, 1rem + 1.2vw, 1.75rem); font-weight: 500; line-height: 1.15; letter-spacing: -0.025em; }
.shot { aspect-ratio: 4 / 5; overflow: hidden; background: #E6E6E3; }
.shot img { width: 118%; max-width: none; margin: 6% 0 0 -9%; filter: grayscale(1) contrast(1.05); }
.mid { align-self: center; max-width: 440px; }
.mid p.lead { margin-bottom: 12px; max-width: 30em; color: #444; }
.field { gap: 0; }
.cols { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; font-size: 0.82rem; }
.cols h2 { font-size: inherit; font-weight: 400; color: #777; }
.links a { display: inline-flex; gap: 4px; align-items: center; text-decoration: underline; text-underline-offset: 3px; }
.l-meta { display: none; } .l-go { width: 12px; height: 12px; }
.mark { font-size: 16.6vw; font-weight: 500; line-height: 0.74; letter-spacing: -0.06em; white-space: nowrap; margin: 0 0 -0.03em -0.04em; }
@media (min-width: 800px) {
	.page { padding: 20px 24px; }
	.cols { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}
@media (prefers-reduced-motion: no-preference) { .mark { animation: mark 1000ms var(--ease-out) 150ms backwards; } @keyframes mark { from { clip-path: inset(100% 0 0 0); transform: translateY(18%); } to { clip-path: inset(-10% 0 -10% 0); } } }
''', '''
<div class="page">
	<header class="top">
		<h1 data-in>Mostafa Saher is a technical instructor teaching AI and cloud, one clear step at a time.</h1>
		<div class="shot" data-in style="--i:1">{{IMG}}</div>
	</header>
	<main class="mid" data-in style="--i:2">
		<p class="lead">Newsletter: notes from the classroom, where I stand on the hype, and the resources I’d hand a student.</p>
		{{FORM}}
	</main>
	<div class="cols">
		<div><h2>Role</h2><p>Technical instructor</p></div>
		<div><h2>Subjects</h2><p>AI, cloud</p></div>
		<div><h2>Elsewhere</h2>{{LINKS}}</div>
		<div><h2>Copyright</h2><p>{{FOOT}}</p></div>
	</div>
	<p class="mark" aria-hidden="true">MOSTAFA ©</p>
</div>
''')

# 05 Lower third — after Fabio Freire
page(5, 'lower-third', 'family=Urbanist:wght@300..600', '#101110', '''
:root { color-scheme: dark; --lime: #C8F250; --focus: var(--lime); --f-bg: #1C1D1B; --f-text: #F2F2EE; --f-ph: #9B9C96; --f-border: 1px solid #30322D; --b-bg: var(--lime); --b-text: #101110; --note: #9B9C96; --err: #FF9B8F; --f-radius: 14px; --b-radius: 9px; }
body { background: #101110; color: #F2F2EE; font-family: "Urbanist", system-ui, sans-serif; font-size: 17px; line-height: 1.5; }
::selection { background: var(--lime); color: #101110; }
.page { max-width: 1320px; margin-inline: auto; padding: 0 20px; }
.top { display: flex; justify-content: space-between; align-items: center; gap: 16px; padding-block: 20px; }
.top b { font-weight: 600; }
.links { display: flex; gap: 20px; font-size: 0.95rem; color: #B9BAB3; }
.l-meta, .l-go { display: none; }
.hero { position: relative; display: grid; grid-template-columns: minmax(0, 1fr); gap: 8px; padding-bottom: 40px; }
.shot { position: relative; order: -1; height: 44svh; justify-self: center; aspect-ratio: 1100 / 1433; }
.shot::before { content: ""; position: absolute; inset: 0 -30% 0; background: radial-gradient(closest-side, #3B4030, rgb(59 64 48 / 0) 72%); }
.shot img { position: relative; height: 100%; width: auto; max-width: none; -webkit-mask-image: linear-gradient(#000 75%, transparent); mask-image: linear-gradient(#000 75%, transparent); }
.pre { color: #9B9C96; font-size: 0.95rem; }
h1 { margin: 6px 0 20px; font-size: clamp(3.2rem, 1.6rem + 8vw, 8.2rem); font-weight: 300; line-height: 0.92; letter-spacing: -0.04em; }
.intro { max-width: 30em; margin-bottom: 20px; color: #B9BAB3; }
.signup { max-width: 440px; }
.foot { padding-block: 0 28px; color: #7E7F79; font-size: 0.875rem; }
@media (hover: hover) and (pointer: fine) { .links a:hover { color: #fff; } }
@media (min-width: 900px) {
	.page { padding-inline: 36px; }
	.hero { grid-template-columns: minmax(0, 1.25fr) minmax(0, 0.75fr); align-items: end; min-height: calc(100svh - 120px); }
	.shot { order: 0; height: min(78svh, 760px); justify-self: end; align-self: end; }
}
''', '''
<div class="page">
	<header class="top"><b>Mostafa Saher</b>{{LINKS}}</header>
	<main class="hero">
		<div class="copy">
			<p class="pre" data-in>I teach it one clear step at a time</p>
			<h1 data-in style="--i:1">ai &amp; cloud<br>instructor</h1>
			<p class="intro" data-in style="--i:2">The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?” My newsletter is where that goes now.</p>
			<div data-in style="--i:3">{{FORM}}</div>
		</div>
		<div class="shot" data-in style="--i:2">{{IMG}}</div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 06 Sky — after Albiona Hoti
page(6, 'sky', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800', '#2F6FE4', '''
:root { --navy: #0C1D4A; --focus: var(--navy); --f-bg: #fff; --f-radius: 999px; --b-radius: 999px; --b-bg: var(--navy); --b-text: #fff; --note: #1B2F66; --err: #8A1608; }
body { background: #FCE9D2; color: var(--navy); font-family: "Bricolage Grotesque", system-ui, sans-serif; font-size: 17px; line-height: 1.5; }
::selection { background: var(--navy); color: #fff; }
.sky { position: relative; min-height: 100svh; overflow: hidden; display: flex; flex-direction: column; padding: 0 20px 28px; background: linear-gradient(180deg, #2F6FE4 0%, #6FA6F2 38%, #BFD9FA 68%, #FCE9D2 100%); }
.top { display: flex; justify-content: space-between; align-items: center; padding-block: 20px; color: #fff; font-weight: 600; }
.top a { padding: 7px 14px; border-radius: 999px; background: #fff; color: var(--navy); font-size: 0.92rem; }
h1 { position: relative; color: #fff; font-size: clamp(4.2rem, 1rem + 17vw, 13.5rem); font-weight: 700; line-height: 0.8; letter-spacing: -0.055em; margin-top: 8px; }
.copy { position: relative; z-index: 2; margin-top: 28px; max-width: 460px; }
.copy p.lead { margin-bottom: 18px; font-size: 1.3rem; font-weight: 500; line-height: 1.25; letter-spacing: -0.02em; }
.field { box-shadow: 0 10px 30px -14px rgb(12 29 74 / 0.5); }
.links { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 22px; }
.links a { display: inline-flex; align-items: center; gap: 6px; padding: 8px 14px; border-radius: 999px; background: rgb(255 255 255 / 0.6); font-weight: 500; font-size: 0.95rem; transition: background-color 160ms ease; }
.l-meta { display: none; } .l-go { transition: transform 200ms var(--ease-out); }
.shot { position: relative; z-index: 1; width: min(84%, 380px); margin: 28px auto -28px; }
.foot { padding: 18px 20px; font-size: 0.875rem; color: #6B5A45; }
@media (hover: hover) and (pointer: fine) { .links a:hover { background: #fff; } .links a:hover .l-go { transform: translate(2px, -2px); } }
@media (min-width: 900px) {
	.sky { padding: 0 40px 40px; }
	.copy { margin-top: auto; }
	.shot { position: absolute; right: 4%; bottom: 0; width: auto; height: 76%; margin: 0; }
	.shot img { height: 100%; width: auto; max-width: none; }
}
''', '''
<main class="sky">
	<header class="top"><span>AI and cloud instructor</span><a href="#email" data-focus-signup>Subscribe</a></header>
	<h1 data-in>mostafa<br>saher</h1>
	<div class="copy" data-in style="--i:2">
		<p class="lead">I teach AI and cloud, one clear step at a time. Get my notes from the classroom by email.</p>
		{{FORM}}
		{{LINKS}}
	</div>
	<div class="shot" data-in style="--i:1">{{IMG}}</div>
</main>
<footer class="foot">{{FOOT}}</footer>
''')

# 07 Friendly — after Jaycee Day
page(7, 'friendly', 'family=Be+Vietnam+Pro:wght@400;500;600;700', '#F3EEFB', '''
:root { --purple: #5B34C4; --focus: var(--purple); --f-bg: #F3EEFB; --f-radius: 16px; --b-radius: 11px; --b-bg: var(--purple); --b-text: #fff; --note: #6A6480; }
body { background: #F3EEFB; color: #1D1830; font-family: "Be Vietnam Pro", system-ui, sans-serif; font-size: 16px; line-height: 1.6; }
::selection { background: var(--purple); color: #fff; }
.col { max-width: 640px; margin-inline: auto; padding: clamp(32px, 8vh, 80px) 20px 48px; display: grid; gap: 16px; }
.me { display: flex; align-items: center; gap: 18px; margin-bottom: 8px; }
.av { flex: none; width: 88px; height: 88px; border-radius: 28px; overflow: hidden; background: #D9C9FA; }
.av img { width: 170%; max-width: none; margin: 4% 0 0 -36%; }
h1 { font-size: 1.9rem; font-weight: 700; line-height: 1.15; letter-spacing: -0.03em; }
.me p { color: #5A5470; font-size: 1.05rem; }
.bio { font-size: 1.08rem; color: #3A3450; margin-bottom: 8px; }
.card { padding: 24px; border-radius: 24px; background: #fff; }
.card.note-card { background: #FFF2B8; }
h2 { font-size: 1.15rem; font-weight: 600; letter-spacing: -0.01em; margin-bottom: 12px; }
.topics li { padding-block: 10px; border-top: 1px solid rgb(29 24 48 / 0.12); }
.topics li:last-child { padding-bottom: 0; }
.topics b { font-weight: 600; margin-right: 6px; }
.topics span { color: #4A4420; }
.card p.lead { color: #5A5470; margin-bottom: 14px; }
.links { display: flex; flex-wrap: wrap; gap: 10px; }
.links a { display: inline-flex; align-items: center; gap: 8px; padding: 12px 18px; border-radius: 999px; background: #fff; font-weight: 600; transition: transform 160ms var(--ease-out); }
.links a:active { transform: scale(0.97); }
.l-meta { display: none; } .l-go { color: var(--purple); transition: transform 200ms var(--ease-out); }
.foot { color: #6A6480; font-size: 0.875rem; margin-top: 16px; }
@media (hover: hover) and (pointer: fine) { .links a:hover .l-go { transform: translate(2px, -2px); } }
''', '''
<main class="col">
	<header class="me" data-in>
		<div class="av">{{IMG}}</div>
		<div><h1>I’m Mostafa.</h1><p>Welcome to my corner of AI and cloud.</p></div>
	</header>
	<p class="bio" data-in style="--i:1">I’m a technical instructor. The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?”, the links I send people afterwards.</p>
	<section class="card" data-in style="--i:2">
		<h2>Get it by email</h2>
		<p class="lead">My newsletter is where all of that goes now.</p>
		{{FORM}}
	</section>
	<section class="card note-card" data-in style="--i:3">
		<h2>What I’m writing</h2>
		<ul class="topics">
	{{TOPICS}}
		</ul>
	</section>
	<nav data-in style="--i:4" aria-label="Elsewhere">{{LINKS}}</nav>
	<footer class="foot">{{FOOT}}</footer>
</main>
''')

# 08 Index — after Craig Weiss
page(8, 'index', 'family=Geist:wght@400..600&family=Geist+Mono:wght@400', '#0C0C0C', '''
:root { color-scheme: dark; --line: #242424; --dim: #8D8D8D; --focus: #EDEDED; --f-bg: #141414; --f-text: #EDEDED; --f-ph: #8D8D8D; --f-border: 1px solid var(--line); --f-radius: 10px; --b-radius: 6px; --b-bg: #EDEDED; --b-text: #0C0C0C; --note: var(--dim); --err: #FF9B8F; }
body { background: #0C0C0C; color: #EDEDED; font-family: "Geist", system-ui, sans-serif; font-size: 15px; line-height: 1.6; }
::selection { background: #EDEDED; color: #0C0C0C; }
.col { max-width: 660px; margin-inline: auto; padding: clamp(40px, 10vh, 96px) 20px 56px; }
.me { display: flex; align-items: center; gap: 12px; }
.av { flex: none; width: 44px; height: 44px; border-radius: 50%; overflow: hidden; background: #2A2A2A; }
.av img { width: 190%; max-width: none; margin: 2% 0 0 -45%; }
h1 { font-size: 1rem; font-weight: 500; }
.bio { margin-top: 20px; color: #B4B4B4; }
.box { margin-top: 28px; border: 1px solid var(--line); border-radius: 12px; }
.row { display: grid; grid-template-columns: minmax(0, 1fr); gap: 4px; padding: 14px 16px; border-top: 1px solid var(--line); }
.row:first-child { border-top: 0; }
.k { font-family: "Geist Mono", ui-monospace, monospace; font-size: 0.78rem; color: var(--dim); padding-top: 2px; }
.v span { color: #B4B4B4; }
h2 { margin: 36px 0 -16px 2px; font-family: "Geist Mono", ui-monospace, monospace; font-size: 0.78rem; font-weight: 400; color: var(--dim); }
.links a { display: flex; align-items: baseline; gap: 12px; padding: 14px 16px; border-top: 1px solid var(--line); transition: background-color 160ms ease; }
.links li:first-child a { border-top: 0; }
.l-meta { margin-left: auto; color: var(--dim); font-family: "Geist Mono", ui-monospace, monospace; font-size: 0.78rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; min-width: 0; }
.l-go { align-self: center; flex: none; color: var(--dim); transition: transform 200ms var(--ease-out); }
.foot { margin-top: 32px; color: var(--dim); font-family: "Geist Mono", ui-monospace, monospace; font-size: 0.78rem; }
@media (hover: hover) and (pointer: fine) { .links a:hover { background: #141414; } .links a:hover .l-go { transform: translate(2px, -2px); color: #EDEDED; } }
@media (min-width: 560px) { .row { grid-template-columns: 110px minmax(0, 1fr); gap: 16px; } }
''', '''
<main class="col">
	<header class="me" data-in>
		<div class="av">{{IMG}}</div>
		<h1>Mostafa Saher</h1>
	</header>
	<p class="bio" data-in style="--i:1">Technical instructor. I teach AI and cloud, one clear step at a time. The best part of every class comes once it’s over, and my newsletter is where that goes now.</p>

	<h2>newsletter</h2>
	<div class="box" data-in style="--i:2">
		<div class="row"><span class="k">subscribe</span><div class="v">{{FORM}}</div></div>
		<div class="row"><span class="k">thoughts</span><p class="v"><span>Notes from the classroom: what students get stuck on, and the explanation that finally made it click.</span></p></div>
		<div class="row"><span class="k">opinions</span><p class="v"><span>Where I stand on new models, cloud services and the hype around them.</span></p></div>
		<div class="row"><span class="k">resources</span><p class="v"><span>The labs, docs, courses and tools I actually use, each with a line on why.</span></p></div>
	</div>

	<h2>elsewhere</h2>
	<nav class="box" data-in style="--i:3" aria-label="Elsewhere">{{LINKS}}</nav>
	<footer class="foot">{{FOOT}}</footer>
</main>
''')

# 09 Columns — after Jimi Filipovski
page(9, 'columns', 'family=Archivo:wght@500..700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600', '#C9C2B6', '''
:root { --focus: #161512; --f-bg: #F4F1EA; --f-radius: 6px; --b-radius: 3px; --b-bg: #C9C2B6; --b-text: #161512; --note: #A8A297; --err: #FFB3A6; --f-pad: 5px; }
body { background: #C9C2B6; color: #161512; font-family: "Source Serif 4", Georgia, serif; font-size: 16px; line-height: 1.5; }
::selection { background: #161512; color: #C9C2B6; }
.page { max-width: 1280px; margin-inline: auto; padding: 14px 16px 40px; }
.tag { font-family: "Archivo", sans-serif; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; }
h1 { margin-top: 10px; font-family: "Archivo", sans-serif; font-size: clamp(2.1rem, 1rem + 4.6vw, 4.4rem); font-weight: 700; line-height: 0.98; letter-spacing: -0.04em; max-width: 16em; text-wrap: balance; }
.cols { display: grid; grid-template-columns: minmax(0, 1fr); gap: 24px; margin-top: 24px; font-size: 0.98rem; }
.cols h2 { font-size: inherit; font-weight: 600; }
.cols p + p { margin-top: 0.8em; }
.topics li { margin-top: 0.4em; } .topics b { font-weight: 600; } .topics b::after { content: ". "; }
.links a { display: inline-flex; align-items: center; gap: 4px; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 3px; }
.l-meta { display: none; } .l-go { width: 13px; height: 13px; }
.lower { display: grid; grid-template-columns: minmax(0, 1fr); gap: 12px; margin-top: 36px; }
.shot { background: #B4AC9E; overflow: hidden; aspect-ratio: 4 / 3; display: flex; justify-content: center; align-items: flex-end; }
.shot img { height: 96%; width: auto; max-width: none; }
.news { display: flex; flex-direction: column; justify-content: space-between; gap: 28px; padding: clamp(22px, 3vw, 36px); background: #161512; color: #EDE8DE; font-family: "Archivo", sans-serif; }
.news h2 { font-size: clamp(1.7rem, 1rem + 2.2vw, 2.6rem); font-weight: 700; line-height: 1; letter-spacing: -0.035em; }
.news p.lead { margin-top: 10px; color: #A8A297; font-family: "Source Serif 4", Georgia, serif; max-width: 30em; }
.news { --focus: #C9C2B6; }
.foot { margin-top: 20px; font-size: 0.85rem; }
@media (min-width: 860px) {
	.page { padding: 18px 24px 40px; }
	.cols { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 24px; }
	.cols .wide { grid-column: span 2; column-count: 2; column-gap: 24px; }
	.lower { grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); }
	.shot { aspect-ratio: auto; min-height: 460px; }
}
''', '''
<div class="page">
	<p class="tag">Mostafa Saher</p>
	<main>
		<h1 data-in>I teach AI and cloud, one clear step at a time.</h1>
		<div class="cols" data-in style="--i:1">
			<div class="wide">
				<p>I am a technical instructor, and I teach AI and cloud for a living. The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?”, the links I send people afterwards.</p>
				<p>My newsletter is where that goes now. Each one carries my thoughts from teaching, an honest opinion on the latest models and cloud services, and the resources I’d actually hand a student.</p>
			</div>
			<div><h2>Contact</h2>{{LINKS}}</div>
			<div><h2>Writing</h2><ul class="topics">
	{{TOPICS}}
			</ul></div>
		</div>
		<div class="lower" data-in style="--i:2">
			<div class="shot">{{IMG}}</div>
			<section class="news">
				<div><h2>Get the newsletter.</h2><p class="lead">Everything that used to stay in the corridor after class, sent to your inbox.</p></div>
				{{FORM}}
			</section>
		</div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 10 Split — after Tom Johnson
page(10, 'split', 'family=Manrope:wght@400..700', '#0D0D0D', '''
:root { --focus: #fff; --f-bg: #1B1B1B; --f-text: #F4F4F2; --f-ph: #9A9A96; --f-border: 1px solid #303030; --f-radius: 12px; --b-radius: 7px; --b-bg: #F4F4F2; --b-text: #0D0D0D; --note: #9A9A96; --err: #FF9B8F; }
body { background: #0D0D0D; color: #F4F4F2; font-family: "Manrope", system-ui, sans-serif; font-size: 16px; line-height: 1.6; }
::selection { background: #F4F4F2; color: #0D0D0D; }
.split { display: grid; grid-template-columns: minmax(0, 1fr); }
.panel { position: relative; overflow: hidden; height: 62svh; background: #D8D8D4; display: flex; justify-content: center; align-items: flex-end; }
.panel img { height: 94%; width: auto; max-width: none; }
.side { display: flex; flex-direction: column; gap: 40px; padding: 28px 20px 32px; }
.side b.name { font-weight: 700; letter-spacing: -0.01em; }
h1 { font-size: clamp(1.9rem, 1.3rem + 2vw, 2.7rem); font-weight: 600; line-height: 1.08; letter-spacing: -0.035em; text-wrap: balance; }
.side p.intro { margin: 16px 0 22px; color: #B5B5B0; }
.links a { display: flex; align-items: center; justify-content: space-between; padding-block: 12px; border-top: 1px solid #262626; font-weight: 600; }
.links li:last-child a { border-bottom: 1px solid #262626; }
.l-meta { display: none; } .l-go { color: #9A9A96; transition: transform 200ms var(--ease-out); }
.foot { color: #7C7C78; font-size: 0.85rem; }
@media (hover: hover) and (pointer: fine) { .links a:hover .l-go { transform: translate(2px, -2px); color: #fff; } }
@media (min-width: 900px) {
	.split { grid-template-columns: minmax(380px, 36%) minmax(0, 1fr); min-height: 100svh; }
	.side { order: -1; justify-content: space-between; padding: 32px 36px; min-height: 100svh; }
	.panel { position: sticky; top: 0; height: 100svh; }
	.panel img { height: 92%; }
}
@media (prefers-reduced-motion: no-preference) { .panel img { animation: stand 1000ms var(--ease-out) 100ms backwards; } @keyframes stand { from { transform: translateY(6%); opacity: 0; } } }
''', '''
<div class="split">
	<div class="panel">{{IMG}}</div>
	<main class="side">
		<b class="name" data-in>Mostafa Saher</b>
		<div data-in style="--i:1">
			<h1>I teach AI and cloud, one clear step at a time.</h1>
			<p class="intro">The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?” My newsletter is where that goes now.</p>
			{{FORM}}
		</div>
		<div data-in style="--i:2">
			{{LINKS}}
			<p class="foot" style="margin-top:20px">{{FOOT}}</p>
		</div>
	</main>
</div>
''')

# Index of drafts
items = [
 ('01-spotlight', 'Spotlight', 'Dark and centred, portrait fading into the page', 'Divesh Borse'),
 ('02-poster', 'Poster', 'Full red poster with your first name across it', 'Cristian Rus'),
 ('03-flanked', 'Flanked', 'Serif headline split either side of a black-and-white portrait', 'Alexander Lehmann'),
 ('04-wordmark', 'Wordmark', 'Swiss white page with a giant name along the bottom', 'Łukasz Żydek'),
 ('05-lower-third', 'Lower third', 'Dark, with a huge light lowercase title and a lime button', 'Fabio Freire'),
 ('06-sky', 'Sky', 'Blue-to-dawn sky with your name in huge lowercase', 'Albiona Hoti'),
 ('07-friendly', 'Friendly', 'Soft lavender page with rounded cards', 'Jaycee Day'),
 ('08-index', 'Index', 'Compact dark developer-style index', 'Craig Weiss'),
 ('09-columns', 'Columns', 'Taupe editorial page with a bold headline over text columns', 'Jimi Filipovski'),
 ('10-split', 'Split', 'Black text column beside a full-height portrait panel', 'Tom Johnson'),
]
rows = '\n'.join(f'\t\t<li><a href="{f}.html"><span class="n">{f[:2]}</span><span><b>{t}</b><span class="d">{d}. After {r} on Pafolios.</span></span></a></li>' for f, t, d, r in items)
open(os.path.join(OUT, 'index.html'), 'w').write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Drafts</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ margin: 0; font: 16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif; }}
main {{ max-width: 620px; margin-inline: auto; padding: 48px 20px; }}
h1 {{ font-size: 1.4rem; margin: 0 0 4px; letter-spacing: -0.02em; }}
p {{ margin: 0 0 24px; opacity: 0.7; }}
ul {{ list-style: none; margin: 0; padding: 0; }}
a {{ display: flex; gap: 16px; padding: 14px 0; border-top: 1px solid color-mix(in srgb, currentColor 16%, transparent); color: inherit; text-decoration: none; }}
.n {{ font-variant-numeric: tabular-nums; opacity: 0.55; }}
.d {{ display: block; opacity: 0.7; font-size: 0.93rem; }}
</style>
</head>
<body>
<main>
	<h1>Ten drafts</h1>
	<p>Each one is modelled on a portfolio from pafolios.com.</p>
	<ul>
{rows}
	</ul>
</main>
</body>
</html>
''')
print('ok', sorted(os.listdir(OUT)))
