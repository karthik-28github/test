from flask import Flask,render_template
from data import Articals


app=Flask(__name__)




Articals=Articals()
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/artical')
def artical():
    return render_template('artical.html',artical=Articals())



if __name__=="__main__":
    app.run(debug=True,port=5001)