from datetime import datetime

date_str = input("Введите дату в формате 'ДД.MM.ГГГГ': ")

try:
    date = datetime.strptime(date_str, '%d.%m.%Y')
    print("Дата корректна.")
except ValueError:
    print("Дата некорректна.")
