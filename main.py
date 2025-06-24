from enum import Enum
from fastapi import FastAPI,Depends,HTTPException
import models
from db import create_table
import services,schemas
from db import get_db,engine
from sqlalchemy.orm import Session
app = FastAPI()

create_table()

#1
@app.get("/caffe/",response_model=list[schemas.Caffe])
def get_all_caffe(db:Session= Depends(get_db)):
    return services.get_caffe(db)

@app.get("/caffe/{id}",response_model=schemas.Caffe)
def get_caffe_byId(id:int,  db :Session=Depends(get_db)):
   check = services.get_caffe_byId(db,id)
   if check :
    return check
   raise  HTTPException(status_code= 404,detail=f"invalid caffe by {id}")
@app.post("/createcaffe/")
def create_caffe(caffe:schemas.CaffeCreate,db:Session =Depends(get_db)):
    return services.create_caffe(db,caffe)

@app.put("/updatecaffe/{id}", response_model=schemas.Caffe)
def update_caffe(caffe: schemas.CaffeCreate, id: int, db: Session = Depends(get_db)):
    db_update = services.update_caffe_byId(db, caffe,id)
    if not db_update:
        raise HTTPException(status_code=404, detail=f"Invalid caffe with ID {id}")
    return db_update

@app.delete("/deletecaffe/{id}")
def delete_caffe(id:int,db:Session= Depends(get_db)):
   delete_entry =services.delete_caffe_byId(db,id)
   if delete_entry:
      return delete_entry
   raise HTTPException(status_code=404, detail=f"Invalid caffe wwith ID {id}")

#
#2 
@app.post("/createstore/")
def create_store(store:schemas.StoreCreate,db: Session = Depends(get_db)):
   return services.create_Store(db,store)

@app.get("/Store/")
def get_store(db:Session=Depends(get_db)):
   return services.get_Store(db)

@app.get("/Store/{id}")
def get_store_byid( id : int,db:Session=Depends(get_db)):
   return services.get_Store_byId(id,db)

@app.put("/storeUpdate/{id}")
def update_store_byid(id: int, Store:schemas.StoreCreate,db:Session=Depends(get_db)):
   rs = services.update_Store_byId(id,db,Store)
   if rs: 
      return rs
   raise HTTPException(status_code=404, detail=f"Invalid Store by {id}")
@app.delete("/deleteStore/{id}")
def delete_store_byid(id:int , db:Session=Depends(get_db)):
   rs = services.delete_Store_byId(id,db)
   if rs:
      return rs
   raise HTTPException(status_code=404,detail=f"Invalid Store by {id}")
#
#3
@app.post("/creatediscount/")
def createDiscount(discount:schemas.DiscountCreate,db:Session =Depends(get_db)):
   return  services.create_Discount(db,discount)

@app.get("/discount/")
def get_discount(db:Session=Depends(get_db)):
   return services.get_Discount(db)

@app.get("/discount/{id}")
def get_discount(id:int,db:Session=Depends(get_db)):
   return services.get_Discount_byId(db,id)

@app.put("/discountUpdate/{id}")
def update_discount(id:int , data :schemas.DiscountCreate,db:Session=Depends(get_db)):
   rs = services.update_discount_byId(db,id,data)
   if rs:
      return rs
   raise HTTPException(status_code=404, detail=f"INVALID ID {id}")
@app.delete ("/deleteDiscount/{id}")
def delete_discount(id:int, db:Session=Depends(get_db)):
   rs = services.delete_discount_byId(db,id)
   if rs :
      return rs 
   raise HTTPException(status_code=404 ,detail=f"Invalid ID{id}")










#
