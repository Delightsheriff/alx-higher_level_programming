#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    temp = list_of_integers
    if temp is None or temp == []:
        return None

    low = 0
    high = len(temp)
    mid = ((high - low) // 2) + low
    mid = int(mid)
    if high == 1:
        return temp[0]
    if high == 2:
        return max(temp)
    if temp[mid] >= temp[mid + 1] and temp[mid] >= temp[mid + 1]:
        return temp[mid]
    if mid > 0 and temp[mid] < temp[mid +1]:
        return find_peak(temp[mid:])
    if mid > 0 and temp[mid] < temp[mid - 1]:
        return find_peak(temp[:mid])
