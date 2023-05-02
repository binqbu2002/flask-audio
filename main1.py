from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_microphone', methods=['POST'])
def detect_microphone():
    HOST = 'server-ip-address'
    PORT = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'detect_microphone')
        data = s.recv(1024)

    microphone = data.decode()
    return microphone

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
