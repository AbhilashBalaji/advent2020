#! usr/bin/python3
import regex as re

print("day 2")
with open("./day2/inp") as f:
    day2 = [line.strip() for line in f]
'''
([\d]*)-([\d]*) (\w): ([\w]*)
g1 : first number 
g2 : second number 
g3 : actual character 
g4 : password
'''
valid1 = 0
valid2 = 0
regexp = re.compile("([\d]*)-([\d]*) (\w): ([\w]*)")
for l in day2:
    r = regexp.match(l)
    if r.group(4).count(r.group(3)) in range(int(r.group(1)),int(r.group(2))+1):
        valid1+=1

    i1 = int(r.group(1)) -1
    i2 = int(r.group(2)) -1

    c1 = r.group(4)[i1]
    c2 = r.group(4)[i2]
    if c1 != c2 and( c1 == r.group(3) or c2 == r.group(3))  :
        valid2+=1

    


print('Part 1',valid1)
print('Part 2',valid2)


# print(day2)