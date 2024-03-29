from flask import Flask, render_template, request
from flaskext.mysql import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootpasswordgiven'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL()
mysql.init_app(app)
#cursor = mysql.get_db().cursor()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO myusers(FirstName, LastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.get_db().commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
