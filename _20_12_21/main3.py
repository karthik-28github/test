from flask import Flask, url_for
from werkzeug.utils import redirect

app=Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'hello %s welcome as guest'%guest

@app.route('/username/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__=="__main__":
    app.debug=True
    app.run(port=8000)