#Program that asks the user for weight in kilograms and converts it to pounds
while True:
    kg = input('Напишите килограммы, а я конвертирую в фунты. Для выхода введите \'q\'\n')
    if kg == 'q':
        break
    try:
        kg = float(kg)
        print(f"{kg} киллограмм = {kg*2.2} фунт")
    except ValueError:
        print('Ошибка. Вводите только цифры, а для выхода из программы введите \'q\'')