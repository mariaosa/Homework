# мое решение
#def month_to_season(a):
   
        #if (a == 1) or (a == 2) or (a == 12):
            #print("Зима")
        #elif (a == 3) or (a == 4) or (a == 5):
              #print("Весна")
        # (a == 6) or (a == 7) or (a == 8):
              #print("Лето")
        #elif (a == 9) or (a ==10) or (a == 11):
              #print("Осень")
            
#month_to_season(10)
        
# решение после разбора д.з.
def month_to_season(m):
    if m in [12,1,2]:
        return "Зима"
    elif m in [3,4,5]:
        return "Весна"
    elif m in [6,7,8]:
        return "Лето"
    elif m in [9,10,11]:
        return"Осень"
    else:
        return "Неверный номер месяца"
    
print(month_to_season(25))
print(month_to_season(10))
print(month_to_season(3))
print(month_to_season(2))
print(month_to_season(8))

