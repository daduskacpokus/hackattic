#!/usr/bin/env sh

set -xe
apk add curl netcat-openbsd
nc -zv db2backup 5432
nc -zv endpoints 5000
curl -XGET http://endpoints:5000/challenges/backup_restore/problem?access_token=x 2>/dev/null|base64 -d -w 0

exit 0