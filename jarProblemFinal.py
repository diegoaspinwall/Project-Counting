#Diego Aspinwall and Aidan
#5-2-18
#jarProblemFinal.py

from random import randint

w=10
n=20

#Strat1/2
onetotal=0
redtotal=0

for i in range(0,2000):
    red=randint(0,n)
    onetotal+=n
    redtotal+=red

oneprob=redtotal/onetotal
D= oneprob*(-1)*w
print('Probability red/green strategy 1 or 2 =', oneprob)
print('D =', D)

#Strat3
twototal=0
picktotal=0

for i in range(0,100000):
    color=randint(0,n-1)+1
    twototal+=n
    picktotal+=color

pickprob=picktotal/twototal
print('Prob yes color strategy 3 =',pickprob)
P= (-1)*(w*pickprob+D)
print('P = ', P)

#Strat4
threetotal=0
twopicktotal=0
for i in range(0,10000):
    red=randint(0,n)
    threetotal+=n
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
            twopicktotal+=color
            #print('Two picks, same one')
        else:
            color=randint(0,n-2)+2
            twopicktotal+=color
            #print('Two picks, different')
    else:
        rando = randint(0,n-1)
        picks.append(rando)
        if picks[0]==picks[2]:
            color=randint(0,n-2)+1
            twopicktotal+=color
            #print('Three picks, 1st and 3rd same')
        else:
            color=randint(0,n-3)+2
            twopicktotal+=color
            #print('Three picks, all different')

pickprob=picktotal/threetotal
print('Prob of picked color',pickprob)