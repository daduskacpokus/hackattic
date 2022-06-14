from flask import Flask, request
app = Flask(__name__)

@app.route('/challenges/backup_restore/problem', methods=['GET'])
def say_get():
  return 'Hello from Server'
  
@app.route('/challenges/backup_restore/solve', methods=['POST'])
def say_post():
  return 'Hello from Server'