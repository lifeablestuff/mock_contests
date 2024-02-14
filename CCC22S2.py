import sys
info = sys.stdin.read().split('\n')
samegroup = []
seperated = []
groups = []
finalized = []
temp = []
same = []
seper = []
violations = 0
#sorting the data
for x in range(len(info)):
    if info[x].isdigit():
        temp = []
        for y in info[x+1:int(info[x])+x+1]:
            temp.append(y)
        groups.append(temp)
        

samegroup.append(groups[0])
seperated.append(groups[1])
finalized=groups[2]
temp = []

for x in samegroup:
   for y in x:
       same.append(y.split(' '))

for x in seperated:
    for y in x:
        seper.append(y.split(' '))

print(finalized)

for x in finalized:
    for y in same:
        temp = x.split(' ')
        print(temp)
        if y[0] and y[1] not in x.split(' '):
            violations += 1
    for z in seper:
        if y[0] and y[1] in x.split(' '):
            violations += 1

print(violations)
