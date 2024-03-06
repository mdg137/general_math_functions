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








        