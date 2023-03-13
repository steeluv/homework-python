number = int(input())
if number % 2 == 0:
    if sum(map(int,str(number))) % 3 == 0:
        print("yes")
else:
    print("No")