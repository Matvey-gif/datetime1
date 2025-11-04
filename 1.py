from datetime import datetime, date, time, timedelta, timezone

import locale
locale.setlocale(locale.LC_TIME, '')

now = datetime.now()

if __name__ == "__main__":

    print("Задача №1:", now.strftime("%m %B %Y года, %H:%M:%S"))