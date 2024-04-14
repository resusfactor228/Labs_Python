from datetime import datetime


def nearest_date(*dates):
    dates = [date for date in dates]
    index = 0
    same_year = []
    same_year_n_month = []
    same_date = []

    # фильтр по годам
    # dates.sort(key=lambda date: date.split(".")[2])
    for i in range(len(dates)):
        if int(dates[i].split(".")[2]) == int(datetime.now().year):
            same_year.append(dates[i])

    delta = 1000
    if not len(same_year):
        for i in range(len(dates)):
            if abs(datetime.now().year - int(dates[i].split(".")[2])) <= delta:
                delta = abs(datetime.now().year - int(dates[i].split(".")[2]))
                index = i
        return dates[index]

    # фильтр по месяцам
    # same_year.sort(key=lambda date: date.split(".")[1])
    for i in range(len(same_year)):
        if int(same_year[i].split(".")[1]) == int(datetime.now().month):
            same_year_n_month.append(same_year[i])

    delta = 1000
    if not len(same_year_n_month):
        for i in range(len(same_year)):
            if abs(datetime.now().month - int(same_year[i].split(".")[1])) <= delta:
                delta = abs(datetime.now().month - int(same_year[i].split(".")[1]))
                index = i
        return same_year[index]

    # фильтр по дням
    # same_year_n_month.sort(key=lambda date: date.split(".")[0])
    for i in range(len(same_year_n_month)):
        if int(same_year_n_month[i].split(".")[0]) == int(datetime.now().day):
            return same_year_n_month[i]

    delta = 1000
    if not len(same_date):
        for i in range(len(same_year_n_month)):
            if abs(datetime.now().day - int(same_year_n_month[i].split(".")[0])) <= delta:
                delta = abs(datetime.now().day - int(same_year_n_month[i].split(".")[0]))
                index = i
        return same_year_n_month[index]


print(datetime.now())
print(nearest_date("02.03.2021", "02.03.2001", "06.09.2024", "08.04.2024", "05.09.2052"))
