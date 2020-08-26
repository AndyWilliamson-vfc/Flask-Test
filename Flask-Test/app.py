
from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


sqlfile='raw_SLP05'

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WDE01010;'
                      'Database=Dickies_BI_UK_Staging;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
sql="SELECT * FROM Dickies_BI_UK_Staging.dbo.raw_INP15 "
cursor.execute(sql)
rows = cursor.fetchall()    

@app.route('/')
@app.route('/home')
def home():
    return render_template("/home.html", rows=rows)

@app.route('/about')
def about():
    return render_template("/about.html", title='About')

@app.route('/selection', methods=['POST', 'GET'])
def selection(): 
    if request.method == 'POST':
        sqlfile = request.form.get('sqlfile')
        return render_template("/home.html", rows=rows)

    return '''<form method="POST">
    File <input type="text" name="sqlfile">
    <input type="submit">
    </form>'''

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
