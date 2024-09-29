from sqlalchemy import create_engine, String, Integer, Float, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True)
    pos_id = Column(Integer, primary_key=False)
    name = Column(String)
    price = Column(Float)
    qty = Column(Integer)
    
    def __repr__(self):
        return f"id: {self.id}, pos_id: {self.pos_id}, name: {self.name}, price: {self.price} qty: {self.qty}"
    
engine = create_engine("sqlite:///product.db")
Session = sessionmaker(bind=engine)
sessionProduct = Session()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
