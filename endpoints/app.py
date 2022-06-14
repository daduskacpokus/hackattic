from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/challenges/backup_restore/problem', methods=['GET'])
def say_get():
  token = request.args.get('access_token')
  if (token == "x"):
    return 'Hello from Server'
  else:
    abort(404)
  
@app.route('/challenges/backup_restore/solve', methods=['POST'])
def say_post():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    data = request.json
    if (data['access_token'] == "x"):
      return 'Hello from Server'
    else:
      abort(404)
  else:
    return 'Content-Type not supported!'  