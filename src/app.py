from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/info', methods=['GET'])
def get_info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'hostname': socket.gethostname(),
        'message': 'Version dinamica v10!!!',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/healthz', methods=['GET'])
def get_health():
    return jsonify({
        'status': 'up'
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")