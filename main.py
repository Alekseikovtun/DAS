import csv
import json


def create_json(json_gps, latitude, longitude):
    x = dict(latitude = latitude, longitude = longitude)
    json_gps.append(x)
    return json_gps


def read_data_for_new_task(filepath):
    with open(filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            yield row


def add_new_row_to_csv(filepath):
    with open(filepath, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        latitude = input('Enter the latitude coordinates: ')
        longitude = input('Enter the longitude coordinates: ')
        str_with_coordinates = [latitude, longitude]
        writer.writerow(str_with_coordinates)


if __name__ == '__main__':
    csv_file_path = 'C:/Users/Asus/Desktop/Python_coding/_Code/Read_and_send_file_DAS/coordinates.csv'
    coordinates_from_file = read_data_for_new_task(csv_file_path)
    json_gps = []
    while True:
        txt = input('Enter or send or end or readjson: ')
        if txt == '':
            gps_row = next(coordinates_from_file)
            print(gps_row)
            coord1 = gps_row[0]
            coord2 = gps_row[1]
            json_file = create_json(json_gps, coord1, coord2)
        if txt == 'readjson':
            print(json_file)
        if txt == 'send':
            add_new_row_to_csv(csv_file_path)
        if txt == 'end':
            break
