#Diego Aspinwall and Aidan
#4-23-18
#jarProblem2.py

from random import randint

w=10
n=20

#Strat 3

total=0
picktotal=0
'''
for i in range(0,100000):
    color=randint(0,n-1)+1
    total+=n
    picktotal+=color

pickprob=picktotal/total
print('Prob of picked color',pickprob)
'''


for i in range(0,1):
    red=randint(0,n)
    total+=1
    jar=[]
    for j in range(0,red):
        jar.append('r')
    for k in range(0,n-red):
        jar.append('g')
    print(jar)

