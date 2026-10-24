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

## Secret scan

The Phase A §7.2 scan (no `.git`, `.env`, `.ftpconfig`, `.htpasswd`, `debug.log`, `*.php`, `*.sql*`; no `DB_PASSWORD`/`AUTH_KEY`/private keys/`phpinfo()`/`mysql_connect` in any text file) found nothing.

Source: the export tarball `src/2014.winnipegelection.ca.tar.gz`, sha256 `edca6350a84cf8f84e76308fb7f90b3e43aff30f446e73b57adac989b349c58c`.
