#!/usr/bin/env sh

set -xe
apk add curl netcat-openbsd jq postgresql
nc -zv db2backup 5432
nc -zv db2restore 5432
nc -zv endpoints 5000
json=`curl -XGET http://endpoints:5000/challenges/backup_restore/problem?access_token=x 2>/dev/null)`
echo $json | jq -r '.dump' | base64 -d -w 0 | psql -h db2restore
psql -h db2restore -c "SELECT json_agg(id) FROM public.ssn WHERE alive = 1;"|awk '{ if(NR==3) print "{ \"access_token\": \"x\", \"alive_ssns\": \""$0"\" }" }'|tee -a data.json
curl -XPOST -H "Content-Type: application/json" \
    -d @data.json \
    http://endpoints:5000/challenges/backup_restore/solve 2>/dev/null 

exit 0