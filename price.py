# def discounted(price, discount, max_discount=20):
#     price = abs(float(price))
#     discount = abs(float(discount))
#     max_discount = abs(float(max_discount))
#     if max_discount > 99:
#         raise ValueError('Слишком большая максимальная скидка')
#     if discount >= max_discount:
#         return price
#     else:
#         return price - (price * discount / 100)

# price1 = 100
# discount1 = 5
# print(discounted(price1, discount1))

# product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,
# 'discount': 5000}

# product['price_discounted'] = discounted(product['price'],
# product['discount'])

# print(product)

# {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,
# 'discount': 5, 'price_discounted': 47500.0}

# Создайте в редакторе файл price.py
# Создайте функцию format_price, которая принимает один аргумент price
# Приведите price к целому числу (тип int)
# Верните строку "Цена: ЧИСЛО руб."
# Вызовите функцию, передав на вход 56.24 и положите результат в переменную
# Выведите значение переменной с результатом на экран

def format_price(price):
    price = abs(int(price))
    return f"Price: {price} rub."

new_price = format_price(56.24)
print(new_price)