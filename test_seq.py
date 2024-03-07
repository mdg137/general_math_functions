import pytest
import seq
import math


def test_fib_gen():
    generator=seq.fib_seq(1000)
    for i in range(0,333):
        a=next(generator)
        b=next(generator)
        c=next(generator)
        assert c==a+b

def test_factorial_recursive():
    assert seq.factorial_recursive(0)==1
    assert seq.factorial_recursive(1)==1
    for i in range(2,11):
        assert seq.factorial_recursive(i)==i*seq.factorial_recursive(i-1)

def test_factorial_generator():
    generator=seq.factorial_generator()
    for i in range(2,11):
        assert next(generator)==math.factorial(i)

def test_general_sequence():
    initial_values=[0,1]
    x=lambda a,b:a*b
    general_generator=seq.general_sequence(initial_values,x)
    for i in range(0,10):
        a=next(general_generator)
        b=next(general_generator)
        assert next(general_generator)==x(a,b)
        
        







        