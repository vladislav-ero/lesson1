# Создайте список из чисел 3, 5, 7, 9 и 10.5
# Выведите содержимое списка на экран
# Добавьте в конец списка строку "Python"
# Выведите длину списка на экран
values = [3, 5, 7, 9, 10.5]
values.append("Python")
print(values) 
# Выведите на экран начальный элемент списка
# Выведите на экран последний элемент списка
# Напечатайте элементы списка со второго по четвертый включительно
# Удалите из списка строку "Python"
print(values[0])
print(values[-1])
print(values[1:4])
values.remove("Python")
print(values)