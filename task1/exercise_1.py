import sys


arguments = sys.argv[1:]
n = int(arguments[0])
m = int(arguments[1])

current_position = 0
path = []

circular_array = list(range(1, n + 1))  # Инициализируем круговой массив

while True:
    path.append(circular_array[current_position])  # Добавляем начальный элемент в список
    new_position = (current_position + m - 1) % n  # Находим следующий начальный элемент двигаясь по кольцу

    if new_position == 0:  # Проверяем условие выхода из кольца
        break

    current_position = new_position  # Актуализируем начальный элемент

path_str = "".join(map(str, path))  # Готовим завершенный путь для вывода
print(path_str)
