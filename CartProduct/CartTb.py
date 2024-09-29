from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CartProduct(Base):
    __tablename__ = "Carts"
    id = Column(Integer, primary_key=True)
    pos_id = Column(Integer)
    name = Column(String)
    price = Column(Float)
    qty = Column(Integer)
    product_id = Column(Integer)

    def __repr__(self):
        return f"id: {self.id}, pos_id: {self.pos_id}, name: {self.name}, price: {self.price}, qty: {self.qty}, product_id: {self.product_id}"

engine = create_engine("sqlite:///cart.db")
Session = sessionmaker(bind=engine)
sessionCart = Session()

if __name__ == "__main__":
    Base.metadata.create_all(engine)