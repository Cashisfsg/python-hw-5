from vacations_calendar import CALENDAR as cal
from datetime import datetime

def check(date):

    try:
        day, month, year = date.split('/')

        if len(day) != 2 or len(month) != 2 or len(year) != 4:
            raise ValueError

        new_date = datetime(int(year), int(month), int(day))

        date = date[:5]

        if date in cal.keys():
            print(cal[date])
            return cal[date]
        else:
            print('No holidays on this day')
            return

    except ValueError:
        print('Incorrect format of date')
        return

if __name__ == '__main__':
    check(input('Enter date if format DD/MM/YYYY: '))