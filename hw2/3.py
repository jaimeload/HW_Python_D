#import fractions

frac_1 = [int(x) for x in input('Введите первую дробь вида “a/b”: ').split('/')]
frac_2 = [int(x) for x in input('Введите вторую дробь вида “a/b”: ').split('/')]

summ = (frac_1[0] * frac_2[1] + frac_2[0] * frac_1[1]) / (frac_1[1] * frac_2[1])
print(f'Сумма дробей: {summ}')
prod = (frac_1[0] * frac_2[0]) / (frac_1[1] * frac_2[1])
print(f'Произведение дробей: {prod}')

f1 = fractions.Fraction(int(frac_1[0]), int(frac_1[1]))
f2 = fractions.Fraction(int(frac_2[0]), int(frac_2[1]))

print(f1 + f2 - summ)
print(f1 * f2 - prod)
