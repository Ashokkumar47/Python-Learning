from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/Job_id/{Job_id}")
def Job_id(Job_id:int):
    return {"Job_id": Job_id}