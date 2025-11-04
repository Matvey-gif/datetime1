from datetime import datetime

dt = datetime(2024, 1, 15, 14, 30, 45)

# Формат 1: "15/01/24"
format1 = dt.strftime("%d/%m/%y")
print(format1)

# Формат 2: "2024-01-15"
format2 = dt.strftime("%Y-%m-%d")
print(format2)

# Формат 3: "January 15, 2024"
format3 = dt.strftime("%B %d, %Y")
print(format3)