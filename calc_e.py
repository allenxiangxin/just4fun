#How to calculate e using Monte Carlo
import random
random.uniform(0, 1)

N=1000000
sum_n = 0.;
for i in range(N):
    n=0
    s=0.
    while s<=1.:
        s=s+random.random()
        n = n+1
    sum_n = sum_n+ n;
print(sum_n/N) #the average

