#Diego Aspinwall and Aidan
#4-24-18
#jarProblem3.py

from random import randint

w=10
n=20

#Strat4

total=0
picktotal=0

for i in range(0,1):
    red=randint(0,n)
    total+=n
    jar=[]
    for j in range(0,red):
        jar.append('r')
    for k in range(0,n-red):
        jar.append('g')
    count=0
    if jar[randint(0,n)]=='r':
        count+=1
    if jar[randint(0,n)]=='r':
        count+=1
    print(count)
