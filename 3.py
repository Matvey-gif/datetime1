from datetime import datetime

import locale
locale.setlocale(locale.LC_TIME, 'ru_RU')

date = datetime(2024, 1, 15)
print(date.strftime('%A'))