num = int(input('Введите число: '))
result = ''
HEX = 16
hex_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

print(hex(num))

while num > 0:
    res = num % HEX
    if res in hex_dict:
        res = hex_dict.get(res)
    result = str(res) + result
    num = num // HEX

print('0x' + result)
