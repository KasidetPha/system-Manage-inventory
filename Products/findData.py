from Products.ProductTB import Product, engine, Product

print("(1) id")
print("(2) pos_id")
print("(3) name")

choice = int(input("Please select your choice: "))

if choice == 1:
    filter_key = "id"
    filter_value = int(input("Enter Product Id: "))
elif choice == 2:
    filter_key = "pos_id"
    filter_value = int(input("Enter posid: "))
elif choice == 3:
    filter_key = "name"
    filter_value = input("Enter Product Name: ")
else:
    print("Invalid choice!")
    filter_key = None
    
if filter_key:
    if __name__ == "__main__":
        products = Product.query(Product).filter(getattr(Product, filter_key) == filter_value).all()
        # print(products)
        
        if products:
            print("     --------")
            for product in products:
                print(f"id: {product.id}\npos_id: {product.pos_id}\nname: {product.name}\nprice: {product.price}\nqty: {product.qty}")
                print("     --------")
        else:
            print("not find product!")