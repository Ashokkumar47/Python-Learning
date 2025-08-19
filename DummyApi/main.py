from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(r"C:\Users\maven\PycharmProjects\PythonLearning\DummyApi\.env")

app = FastAPI()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]

# Pydantic model for validation
class CalData(BaseModel):
    Number_of_positions_hired: int
    Average_Time_Spent: float
    Average_Cost_per_Hire: float
    Name: str
    email: str
    Phone_Number: int

# Insert data into MongoDB
@app.post("/cal/")
async def insert_cal_data(data: CalData):
    result = await db.cal.insert_one(data.dict())  # "cal" is collection name
    return {"message": "Data inserted", "inserted_id": str(result.inserted_id)}

# Check connection
@app.get("/")
async def root():
    return {"message": "MongoDB Connected Successfully!"}
