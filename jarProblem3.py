#Diego Aspinwall and Aidan
#4-24-18
#jarProblem3.py

from random import randint

w=10
n=20

#Strat4

total=0
redtotal=0

for i in range(0,10000):
    red=randint(0,n)
    total+=n
    redtotal+=red

redprob=redtotal/total
print('Prob of red',redprob)
print('Prob of green',1-redprob)
print('D =', redprob*(-1)*w)
