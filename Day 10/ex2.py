def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True

    return leap


def days_in_month(year, month):
    month = month - 1
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 1 and is_leap(year):
        days = 29
    else:
        days = months_days[month]

    return days


year = int(input("Enter year: "))
month = int(input("Enter month: "))

days = days_in_month(year, month)

print(days)

dedede
dedede
