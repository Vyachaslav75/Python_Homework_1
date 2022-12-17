user_number = 0
while not (user_number):
    num = input('Введите номер дня недели:')
    if num.isdigit():
        if 0 < int(num) < 8:
            user_number = int(num)
        else:
            print('Введите число от 1 до 7')
    else:
        print('Введите число от 1 до 7')
if user_number in (6, 7):
    print(f'{user_number} -> да')
else:
    print(f'{user_number} -> нет')
