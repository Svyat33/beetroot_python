# Lesson 11
# Task 3. Product Store
# Write a class Product that has three attributes:
#     type
#     name
#     price
# Then create a class ProductStore, which will have some Products and will
# operate with all products in the store. All methods, in case they can’t
# perform its action, should raise ValueError with appropriate error
# information.
#
# Tips: Use aggregation/composition concepts while implementing the
# ProductStore class. You can also implement additional classes to
# operate on a certain type of product, etc.
#
# Also, the ProductStore class must have the following methods:
#
#  add(product, amount) - adds a specified quantity of a single product
#       with a predefined price premium for your store(30 percent)
#  set_discount(identifier, percent, identifier_type=’name’) - adds a
#       discount for all products specified by input identifiers (type or
#       name). The discount must be specified in percentage
#  sell_product(product_name, amount) - removes a particular amount of
#       products from the store if available, in other case raises an error.
#       It also increments income if the sell_product method succeeds.
#  get_income() - returns amount of many earned by ProductStore instance.
#  get_all_products() - returns information about all available products
#       in the store.
#  get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

'''
class Product:

    pass

class ProductStore:

pass

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product(Food, 'Ramen, 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell(‘Ramen’, 10)

assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
'''


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

    def __str__(self):
        return f'Product class object. TYPE: {self.type}, NAME: {self.name}, PRICE: {self.price}'


class ProductStore:
    def __init__(self):
        self.products = []
        self.products_amount = {}

    # # От Святослава
    # def check_equal(self, product):
    #     if product in self.products:
    #         self.products_kvo[hash(product)] += kvo
    #     else:
    #         self.products_kvo[hash(product)] = kvo
    #         self.products.append(product)

    # adds a specified quantity of a single product with a predefined price premium for your
    # store(30 percent).
    def add(self, product, amount):
        pass

    # adds a discount for all products specified by input identifiers (type or name).
    # The discount must be specified in percentage
    def set_discount(self, identifier, percent, identifier_tyoe='name'):
        pass

    # removes a particular amount of products from the store if available, in other case
    # raises an error. It also increments income if the sell_product method succeeds.
    def sell_product(self, product_name, amount):
        pass

    # returns amount of many earned by ProductStore instance.
    def get_income(self):
        pass

    # returns information about all available products in the store.
    def get_all_products(self):
        pass

    # returns a tuple with product name and amount of items in the store.
    def get_product_info(self, product_name):
        pass


if __name__ == '__main__':
    p = Product('Sport', 'Football T-Shirt', 100)

    p2 = Product('Food', 'Ramen', 1.5)

    s = ProductStore()

    s.add(p, 10)

    s.add(p2, 300)

    s.sell_product('Ramen', 10)

    assert s.get_product_info('Ramen') == ('Ramen', 290)
