from models import Caffe,Store,Discount
from sqlalchemy.orm import Session
from schemas import CaffeCreate,StoreCreate,DiscountCreate


#1

def create_caffe(db:Session,data:CaffeCreate):
    caffe_instance = Caffe(**data.model_dump())
    db.add(caffe_instance)
    db.commit()
    db.refresh(caffe_instance)
    return caffe_instance
def get_caffe(db:Session):
    return db.query(Caffe).all()
def get_caffe_byId(db:Session,caffeId:int):
    return db.query(Caffe).filter(Caffe.id == caffeId).first()

def update_caffe_byId(db:Session,caffe:CaffeCreate,caffe_id:int):
    caffe_queryset = db.query(Caffe).filter(Caffe.id == caffe_id).first()
    if caffe_queryset :
        for key,value in caffe.model_dump().items():
            setattr(caffe_queryset,key,value)
        db.commit()
        db.refresh(caffe_queryset)
    return caffe_queryset
def delete_caffe_byId(db:Session,caffe_id:int):
    caffe_result = db.query(Caffe).filter(Caffe.id == caffe_id).first()
    if caffe_result :
        db.delete(caffe_result)
        db.commit()
    return caffe_result

# 



# 2
def create_Store(db:Session,data:StoreCreate):
    store_instance = Store(**data.model_dump())
    db.add(store_instance)
    db.commit()
    db.refresh(store_instance)
    return "SUCCESS"

def get_Store(db:Session):
    return db.query(Store).all()

def get_Store_byId(id:int ,db:Session):
    return db.query(Store).filter(Store.id==id).first()

def update_Store_byId(id:int , db:Session,store:StoreCreate):
    caffe_result = db.query(Store).filter(Store.id==id).first()
    if caffe_result:
        for key,value in store.model_dump().items():
            setattr(caffe_result,key,value)
        db.commit()
        db.refresh(caffe_result)
    return caffe_result
def delete_Store_byId(id: int , db:Session):
    result = db.query(Store).filter(Store.id==id).first()
    if result: 
        db.delete(result)
        db.commit()
    return result
#3
def create_Discount(db:Session,data:DiscountCreate):
    disscount_instance = Discount(**data.model_dump())
    db.add(disscount_instance)
    db.commit()
    db.refresh(disscount_instance)
    return "SUCESS"

def get_Discount(db:Session):
    return db.query(Discount).all()

def get_Discount_byId(db:Session,id:int):
    return db.query(Discount).filter(Discount.id==id).first()
def update_discount_byId(db: Session, id: int, data: DiscountCreate):
    rs = db.query(Discount).filter(Discount.id == id).first()  
    if rs:
        for key, value in data.model_dump().items():
            setattr(rs, key, value)
        db.commit()
        db.refresh(rs)  
    return rs
def delete_discount_byId(db:Session , id:int):
    rs = db.query(Discount).filter(Discount.id==id).first()
    if rs :  
        db.delete(rs)
        db.commit()
    return rs