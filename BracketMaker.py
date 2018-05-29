#Insert teams 
teams = []

import random

randomGroup = []
a = []
b = []
c = []
d = []

length = len(teams)
groupLength = int(length/4)

for i in range(length):
    rand = int(random.randrange(0,length-i))
    randomGroup.append(teams[rand])
    teams.pop(rand)

for i in reversed(range(groupLength)):
    a.append(randomGroup[i])
    randomGroup.pop(i)
    b.append(randomGroup[i])
    randomGroup.pop(i)
    c.append(randomGroup[i])
    randomGroup.pop(i)
    d.append(randomGroup[i])
    randomGroup.pop(i)

print(a)
print(b)
print(c)
print(d)

print("Group A")
for i in range(int(groupLength/2)):
    print(str(i+1) + ": " + a[i] + " vs " + str(groupLength-i) + ": " + a[(groupLength-1)-i])
print("Group B")
for i in range(int(groupLength/2)):
    print(str(i+1) + ": " + b[i] + " vs " + str(groupLength-i) + ": " + b[(groupLength-1)-i])
print("Group C")
for i in range(int(groupLength/2)):
    print(str(i+1) + ": " + c[i] + " vs " + str(groupLength-i) + ": " + c[(groupLength-1)-i])
print("Group D")
for i in range(int(groupLength/2)):
    print(str(i+1) + ": " + d[i] + " vs " + str(groupLength-i) + ": " + d[(groupLength-1)-i])
