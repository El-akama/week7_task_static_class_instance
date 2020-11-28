
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
# Велосипед.
# Создайте класс Bike в котором будут инициализированы следующие атрибуты: 
# self.cost
# (стоимость)
# self.make (производитель)
# self.model (модель)
# self.year (год выпуска)
# self.condition (состояние)
# self._sale_price = None (цена для продажи, по умолчанию None)
# self.sold = False (продан или нет, по умолчания False)
# Также укажите мин. прибыль, которая должна прийти с продажи велосипеда. Создайте метод
# для указания цены для продажи, который принимает цену и если она меньше стоимости, то
# ставит дефолтную цену для продажи (стоимость + мин. прибыль).
# Для ремонта велосипеда будет использоваться метод service, которая принимает стоимость
# ремонта и новое состояние велосипеда, соответственно продажная цена велосипеда
# возрастает на столько, сколько обошелся ремонт и возвращает нынешнюю цену для продажи.
# При продаже велосипеда будет использоваться метод sell, который меняет значение self.sold на

# True и возвращает прибыль с продажи.
# Допишите метод get_default_bike, который будет создавать дефолтный велосипед. Создайте
# объект bike = Bike.get_default_bike() и используете его методы и получите значения всех его
# атрибутов.

class Bike:
    def __init__(self, cost, make, model, year, condition, _sale_price, sold):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self.condition =condition
        self._sale_price = None #(цена для продажи, по умолчанию None)
        self.sold = False #(продан или нет, по умолчания False)
      
    def price(self, price, min_prof):
        self._sale_price = price
        self.min_prof = min_prof
        if price < min_prof:
            return min_prof + self.cost
        else: 
            return self._sale_price

    def service(self, cost_repair, new_condition):

        
