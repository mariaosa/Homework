#код вызывает функцию и передает в нее год, 
#результат сохраняется в переменную

def is_year_leap(year):
    year = 1970
    print(year)

is_year_leap(1970)


# мое решение задания
def is_year_leap(y):

    if(y % 4 == 0):
        print("год " + str(y), True)
    else:
        print("год " + str(y), False)  
                
is_year_leap(2001)

#решение после разбора д.з.
y = int(input())
def is_year_leap(y):
    if y % 4 == 0:
        return True
    else:
        return False
result = is_year_leap(y)
print(f'год{y}: {result}')

is_year_leap(y)



    
