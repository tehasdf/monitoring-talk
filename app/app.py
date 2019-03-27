from flask import Flask, jsonify

from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter, Info


i = Info('foo', 'Description')
i.info({'hello': 'world'})
c = Counter('my_requests_total', 'HTTP', ['method', 'endpoint'])


app = Flask(__name__)


@app.route('/')
def index():
    c.labels('GET', '/').inc()
    return jsonify({'hello': 'world'})


app = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})
