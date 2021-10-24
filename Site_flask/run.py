from flask import Flask, render_template,g,request,jsonify
from flask_bootstrap import Bootstrap
from Core.Core_Mongodb import MongodbClient
app = Flask(__name__)

bootstrap = Bootstrap(app)
def get_conn():
	if not hasattr(g,'mongo'):
		g.mongo = MongodbClient()
	return g.mongo

@app.route('/',methods=["GET","POST"])
def index():
	conn = get_conn()
	data = request.get_json()
	if data:
		time = data.get("datetime")
		messages = conn.mongo_search("shtjp",time=time)
		""" 
		添加一个新的jinja模板，在得到ajax的post信息后，向前端发送此代码片段，并将这部分jinja模板替换之前的代码
		原因为，浏览器会先渲染jinja模板后执行JavaScript命令，所有将渲染好的代码直接传递给母模板可解决问题
		"""
		return render_template('other.html', messages=messages)
	else:

		messages = conn.mongo_search("shtjp")
		return render_template('index.html', messages=messages)
@app.route('/chi',methods=["GET","POST"])
def chi():
	conn = get_conn()
	data = request.get_json()
	if data:
		time = data.get("datetime")
		messages = conn.mongo_search("shtchi",time=time)
		""" 
		添加一个新的jinja模板，在得到ajax的post信息后，向前端发送此代码片段，并将这部分jinja模板替换之前的代码
		原因为，浏览器会先渲染jinja模板后执行JavaScript命令，所有将渲染好的代码直接传递给母模板可解决问题
		"""
		return render_template('other.html', messages=messages)
	else:
		messages = conn.mongo_search("shtchi")
		return render_template('index.html', messages=messages)

@app.route('/ua',methods=["GET","POST"])
def ua():
	conn = get_conn()
	data = request.get_json()
	if data:
		time = data.get("datetime")
		messages = conn.mongo_search("shtua",time=time)
		""" 
		添加一个新的jinja模板，在得到ajax的post信息后，向前端发送此代码片段，并将这部分jinja模板替换之前的代码
		原因为，浏览器会先渲染jinja模板后执行JavaScript命令，所有将渲染好的代码直接传递给母模板可解决问题
		"""
		return render_template('other.html', messages=messages)
	else:
		messages = conn.mongo_search("shtua")
		return render_template('index.html', messages=messages)



# @app.route('/user/<string:name>')
# def user(name):
# 	return render_template('user.html', name=name)

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.run(port=5555,debug=True)