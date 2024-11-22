from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hehe():
    return {"message": "Hello world!"}
        