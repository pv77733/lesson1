print ("Привет, мир!")
print ("Привет, программист!")
print (2+2)
print (10/3)

a = 'Привет'
b = 'мир'
c = 2
# d = a + ' ' + b + c + '!'
# print(d)
#d = f '{a} {b}'

c = f'{a} {b}!'
print(len(c))

#name = input('Введите ваше имя: ')
#print(f'Привет, {name}! Как дела?')

#print(bool("1"))
#print(bool(''))
#print (bool(0))

spisok = [3 , 5 , 7 , 9 , 10.5]
print (spisok)
spisok.append ("python")
print (len(spisok))
print(spisok[0])
print(spisok[-1])
print(spisok[1:4])
print(spisok.remove('python'))
print(spisok)

slovar = {"city": "Москва", "temperature": "20"}
print(slovar["city"])
slovar["temperature"] = str(int(slovar["temperature"]) -5)
print(slovar)

print('country' in slovar)
print( slovar.get("country",'Россия' ))
#slovar['']
print(len(slovar))

def hello_user():
    while True:
        try:
            user_say = input('Скажи что-нибудь: ')
            if user_say == 'Пока':
                print('Ну пока')
                break
            else:
                print(f'Сам ты {user_say}')
        except KeyboardInterrupt:
            print("Пока")
            break
hello_user()
