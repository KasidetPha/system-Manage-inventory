from CartTb import CartProduct, sessionCart, engine

cart_products = sessionCart.query(CartProduct).all()

print("     ---------")
for cartProduct in cart_products:
    print(f"id: {cartProduct.id}\nname: {cartProduct.name}\nprice: {cartProduct.price}\nqty: {cartProduct.qty}\nproduct_id: {cartProduct.product_id}")
    print("     ---------")