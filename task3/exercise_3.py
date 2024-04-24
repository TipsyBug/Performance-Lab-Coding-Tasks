import json
import sys


def read_json_file(file_path):
    # Читаем JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def update_tests_with_values(tests, values):
    for test in tests:
        # Обновляем найденные значения в values
        if str(test['id']) in values:
            test['value'] = values[str(test['id'])]
        # Рекурсим найденные вложенные тесты
        if 'values' in test:
            update_tests_with_values(test['values'], values)


def write_json_file(file_path, data):
    # Сохраняем JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main(values_json_path, tests_json_path, report_json_path):
    # Загружаем значения из values.json
    values_data = read_json_file(values_json_path)

    # Создаем словарь значений с ключами в виде строк
    values_dict = {str(value_dict['id']): value_dict['value'] for value_dict in values_data['values']}

    # Загружаем  и обновляем структуру из tests.json
    tests_struct = read_json_file(tests_json_path)
    update_tests_with_values(tests_struct['tests'], values_dict)

    # Записываем результат в report.json
    write_json_file(report_json_path, tests_struct)


main(sys.argv[1], sys.argv[2], sys.argv[3])
