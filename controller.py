#!/usr/bin/env python3

import flask
import sys

app = flask.Flask(__name__)
print(*sys.path, sep='\n')


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/ip')
def ip():
    return flask.request.remote_addr


if __name__ == '__main__':
    app.run()
