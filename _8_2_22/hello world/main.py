from fastapi import FastAPI                     #import fastapi
import uvicorn                                  # import uvicorn

app=FastAPI()

@app.get('/')
def home():
    return "hello world"


if __name__=="__main__":
    uvicorn.run(app)