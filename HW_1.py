# 1) Создать переменную типа String
name = "Ivan"
print(name, type(name))
# 2) Создать переменную типа Integer
age = 999
print(age, type(age))
# 3) Создать переменную типа Float
salary = 999.99
print(salary, type(salary))
# 4) Создать переменную типа Bytes
number = b"xf0"
print(number, type(number))
# 5) Создать переменную типа List
list = [12, 13, 14, 15]
print(list, type(list))
# 6) Создать переменную типа Tuple
tuple = (10, 11, "hello")
print(tuple, type(tuple))
# 7) Создать переменную типа Set
set1 = {1, 2, 5, 7}
print(set1, type(set1))
# 8) Создать переменную типа Frozen set
frozenset1 = frozenset([1, 2, 4])
print(frozenset1, type(frozenset1))
# 9) Создать переменную типа Dict
dict = {"name": "Pavel",
        "age": 999}
print(dict, type(dict))
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
name1 = "stringG"
name2 = "stringGG"
name_ = name1 + name2
print(name_)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(name, age, sep=", ")
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(name, age, sep=" + ")


