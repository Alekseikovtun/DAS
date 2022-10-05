import csv
import json


def create_json(latitude, longitude):
    x = dict(latitude=latitude, longitude=longitude)
    return x


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
    return str_with_coordinates


if __name__ == '__main__':
    csv_file_path = 'coordinates.csv'
    coordinates_from_file = read_data_for_new_task(csv_file_path)
    while True:
        txt = input('Enter or send or end: ')
        try:
            if txt == '':
                gps_row = next(coordinates_from_file)
                coord1 = gps_row[0]
                coord2 = gps_row[1]
                print(create_json(coord1, coord2))
        except StopIteration:
            print('Request for new coordinates...')
            last_row = add_new_row_to_csv(csv_file_path)
            coord1 = last_row[0]
            coord2 = last_row[1]
            print(create_json(coord1, coord2))
        if txt == 'send':
            add_new_row_to_csv(csv_file_path)
        if txt == 'end':
            break
