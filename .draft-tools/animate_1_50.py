import re, os, sys
D = '/home/user/My-Portfolio/v2/drafts/pf'
FX = ['rise', 'blur', 'flip', 'pop', 'drop']
CHARS = {2, 16, 27, 28, 41, 42}           # short name headlines read best letter by letter
AVATAR = {'face', 'av', 'ph'}               # small portraits: gentle float only
NO_PAR = {32, 38, 10}                       # portraits already positioned with translate or sticky
def classes(tag):
    m = re.search(r'class="([^"]*)"', tag); return set(m.group(1).split()) if m else set()
def add_attr(tag, attr):
    return tag[:-1] + ' ' + attr + '>' if tag.endswith('>') else tag
for f in sorted(x for x in os.listdir(D) if re.match(r'^(0[1-9]|[1-4]\d|50)-', x)):
    n = int(f[:2]); p = os.path.join(D, f); s = open(p).read()
    if 'fx.js' in s: continue
    s = s.replace('<link rel="stylesheet" href="base.css">', '<link rel="stylesheet" href="base.css">\n<link rel="stylesheet" href="fx.css">')
    s = s.replace('<script src="signup.js" defer></script>', '<script src="fx.js" defer></script>\n<script src="signup.js" defer></script>')
    # 1. headline
    m = re.search(r'<h1\b[^>]*>', s)
    if m and 'class="sr"' not in m.group(0):
        t = m.group(0).replace(' data-in', '')
        mode = 'data-split="chars" style="--stag:35ms"' if n in CHARS else 'data-split'
        if 'style=' in t and n in CHARS: mode = 'data-split="chars"'
        fx = FX[n % len(FX)]
        t = add_attr(t, mode + ('' if fx == 'rise' else f' data-fx="{fx}"'))
        s = s[:m.start()] + t + s[m.end():]
    # 2. portrait(s)
    out, last = [], 0
    for m in re.finditer(r'<img src="\.\./assets/mostafa-cutout\.webp"[^>]*>', s):
        pre = s[last:m.start()]
        ps = list(re.finditer(r'<(div|figure|span)\b[^>]*>', pre))
        if ps and not ps[-1].group(0).startswith('<span data-year'):
            pm = ps[-1]; tag = pm.group(0); cl = classes(tag)
            if 'data-par' not in tag and 'data-wipe' not in tag:
                if cl & AVATAR: new = add_attr(tag, 'data-inview') if False else tag.replace('class="', 'class="fx-float ', 1) if 'class="' in tag else tag
                else:
                    extra = 'data-wipe' + ('' if n in NO_PAR else ' data-par="14"')
                    if ' data-in' in tag: tag2 = tag.replace(' data-in', '', 1)
                    else: tag2 = tag
                    new = add_attr(tag2, extra)
                pre = pre[:pm.start()] + new + pre[pm.end():]
        out.append(pre + m.group(0)); last = m.end()
    s = ''.join(out) + s[last:]
    # 3. staggered list reveals
    def stagger(mm):
        body = mm.group(2); k = [0]
        def li(x): k[0] += 1; return f'<li data-reveal style="--i:{k[0]-1}">'
        return mm.group(1) + re.sub(r'<li>', li, body) + mm.group(3)
    s = re.sub(r'(<ul class="(?:tp|links[^"]*)"[^>]*>)(.*?)(</ul>)', stagger, s, flags=re.S)
    # 4. magnetic subscribe button
    s = s.replace('<button class="btn" type="submit">', '<button class="btn" type="submit" data-mag="0.22">')
    open(p, 'w').write(s); print('animated', f)
