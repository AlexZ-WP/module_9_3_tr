from module_9.module_9_3 import second

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

'''
1. В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из 
списков first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.


'''
first_result = (len(x) - len(y) for x in first for y in second  if len(x) != len(y))
first_result_1 = ( len(x) - len(y) for x,y  in zip(first,second) if len(x) != len(y))
#first_result_3 = (zip(len(x) - len(y)) for x in first for y in second  if len(x) != len(y))

print('f_r', list(first_result))
print('f_r_1', list(first_result_1))
#print(list(first_result_3))
'''
2. В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк
в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте 
функции range и len.
'''

second_result = (len(x) - len(y) for x in first for y in second)
second_result_1= (len(str(x)) - len(str(y)) for x in range(len(first)) for y in  range(len(second)))
second_result_2= (len(first[i]) == len(second[i]) for i in range(len(first)))

print('s_r', list(second_result))
print('s_r_1', list(second_result_1))
print('s_r_1', list(second_result_2))