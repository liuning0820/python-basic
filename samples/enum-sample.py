# -*- coding: utf-8 -*-
from enum import IntEnum


class TripSource(IntEnum):
    FROM_WEBSITE = 11
    FROM_IOS_CLIENT = 12


def mark_trip_as_featured(source):
    if source == TripSource.FROM_WEBSITE:
        # print(type(source))
        print(source.value)
    elif source == TripSource.FROM_IOS_CLIENT:
        # print(type(source))
        print(source.value)


print(type(TripSource.FROM_WEBSITE))
mark_trip_as_featured(TripSource.FROM_WEBSITE)
