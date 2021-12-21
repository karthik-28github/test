from flask import Flask

app=Flask(__name__)

@app.route('/blog/<int:postID>')
def blog(postID):
    return 'bolg number is %d'%postID

@app.route('/rev/<float:num>')
def rev(num):
    return 'the reverses number is %f'%num

if __name__=="__main__":
    app.run()