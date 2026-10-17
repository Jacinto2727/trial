from math import sqrt
num=int(input("Enter number:"))
def check_prime(num):
    if num<2 or (num !=2 and num%2==0): # negative and 1  
        return False
    for i in range(3,int(sqrt(num))+1,2): # loop should not start from 1
            if num%i==0:        # as soon as num gets divisible by number apart from 1, it is not prime
                return False
    return True
            
print(check_prime(num))
    