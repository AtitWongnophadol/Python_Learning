import math

def isPrime(number):
    if number<2:
        return False
    elif number<=3:
        return True
    else:
        i=2
        count=0
        while i<number:
            if number%i == 0:
                return False
            i+=1
        return True     

def uniquePrimeNumber(x):
    list=[]
    x=abs(x)
    if x<2 or x!=int(x):
        return list
    elif isPrime(x):
        list.append(x)
        return list
    else:
        if x%2==0:
            list.append(2)
            z=x/2
        else:
            z=x
        y=math.sqrt(z)
        if y==int(y):
            for i in range(3,int(y)+1,2): 
                    if x%i==0:
                        if isPrime(i): 
                            list.append(i)
                        x=x/i   
            return list      
        else:  
            for i in range(3,int(z),2): 
                    if x%i==0:
                        if isPrime(i): 
                            list.append(i)
                        x=x/i   
            return list      

#z=1234567890000000
#z=4849845
#z=-969969
#z=1769
z=3721
print(uniquePrimeNumber(z))
print("The number of unique prime numbers for "+str(z)+" is "+str(len(uniquePrimeNumber(z))))
