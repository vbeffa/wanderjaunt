from datetime import datetime, date, time, timedelta

class Turn:
    def __init__(self, created_at, scheduled_for, is_same_day):
        self.created_at = created_at
        self.scheduled_for = scheduled_for
        self.is_same_day = is_same_day

turns = [
    # Week 1
    # some turns added on Wed 10/27, not shown
    # Tue 11/2 - 5 turns added between Thur 10/28 and Tue 11/2
    Turn(datetime(2021, 10, 28), datetime(2021, 11, 2), False),
    Turn(datetime(2021, 10, 29), datetime(2021, 11, 2), False),
    Turn(datetime(2021, 10, 30), datetime(2021, 11, 2), False),
    Turn(datetime(2021, 10, 31), datetime(2021, 11, 2), False),
    Turn(datetime(2021, 11, 1), datetime(2021, 11, 2), False),

    # Week 2
    # some turns added on Wed 11/3, not shown
    # Tue 11/9 - 4 turns added between Thur 11/4 and Tue 11/9
    Turn(datetime(2021, 11, 4), datetime(2021, 11, 9), False),
    Turn(datetime(2021, 11, 5), datetime(2021, 11, 9), False),
    Turn(datetime(2021, 11, 6), datetime(2021, 11, 9), False),
    Turn(datetime(2021, 11, 7), datetime(2021, 11, 9), False),

    # Week 3
    # some turns added on Wed 11/10, not shown
    # Tue 11/16 - 6 turns added between Thur 11/11 and Tue 11/16
    Turn(datetime(2021, 11, 11), datetime(2021, 11, 16), False),
    Turn(datetime(2021, 11, 12), datetime(2021, 11, 16), False),
    Turn(datetime(2021, 11, 13), datetime(2021, 11, 16), False),
    Turn(datetime(2021, 11, 14), datetime(2021, 11, 16), False),
    Turn(datetime(2021, 11, 15), datetime(2021, 11, 16), False),
    Turn(datetime(2021, 11, 16), datetime(2021, 11, 16), True),

    # Week 4
    # some turns added on Wed 11/17, not shown
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

# today = date.today()
today = datetime(2021, 11, 25) # for testing

# projected sameday turns
def projected_sameday_turns(date):
    """
    returns the average of the sameday turns on a given day for the last 4 weeks
    """
    return (sameday_turns(date - timedelta(days=7)) + \
        sameday_turns(date - timedelta(days=14)) + \
        sameday_turns(date - timedelta(days=21)) + \
        sameday_turns(date - timedelta(days=28))) / 4

def sameday_turns(date):
    """
    returns the number of sameday turns on a given day
    """
    return sum(map(lambda turn : turn.scheduled_for == date and turn.is_same_day, turns))

# projected turns
def projected_turns(date):
    """
    returns the number of currently scheduled turns for date,
    plus the number of additional projected turns between now and date
    based on the average of the last 4 weeks
    """
    return scheduled_turns(date) + avg_turns(today, date)

def scheduled_turns(date):
    """
    returns the number of turns scheduled on a given day
    """
    return sum(map(lambda turn : turn.scheduled_for == date, turns))

def avg_turns(today, date):
    """
    returns the average turns between now and date for the past 4 weeks
    """
    today_beginning = datetime.combine(today, time())
    return (scheduled_between(today_beginning - timedelta(days=7), date - timedelta(days=7)) + \
        scheduled_between(today_beginning - timedelta(days=14), date - timedelta(days=14)) + \
        scheduled_between(today_beginning - timedelta(days=21), date - timedelta(days=21)) + \
        scheduled_between(today_beginning - timedelta(days=28), date - timedelta(days=28))) / 4

def scheduled_between(date1, date2):
    """
    returns the number of turns scheduled between two dates
    """
    return sum(map(lambda turn : date1 <= turn.created_at <= date2, turns))

# tests
assert(scheduled_turns(datetime(2021, 11, 30)) == 6)
assert(scheduled_between(datetime(2021, 10, 28), datetime(2021, 11, 1)) == 5)
assert(scheduled_between(datetime(2021, 11, 4), datetime(2021, 11, 7)) == 4)
assert(scheduled_between(datetime(2021, 11, 11), datetime(2021, 11, 16)) == 6)
assert(scheduled_between(datetime(2021, 11, 18), datetime(2021, 11, 22)) == 5)
assert(avg_turns(today, datetime(2021, 11, 30)) == 5.0)

# test main funcs
assert(projected_turns(datetime(2021, 11, 30)) == 11.0)
assert(projected_sameday_turns(datetime(2021, 11, 30)) == 0.25)
