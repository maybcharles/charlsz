from pathlib import Path as w

def isComposite(number):
    if number==2 or number!=int(number) or number<0:
        return False
    if number==0:
        return True
    sqrtNumber=number**0.5
    for i in range (int(sqrtNumber)):
        x=number/(i+2)
        if x==int(x):
            return True
        else:
            continue
    return False

def primeFactors1(number):
    if number==0:
        return False
    if isComposite(number):
        half_number=number/2
        for i in range (int(half_number)):
            y=i+1
            x=number/y
            if not isComposite(x) and x==int(x):
                print(x)

                
def primeFactors2(number):
    if number==0:
        return False
    if isComposite(number):
        half_number=number/2
        for i in range (int(half_number)):
            y=i+1
            x=number/y
            if not isComposite(y) and x==int(x):
                print(y)

def fullthing(number):
    if isComposite(number):
        if number==0:
            print('no prime factors')
            return False
    half_number=number/2
    primeFactors1(number)
    primeFactors2(number)
    x=2
    n=1
    while x>=2:
        x=number**(1/n)
        if x==int(x) and not isComposite(x):
            for i in range (n-2):
                print(x)
            n=n+1
        else:
            n=n+1
    

def differentPrimeFactors(number):
    if number!=int(number):
        print('this is a float')
        return False
    if number==0:
        print('this has no prime factors')
    if number<0:
        print('this is negative')
        return False
    if not isComposite(number):
        print('this is prime')
        return False
    if isComposite(number) and number!=0:
        x=2
        changing_number=number
        factors='1,'
        while changing_number!=1:
            changing_number=changing_number/x
            if changing_number!=int(changing_number):
                changing_number=changing_number*x
                x=x+1
            else:
                string_x=str(x)
                factors=factors+string_x+','
                w=open('prime_factors.txt','a')
                w.write(factors)
                w.close()
        w=open('prime_factors.txt','w')
        w.write(factors)
        w.close()
        print(factors)
    
