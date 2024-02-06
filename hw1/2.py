a = int(input('Длина стороны a: '))
b = int(input('Длина стороны b: '))
c = int(input('Длина стороны c: '))

if a >= b + c or b >= a + c or c >= a + b:
    print('Такого треугольника быть не может')

else:
    print('Треугольник существует', end='')
    if a == b or b == c or a == c:
        print(' и он равнобедренный')
    elif a == b == c:
        print(' и он равносторонний')
    else:
        print(' и он разносторонний')