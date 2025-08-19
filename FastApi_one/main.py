from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/cal")
def input(Number_of_positions_hired:int,Average_Time_Spent:float,Average_Cost_per_Hire:float,Name:str,email:str,Phone_Number:int):
    return {"Number_of_positions_hired":Number_of_positions_hired,"Average_Time_spent":Average_Time_Spent,"Average_cost_per_Hire":Average_Cost_per_Hire,"Name":Name,"email":email,"Phone_Number":Phone_Number}
