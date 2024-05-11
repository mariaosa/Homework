#первый вариант
def bank(x,y):
    for i in range(1, y + 1):
        count = x + (x/10)
        x = count
        print(round(count,2))

bank(1000, 10)

#второй вариант
percent = 0.1
def bank(deposit, year):
    for i in range(year):
        deposit = deposit + (deposit + percent)
    return print(deposit)

bank(1000,10)