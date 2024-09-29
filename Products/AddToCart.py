import sys

sys.path.append(r'C:\Users\User\Desktop\system Manage inventory\Products')
sys.path.append(r'C:\Users\User\Desktop\system Manage inventory\CartProduct')

from CartTb import CartProduct, sessionCart, engine as cart_engine
from ProductTB import sessionProduct, Product, engine as product_engine

# product_id = int(input("Enter ProductID: "))
id_product = 4

if __name__ == "__main__":
    try:
        qty_n = 0
        product = sessionProduct.query(Product).filter(Product.id == id_product).first()
        cartProduct = sessionCart.query(CartProduct).filter(CartProduct.product_id == id_product).first()
        print(f"product: {product}")
        print(f"cartProduct: {cartProduct}")
        
        if product:
            if cartProduct == None:
                new_cartProduct = CartProduct(
                    pos_id=product.pos_id,
                    name=product.name, 
                    price=product.price, 
                    qty=qty_n+1,
                    product_id=product.id
                )
                product.qty = product.qty - 1
                sessionCart.add(new_cartProduct)
                sessionCart.commit()
                sessionProduct.commit()
                print("Added to cart Sucessfuly!")
            else:
                if cartProduct.product_id == id_product:
                    cartProduct.qty = cartProduct.qty + 1
                    product.qty = product.qty -1
                    sessionCart.commit()
                    sessionProduct.commit()
                    print("Update qty successfuly!")
                    print(f"name: {product.name}\nเหลือ: {product.qty}")
        else:
            print("not have product in system.")
    except Exception as e:
        print(f"error => {e}")
    
    finally:
        sessionProduct.close()
        sessionCart.close()