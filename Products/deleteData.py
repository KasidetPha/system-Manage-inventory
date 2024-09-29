from ProductTB import sessionProduct, engine, Product

if __name__ == "__main__":
    product_to_delete = sessionProduct.query(Product).filter(Product.id == 1).first()

    # print(product_to_delete)

    # print(product)
    if product_to_delete:
        sessionProduct.delete(product_to_delete)
    sessionProduct.commit()

    print("Delete successfuly!")