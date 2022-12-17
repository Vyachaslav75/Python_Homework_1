user_number = 0
while not (user_number):
    num = input('Введите номер четверти:')
    if num.isdigit():
        if 0 < int(num) < 5:
            user_number = int(num)
        else:
            print('Введите число от 1 до 4')
    else:
        print('Введите число от 1 до 4')
if user_number == 1:
    print('Диапазон (x, y) x=(0, %c), y=(0, %c)' % (0x221E, 0x221E))
elif user_number == 2:
    print('Диапазон (x, y) x=(-%c, 0), y=(0, %c)' % (0x221E, 0x221E))
elif user_number == 3:
    print('Диапазон (x, y) x=(-%c, 0), y=(-%c, 0)' % (0x221E, 0x221E))
elif user_number == 4:
    print('Диапазон (x, y) x=(0, %c), y=(-%c, 0)' % (0x221E, 0x221E))
