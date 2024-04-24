import sys


# Устанавливаем границы значений координат, радиуса и количества точек
MIN_COORD = -10 ** 38
MAX_COORD = 10 ** 38
MAX_RADIUS = 10 ** 38
MIN_POINTS = 1
MAX_POINTS = 100


def read_circle_data(filepath):
    # Читаем данные окружности и проверяем валидность
    with open(filepath, 'r') as file:
        center = tuple(map(float, file.readline().split()))
        if not (MIN_COORD < center[0] < MAX_COORD) or not (MIN_COORD < center[1] < MAX_COORD):
            raise ValueError(f"Координаты центра должны быть в диапазоне от {MIN_COORD} до {MAX_COORD}")
        radius = float(file.readline())
        if not (0 < radius < MAX_RADIUS):
            raise ValueError(f"Радиус должен быть в диапазоне от 0 до {MAX_RADIUS}")
        return center, radius


def read_points(filepath):
    # Читаем данные точек и проверяем валидность
    with open(filepath, 'r') as file:
        points = [tuple(map(float, line.split())) for line in file.readlines()]
        if not (MIN_POINTS <= len(points) <= MAX_POINTS):
            raise ValueError(f"Количество точек должно быть от {MIN_POINTS} до {MAX_POINTS}")
        for point in points:
            if not (MIN_COORD < point[0] < MAX_COORD) or not (MIN_COORD < point[1] < MAX_COORD):
                raise ValueError(f"Координаты точек должны быть в диапазоне от {MIN_COORD} до {MAX_COORD}")
        return points


def point_circle_position(center, radius, point):
    # Проверяем положение точки относительно окружности
    distance_squared = (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2
    radius_squared = radius ** 2
    if distance_squared < radius_squared:
        return 1
    elif distance_squared == radius_squared:
        return 0
    else:
        return 2


def main(circle_data, points_data):
    # Читаем данные окружности и точек
    center, radius = read_circle_data(circle_data)
    points = read_points(points_data)

    for point in points:
        position = point_circle_position(center, radius, point)
        print(position)


main(sys.argv[1], sys.argv[2])
