from fastapi import FastAPI

app=FastAPI()

@app.get("/cal/")
def input(Number_of_positions_hired:int,Average_Time_Spent:float,Average_Cost_per_Hire:float,Name:str,email:str,Phone_Number:int):
    return {"Number_of_positions_hired":Number_of_positions_hired,"Average_Time_spent":Average_Time_Spent,"Average_cost_per_Hire":Average_Cost_per_Hire,"Name":Name,"email":email,"Phone_Number":Phone_Number}

@app.get("/item/{item_id}")
def item(item_id:int):
    return {"item_id": item_id}

@app.get("/name/{name}")
def name(name:str):
    return {"name":name}

@app.get("/job_id/{job_id}")
def job_id(job_id:int,q:str=None):
    return {"job_id": job_id, "query": q}

@app.get("/product/{name1}")
def product(name1:str,skip:int=0,limit:int=10):
    return {"product":name1,"skip": skip, "limit": limit}


