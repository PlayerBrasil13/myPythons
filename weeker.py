class WeekDayError(Exception):
    pass
	

class Weeker:
    week_days = "Mon", "Thu", "Wed", "Thu", "Fri", "Sat", "Sun"
    def __init__(self, day):
        if day in Weeker.week_days:
            self.__day = day
            self.__index_day = Weeker.week_days.index(day)
        else: raise WeekDayError

    def __str__(self):
        self.__index_day %= 7
        self.__day = Weeker.week_days[self.__index_day]
        return self.__day

    def add_days(self, n):
        self.__index_day += n

    def subtract_days(self, n):
        self.__index_day -= n

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
