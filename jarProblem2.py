#Diego Aspinwall and Aidan
#4-23-18
#jarProblem.py

from random import randint

w=10
n=20

#Strat1/2- Always red/green
'''
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

'''


total=0
picktotal=0

for i in range(0,100000):
    color=randint(0,n-1)+1
    total+=n
    picktotal+=color

pickprob=picktotal/total
print('Prob of picked color',pickprob)


