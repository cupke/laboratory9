original_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# Применяем метод items() для получения объекта dict_items
dict_items = original_dict.items()

# Создаем новый словарь, "обратный" исходному
reversed_dict = {value: key for key, value in dict_items}

print("Исходный словарь:")
print(original_dict)
print("\nНовый словарь (обратный исходному):")
print(reversed_dict)
