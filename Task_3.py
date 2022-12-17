user_number = False
while not (user_number):
    coord_x = input('Введите координату x:')
    coord_y = input('Введите координату y:')
    try:
        coord_x = int(coord_x)
        coord_y = int(coord_y)
        user_number = True
    except ValueError:
        print('Введите целое число')
    if coord_x == 0:
        print('Точка лежит на оси y введите целое число не равное 0')
        user_number = False
    elif coord_y == 0:
        print('Точка лежит на оси x введите целое число не равное 0')
        user_number = False
if coord_x > 0 and coord_y > 0:
    print(f'x={coord_x}; y={coord_y} -> 1')
elif coord_x < 0 and coord_y > 0:
    print(f'x={coord_x}; y={coord_y} -> 2')
elif coord_x < 0 and coord_y < 0:
    print(f'x={coord_x}; y={coord_y} -> 3')
elif coord_x > 0 and coord_y < 0:
    print(f'x={coord_x}; y={coord_y} -> 4')
