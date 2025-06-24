from db import Base
from sqlalchemy import Integer,Column,String,Boolean,Double


class Caffe(Base):
    __tablename__="Caffe"
    id = Column(Integer,primary_key=True, index=True)
    isfv = Column(Boolean,index=True)
    description = Column(String,index=True)
    name = Column(String,index=True)
    urlImage=Column(String,index=True)
    prince =Column(Integer,index=True)

class Store (Base):
    __tablename__="store"
    id = Column(Integer,primary_key=True, index=True)
    
    address = Column(String,index=True)
    lat =Column(Double,index=True)
    long=Column(Double,index=True)  
    urlImage=Column(String,index=True)
    urlImage1=Column(String,index=True)
    urlImage2=Column(String,index=True)
    urlImage3=Column(String,index=True)

class Discount(Base):
    __tablename__="Discount"
    id = Column(Integer,primary_key=True, index=True)
    
    name = Column(String ,index=True)
    
    discountPrince=Column(Double,index=True)  

    