from datetime import datetime

import locale
locale.setlocale(locale.LC_TIME, 'ru_RU')

now = datetime.now()

if __name__ == "__main__":

    print(now.strftime("%m %B %Y года, %H:%M:%S"))