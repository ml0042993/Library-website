from flask import Flask, render_template,g
from flask_bootstrap import Bootstrap
from Core.Core_Mongodb import MongodbClient
app = Flask(__name__)

bootstrap = Bootstrap(app)
def get_conn():
	if not hasattr(g,'mongo'):
		g.mongo = MongodbClient()
	return g.mongo

@app.route('/')
def index():
	conn = get_conn()
	messages = conn.mongo_search("shtjp")
	return render_template('index.html',messages = messages)
@app.route('/chi')
def chi():
	conn = get_conn()
	messages = conn.mongo_search("shtchi")
	return render_template('index.html',messages = messages)
@app.route('/ua')
def ua():
	conn = get_conn()
	messages = conn.mongo_search("shtua")
	return render_template('index.html',messages = messages)


# @app.route('/user/<string:name>')
# def user(name):
# 	return render_template('user.html', name=name)

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.run(port=5555,debug=True)