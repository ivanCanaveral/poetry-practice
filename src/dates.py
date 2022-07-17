""" things to deal with dates"""

import datetime
from xmlrpc.client import DateTime


def is_friday(day: DateTime) -> bool:
    """it's Friday then..."""
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return day.weekday() == 4
