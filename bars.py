import json
import os
import math


def load_data(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['Cells']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['Cells']['SeatsCount'])
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    closet_bar = min(data, key=lambda x: math.sqrt
                     ((x['Cells']['geoData']['coordinates'][0]-longitude)**2 +
                      (x['Cells']['geoData']['coordinates'][1]-latitude)**2))

    return closet_bar


def show_info_for_bar(bar):
    print('\nНазвание: %s' % (bar['Cells']['Name']))
    print('Вместимость: %s' % (bar['Cells']['SeatsCount']))
    print('Координаты: %s\n' % (bar['Cells']['geoData']['coordinates']))


if __name__ == '__main__':
    while True:
        filepath = input('Введите путь к файлу: ')
        data = load_data(filepath)

        if data is None:
            print('Вы ввели не корректный путь к файлу, повторите ввод')

        else:
            break

        print('\n1.Показать самый большой бар\n'
              '2.Показать самый маленький бар\n'
              '3.Показать ближайший бар \n'
              '4.Выход из программы\n')

    while True:
        number = float(input('>> '))

        if number == 1:
            show_info_for_bar(get_biggest_bar(data))

        elif number == 2:
            show_info_for_bar(get_smallest_bar(data))

        elif number == 3:
            longitude = float(input('Введите вашу долготу: '))
            latitude = float(input('Введите вашу широту: '))
            show_info_for_bar(get_closest_bar(data, longitude, latitude))

        elif number == 4:
            break

        else:
            print('Вы ввели некорректное значение, повторите ввод')
