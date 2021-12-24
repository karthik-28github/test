from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route('/home')
def home():
    return "this is the home screen"

@app.route("/login_validate",methods=["post"])
def loginvalidate():
    email=request.form.get("email")
    password = request.form.get("password")
    return "your email is {} and password is {}".format(email,password)


if __name__=="__main__":
    app.run(debug=True,port=5001)
