immutable_var = (1, 2, True, ["Пятница", "Суббота"], ("Суббота", "Воскресенье"), "Июль")
print(immutable_var)

immutable_var[3].append("Воскресенье")
immutable_var[3].insert(0, "Четверг")
immutable_var[3].insert(0, "Понедельник")
immutable_var[3].insert(1, "Вторник")
immutable_var[3].insert(2, "Среда")
try:
    immutable_var[1] = 0
except TypeError:
    print("Нельзя изменить значение элемента в неизменяемом объекте")

print(immutable_var)

mutable_var = immutable_var[3]
print(mutable_var)
mutable_var[5] = 'Saturday'
item6 = mutable_var.pop(6)
mutable_var.append('Sunday')
mutable_var[0] = mutable_var[0].upper()
print(mutable_var)
mutable_var[0] = mutable_var[0].capitalize()
print(mutable_var)
print(item6)
weekdays = mutable_var[:5]
print(weekdays)
print(tuple(weekdays))

weekdays = tuple(weekdays) + immutable_var[4]
print(weekdays)
