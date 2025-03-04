class Product:
    
    discount_rate = 0.1  

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        """Calculate the price after applying the discount."""
        return self.price * (1 - Product.discount_rate)



product1 = Product("Laptop", 50000)
product2 = Product("Smartphone", 30000)

print(f"Original Price of {product1.name}: ₹{product1.price}")
print(f"Discounted Price: ₹{product1.get_discounted_price()}")

print(f"Original Price of {product2.name}: ₹{product2.price}")
print(f"Discounted Price: ₹{product2.get_discounted_price()}")