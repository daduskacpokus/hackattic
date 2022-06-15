#!/usr/bin/python

from flask import Flask, request, abort, send_file
import gzip
from sh import pg_dump
app = Flask(__name__)

@app.route('/challenges/backup_restore/problem', methods=['GET'])
def do_get():
  token = request.args.get('access_token')
  if (token == "x"):
    with gzip.open('backup.gz', 'wb') as f:
      pg_dump('-h', 'postgres', '-U', 'postgres', '-d', 'hackattic', _out=f)
    return send_file('backup.gz')
  else:
    abort(404)
  
@app.route('/challenges/backup_restore/solve', methods=['POST'])
def do_post():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    data = request.json
    if (data['access_token'] == "x"):
      return 'Hello from Server'
    else:
      abort(404)
  else:
    return 'Content-Type not supported!'  