connect = True

while connect == True:
    number = input('Число : ')
    percent = input('Процент : ')
    while type(number) != int:
        try:
            number = int(number)
            percent = int(percent)
        except ValueError:
            print('Вводите цифры')
            number = input('Введите число : ')
            print()
            percent = input('Введите процент : ')
            print()
    while type(number) != float:
        try:
            number = float(number)
            percent = float(percent)
        except ValueError:
            print('Вводите цифры')
            number = input('Введите число : ')
            print()
            percent = input('Введите процент : ')
            print()

    finish = number / 100 * percent
    print('Ваш ответ : ', float(finish))

