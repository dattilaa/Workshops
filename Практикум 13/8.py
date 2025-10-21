from datetime import datetime

def convert_data(date_str):
    try:
        date = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        format_date = date.strftime('%d.%m.%y')
        format_time = date.strftime('%I:%M:%S %p')
        print(f'{format_date} {format_time}')
    except ValueError as error:
        if 'time data' in str(error):
            print('Неверный формат даты или времени')
        elif 'unconverted data remains' in str(error):
            print('Присутствуют символы, не относящиеся к дате')
        else:
            print('Некорректные данные')


convert_data(input('Введите дату и время: '))