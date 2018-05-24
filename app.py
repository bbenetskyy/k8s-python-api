from flask import Flask
import os
import socket
app = Flask(__name__)

@app.route("/")
def hello():
     html = "<h3>Hostname: {hostname}</h3>"
     return html.format(hostname=socket.gethostname())

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=80)