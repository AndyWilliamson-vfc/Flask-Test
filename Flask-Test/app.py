"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import render_template 
import pyodbc

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
@app.route('/home')
def home():
    return render_template("/home.html")

@app.route('/about')
def about():
    return render_template("/about.html")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WDE01010;'
                      'Database=Dickies_BI_UK_Staging;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM raw_INP15 where cono15='+"'DC'")

for row in cursor:
    print(row)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
