from datetime import datetime, timedelta
current_date = datetime(2024, 1, 15)
future = current_date + timedelta(days=1)
print(f"Cледующий день: {future.strftime("%Y-%m-%d")}")