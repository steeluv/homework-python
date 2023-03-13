category = input('Категория товара ')
if category == 'продукты':
    price = int(input())
    if price < 100:
        print('Попробуйте нашу выпечку!')
    if price >= 100 and price < 500:
        print('Как начёт орехов в шоколаде?')
    if price >=500:
        print('Попоробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома!')

