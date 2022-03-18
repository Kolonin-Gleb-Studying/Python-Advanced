# Количество совпадающих
'''
# Входные данные приму как список целых чисел
# Для этого нужно использовать генератор

# s1 = set(input().split())
# s2 = set(input().split())
# print(len(s1 & s2))
'''

# Общие числа в порядке возрастания
'''
# Заполнение множеств с консоли
set1 = set( list([ int(num) for num in input().split()]) )
set2 = set( list([ int(num) for num in input().split()]) )
# Нужно ли приводить эл. множества к цел. типу?
# Да, т.к. при сортировке строк, содержащих числа 
# Python будет сортировать по первому разряду, т.е. 1 10 2 А НЕ 1 2 10

# Числа в порядке возрастания в пересечении

set3 = set1 & set2
print(*sorted(set3))
'''
