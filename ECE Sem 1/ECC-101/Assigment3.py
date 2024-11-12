
# Question 1

def smallestFactor(n):
    fac = 2
    while(fac<=n):
        if(n%fac==0):
            return fac
        fac+=1

# Question 2

def hcf(a, b):
    fac = 2
    hcf = 1
    while(fac<=a and fac<=b):
        if(a%fac==0 and b%fac==0):
            hcf = fac
        fac+=1
    return hcf

# Question 3

def bin(x):
     binary=""
     while x>0:
          y= str(x%2)
          x= x//2
          binary = y + binary
     return binary 

def power(a, b):
    binary = bin(b)
    n = a
    ans = 1
    for s in binary[::-1]:
        if(s=="1"):
            ans*=n
        n*=n
    return ans

# Question 4

def fib(n):
    if(n==1 or n==2):
        return 1
    if(n%2==0):
        return fib(n/2)**2 + 2*fib(n/2)*fib(n/2-1)
    return fib(n//2)**2 + fib(n//2+1)**2

# Question 5

import random
from matplotlib.pyplot import plot, figure, show

def long(a):
    if len(a) == 1:
        figure(1)
        plot(a)
        return 1
    s, e = 0, 0
    plot1 = plot2 = plot3 = plot4 = 0
    i = 0
    while(i<len(a)-1):
        j = i
        while(i<len(a)-1 and a[i]<=a[i + 1]):
            i += 1
        if (i-j>s-1):
            s = i-j+1
            plot1, plot2 = j, i
        i+=1
    i=0
    while (i<len(a)-1):
        j = i
        while (i<len(a)-1 and a[i]>=a[i+1]):
            i+=1
        if (i-j>e-1):
            e=i-j+1
            plot3, plot4 = j, i
        i+=1
    figure(1)
    plot(a)
    if s>=e:
        plot(range(plot1, plot2 + 1), a[plot1:plot2 + 1])
        return s
    else:
        plot(range(plot3, plot4 + 1), a[plot3:plot4 + 1])
        return e

a = [random.randint(1, 100) for x in range(1,100)]
show()

# Question 6

def merge(a,b):
    i = 0 
    j = 0 
    c = []
    while i<=len(a)-1 or j<=len(b)-1:
        if i>len(a)-1:
            c.append(b[j])
            j+=1
        elif j>len(b)-1:
            c.append(a[i])
            i+=1
        elif a[i]>b[j]:
            c.append(b[j])
            j = j+1
        else:
            c.append(a[i])
            i = i+1
    return c

def merge_sort(list):
    if len(list) == 1:
        return list
    else:
        z = int(len(list)/2)
        L1 = list[:z]
        L2 = list[z:]
        return merge(merge_sort(L1),merge_sort(L2))
print(merge_sort([1,4,3,65]))