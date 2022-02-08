from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/{num1}')
def home(num):
    return {f"my favorite number is{num}"}


if __name__ == "__main__":
    uvicorn.run(app, debug=True, port=8001)
