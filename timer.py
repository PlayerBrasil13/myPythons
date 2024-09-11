class Timer:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return f"{self.__hour:02d}" + ":" + f"{self.__minute:02d}" + ":" + f"{self.__second:02d}"

    def next_second(self):
        self.__second += 1
        if self.__second > 59:
            self.__second = 0
            self.__minute += 1
        if self.__minute > 59:
            self.__minute = 0
            self.__hour += 1
        if self.__hour > 23:
            self.__hour = 0

    def prev_second(self):
        self.__second -= 1
        if self.__second < 0:
            self.__second = 59
            self.__minute -= 1
        if self.__minute < 0:
            self.__minute = 59
            self.__hour -= 1
        if self.__hour < 0:
            self.__hour = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
