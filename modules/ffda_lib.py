import time
from datetime import datetime


def pretty_date(timestamp=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    now = datetime.now()
    compare = None
    if type(timestamp) is int:
        compare = datetime.fromtimestamp(timestamp)
    elif type(timestamp) is float:
        compare = datetime.fromtimestamp(int(timestamp))
    elif isinstance(timestamp, datetime):
        compare = timestamp
    elif not timestamp:
        compare = now

    diff = now - compare
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "gerade eben"
        if second_diff < 60:
            return "vor " + str(second_diff) + " Sekunden"
        if second_diff < 120:
            return "vor einer Minute"
        if second_diff < 3600:
            return "vor " + str(second_diff / 60) + " Minuten"
        if second_diff < 7200:
            return "vor einer Stunde"
        if second_diff < 86400:
            return "vor " + str(second_diff / 3600) + " Stunden"
    if day_diff == 1:
        return "gestern"
    if day_diff < 7:
        return "vor " + str(day_diff) + " Tagen"

    return "am " + compare.strftime('%d.%m.%Y um %H:%M Uhr')


def day_changed(since):
    then = datetime.fromtimestamp(since).strftime('%x')
    return then != time.strftime('%x')