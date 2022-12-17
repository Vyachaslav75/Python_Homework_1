for x in (False, True):
    for y in (False, True):
        for z in (False, True):
            if not (x and y and z) == (not x or not y or not z):
                print(f'X={x}, Y={y}, Z={z}, Result= True')
            else:
                print(f'X={x}, Y={y}, Z={z}, Result= False')
