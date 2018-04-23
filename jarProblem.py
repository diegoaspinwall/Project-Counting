#Diego Aspinwall and Aidan
#4-23-18
#jarProblem.py

from random import randint

w=10
n=20

#Strat1

total=0
redtotal=0

for i in range(0,10000):
    red=randint(0,n)
    total+=20
    redtotal+=red

redprob=redtotal/total
print(redprob)
print(1-redprob)

