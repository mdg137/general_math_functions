import functools
def fib_seq(n): #recursive fibonacci sequence up to F_n
    fib0=0
    fib1=1
    m=0
    while m<=n:
        fibn=fib1+fib0
        yield fibn
        fib0,fib1=fib1,fib0+fib1
        m+=1

def factorial_recursive(value): #recursive factorial function
    if value == 0:
        return 1
    elif value == 1:
        return 1
    else:
        answer=value*factorial_recursive(value-1)
        return answer

def factorial_generator(): #iterative factorial function (note this does not start at element 0)
    fact0=1
    fact1=2
    while True:
        yield fact1*fact0
        fact0,fact1=fact1*fact0,fact1+1

def general_sequence(initial_values,lambda_function): #general constant-recursive sequence, defined by an arbitrary array of initial values, and a lambda function on those values
    while True:
        next_value=functools.reduce(lambda_function,initial_values) #iterates over initial values with lambda to produce next value
        yield next_value #yields the next value
        initial_values.pop(0) #removes initial element
        initial_values.append(next_value) #puts new element onto end of initial values. 

