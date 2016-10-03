class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.calculate()

    def __repr__(self):
        return "%02d:%02d" % (self.hour, self.minute)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def calculate(self):
        self.hour += self.minute // 60
        self.hour %= 24
        self.minute %= 60
        return self

    def add(self, minutes):
        self.minute += minutes
        return self.calculate()


    # First Try
    # def Clock(hour, minute):
    #     totalMinutes = (hour % 24) * 60
    #     totalMinutes += minute % 1440
    #     totalMinutes = totalMinutes % 1440
    #     outputHour = totalMinutes / 60
    #     outputMinutes = totalMinutes % 60
    #     outputTime = format(outputHour, '02') + ":" + format(outputMinutes, '02')
    #     return outputTime
