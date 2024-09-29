from CartTb import CartProduct, sessionCart, engine

for i in range(1,3):
    cartProduct_to_delete = sessionCart.query(CartProduct).filter(CartProduct.id == i).first()
    if (cartProduct_to_delete):
        sessionCart.delete(cartProduct_to_delete)
        
    sessionCart.commit()
    print("delete successfuly!")