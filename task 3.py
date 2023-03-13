price1 = int(input())
price2 = int(input())
price3 = int(input())
if price1 < price2 < price3:
    print('Акция!')
    print(round((price1 + price2 + price3)/2, 2))
elif price1 > price2 > price3 :
    print('Акция!')
    print(round((price1 + price2 + price3)/3, 2))
else:
    print('К оплате:')
    print(price1 + price2 + price3)
