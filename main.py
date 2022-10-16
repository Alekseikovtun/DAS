import service.db as db

if __name__ == '__main__':
    while True:
        txt = input('Enter or a or s or e: ')
        try:
            if txt == '':
                db.read_data_for_new_task()
                pass
        except StopIteration:
            # End-of-file error handler
            pass
        if txt == 'a':
            latitude = input('Enter the latitude coordinate: ')
            longitude = input('Enter the longitude coordinate: ')
            db.add_coordinate_to_db(latitude, longitude)
        if txt == 's':
            drone_id = input('Enter the drone id: ')
            battery = input('Enter the battery level: ')
            d_latitude = input('Enter the departure latitude coordinate: ')
            d_longitude = input('Enter the departure longitude coordinate: ')
            db.add_dron_status(drone_id, battery, d_latitude, d_longitude)
        if txt == 'e':
            break
