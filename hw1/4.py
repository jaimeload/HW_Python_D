LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRY_LIMIT = 10
TRY_COUNT = TRY_LIMIT

import random
random_n = random.randint(LOWER_LIMIT, UPPER_LIMIT)

while TRY_COUNT > 0:
    n = int(input(f'Попытка {int(TRY_LIMIT - TRY_COUNT + 1)} из {TRY_LIMIT} - Введите число: '))
    if n > random_n:
        print('Меньше')
    elif n < random_n:
        print('Больше')
    else:
        print('Вы угадали!')
        break
    TRY_COUNT = TRY_COUNT - 1
