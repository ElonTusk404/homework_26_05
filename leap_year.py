#Программа получает от пользователя год и высчитывает сколько високосных годов было между введеным годом и 1600 годом
print('Введите год, а я выведу количество високосных годов между введенным годом и 1600 годом.')
print('Для выхода из программы введите \'q\'.')

while True:
    year_from_user = input('Введите год: ')
    if year_from_user == 'q':
        break
    try:
        year_from_user = int(year_from_user)
        count = 0
        if year_from_user > 1600:
            for year in range(1600, year_from_user + 1):
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    count += 1
        if year_from_user < 1600:
            for year in range(year_from_user, 1600 + 1):
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    count += 1
        print(f"Между 1600 годом и {year_from_user} годом {count} високосных годов.")
    except ValueError:
        print('Ошибка. Введите только год без слов, а для выхода из программы введите \'q\'.')
