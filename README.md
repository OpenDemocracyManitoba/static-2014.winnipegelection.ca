# 2014.winnipegelection.ca (static archive)

Static copy of **2014.winnipegelection.ca**, taken from olddroplet (`odm-nginx-ruby-php-2018`, 159.203.24.194) on 2026-10-24, before the server was retired. Static HTML export of the 2014 Winnipeg election Rails app.

`site/` is the served web root as it was on disk (2440 files), minus the files listed below. No crawl was needed: this site was already static.

## Serving

Serve `site/` as static files from the domain root.
* Rails page-cache export: links have no extension and nginx served them with `try_files $uri $uri.html`.

## Left out of `site/`

* nothing

These were left out because they were not site content: version control, PHP, or (per the archive plan) files that should not be public. The full web root is kept in a private archive repo.

## Links to internal or old hosts

None found (`upcoming.manitobaelection.ca`, `http://www.manitobaelection.ca`, `159.203.24.194`).

## Analytics removed

Google Tag Manager / Google Analytics (and the Google Ads tag that rides on `gtag.js`) were removed in Phase B of the olddroplet migration (owner decision D7, 2026-10-24) by `python3 -I strip_analytics.py 2014.winnipegelection.ca --apply`. Files changed: 1,479 HTML files, 1 `index.html.old`. IDs: `UA-17537013-1`. Each loader went together with its inline block and the comment around it. Other third-party scripts (fonts, embeds, Jetpack stats) were left as they were.

Snippet shapes removed (IDs and whitespace normalised):

* 1,480 ×

  ```html
  <script async src="https://www.googletagmanager.com/gtag/js?id=<ID>"></script><script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', '<ID>'); </script>
  ```

## ActiveAdmin assets removed

Owner decision (Phase B, 2026-10-24): the archive doesn't host the Rails admin. The site never had admin pages in `site/`, but the compiled ActiveAdmin assets were there. `python3 -I drop_admin_assets.py 2014.winnipegelection.ca --apply` removed these 22 files, which no public page references:

* `assets/active_admin-ac5375ac9cc8c00c798189ce4dd29531.css`
* `assets/active_admin-ac5375ac9cc8c00c798189ce4dd29531.css.gz`
* `assets/active_admin-ef6e7e458629040f3e84d784f28aa7cb.js`
* `assets/active_admin-ef6e7e458629040f3e84d784f28aa7cb.js.gz`
* `assets/active_admin/admin_notes_icon-468d26850cfb42dc49961d211d624489.png`
* `assets/active_admin/application-860ccf17ab05ad1b3e972c379b4d0909.js`
* `assets/active_admin/application-860ccf17ab05ad1b3e972c379b4d0909.js.gz`
* `assets/active_admin/datepicker/datepicker-header-bg-a943f37acee45474e7a3df8d759ef43b.png`
* `assets/active_admin/datepicker/datepicker-input-icon-b657b36c74072becda1495c9b77dc15c.png`
* `assets/active_admin/datepicker/datepicker-next-link-icon-0bde768951c828c245c79c5f8ed6c799.png`
* `assets/active_admin/datepicker/datepicker-nipple-1b5f50b5a084b816d0ec341bc20c8b29.png`
* `assets/active_admin/datepicker/datepicker-prev-link-icon-a4276cf9a2fd0f1659c04191ea1bb5ac.png`
* `assets/active_admin/index_list_icons/block_icon-5160bae7dffbc7f34540829fa50e0090.svg`
* `assets/active_admin/index_list_icons/blog_icon-67e1f35741ec0b9a7fa3f677564b4603.svg`
* `assets/active_admin/index_list_icons/grid_icon-912adc4674299af5295e6ae3315fc1a5.svg`
* `assets/active_admin/index_list_icons/table_icon-0cca9e722525fdbaecb12f389ef4d9f7.svg`
* `assets/active_admin/loading-9343f1c705c2df306301db1e0d568554.gif`
* `assets/active_admin/nested_menu_arrow-d9ce048353f471469e0dd1f1ba4333d0.gif`
* `assets/active_admin/nested_menu_arrow_dark-37136c90075d14f9a2f025b46b17a76b.gif`
* `assets/active_admin/orderable-1083a7abf8d1c9a2fd8288c5b315f5cb.png`
* `assets/active_admin/print-161bad35671c044ce2d93f9624b02428.css`
* `assets/active_admin/print-161bad35671c044ce2d93f9624b02428.css.gz`

**Left as is:** the Sprockets manifest `assets/manifest-*.json` (Rails' build listing of every compiled asset) still names them, and `assets/application-*.js` contains ActiveAdmin's bundled code (CSS class names only; it loads no admin file).

## Unrelated files removed

Owner decision (Phase B, 2026-10-25): files that aren't part of the site were removed by `python3 -I drop_unrelated.py 2014.winnipegelection.ca --apply` (25 files). No remaining file references them.

* `doc/` (4 files): graphviz model/controller diagrams of the Rails app (developer docs)
* `uploads/tmp/` (20 files): upload cache left behind by the image uploader
* `index.html.old` (1 file): an old copy of the home page, unreferenced

## Hosting

Served from **Cloudflare Workers static assets** (Phase B of the olddroplet migration). `wrangler.jsonc`, `.gitignore` and this section are written by `hosting.py` (`python3 -I hosting.py 2014.winnipegelection.ca <preview|routed|final>`).

* **Worker:** `static-2014-winnipegelection-ca`, account `Stungeye@gmail.com's Account`.
* **Deploy:** `npx wrangler@4.148.0 deploy` from the repo root. Only `site/` is uploaded.
* **Routes:** `2014.winnipegelection.ca/*` on zone `winnipegelection.ca`, over the existing proxied DNS record.
* **workers.dev:** off (R11). Per-version preview URLs are off (`preview_urls: false`).
* **Serving:** `html_handling: auto-trailing-slash` (`/foo` serves `foo.html`, `/foo/` serves `foo/index.html`; the other forms 307 to those) and `not_found_handling: 404-page` (the site's own `404.html`).
* **http → https:** the zone setting "Always Use HTTPS" (301 at Cloudflare's edge).
* **Redirect rules:** none.
* **Rollback:** while the old origin is up, remove `routes` from `wrangler.jsonc` and deploy (or delete the route in the dashboard); the origin serves again at once. A bad version can be rolled back with `npx wrangler@4.148.0 rollback`.

## Secret scan

The Phase A §7.2 scan (no `.git`, `.env`, `.ftpconfig`, `.htpasswd`, `debug.log`, `*.php`, `*.sql*`; no `DB_PASSWORD`/`AUTH_KEY`/private keys/`phpinfo()`/`mysql_connect` in any text file) found nothing.

Source: the export tarball `src/2014.winnipegelection.ca.tar.gz`, sha256 `edca6350a84cf8f84e76308fb7f90b3e43aff30f446e73b57adac989b349c58c`.
