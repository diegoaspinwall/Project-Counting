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

print('Probability red/green strategy 1/2 =', oneprob)
