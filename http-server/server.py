from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/log',methods=['POST'])
def index():
  body = request.form
  print(body["asctime"], body['filename'], body['msg'])
  return ""

if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 3000, debug=True)
