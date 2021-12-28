from flask import Flask,render_template,request,session
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key='karthik'
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///./text.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db=SQLAlchemy(app)
class Table(db.Model):
    id=db.Column(db.String(15),primary_key=True,nullable=False)
    password=db.Column(db.String(10),nullable=False)
    def __init__(self,id,password):
        self.id=id
        self.password=password



@app.route('/')
def index():
    return render_template("index.html")
@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        id=request.form['id1']
        password=request.form['password1']
        user=Table(id,password)
        db.session.add(user)
        db.session.commit()
        return render_template("index.html",id=id,name=password)
    else:
        return render_template("login.html")
@app.route('/display')
def display():
    content=Table.query.all()
    # content=Table.query.filter(Table.id==id).all()

    return render_template("index.html",con=content)
@app.route("/testlogin",methods=['POST','GET'])
def testlogin():
    if request.method=='POST':
        id=request.form['id1']
        password=request.form['password1']

        content=Table.query.filter(Table.id==id).all()
        if id in content:
            return "yes it is valid"
        else:
            return render_template("index.html",con=content)
    else:
        user = Table.query.all()
        print(user)
        return render_template("login.html")



if __name__=="__main__":
    db.create_all()
    app.run(debug=True,)
