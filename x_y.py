#Program that asks the user to enter two numbers, x, and y, and computes | x − y | /  x+y
print('Введите два числа и я расчитаю их по формуле | x − y | /  x+y\nДля выхода их программы введите \'q\'')
while True:
    x = input('Введите число x: ')
    y = input('Введите число y: ')
    if x == 'q' or y == 'q':
        break
    try:
        x = float(int(x))
        y = float(int(y))
        print(f"Результат:{abs(x - y) / (x + y)}")
    except ValueError:
        print('Ошибка. Для корректной работы программы вводите числа, а для выхода из программы введите \'q\'')
    except ZeroDivisionError:
        print('На нуль делить нельзя')