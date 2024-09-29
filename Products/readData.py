from ProductTB import Product, sessionProduct, engine

products = sessionProduct.query(Product).all()

# print(products)
print("  ----------  ")
for product in products:
    print(f"id: {product.id}\npos_id: {product.pos_id}\nname: {product.name}\nprice: {product.price}\nqty: {product.qty}")
    print("  ----------  ")