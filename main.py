import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

import service.db as db
from models import station

engine = sa.create_engine(station.db)
Session = sessionmaker(bind=engine)
connection = engine.connect()


if __name__ == '__main__':
    # select = connection.execute(
    #     """SELECT * FROM task"""
    # )
    # res = select.all()
    # print(res)
    while True:
        txt = input('Enter or a or e: ')
        try:
            if txt == '':
                # read next coord from db
                pass
        except StopIteration:
            # End-of-file error handler
            pass
        if txt == 'a':
            db.add_coordinate_to_db()
        if txt == 'e':
            break
