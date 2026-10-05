def gen_secs():
    for i in range(60):
        yield i
def gen_minutes():
    for i in range(60):
        yield i
def gen_hours():
    for i in range(24):
        yield i
def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)





def gen_years(start=2019):
    year = start
    while True:
        yield year
        year += 1
def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    if month == 2:
        days = 29 if leap_year else 28
    elif month in [4, 6, 9, 11]:
        days = 30
    else:
        days = 31

    for day in range(1, days + 1):
        yield day


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def gen_date():
    for year in gen_years():
        leap = is_leap_year(year)

        for month in gen_months():
            for day in gen_days(month, leap):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)



date_gen = gen_date()
counter = 0
while True:
    date = next(date_gen)
    counter += 1
    if counter % 1000000 == 0:
        print(date)