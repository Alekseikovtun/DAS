import service.db as db

if __name__ == '__main__':
    while True:
        txt = input('Enter or a or e: ')
        try:
            if txt == '':
                db.read_data_for_new_task()
                pass
        except StopIteration:
            # End-of-file error handler
            pass
        if txt == 'a':
            latitude = input('Enter the latitude coordinates: ')
            longitude = input('Enter the longitude coordinates: ')
            db.add_coordinate_to_db(latitude, longitude)
        if txt == 'e':
            break
