
# task1
# def dollarize(amount):
#     if amount >= 0:
#         return '${:,.2f}'.format(amount)
#     else:
#         return '-${:,.2f}'.format(-amount)
# print(dollarize(-12345345.3456))

# class MoneyFmt:
#     amount = None

#     def __init__(self, amount):
#         self.amount = amount

#     def update(self, value):
#         self.amount = value

#     def __repr__(self):
#         return str(self.amount)

#     def __str__(self):
#         if self.amount >= 0:
#             return '${:,.2f}'.format(self.amount)
#         else:
#             return '-${:,.2f}'.format(-self.amount)

# cash = MoneyFmt(12345678.021)
# print(cash)
# cash.update(100000.4567)
# print(cash)
# cash.update(-0.3)
# print(cash)
# print(repr(cash))

# task2
# class Bike:

#     minimum_profit = 1000

#     @classmethod
#     def new_bike(cls):
#         return cls(2000, 'red', 'kr', 2010, 'new')

#     def __init__(self, cost, make, model, year, condition, sale_price = None, sold = False):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self.sale_price = sale_price
#         self.sold = sold

#     def price_sold(self, value):
#         if value - self.cost < Bike.minimum_profit:
#             self.sale_price = Bike.minimum_profit + self.cost
#         elif value - self.cost > Bike.minimum_profit:
#             self.sale_price = value

#     def service(self, value):
#         self.sale_price += value

#     def sell(self):
#         self.sold = True
#         return self.sale_price


# obj1 = Bike.new_bike()
# obj1.price_sold(500)
# obj1.service(500)
# print(obj1.sell())