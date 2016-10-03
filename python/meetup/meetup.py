from datetime import date
import dateutil.relativedelta as relativedelta
import re
import time


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, dow, arg):
    weekday = relativedelta.weekday(time.strptime(dow, '%A').tm_wday)
    startDate = date(year, month, 1)
    if arg == "teenth":
        return relativedelta.relativedelta(day=13, weekday=weekday) + startDate
    elif arg == "last":
        return relativedelta.relativedelta(months=1, days=-7, weekday=weekday) + startDate
    else:
        occurance = int(re.findall('(\d+)', arg)[0])
        meetupDay = relativedelta.relativedelta(weekday=weekday(occurance)) + startDate
        if meetupDay.month == month:
            return meetupDay
        else:
            raise MeetupDayException()
