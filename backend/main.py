from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello from FastAPI!"}

@app.post("/data")
async def receive_data(request: Request):
    body = await request.json()
    print(f"Received from edge: {body}")
    return {"status": "ok"}
