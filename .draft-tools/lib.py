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
    for k, v in (('{{LINKS_INLINE}}', LINKS.replace('class="links"', 'class="links li-inline"')), ('{{LINKS_ROWS}}', LINKS.replace('class="links"', 'class="links li-rows"')), ('{{TOPICS_UL}}', '<ul class="tp">\n\t' + TOPICS + '\n</ul>'), ('{{H}}', 'I teach AI and cloud, one clear step at a time.'), ('{{INTRO}}', 'The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?”, the links I send people afterwards. My newsletter is where that goes now.'), ('{{TOP}}', '<header class="top"><b>Mostafa Saher</b><a href="#email" data-focus-signup>Subscribe</a></header>')):
        html = html.replace(k, v)
    html = html.replace('{{FORM}}', FORM).replace('{{LINKS}}', LINKS).replace('{{TOPICS}}', TOPICS).replace('{{IMG}}', IMG).replace('{{FOOT}}', FOOT)
    open(os.path.join(OUT, f'{n:02d}-{slug}.html'), 'w').write(html)

