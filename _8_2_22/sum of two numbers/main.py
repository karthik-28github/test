from fastapi import  FastAPI
import uvicorn


app=FastAPI()
@app.get('/')
def home():
    return "sum of two numbers"

@app.get('/{num1},{num2}')
def home1(num1,num2):
        sum=int(num1)+int(num2)
        return {f"the sum of {num1} {num2} is {sum}"}



if __name__=="__main__":
    uvicorn.run(app,debug=True,port=8002)
