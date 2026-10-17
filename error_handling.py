'''
1) Avoid shutting down the full code
2) We should handle error gracefuuly

Syntax error:During compilation
Exception/Runtime error: During execution in interpreter

Whenever python comes accross errors it specifies the code snippets that were responsible for those errors
This is known as Stack Trace, has its own advantages but causes security vulnerabilities
'''
#1 Try and Except block
''' Put those things in try block where you expect there are chances of error'''
numerator=10
try:
    denominator=int(input("Enter denominator:"))
    print(numerator/denominator)
except:
    print("An error occured!")

