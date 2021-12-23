from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLAlchemy_DATABASE_URI"]="sqllite:///./marketdb.db"
db=SQLAlchemy(app)

class item(db.Model):
    id = db.Column(db.Integer(),primarykey=True, nullable=False,unique=True)
    name=db.Column(db.String(length=30),nullable=False,Unique=True)
    price=db.Column(db.Integer(),nullable=False)
    barcode=db.Column(db.String(length=20),nullable=False,unique=True)
    description=db.Column(db.String(length=50),nullable=False,unique=True)





@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
@app.route('/market')
def market_page():
    item_list=[
        {'id':1,'name':'phone','barcode':123456789,'price':750},
        {'id':2,'name':'laptop','barcode':123456987,'price':950},
        {'id':3,'name': 'iPad','barcode': 873456789,'price':850}
    ]
    return render_template('market.html',items=item_list)



if __name__=="__main__":
    app.run(debug=True,port=8001)