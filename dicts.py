# Создайте словарь:
# {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь

weather = {"city": "Москва", "temperature": "20"}
print(weather["temperature"])
weather["temperature"] = str(int(weather["temperature"]) - 5)
print(weather["temperature"])
# print(type(weather["temperature"]))

# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением '27.05.2019'
# Выведите на экран длину словаря

print(weather.get("country", "Russia"))
weather["date"] = "27.05.2019"

print(len(weather))
# print(weather)