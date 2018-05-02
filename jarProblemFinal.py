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
P= (-1)*(w*oneprob+D)
print('P= ', P)
