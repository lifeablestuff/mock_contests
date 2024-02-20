'''
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
<<<<<<< HEAD

=======
'''
temp = []
>>>>>>> 4de37bd1c744d97f0fd84bd0101e17ee3d08fd4c
violations = 0
temp = []

same_violated = False
seper_violated = False
confirm = False
for x in finalized:
    temp.append(x[0].split(' '))
<<<<<<< HEAD
print(temp)

if len(same)> 0:
    for y in same:
        for s in temp:
            if y[0] not in s or y[1] not in s:   
                same_violated = True
            else:
                same_violated = False
        if same_violated == True:
            violations += 1

if len(seper) >0:
    for z in seper:
        for g in temp:
            if z[0] in g and z[1] in g:
                seper_violated = True
            else:
                seper_violated = False
                print(z[0],z[1])
        if seper_violated == True:
            violations +=1
=======

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
        

>>>>>>> 4de37bd1c744d97f0fd84bd0101e17ee3d08fd4c

print(violations)