"""Phase B (owner decision, 2026-10-24): drop the Rails ActiveAdmin assets from a Rails static archive (2011, 2014).
Usage: python3 -I drop_admin_assets.py [<host>] [--apply]   (from the repo root; dry run by default; host defaults to 2011)
The archive has no admin pages; these compiled admin assets aren't referenced by any public file. Refuses to run if one is.
On 2014 the Sprockets manifest (assets/manifest-*.json, a build listing of every compiled asset) names them; it is left as is."""
import os, re, sys

APPLY = '--apply' in sys.argv[1:]
host = next((a for a in sys.argv[1:] if not a.startswith('--')), '2011.manitobaelection.ca')
ADMIN = {
    '2011.manitobaelection.ca': r'^(images/active_admin/.*|javascripts/active_admin(_vendor)?\.js|stylesheets/active_admin\.css|stylesheets/admin/.*)$',
    '2014.winnipegelection.ca': r'^assets/active_admin(/.*|-[0-9a-f]{32}\.(css|js)(\.gz)?)$',
}[host]
ADMIN = re.compile(ADMIN)
MANIFEST = re.compile(r'^assets/manifest-[0-9a-f]{32}\.json$')
files = sorted(os.path.relpath(os.path.join(r, f), 'site') for r, _, fs in os.walk('site') for f in fs)
drop = [f for f in files if ADMIN.match(f)]
if host == '2011.manitobaelection.ca':
    names = re.compile(rb'active_admin|stylesheets/admin/')
else:   # 2014: application.js carries ActiveAdmin's CSS class names, so look for the dropped files themselves
    names = re.compile(b'|'.join(re.escape(os.path.basename(f).encode()) for f in drop))
users = [f for f in files if f not in drop and not MANIFEST.match(f) and names.search(open(os.path.join('site', f), 'rb').read())]
print(f'{"APPLY" if APPLY else "dry run"}: {len(drop)} ActiveAdmin files')
for f in drop:
    print('  ', f)
if users:
    sys.exit(f'refusing: public files reference them: {users[:10]}')
if APPLY:
    for f in drop:
        os.remove(os.path.join('site', f))
    for r, ds, fs in sorted(os.walk('site'), reverse=True):   # deepest first
        if 'active_admin' in r or r.endswith('stylesheets/admin'):
            if not os.listdir(r):
                os.rmdir(r)
    run = 'drop_admin_assets.py' + ('' if host == '2011.manitobaelection.ca' else f' {host}')
    section = ('## ActiveAdmin assets removed\n\n'
               'Owner decision (Phase B, 2026-10-24): the archive doesn\'t host the Rails admin. The site never had admin pages in `site/`, '
               f'but the compiled ActiveAdmin assets were there. `python3 -I {run} --apply` removed these {len(drop)} files, '
               'which no public page references:\n\n' + ''.join(f'* `{f}`\n' for f in drop))
    if host == '2011.manitobaelection.ca':
        section += ('\n**Not admin, left as is:** `pages/13/historical-election-maps.html` loads `/stylesheets/ui-lightness/jquery-ui-1.8.16.custom.css` '
                    'and `/javascripts/jquery-ui-1.8.16.custom.min.js` for its slider. Neither file was on the server, so they 404ed on the live site too.\n')
    else:
        section += ('\n**Left as is:** the Sprockets manifest `assets/manifest-*.json` (Rails\' build listing of every compiled asset) still names them, '
                    'and `assets/application-*.js` contains ActiveAdmin\'s bundled code (CSS class names only; it loads no admin file).\n')
    r = open('README.md').read()
    i = r.find('\n## Hosting\n')
    i = i if i >= 0 else r.find('\n## Secret scan')
    open('README.md', 'w').write(r[:i + 1] + section + '\n' + r[i + 1:])
