from datetime import datetime, date, time, timedelta

class Turn:
    def __init__(self, created_at, scheduled_for, is_same_day):
        self.created_at = created_at
        self.scheduled_for = scheduled_for
        self.is_same_day = is_same_day

turns = [
    # Week 1
    # some turns added between on Wed 10/27
    # Tue 11/2 - 5 turns added between Thur 10/28 and Tue 11/2
    Turn(datetime(2021, 10, 28), datetime(2021, 11, 2), False),
    Turn(datetime(2021, 10, 29), datetime(2021, 11, 2), False),
    Turn(datetime(2021, 10, 30), datetime(2021, 11, 2), False),
    Turn(datetime(2021, 10, 31), datetime(2021, 11, 2), False),
    Turn(datetime(2021, 11, 1), datetime(2021, 11, 2), False),

    # Week 2
    # some turns added between on Wed 11/3
    # Tue 11/9 - 4 turns added between Thur 11/4 and Tue 11/9
    Turn(datetime(2021, 11, 4), datetime(2021, 11, 9), False),
    Turn(datetime(2021, 11, 5), datetime(2021, 11, 9), False),
    Turn(datetime(2021, 11, 6), datetime(2021, 11, 9), False),
    Turn(datetime(2021, 11, 7), datetime(2021, 11, 9), False),

    # Week 3
    # some turns added between on Wed 11/10
    # Tue 11/16 - 6 turns added between Thur 11/11 and Tue 11/16
    Turn(datetime(2021, 11, 11), datetime(2021, 11, 16), False),
    Turn(datetime(2021, 11, 12), datetime(2021, 11, 16), False),
    Turn(datetime(2021, 11, 13), datetime(2021, 11, 16), False),
    Turn(datetime(2021, 11, 14), datetime(2021, 11, 16), False),
    Turn(datetime(2021, 11, 15), datetime(2021, 11, 16), False),
    Turn(datetime(2021, 11, 16), datetime(2021, 11, 16), True),

    # Week 4
    # some turns added between on Wed 11/17
    # Tue 11/23 - 5 turns added between Thur 11/18 and Tue 11/23
    Turn(datetime(2021, 11, 18), datetime(2021, 11, 23), False),
    Turn(datetime(2021, 11, 19), datetime(2021, 11, 23), False),
    Turn(datetime(2021, 11, 20), datetime(2021, 11, 23), False),
    Turn(datetime(2021, 11, 21), datetime(2021, 11, 23), False),
    Turn(datetime(2021, 11, 22), datetime(2021, 11, 23), False),

    # Curr week
    # Tue 11/30 - 6 turns so far
    Turn(datetime(2021, 11, 24), datetime(2021, 11, 30), False),
    Turn(datetime(2021, 11, 24), datetime(2021, 11, 30), False),
    Turn(datetime(2021, 11, 24), datetime(2021, 11, 30), False),
    Turn(datetime(2021, 11, 24), datetime(2021, 11, 30), False),
    Turn(datetime(2021, 11, 24), datetime(2021, 11, 30), False),
    Turn(datetime(2021, 11, 24), datetime(2021, 11, 30), False)
]

# projected sameday turns
def projected_sameday_turns(date):
    return avg_sameday_turns(date)

def sameday_turns(date):
    return sum(map(lambda turn : turn.scheduled_for == date and turn.is_same_day, turns))

def avg_sameday_turns(date):
    return (sameday_turns(date - timedelta(days=7)) + \
        sameday_turns(date - timedelta(days=14)) + \
        sameday_turns(date - timedelta(days=21)) + \
        sameday_turns(date - timedelta(days=28))) / 4

# projected turns
def projected_turns(date):
    today_beginning = datetime.combine(date.today(), time())
    return scheduled_turns(date) + avg_turns(today_beginning, date)

def scheduled_turns(date):
    return sum(map(lambda turn : turn.scheduled_for == date, turns))

def avg_turns(today, date):
    return (scheduled_between(today - timedelta(days=7), date - timedelta(days=7)) + \
        scheduled_between(today - timedelta(days=14), date - timedelta(days=14)) + \
        scheduled_between(today - timedelta(days=21), date - timedelta(days=21)) + \
        scheduled_between(today - timedelta(days=28), date - timedelta(days=28))) / 4

def scheduled_between(date1, date2):
    return sum(map(lambda turn : date1 <= turn.created_at <= date2, turns))

# test helpers
print(scheduled_turns(datetime(2021, 11, 30)))
print(scheduled_between(datetime(2021, 11, 18), datetime(2021, 11, 22)))
today_beginning = datetime.combine(date.today(), time())
print(avg_turns(today_beginning, datetime(2021, 11, 30)))

# test main funcs
print(projected_turns(datetime(2021, 11, 30)))
print(projected_sameday_turns(datetime(2021, 11, 30)))
