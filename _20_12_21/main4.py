from flask import *

app=Flask(__name__)


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['nm']
        return render_template("login.html")

@app.route('/success')
def success(user):
    return render_template("success.html",user=user)


if __name__=="__main__":
    app.run(debug=True)


