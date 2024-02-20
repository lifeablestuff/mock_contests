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

'''
same = [['A','B'],['G','L'],['J','K']]
seper = [['D','F'],['D','G']]
finalized = [['A C G'],['B D F'],['E H I'],['J K L']]
'''
temp = []
violations = 0
same_violated = False
seper_violated = False
confirm = False
for x in finalized:
    temp.append(x[0].split(' '))

for y in same:
    for s in temp:
        if y[0] in s and y[1] in s:
            same_violated = False
            break
        else:
            same_violated = True
     
    if same_violated == True:
        violations += 1
confirm = False

for z in seper:
    for g in temp:
        if z[0] in g and z[1] in g:
                seper_violated = True
                break
        else:
            seper_violated = False
    if seper_violated == True:
        violations += 1
        


print(violations)