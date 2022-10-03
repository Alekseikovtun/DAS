import csv


def rows_from_csv(filepath):
    with open(filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            yield row


if __name__ == '__main__':
    csv_file_path = 'C:/Users/Asus/Desktop/Python_coding/_Code/Read_and_send_file_DAS/coordinates.csv'
    for row in rows_from_csv(csv_file_path):
        print(row)
