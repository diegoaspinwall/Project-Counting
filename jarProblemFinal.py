#Diego Aspinwall and Aidan
#5-2-18
#jarProblemFinal.py

from random import randint

w=10
n=20
repeated=3000

#the different totals and picktotals (onetotal, twototal...) are just so python doesn't get confused

#Strat1/2
onetotal=0
redtotal=0

for i in range(0,repeated):
    red=randint(0,n)
    onetotal+=n
    redtotal+=red

oneprob=redtotal/onetotal
D= oneprob*(-1)*w
#see the document for explanation of above
print('Probability red/green strategy 1 or 2 =', oneprob)
print('D =', D)

#Strat3
twototal=0
picktotal=0

for i in range(0,repeated):
    red=randint(0,n)
    twototal+=1
    jar=[]
    #makes a jar
    for j in range(0,red):
        jar.append('r')
    for k in range(0,n-red):
        jar.append('g')
    #fills it with random arrangement of red and green
    pick=jar[randint(0,n-1)]
    #chooses random marble
    if pick==jar[randint(0,n-1)]:
        picktotal+=1
    #chooses again, if both are same adds one to the picktotal

pickprob=picktotal/twototal
print('Prob yes color strategy 3 =',pickprob)
P= (-1)*(w*pickprob+D)
print('P = ', P)

#Strat4
threetotal=0
twopicktotal=0
for i in range(0,repeated):
    red=randint(0,n)
    threetotal+=1
    jar=[]
    for j in range(0,red):
        jar.append('r')
    for k in range(0,n-red):
        jar.append('g')
    #creates and fills a jar
    pick=[]
    for b in range(1,3):
        rando = randint(0,n-1)
        if jar[rando]=='r':
            pick.append('r')
        else:
            pick.append('g')
    if pick[0]==pick[1]:
        guess=pick[0]
    else:
        rando = randint(0,n-1)
        if jar[rando]=='r':
            guess='r'
        else:
            guess='g'
    if jar[randint(0,n-1)]==guess:
        twopicktotal+=1

twopickprob=twopicktotal/threetotal
print('Prob of yes color strategy 4 =',twopickprob)
R= (-1)*(w*twopickprob+D)
print('R =', R)

#Strat5
fourtotal=0
threepicktotal=0

for i in range(0,repeated):
    red=randint(0,n)
    fourtotal+=1
    jar=[]
    unchangedjar=[]
    for j in range(0,red):
        jar.append('r')
        unchangedjar.append('r')
    for k in range(0,n-red):
        jar.append('g')
        unchangedjar.append('g')
    pick=[]
    for b in range(1,3):
        rando = randint(0,n-b)
        if jar[rando]=='r':
            pick.append('r')
        else:
            pick.append('g')
        jar.remove(jar[rando])
    if pick[0]==pick[1]:
        guess=pick[0]
        if unchangedjar[randint(0,n-1)]==guess:
            threepicktotal+=1
    else:
        rando = randint(0,n-3)
        if jar[rando]=='r':
            jar.remove(jar[rando])
            guess='r'
        else:
            jar.remove(jar[rando])
            guess='g'
        if unchangedjar[randint(0,n-1)]==guess:
            threepicktotal+=1

threepickprob=threepicktotal/fourtotal
print('Prob of yes color strategy 5',threepickprob)
S= (-1)*(w*threepickprob+D)
print('S =', S)
