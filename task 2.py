hours = int(input())
price = int(input())
if hours >= 10 and hours <=12:
    print(price/2)
elif hours >=20 and hours <=22:
    print(price/4)
else:
    print(price)
