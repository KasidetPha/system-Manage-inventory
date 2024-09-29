from ProductTB import Product, sessionProduct, engine

if __name__ == "__main__":
    product = sessionProduct.query(Product).filter(Product.pos_id == None).first()
    
    print(product)
    
    product.pos_id = 345124
    sessionProduct.commit()
    
    print("Update successfuly!")