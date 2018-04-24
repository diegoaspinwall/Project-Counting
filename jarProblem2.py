#Diego Aspinwall and Aidan
#4-23-18
#jarProblem.py

from random import randint

w=10
n=20

total=0
picktotal=0

for i in range(0,100000):
    color=randint(0,n-1)+1
    total+=n
    picktotal+=color

pickprob=picktotal/total
print('Prob of picked color',pickprob)


