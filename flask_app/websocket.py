import time
import asyncio
#import websockets
from io import BytesIO
import os
import json

from flask import Flask, jsonify, request, make_response
from flask_socketio import SocketIO, send, emit

#import predict

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def ack():
    print('response has been received!')

@socketio.on('json')
def analyze(json):
    print('receive json in json: ' + str(json))
    # return 'one', 2
    # emit('my response', json, callback=ack)
    return 'my response', 200

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})
    print('connect!')

@socketio.on('disconnect')
def test_disconnect():
    print('disconnect!')

@socketio.on('my message')
def analyze(json):
    print('receive json: ' + str(json))
    emit('my response', json, callback=ack)

@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    pass

if __name__=='__main__':
    socketio.run(app, debug=True, port=8111)
