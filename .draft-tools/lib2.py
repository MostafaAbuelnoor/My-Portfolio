import os, lib
def page(n, slug, fonts, theme, css, body, script=''):
    if script: body = body.rstrip() + '\n<script>\ndocument.addEventListener("DOMContentLoaded", () => {\n' + script.strip() + '\n});\n</script>'
    lib.page(n, slug, fonts, theme, css, body)
    p = os.path.join(lib.OUT, f'{n:02d}-{slug}.html') if n < 100 else os.path.join(lib.OUT, f'{n}-{slug}.html')
    if n >= 100: os.rename(os.path.join(lib.OUT, f'{n:02d}-{slug}.html'), p) if os.path.exists(os.path.join(lib.OUT, f'{n:02d}-{slug}.html')) and f'{n:02d}' != str(n) else None
    s = open(p).read()
    s = s.replace('<link rel="stylesheet" href="base.css">', '<link rel="stylesheet" href="base.css">\n<link rel="stylesheet" href="fx.css">')
    s = s.replace('<script src="signup.js" defer></script>', '<script src="fx.js" defer></script>\n<script src="signup.js" defer></script>')
    open(p, 'w').write(s)
