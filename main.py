'''
from fastapi import FastAPI

app = FastAPI()

@app.get('/vic')

def view():

    return "Hello Welcome to FastAPI..."
    '''
   #path parameter
'''

from fastapi import FastAPI

app = FastAPI()

@app.get('/vic/{id}')

def view(id):
    return f"id: {id}"
'''
'''
from fastapi import FastAPI

emp = [
    {'id':101,'name':'Victor','place':'Thanjavur'},
    {'id':102,'name':'Noora','place':'Keelavasal'}
]

app = FastAPI()

@app.get('/vic/{id}')

def view(id:int):

    for e in emp:
        if e['id']==id:
            return e
'''

   #Quary parameter:

'''
from fastapi import FastAPI
emp = [
    {'id':101,'name':'Victor','place':'Thanjavur'},
    {'id':102,'name':'Noora','place':'Keelavasal'}
]

app = FastAPI()
@app.get('/vic/{id}')      #path parameter
def viewpath(id:int):

    for e in emp:
        if e['id']==id:
            return e



@app.get('/vic')          #Quary parameter
def viewquary(id:int):

    for e in emp:
        if e['id']==id:
            return e
        
'''

       #Request body == Used to send structured data to server

       #pydantic model == Validatio(Ex- fixed the number length), serialization(one formet to another formet converted), documentation

'''
   #ex 1:

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    Name : str
    Price : float
    availabilty : bool

app = FastAPI()

@app.post("/vic/")
def view(data : Item):
    
    return {"message": "Item Recived", "data" : data}
'''

'''
   #ex:2   (Using optional):

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional           #Optional model

class Item(BaseModel):
    Name : str
    Price : float
    availabilty : Optional[bool] = None

app = FastAPI()

@app.post("/vic/")
def view(data : Item):
    
    return {"message": "Item Recived", "data" : data}
'''

'''
            #Validation :

from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

class Item(BaseModel):
    name : str = Field(min_length=3, max_length=50,pattern="^[a-zA-Z]")
    price : float = Field(gt=0, lt=10000)
    availablity : Optional[bool] = None

app = FastAPI()
@app.post("/vic/")
def view(data:Item):

    return {"message" : "Item recived", "data":data}
'''


             #  Nested Model

'''
from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

class manf(BaseModel):
    company : str
    country : str

class Item(BaseModel):
    name : str = Field(min_length=3, max_length=50,pattern="^[a-zA-Z]")
    price : float = Field(gt=0, lt=10000)
    availablity : Optional[bool] = None
    manifacturer : manf


app = FastAPI()
@app.post("/vic/")
def view(data:Item):

    return {"message" : "Item recived", "data":data}
'''

'''

        #Validation (Query):

from fastapi import FastAPI,Query

emp = [
    {"id":101, "name":"Victor", "place":"Chennai"},
    {"id":102, "name":"Noora", "place":"Thanjavur"}
]

app = FastAPI()

@app.get("/vic/")
def viewquery(id:int = Query(ge=100, le=200),
              name: str = Query(min_length=3,max_length=50,regex="^[A-Za-z]")):
    
    for e in emp:
        if e["id"] == id and e["name"].lower() == name.lower():

            return e
'''

     #Validation Path:


'''
from fastapi import FastAPI,Path

emp = [
    {"id":102,"name":"Victor","place":"Chennai"},
    {"id":104,"name":"Noora","place":"Thanjavur"}
]

app = FastAPI()

@app.get("/vic/{id}")
def viewpath(id: int = Path(ge=100, le=200, multiple_of=2)):
    
    for e in emp:
        if e["id"] == id:
            return e
        
@app.get("/vic/{id}/{name}")
def viewpath(id: int = Path(ge=100, le=200, multiple_of=2),
             name: str = Path(min_length=3, max_length=50, regex="^[A-za-z]")):
    for e in emp:
        if e["id"]==id and e["name"].lower() == name.lower():

            return e
'''

           #Form Data:

'''
from fastapi import FastAPI,Form

app = FastAPI()

@app.post("/feedback/")
def feed(
    name: str = Form(),
    email: str = Form(),
    ratting: int = Form()
      ):

      return {
            "status": "Feedback Recived",
            "name": "name",
            "email": "email",
            "Ratting": 'ratting'
      }
'''

                   #File Upload method:

'''
from fastapi import FastAPI,File,UploadFile

app = FastAPI()

@app.post("/file_upload/")
async def file_upload(file:UploadFile = File()):

    content = await file.read()

    try:
        text_p = content.decode("utf-8")[:200]

    except e:
        text_p = "cannot be read content"

    return{
        "File Name": file.filename,
        "Content Type": file.content_type,
        "Size in Bytes": len(content),
        "Text": text_p
    }
'''


             #Multiple File Upload:

'''
from fastapi import FastAPI,File,UploadFile
from typing import List

app = FastAPI()
@app.post("/file_upload/")
async def file_upload(files: List[UploadFile] = File()):

    #read file content as bytes:

    result = []

    for file in files:
        content = await file.read()

        try:
            text = content.decode("utf-8")

        except UnicodeDecodeError:
            text = "Binary content not a readable text file."

        result.append({
            "File Name": file.filename,
            "content_type": file.content_type,
            "File_size_Bytes": len(content),
            "Content_preview": text[:10000]
        })

    return result

    '''


     #Fast APIs New Class:
'''
from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)
'''
# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, Base, get_db

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

