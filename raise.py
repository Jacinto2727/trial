num=10
try:
    den=int(input("Enter Denominator"))
    if (den==0):
        raise ZeroDivisionError("please enter a Denominator which is not 0")
    print(num/den)
except ZeroDivisionError as e:
    print(e)
    