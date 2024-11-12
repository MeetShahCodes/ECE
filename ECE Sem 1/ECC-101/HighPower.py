import time

def powerBin(a, n):
    binary = bin(n)
    if(int(binary[-1])==0):
        x = 1
    else:
        x=a
    ans = 1
    for i in range(1, len(binary)-2):
        if(int(binary[-i-1])==0):
            ans *= x
        else:
            ans *= a*x
    return ans
print(powerBin(3, 11))

def power(a, n):
    if(n==0):
        return 1
    elif(n==1):
        return a
    if(n%2==0):
        return power(a, n/2)*power(a, n/2)
    return power(a, n//2)*power(a, n//2+1)

def powerDefault(a, n):
    return a**n

def checkTime(func):
    start_time = time.time()
    func(3, 29)
    end_time = time.time()
    return end_time-start_time

# powerTime = checkTime(power)
# powerDefaultTime = checkTime(powerDefault)
# print(powerTime>powerDefaultTime)

