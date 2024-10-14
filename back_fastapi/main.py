from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class UserInput(BaseModel):
    operation : str
    x : float
    y : float
    


@app.post("/data")
def operate():
    return "Hi!"