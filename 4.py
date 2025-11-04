from datetime import date
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if today < date(today.year, birth_date.month, birth_date.day):
        age -= 1
    return age
birth_day = date(1990, 5, 15)
print(f"Возраст: {calculate_age(birth_day)} лет")

