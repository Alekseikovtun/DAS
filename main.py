import csv


# def read_data_for_new_task(filepath):
#     with open(filepath, 'r') as csv_file:
#         reader = csv.reader(csv_file)
#         for row in reader:
#             yield row

class ReadData:
    def __init__(self, csv_file_path):
        while True:
            self.count = 0
            self.filepath = csv_file_path
            messege = input('Введите Enter для вывода следующего значения или End для выхода из цикла: ')
            with open(self.filepath, 'r') as csv_file:
                reader = csv.reader(csv_file)
                self.row_count = sum(1 for row in reader)
                for row in reader:
                    print(row)
            if messege == 'End':
                break

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.row_count:
            raise StopIteration
        self.count += 1


def add_new_row_to_csv(filepath):
    with open(filepath, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        latitude = input('Введите координаты широты: ')
        longitude = input('Введите координаты долготы: ')
        str_with_coordinates = [latitude, longitude]
        writer.writerow(str_with_coordinates)


if __name__ == '__main__':
    csv_file_path = 'C:/Users/Asus/Desktop/Python_coding/_Code/Read_and_send_file_DAS/coordinates.csv'
    while True:
        messege = input("Enter or Send or End: ")
        if messege == 'Enter':
            ReadData(csv_file_path)
            ReadData.__next__
        if messege == 'Send':
            add_new_row_to_csv(csv_file_path)
        if messege == 'End':
            break
