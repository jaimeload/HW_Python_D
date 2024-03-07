import random


def can_place_queens(queens):
    for i in range(8):
        for j in range(i+1, 8):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                return False
    return True
def generate_random_queens():
    queens = []
    for i in range(8):
        queens.append((i+1, random.randint(1, 8)))
    return queens

def check_successful_placements(num_attempts):
    successful_placements = []

    for _ in range(num_attempts):
        queens = generate_random_queens()
        if can_place_queens([coord[1] for coord in queens]):
            successful_placements.append(queens)

        if len(successful_placements) == 4:
            break

    return successful_placements

successful_results = check_successful_placements(1000)

for i, result in enumerate(successful_results):
    print(f"Successful placement {i+1}: {result}")