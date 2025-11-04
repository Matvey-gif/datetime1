from datetime import datetime
import calendar

date = datetime(2024, 2, 15)
last_day = calendar.monthrange(date.year, date.month)[1]
print(last_day)