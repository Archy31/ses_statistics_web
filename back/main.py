from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User_input(BaseModel):
    operation : str
    x : float
    y : float
    


@app.post("/data")
def operate(input:User_input):
    return "Hi!"