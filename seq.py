import numpy as np

def fib_seq(n):
    fib0=0
    fib1=1
    m=0
    while m<=n:
        fibn=fib1+fib0
        yield fibn
        fib0,fib1=fib1,fib0+fib1
        m+=1

def factorial_recursive(value):
    if value == 0:
        return 1
    elif value == 1:
        return 1
    else:
        answer=value*factorial_recursive(value-1)
        return answer

def factorial_generator():
    fact0=1
    fact1=2
    while True:
        yield fact1*fact0
        fact0,fact1=fact1*fact0,fact1+1

x=factorial_generator()
for i in range(2,13):
    print(next(x),i)

        


