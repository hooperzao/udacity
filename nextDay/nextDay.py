# -*- coding: utf-8 -*-
# @Time      : 023/8/23/17 11:57 PM
# @Author    : Hooper Chao
# @File      : nextDay
# @Created by: PyCharm
###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###


def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


def nextDay0(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if month < 12:
        if day < 30:
            return year, month, day + 1
        else:
            return year, month + 1, 1
    else:
        if day < 30:
            return year, month, day + 1
        else:
            return year + 1, 1, 1


def nextDay1(year, month, day):
    if day == 30:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    else:
        day += 1
    return (year, month, day)


print nextDay(1999, 12, 30)
print nextDay(2013, 1, 30)
print nextDay(2012, 12, 30)
print nextDay(2012, 12, 1)