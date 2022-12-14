#!/usr/bin/env python
from flask_script import Manager
from testsql import Proxy
from extentions import db
from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///proxy.db'
db.init_app(app)
manager = Manager(app)


@manager.option('--host', '-h', dest='host')
@manager.option('--port', '-p', dest='port')
def runserver(host='0.0.0.0', port=5000):
    app.run(port=port, host=host, threaded=True)

@manager.command
def save_in_sql():
    proxy = Proxy.create_proxy({"server": "18.234.85.155", "port": "443"})

if __name__ == '__main__':
    manager.run()