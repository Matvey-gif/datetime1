from datetime import datetime

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 2, 1)
difference = date2 - date1


if __name__ == "__main__":

    print(difference.days, "день")