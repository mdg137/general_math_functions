import numpy as np 
import math
from tqdm import trange
import time
def list_primes(limit=10):
    if limit<2:
        return False
    else:
        answer=[]
        for i in trange(2,limit+1):
            if i==2 or i==3:
                answer.append(i)
            else:
                flag=True
                for j in range(2,int(i**0.5)+1):
                    if i % j==0:
                        flag=False
                        break        
                if flag==False: continue
                else:
                    answer.append(i)
    return answer
                        


def isitprime(a = 0):
    if type(a) is not int:
        return False
    elif a<2:
        return False
    elif a==2:
        return True
    isprime=True
    sample=list_primes(np.ceil(a/2).astype(int))
    for i in range (0,len(sample)):
        if np.divide(a,sample[i])==np.divide(a,sample[i]).astype(int):
            isprime=False
    return isprime

def isitprime_generator(n):
    previous_primes=[2]
    j=2
    i=0
    while j<n and j>=2:
        if j==2:
            yield j
            i+=1
            j+=1
        else:   
            flag=True
            for x in previous_primes:
                if j/x==j//x:
                    flag=False
                    break    
            if flag==True:
                previous_primes.append(j)
                yield j
                i+=1
                j+=1
            else:
                j+=1
    

def smallest_prime_factor(value):
    x=isitprime_generator((value//2)+1)
    progress=0
    for i in x:
        progress+=1
        if value/i==value//i:
            return i
    return value

def prime_factors(value):
    x=2
    arr=[]
    while x>1:
        if smallest_prime_factor(value)==value:
            arr.append(value)
            return arr
            break
        x=value//smallest_prime_factor(value)
        arr.append(smallest_prime_factor(value))
        value=x


def divisorset(s):
    ''' 
    Input is a set of prime factors for a given number. Output is set of all divisors.
    Computed by generating a powerset of s (set of all subsets) using a boolean mask,
    Then taking the products of every subset and eliminating duplicates using set()
    '''
    s.sort() #sorts the prime factors
    power_set=[] 
    factor_set=[]
    value=np.prod(s) #The original value created from the prime factor set s
    for i in range(1<<len(s)): #1<<len(s) = 2**len(s), the cardinality of a powerset
        factor=np.prod([s[j] for j in range(len(s)) if i & (1<<j)]) #a product of the elements of the i-th subset in the powerset
        factor_set.append(factor)
    factor_set=set(factor_set)
    return factor_set

        

    