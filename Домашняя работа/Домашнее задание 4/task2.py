num = int(input())

if num == 0:
    print('Зелёный')
if 1 <= num <= 10 and num % 2 == 0:
    print('Чёрный')
if 1 <= num <= 10 and num % 2 != 0:
    print('Красный')

if 11 <= num <= 18 and num % 2 == 0:
    print('Красный')
if 11 <= num <= 18 and num % 2 != 0:
    print('Чёрный')

if 19 <= num <= 28 and num % 2 == 0:
    print('Чёрный')
if 19 <= num <= 28 and num % 2 != 0:
    print('Красный')

if 29 <= num <= 36 and num % 2 == 0:
    print('Красный')
if 29 <= num <= 36 and num % 2 != 0:
    print('Чёрный')

if num < 0:
    print('Ошибка ввода')
if num > 36:
    print('Ошибка ввода')