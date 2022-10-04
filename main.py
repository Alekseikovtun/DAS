import csv


def read_data_for_new_task(filepath):
    with open(filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            yield row


def add_new_row_to_csv(filepath):
    with open(filepath, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        latitude = input('Введите координаты широты: ')
        longitude = input('Введите координаты долготы: ')
        str_with_coordinates = [latitude, longitude]
        writer.writerow(str_with_coordinates)


if __name__ == '__main__':
    csv_file_path = 'C:/Users/Asus/Desktop/Python_coding/_Code/Read_and_send_file_DAS/coordinates.csv'
    coordinates_from_file = read_data_for_new_task(csv_file_path)
    while True:
        txt = input('Enter or send or end: ')
        if txt == '':
            print(next(coordinates_from_file))
        if txt == 'send':
            add_new_row_to_csv(csv_file_path)
        if txt == 'end':
            break
