from flask import Flask,g
from Proxypool.Mongodb_write import MongodbClient

__all__ = ["app"]
app = Flask(__name__)

def get_conn():
	if not hasattr(g,'mongo'):
		g.mongo = MongodbClient()
	return g.mongo

@app.route('/')
def index():
	return '<h2>代理接口</h2>'
@app.route('/random')
def get_proxy():
	conn = get_conn()
	return conn.random()

@app.route('/count')
def get_count():
	conn = get_conn()
	return str(conn.count())

if __name__ == '__main__':
	app.run()