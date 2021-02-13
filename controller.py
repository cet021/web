#!/usr/bin/env python3

import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/ip')
def ip():
    return flask.request.remote_addr


if __name__ == '__main__':
    app.run()
