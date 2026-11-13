while True:
    text = input("Введите число: ")
    if text.isdigit():
        num = int(text)
        print("Введено целое число:", num)
        break
    else:
        print("Ошибка. Попробуйте еще раз.")