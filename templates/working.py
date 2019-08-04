from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql12300737'
app.config['MYSQL_PASSWORD'] = 'L8g7kVa3tj'
app.config['MYSQL_DB'] = 'sql12300737'
mysql = MySQL(app)
#mysql.init_app(app)

@app.route('/')
def index():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT name FROM example WHERE id=1000''')
	rv = cur.fetchall()
	return str(rv)

if __name__ == '__main__':
	app.run(debug=True)








