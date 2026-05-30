# NadoshaDev | Booking System V8
# Финальная версия на сегодня: list comprehension + проверка на пустые слоты + цикл подтверждения

all_times = ["10:00", "11:00", "12:00", "13:00"]
busy_times = ["11:00"]

while True:
    # Собираем свободные слоты (list comprehension)
    free_times = [time for time in all_times if time not in busy_times]

    # Защита от пустого списка
    if not free_times:
        print("Свободных мест нет")
        break

    # Вывод нумерованного списка
    for index in range(len(free_times)):
        print(f"{index + 1} - {free_times[index]}")

    # Ввод пользователя
    selected_number = input("Выберите удобное время (введите номер): ").strip()

    # Валидация: проверка на число
    while not selected_number.isdigit():
        print("Ошибка: введите только цифру.")
        selected_number = input("Выберите удобное время (введите номер): ").strip()

    # Валидация: проверка диапазона
    while not 0 < int(selected_number) <= len(free_times):
        print("Ошибка: такого номера нет в списке.")
        selected_number = input("Выберите удобное время (введите номер): ").strip()

    # Выбор времени
    index = int(selected_number) - 1
    selected_time = free_times[index]

    # Подтверждение
    confirmation = input(f"Подтвердить запись на {selected_time}? (да/нет): ").strip().lower()

    if confirmation == "да":
        busy_times.append(selected_time)
        print(f"✅ Вы записаны на: {selected_time}")
        break
    else:
        print("Выбор отменён, попробуйте снова.\n")
