### So, here is what you need to start

```
docker-compose up --build

docker-compose logs -f backuprestore
```

And this is an example of what you should to get instead

```
Attaching to hackattic_backuprestore_1
backuprestore_1  | + apk add curl netcat-openbsd jq postgresql
backuprestore_1  | fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/main/x86_64/APKINDEX.tar.gz
backuprestore_1  | fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/community/x86_64/APKINDEX.tar.gz
backuprestore_1  | (1/27) Installing ca-certificates (20211220-r0)
backuprestore_1  | (2/27) Installing brotli-libs (1.0.9-r6)
backuprestore_1  | (3/27) Installing nghttp2-libs (1.47.0-r0)
backuprestore_1  | (4/27) Installing libcurl (7.83.1-r1)
backuprestore_1  | (5/27) Installing curl (7.83.1-r1)
backuprestore_1  | (6/27) Installing oniguruma (6.9.8-r0)
backuprestore_1  | (7/27) Installing jq (1.6-r1)
backuprestore_1  | (8/27) Installing libmd (1.0.4-r0)
backuprestore_1  | (9/27) Installing libbsd (0.11.6-r2)
backuprestore_1  | (10/27) Installing netcat-openbsd (1.130-r3)
backuprestore_1  | (11/27) Installing postgresql-common (1.1-r0)
backuprestore_1  | Executing postgresql-common-1.1-r0.pre-install
backuprestore_1  | (12/27) Installing libpq (14.4-r0)
backuprestore_1  | (13/27) Installing ncurses-terminfo-base (6.3_p20220521-r0)
backuprestore_1  | (14/27) Installing ncurses-libs (6.3_p20220521-r0)
backuprestore_1  | (15/27) Installing readline (8.1.2-r0)
backuprestore_1  | (16/27) Installing postgresql14-client (14.4-r0)
backuprestore_1  | (17/27) Installing tzdata (2022a-r0)
backuprestore_1  | (18/27) Installing icu-data-en (71.1-r2)
backuprestore_1  | Executing icu-data-en-71.1-r2.post-install
backuprestore_1  | *
backuprestore_1  | * If you need ICU with non-English locales and legacy charset support, install
backuprestore_1  | * package icu-data-full.
backuprestore_1  | *
backuprestore_1  | (19/27) Installing libgcc (11.2.1_git20220219-r2)
backuprestore_1  | (20/27) Installing libstdc++ (11.2.1_git20220219-r2)
backuprestore_1  | (21/27) Installing icu-libs (71.1-r2)
backuprestore_1  | (22/27) Installing gdbm (1.23-r0)
backuprestore_1  | (23/27) Installing libsasl (2.1.28-r0)
backuprestore_1  | (24/27) Installing libldap (2.6.2-r0)
backuprestore_1  | (25/27) Installing xz-libs (5.2.5-r1)
backuprestore_1  | (26/27) Installing libxml2 (2.9.14-r0)
backuprestore_1  | (27/27) Installing postgresql14 (14.4-r0)
backuprestore_1  | Executing postgresql14-14.4-r0.post-install
backuprestore_1  | *
backuprestore_1  | * If you want to use JIT in PostgreSQL, install postgresql14-jit or
backuprestore_1  | * postgresql-jit (if you didn't install specific major version of postgresql).
backuprestore_1  | *
backuprestore_1  | Executing busybox-1.35.0-r13.trigger
backuprestore_1  | Executing ca-certificates-20211220-r0.trigger
backuprestore_1  | Executing postgresql-common-1.1-r0.trigger
backuprestore_1  | * Setting postgresql14 as the default version
backuprestore_1  | OK: 41 MiB in 41 packages
backuprestore_1  | + nc -zv db2backup 5432
backuprestore_1  | Connection to db2backup 5432 port [tcp/postgresql] succeeded!
backuprestore_1  | + nc -zv db2restore 5432
backuprestore_1  | Connection to db2restore 5432 port [tcp/postgresql] succeeded!
backuprestore_1  | + nc -zv endpoints 5000
backuprestore_1  | Connection to endpoints 5000 port [tcp/*] succeeded!
backuprestore_1  | + curl -XGET 'http://endpoints:5000/challenges/backup_restore/problem?access_token=x'
backuprestore_1  | + json='{ "dump": "LS0KLS0gUG9zdGdyZVNRTCBkYXRhYmFzZSBkdW1wCi0tCgotLSBEdW1wZWQgZnJvbSBkYXRhYmFzZSB2ZXJzaW9uIDE0LjMKLS0gRHVtcGVkIGJ5IHBnX2R1bXAgdmVyc2lvbiAxNC40CgpTRVQgc3RhdGVtZW50X3RpbWVvdXQgPSAwOwpTRVQgbG9ja190aW1lb3V0ID0gMDsKU0VUIGlkbGVfaW5fdHJhbnNhY3Rpb25fc2Vzc2lvbl90aW1lb3V0ID0gMDsKU0VUIGNsaWVudF9lbmNvZGluZyA9ICdVVEY4JzsKU0VUIHN0YW5kYXJkX2NvbmZvcm1pbmdfc3RyaW5ncyA9IG9uOwpTRUxFQ1QgcGdfY2F0YWxvZy5zZXRfY29uZmlnKCdzZWFyY2hfcGF0aCcsICcnLCBmYWxzZSk7ClNFVCBjaGVja19mdW5jdGlvbl9ib2RpZXMgPSBmYWxzZTsKU0VUIHhtbG9wdGlvbiA9IGNvbnRlbnQ7ClNFVCBjbGllbnRfbWluX21lc3NhZ2VzID0gd2FybmluZzsKU0VUIHJvd19zZWN1cml0eSA9IG9mZjsKClNFVCBkZWZhdWx0X3RhYmxlc3BhY2UgPSAnJzsKClNFVCBkZWZhdWx0X3RhYmxlX2FjY2Vzc19tZXRob2QgPSBoZWFwOwoKLS0KLS0gTmFtZTogc3NuOyBUeXBlOiBUQUJMRTsgU2NoZW1hOiBwdWJsaWM7IE93bmVyOiBwb3N0Z3JlcwotLQoKQ1JFQVRFIFRBQkxFIHB1YmxpYy5zc24gKAogICAgaWQgaW50ZWdlciBOT1QgTlVMTCwKICAgIGFsaXZlIGludGVnZXIgTk9UIE5VTEwKKTsKCgpBTFRFUiBUQUJMRSBwdWJsaWMuc3NuIE9XTkVSIFRPIHBvc3RncmVzOwoKLS0KLS0gRGF0YSBmb3IgTmFtZTogc3NuOyBUeXBlOiBUQUJMRSBEQVRBOyBTY2hlbWE6IHB1YmxpYzsgT3duZXI6IHBvc3RncmVzCi0tCgpDT1BZIHB1YmxpYy5zc24gKGlkLCBhbGl2ZSkgRlJPTSBzdGRpbjsKMAkwCjEJMAoyCTEKMwkxCjQJMAo1CTEKXC4KCgotLQotLSBOYW1lOiBzc24gc3NuX3BrZXk7IFR5cGU6IENPTlNUUkFJTlQ7IFNjaGVtYTogcHVibGljOyBPd25lcjogcG9zdGdyZXMKLS0KCkFMVEVSIFRBQkxFIE9OTFkgcHVibGljLnNzbgogICAgQUREIENPTlNUUkFJTlQgc3NuX3BrZXkgUFJJTUFSWSBLRVkgKGlkKTsKCgotLQotLSBQb3N0Z3JlU1FMIGRhdGFiYXNlIGR1bXAgY29tcGxldGUKLS0KCg==" }'
backuprestore_1  | + echo '{' '"dump":' '"LS0KLS0gUG9zdGdyZVNRTCBkYXRhYmFzZSBkdW1wCi0tCgotLSBEdW1wZWQgZnJvbSBkYXRhYmFzZSB2ZXJzaW9uIDE0LjMKLS0gRHVtcGVkIGJ5IHBnX2R1bXAgdmVyc2lvbiAxNC40CgpTRVQgc3RhdGVtZW50X3RpbWVvdXQgPSAwOwpTRVQgbG9ja190aW1lb3V0ID0gMDsKU0VUIGlkbGVfaW5fdHJhbnNhY3Rpb25fc2Vzc2lvbl90aW1lb3V0ID0gMDsKU0VUIGNsaWVudF9lbmNvZGluZyA9ICdVVEY4JzsKU0VUIHN0YW5kYXJkX2NvbmZvcm1pbmdfc3RyaW5ncyA9IG9uOwpTRUxFQ1QgcGdfY2F0YWxvZy5zZXRfY29uZmlnKCdzZWFyY2hfcGF0aCcsICcnLCBmYWxzZSk7ClNFVCBjaGVja19mdW5jdGlvbl9ib2RpZXMgPSBmYWxzZTsKU0VUIHhtbG9wdGlvbiA9IGNvbnRlbnQ7ClNFVCBjbGllbnRfbWluX21lc3NhZ2VzID0gd2FybmluZzsKU0VUIHJvd19zZWN1cml0eSA9IG9mZjsKClNFVCBkZWZhdWx0X3RhYmxlc3BhY2UgPSAnJzsKClNFVCBkZWZhdWx0X3RhYmxlX2FjY2Vzc19tZXRob2QgPSBoZWFwOwoKLS0KLS0gTmFtZTogc3NuOyBUeXBlOiBUQUJMRTsgU2NoZW1hOiBwdWJsaWM7IE93bmVyOiBwb3N0Z3JlcwotLQoKQ1JFQVRFIFRBQkxFIHB1YmxpYy5zc24gKAogICAgaWQgaW50ZWdlciBOT1QgTlVMTCwKICAgIGFsaXZlIGludGVnZXIgTk9UIE5VTEwKKTsKCgpBTFRFUiBUQUJMRSBwdWJsaWMuc3NuIE9XTkVSIFRPIHBvc3RncmVzOwoKLS0KLS0gRGF0YSBmb3IgTmFtZTogc3NuOyBUeXBlOiBUQUJMRSBEQVRBOyBTY2hlbWE6IHB1YmxpYzsgT3duZXI6IHBvc3RncmVzCi0tCgpDT1BZIHB1YmxpYy5zc24gKGlkLCBhbGl2ZSkgRlJPTSBzdGRpbjsKMAkwCjEJMAoyCTEKMwkxCjQJMAo1CTEKXC4KCgotLQotLSBOYW1lOiBzc24gc3NuX3BrZXk7IFR5cGU6IENPTlNUUkFJTlQ7IFNjaGVtYTogcHVibGljOyBPd25lcjogcG9zdGdyZXMKLS0KCkFMVEVSIFRBQkxFIE9OTFkgcHVibGljLnNzbgogICAgQUREIENPTlNUUkFJTlQgc3NuX3BrZXkgUFJJTUFSWSBLRVkgKGlkKTsKCgotLQotLSBQb3N0Z3JlU1FMIGRhdGFiYXNlIGR1bXAgY29tcGxldGUKLS0KCg=="' '}'
backuprestore_1  | + jq -r .dump
backuprestore_1  | + base64 -d -w 0
backuprestore_1  | + psql -h db2restore
backuprestore_1  | SET
backuprestore_1  | SET
backuprestore_1  | SET
backuprestore_1  | SET
backuprestore_1  | SET
backuprestore_1  |  set_config 
backuprestore_1  | ------------
backuprestore_1  |  
backuprestore_1  | (1 row)
backuprestore_1  | 
backuprestore_1  | SET
backuprestore_1  | SET
backuprestore_1  | SET
backuprestore_1  | SET
backuprestore_1  | SET
backuprestore_1  | SET
backuprestore_1  | CREATE TABLE
backuprestore_1  | ALTER TABLE
backuprestore_1  | COPY 6
backuprestore_1  | ALTER TABLE
backuprestore_1  | + psql -h db2restore -c 'SELECT json_agg(id) FROM public.ssn WHERE alive = 1;'
backuprestore_1  | + awk '{ if(NR==3) print "{ \"access_token\": \"x\", \"alive_ssns\": \""$0"\" }" }'
backuprestore_1  | + tee -a data.json
backuprestore_1  | { "access_token": "x", "alive_ssns": " [2, 3, 5]" }
backuprestore_1  | + curl -XPOST -H 'Content-Type: application/json' -d @data.json http://endpoints:5000/challenges/backup_restore/solve
backuprestore_1  | + exit 0
backuprestore_1  |  [2, 3, 5]
hackattic_backuprestore_1 exited with code 0

```

All the best!