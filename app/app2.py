from flask import Flask, jsonify

from telegraf.client import TelegrafClient

client = TelegrafClient(host='localhost', port=8092, tags={'server': 'serve1'})


app = Flask(__name__)


@app.route('/')
def index():
    client.metric('request', 1)
    return jsonify({'hello': 'world'})
