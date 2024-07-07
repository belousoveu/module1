my_dict = {'Anna': 1990, 'Mary': 1999, 'Peter': 2003, 'John': 1987}
print(my_dict)
print(my_dict.get('Mary', 'not found'))
print(my_dict.get('George', 'not found'))
# add 2 new items
my_dict.setdefault('George', 1990)
my_dict['Samantha'] = 1995
# add Martin and update value of key 'Samantha'
new_dict = {'Martin': 1995, 'Samantha': 1998}
my_dict.update(new_dict)
print(my_dict)
obj = my_dict.pop('Mary')
print(obj)
print(my_dict)
print(len(my_dict))
# создаем my_set
my_set = {1, 16, 4.5, 5 == 5, len(my_dict), 'a', 'b', True, 1 > 2, 'a'}
# выясняется интересный факт, который не отражен в лекции - логическое значение True и целочисенное 1
# - это для множества одно и то же самое
print(my_set)
# >> {False, 1, 4.5, 6, 'b', 16, 'a'} Значение True отсутствует в множестве, поскольку есть 1
## add 2 items
my_set.add(1.5 * 4.0)
## еще один момент - float автоматически преобразуется в int, а поскольку 6 уже есть
# в множестве, то элемент не добавится.
my_set.add((1, 2, 3))
my_set.add('True')  # все равно добавим True во множество, хотя бы и в виде строки :)
print(my_set)
my_set.remove(True)  # удаляем 1
print(my_set)
