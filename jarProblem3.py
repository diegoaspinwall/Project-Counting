#Diego Aspinwall and Aidan
#4-24-18
#jarProblem3.py

from random import randint

w=10
n=20

#Strat5

total=0
picktotal=0

#IF THE CHOICES ARE THE SAME, DIFF RANDOGUESSS
#Strat4

for i in range(0,10000):
    red=randint(0,n)
    total+=n
    jar=[]
    for j in range(0,red):
        jar.append('r')
    for k in range(0,n-red):
        jar.append('g')
    count=0
    picks=[]
    #print(jar)
    for b in range(1,3):
        rando = randint(0,n-1)
        if jar[rando]=='r':
            count+=1
        picks.append(rando)
    if count==0 or count==2:
        if picks[0]==picks[1]:
            color=randint(0,n-2)+1
            picktotal+=color
            #print('Two picks, same one')
        else:
            color=randint(0,n-2)+2
            picktotal+=color
            #print('Two picks, different')
    else:
        rando = randint(0,n-1)
        picks.append(rando)
        if picks[0]==picks[2]:
            color=randint(0,n-2)+1
            picktotal+=color
            #print('Three picks, 1st and 3rd same')
        else:
            color=randint(0,n-3)+2
            picktotal+=color
            #print('Three picks, all different')

pickprob=picktotal/total
print('Prob of picked color',pickprob)


'''
for i in range(0,10000):
    red=randint(0,n)
    total+=1
    jar=[]
    for j in range(0,red):
        jar.append('r')
    for k in range(0,n-red):
        jar.append('g')
    pick=[]
    for b in range(1,3):
        rando = randint(0,n-1)
        if jar[rando]=='r':
            pick.append('r')
        else:
            pick.append('g')
    #print(pick)
    if pick[0]==pick[1]:
        guess=pick[0]
        #print('same')
    else:
        rando = randint(0,n-1)
        if jar[rando]=='r':
            guess='r'
        else:
            guess='g'
    #print(guess)
    if jar[randint(0,n-1)]==guess:
        picktotal+=1
print(picktotal/total)
'''

print('R/S =', (w-5)*(1-(picktotal/total))+(-5)*(picktotal/total))
#change -5 sometime?
