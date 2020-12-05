#! /usr/bin/env python3

print("day 5")

with open("./day5/inp") as f:
    day5 = [line.strip() for line in f]

tr = str.maketrans('FBLR', '0101')
seats = sorted(int(line.translate(tr), 2) for line in day5)
print(max(seats))
print(next(s + 1 for i, s in enumerate(seats[:-1]) if seats[i + 1] == s + 2))


