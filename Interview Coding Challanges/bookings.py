#!/bin/python3
import sys

polygons = []

for line in sys.stdin.readlines():
    polygon = line.split(' ')
    for i in range(len(polygon)):
        polygon[i] = int(polygon[i])
    polygons.append(polygon)

squares = 0
recs = 0
other = 0

for polygon in polygons:
    if polygon[0] == polygon[1] == polygon[2] == polygon[3]:
        squares = squares + 1
        print(polygon, 's')
    elif ((polygon[0] == polygon[2]) and
        (polygon[1] == polygon[3])):
        recs = recs + 1
        print(polygon, 'r')
    else:
        other += 1
        print(polygon, 'o')

print(squares, recs, other)
