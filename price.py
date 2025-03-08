price = 100
discount = 5


def discounted(price, discount):
    price_with_discount = price - (price * discount / 100)
    print(price_with_discount)


discounted(100, 5)
discounted(100, 10)


def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    if max_discount >=100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
       return price
    else: 
       return price - (price * discount / 100)
print(discounted(1000, 30, 10))

def get_summ(one, two, delimiter ='&'):
    return f"{one}{delimiter}{two}".upper()
print(get_summ(1, 2, ","))
print(get_summ("привет","пока", ","))
print(get_summ("привет","пока"))

def format_price(price):
    return f"Цена: {price} руб."
print(format_price(100))
print(format_price(56.24))

def add(a, b):
    return a + b
print(add(2, 2))
result = add(5, 7)
print(result)
summa = add(result, 10)
print(summa)

def check_wheather(temperature):
    if temperature < 0:
        print("На улице холодно")
    elif temperature < 15:
        print('На улице прохладно')
    elif temperature < 25:
        print('На улице тепло')
    else:
        print('На улице жарко')
print(check_wheather(9))


def cut_cake(people):
    try: 
        z = 1 / people
        print(f'Каждый получит {z} пирога')
    except ZeroDivisionError:
        print('Не могу поделить на 0')


def discounted(price, discount, max_discount=20):
    try: 
        price = abs(float(price))
        discount = abs(float(discount))
    except ValueError: 
        return "Ошибка значения"
    max_discount = abs(int(max_discount))
    if max_discount >=100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
       return price
    else: 
       return price - (price * discount / 100)
print(discounted(20.1, 40.22, 33.25))
print(discounted("20.1", 40.22, 33.25)) 
print(discounted("привет", 40.22, 33.25))