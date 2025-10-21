from datetime import datetime as dt

def count_time_sec(data_str):
    try:
        data = dt.strptime(data_str, '%m/%d/%Y %H:%M:%S')
        year = int(data.strftime('%Y'))
        time_delta = data - dt(year, 1, 1, 0, 0, 0)
        print(time_delta.total_seconds())
    except ValueError as error:
        if 'time data' in str(error):
            print('Неверный формат даты или времени')
        elif 'unconverted data remains' in str(error):
            print('Присутствуют символы, не относящиеся к дате')
        else:
            print('Некорректные данные')

count_time_sec(input('Введите дату и время: '))
