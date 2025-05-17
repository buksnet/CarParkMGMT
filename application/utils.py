from datetime import timedelta

from dateutils import relativedelta


def to_relativedelta(tdelta: timedelta):
    return relativedelta(seconds=int(tdelta.total_seconds()),
                         microseconds=tdelta.microseconds)
