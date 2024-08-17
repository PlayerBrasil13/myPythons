def is_year_leap(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year): month_list[1] += 1
    return month_list[month]

def day_of_year(year, month, day):
    month_sum = 0
    if day > days_in_month(year, month-1): return
    for i in range(month):
        month_sum += days_in_month(year, i)
    return month_sum

print(day_of_year(2024, 7, 18))
