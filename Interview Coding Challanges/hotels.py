#!/bin/python3

words = input().split(' ')
numOfReviews = int(input())

reviews = []

for n in range(numOfReviews):
    hotelId = input()
    content = input()
    reviews.append([hotelId, content, 0])

for review in reviews:
    count = 0
    print(review[1])
    for word in review[1]:
        if word in words:
            count += 1
    review[2] = count

print(reviews)