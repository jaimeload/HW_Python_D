def can_place_queens(queens):
    for i in range(8):
        for j in range(i+1, 8):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                return False
    return True

coordinates = [(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]

def check_queens_attack(coordinates):
    queens = [coord[1] for coord in coordinates]
    return can_place_queens(queens)

result = check_queens_attack(coordinates)
print(result)