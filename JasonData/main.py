from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return 'welcome!'

@app.route('/query_example')
def query():
	name = request.args.get('name')
	framework = request.args['framework']
	return '''<h1>My name is:{}</h1>
			  <h1>I am using : {}</h1>'''.format(name,framework)

@app.route('/form', methods=['POST','GET'])
def form():
	if request.method == 'POST':
		fname = request.form.get('fname')
		lname = request.form.get('lname')
		return "<h1>my firstname is {} and last name is {}</h1>".format(fname, lname)

	return ''' <form method ="POST">
	fname <input type="text" name=fname>
	lname <input type="text" name =lname>
	<input type = "submit">
	</form>'''












if __name__ == '__main__':
	app.run()