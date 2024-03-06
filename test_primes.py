import pytest
import primes

def test_isitprime():
    assert primes.isitprime(1009)==True
    assert primes.isitprime(1247)==False

def test_isitprime_generator():
    x=primes.isitprime_generator(24)
    for value in x:
        assert primes.isitprime(value)==True

def test_smallest_prime_factor():
    assert primes.smallest_prime_factor(76576500)==2

def test_prime_factors():
    assert primes.prime_factors(360)==[2,2,2,3,3,5]

def test_divisorset():
    assert primes.divisorset(primes.prime_factors(360))==set([1.0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360])