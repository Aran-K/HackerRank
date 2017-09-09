#!/bin/python3
import math

count = 0


def count_inversions(a):
    length = len(a)
    if (length <= 1):
        return a
    else:
        midP = int(math.floor(length / 2))
        left = a[:midP]
        right = a[midP:]
        return merge(count_inversions(left), count_inversions(right))


def merge(left, right):
    global count
    result = []
    i = 0
    j = 0
    lenL = len(left)
    lenR = len(right)

    while(i < lenL and j < lenR):
        if (left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += lenL - i
            j += 1

    while (i < lenL):
        result.append(left[i])
        i += 1

    while (j < lenR):
        result.append(right[j])
        j += 1

    return result


a = [2, 1, 3, 1, 4, 2]
print(count_inversions(a))
print(count)
