class CashRegister:
    TAX = 0.05

    def __init__(self, cashier):
        self.cashier = cashier
        self.totalbill = 0
        self.products = {}

    def add_product(self, product_name, amount=1):
        # new_products is a dictionary.
        self.products[product_name["name"]] = {
            "price": product_name["price"],
            "quantity": amount
        }
        self.totalbill += product_name["price"] * amount

    def show_products(self):
        print(self.products)

    def remove_product(self, product):
        # product is a string with the name of the product.
        del self.products[product]

    def update_price(self, product, new_price):
        # product is a string with the name of the product.
        self.products[product]["price"] = new_price

    def print_subtotal(self):
        print(f"Subtotal: {self.totalbill}")

    def find_taxes(self):
        return round(self.totalbill * CashRegister.TAX, 2)

    def print_taxes(self):
        print(f"Taxes: {self.find_taxes()}")

    def find_total(self):
        return round(self.totalbill + self.find_taxes(), 2)

    def print_total(self):
        print(f"Total: {self.find_total()}")

    def clear_purchase(self):
        self.products.clear()


# Create the instance
my_cash_register = CashRegister("Nora")

# Create the products
product1 = {"name": "Juice Box", "price": 12.56}
product2 = {"name": "Chips", "price": 3.99}
product3 = {"name": "Milk", "price": 5.69}

# Add the products
my_cash_register.add_product(product1)
my_cash_register.add_product(product2, 5)
my_cash_register.add_product(product3, 9)

my_cash_register.show_products()

# Remove a product
my_cash_register.remove_product("Milk")
my_cash_register.show_products()

# Update the price of a product
my_cash_register.update_price("Chips", 4.97)
my_cash_register.show_products()

# Print the subtotal, taxes, and total
my_cash_register.print_subtotal()
my_cash_register.print_taxes()
my_cash_register.print_total()

# Clear the purchase
my_cash_register.clear_purchase()
my_cash_register.show_products()
