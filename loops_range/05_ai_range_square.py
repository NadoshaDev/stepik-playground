# NadoshaDev | AI Practice: Range Filter & Squaring
# Тема: list comprehension + фильтрация по диапазону

numbers = [1, 2, 3, 4, 5, 6]

# Оставляем только те, что больше 2 и меньше 6, возводим в квадрат
filtered_numbers = [number ** 2 for number in numbers if 2 < number < 6]

print(filtered_numbers)
