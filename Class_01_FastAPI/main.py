# FastAPI se import kar rahe hain, taaki hum API bana sakein
from fastapi import FastAPI # type: ignore
from pydantic import BaseModel  # structure define karta hai data ka


# FastAPI ka ek instance bana rahe hain
app = FastAPI()

names = ["Shoaib", "Ali", "Ahmed"]  # Yeh ek list hai jisme kuch naam hain




#<----------------------------------------------------------------------------------------------->
# 1. GET Request # => data lana


# Yeh ek GET request ka Url define kar raha hai jo root ("/") pe chalega.
@app.get("/") # url
def get_function():  # jab url call hoga tab ye function khud se chalega.
    return names 


#<----------------------------------------------------------------------------------------------->
# 2. POST Request => Data create karna

class kuch(BaseModel): # BaseModel <= structure define karta hai data ka
    name: str


@app.post("/") # this functin is creating API URL
def post_function(data: kuch):
    names.append(data.name)  # is data ko list mein add kar rahy hain.
    return names


#<----------------------------------------------------------------------------------------------->
# 3. DELETE Request => Data delete karna

@app.delete("/data/{name}") # url
def delete_function(name: str):
    names.remove(name)
    return names
    
    
#<----------------------------------------------------------------------------------------------->
# 3. PUT Request => Data Update karna

@app.put("/{name}") # url
def put_functon(name: str, data: kuch): 
    for i, list_name in enumerate(names):
        if list_name == name:
            names[i] = data.name
            break
    return names
