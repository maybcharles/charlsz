
def isNotPrimeCheck(number):
    sqrtNumber=number**0.5;
    if number==2:
        return False
    if number<0:
        print('this is negative');
        return False;
    if number==0:
        print('this is zero, so be careful');
        return True;
    if not number==int(number):
        print('this is not an interger');
        return False;
    for i in range (int(sqrtNumber)):
        x=number/(i+2);
        if x==int(x):
            return True
    return False

def isNotPrime2(number):
    sqrtNumber=number**0.5;
    if number==2:
        return False
    if number<0:
        return False;
    if number==0:
        return True;
    if not number==int(number):
        return False;
    for i in range (int(sqrtNumber)):
        x=number/(i+2);
        if x==int(x):
            return True
    return False

def primeFactors(number):
    if isNotPrimeCheck(number)and number !=0:
        sqrt_number=number**0.5;
        for i in range (int(sqrt_number)+1):
            x=number/(i+1);
            if isNotPrime2(x):
                continue;
            else:
                print(x);
    elif number==0:
            print('no prime factors')
    else:
        print('prime')
