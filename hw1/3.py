n = int(input('Введите положительное число, не больше 100000 : '))

if n < 0 or n > 100000:
    print("Число должно быть положительным и не больше 100000")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print('Число простое')
    else:
        print('Число составное')