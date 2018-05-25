from flask import Flask
from flask import request
import os
import socket

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route("/")
def hello():
     html = "<h3>Hostname: {hostname} v2</h3>"
     return html.format(hostname=socket.gethostname())

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    html = 'Server {hostname} shutting down...'
    return html.format(hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)