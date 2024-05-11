#первое решение
var_1 = 37
var_2 = 99
var_1, var_2 = var_2, var_1
print('var_1=', var_1, 'var_2=', var_2)

#второе решение
var_1 = 37
var_2 = 99
temp = var_1
var_1 = var_2
var_2 = temp
print('var_1=', var_1, 'var_2=', var_2)