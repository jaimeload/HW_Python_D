my_list = [1, 2, 3, 3, 0, 3, 4, 5, 6, 0, 7, 7, 9, 8, 9, 7, 7, 0, 1]
my_set = set(my_list)
doubles = []

for item in my_set:
    my_list.remove(item)
    if item in my_list:
         doubles.append(item)

print(doubles)
