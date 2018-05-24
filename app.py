from flask import Flask
import os
import socket
app = Flask(__name__)

@app.route("/")
def hello():
     html = "<h3>Hostname: {hostname}</h3>"
     return html.format(hostname=socket.gethostname())

@app.route("/destroy")
def destroy():
     raise Exception("Arrange to destroy, order sucks!")
     
if __name__ == "__main__":
     app.run(host='0.0.0.0', port=80)