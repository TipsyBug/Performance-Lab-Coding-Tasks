import sys


def min_moves(nums):
    # Считаем шаги до медианы по списку
    nums.sort()
    median = nums[len(nums) // 2]

    moves = 0

    for num in nums:
        moves += abs(num - median)
    return moves


def main(file_path):
    # Читаем данные из файла и выводим результат с минимальным количеством ходов
    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file.readlines()]

    print(min_moves(nums))


main(sys.argv[1])
