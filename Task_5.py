def input_coord():
    user_number = False
    while not (user_number):
        coord_x = input('Введите координату x:')
        coord_y = input('Введите координату y:')
        try:
            coord_x = float(coord_x)
            coord_y = float(coord_y)
            user_number = True
        except ValueError:
            print('Введите число')
    return [coord_x, coord_y]


print('Введите координаты точки A')
A = input_coord()
print('Введите координаты точки B')
B = input_coord()
result = ((B[0]-A[0])**2+(B[1]-A[1])**2)**(1/2)
print(f'A({A[0]}, {A[1]}); B ({B[0]}, {B[1]}) -> {result}')
