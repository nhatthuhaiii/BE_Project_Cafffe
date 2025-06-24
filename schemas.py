from pydantic import BaseModel

class CaffeBase(BaseModel):
    name:str
    description:str
    isfv:bool
    urlImage:str
    prince :int
class CaffeCreate(CaffeBase):
    pass
class Caffe(CaffeBase):
    id:int 
    class Config:
        orm_mode=True
        from_attribute=True



class StoreBase(BaseModel):
    address : str
    lat : float
    long : float
    urlImage: str
    urlImage1: str
    urlImage2: str
    urlImage3: str
class StoreCreate(StoreBase):
    pass
class Store(StoreBase):
    id:int
    class Config:
        orm_mode=True
        from_attribute=True


class DiscountBase(BaseModel):
    name : str
    discountPrince: float
class DiscountCreate(DiscountBase):
    pass
class Discount(DiscountBase):
    id:int
    class Config:
        orm_mode=True
        from_atribute=True