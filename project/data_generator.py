from application import db
from application.models import Desk

dates = [
    '19/10/2020',
    '20/10/2020',
    '21/10/2020',
    '22/10/2020',
    '23/10/2020',
    '24/10/2020',
    '25/10/2020'
]

def main():

    for date in dates:                    # 7 dates
        for floor in range(1,5):          # 4 floors
            for row in range(1,5):        # 4 rows
                for col in range(1,5):    # 4 columns

                    r = [str(date), str(floor), str(floor) + str(row) + str(col), 'N']
                    print(r)
                    d = Desk(date=r[0],floor=r[1],desk=r[2],occupied=r[3])
                    db.session.add(d)

    db.session.commit()


if __name__ == "__main__":
    main()
