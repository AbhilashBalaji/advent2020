#! /usr/bin/env python3
print("day 1")
with open("./day1/inp") as f:
    day1 = [line.strip() for line in f]
day1 = list(map(lambda x : int(x),day1))
# print(day1)
day1 = sorted(day1)
for i in day1 :
    for j in day1:
        if 2020-(i+j) in day1:
            print(i,j,2020-(i+j))
            print(i*j*(2020-i-j))
            break