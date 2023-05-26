#Программа высчитывает 'perfect number' до определенного числа введенного пользователем и выводит ответ в виде массива
while True:
    print('Введите число и я высчитаю какие числа являются являются идеальными в диапазоне от 1 до x')
    print('Для выхода из программы введите \'q\'')
    x = input('Введите число: ')
    if x == 'q':
        break
    try:
        x = int(x)
        result = []
        for num in range(1, x + 1):
            summa = 0
            for i in range(1, num):
                if num % i == 0:
                    summa += i
            if summa == num:
                result.append(num)
        print(f"В диапазоне от 1 до {x} идеальными числами являются:\n{result}")
    except ValueError:
        print('Ошибка. Введите только число, а для выхода из программы \'q\'')
#Тесты:
#input: 10000 output: [6, 28, 496, 8128]
#input: 300 output : [6, 28]