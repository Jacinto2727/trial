from math import sqrt

num=int(input("Enter value:"))

def check_factors(num):
    result=[]
    for i in range(1,int(sqrt(num))+1):
        if num%i==0:
            result.append(i)
            if num//i!=i:
                result.append(num//i)
    result.sort()
    return result

ans=check_factors(num)
print(ans)
