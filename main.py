#pip install flask-mysql
#pip install flask-mysqldb

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql12300737'
app.config['MYSQL_PASSWORD'] = 'L8g7kVa3tj'
app.config['MYSQL_DB'] = 'sql12300737'
#app.config['MYSQL_PORT'] = 3306
#app.config['MYSQL_UNIX_SOCKET'] = 'TCP'
#app.config['MYSQL_CONNECT_TIMEOUT'] = '120'

mysql = MySQL()
#cur = mysql.connection.cursor()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['name']
        lastName = details['id']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO example (name, id) VALUES (%s, %s)", (name, id))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
