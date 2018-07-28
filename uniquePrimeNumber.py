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
    if x<2:
        return 0
    else:
        if x%2==0:
            list.append(2)
            z=x/2
            n=z
            for i in range(3,math.floor(math.sqrt(z)),2):
                if n%i==0:
                    if isPrime(i): 
                        list.append(i)
                    n=n/i    
        return(list)            

z=1234567890000000
print(uniquePrimeNumber(z))
print("The number of unique prime numbers for "+str(z)+" is "+str(len(uniquePrimeNumber(1234567890000000))))



