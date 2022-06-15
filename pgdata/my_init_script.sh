#!/bin/sh
export PGPASSWORD=$POSTGRESQL_PASSWORD # Set appropriately
psql -Upostgres $POSTGRESQL_DATABASE <<EOF
CREATE TABLE IF NOT EXISTS SSN (
    id          integer PRIMARY KEY,
    alive       integer NOT NULL
);
INSERT INTO SSN VALUES
    ('0', '0'),
    ('1', '0'),
    ('2', '1'),
    ('3', '1'),
    ('4', '0'),
    ('5', '1');
EOF