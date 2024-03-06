import numpy as np 
import math
def list_primes(limit=10):
    '''
    Lists all the prime numbers below a limit. Example for limit=10: 2,3,5,7
    '''
    if limit<2: 
        return False #exclude a limit below the first prime number
    else:
        answer=[] 
        for i in range(2,limit+1): #loop over numbers between 2 and limit
            if i==2 or i==3: #if loop iteration is at 2 or 3, add them to the list
                answer.append(i) 
            else: #else, check if i is prime
                flag=True 
                for j in range(2,int(i**0.5)+1): #loop over range 2 to sqrt(i) (since a non-prime number i will have at least one prime factor < sqrt(i))
                    if i % j==0: #if i is divisible by j, then i is not prime, flag=false, break out of the loop
                        flag=False
                        break        
                if flag==False: continue #if flag=false then i is not prime, continue to the next loop iteration
                else: #if flag=true, i was not divisible by any j, i is prime, add it to the list
                    answer.append(i)
    return answer #returns list of primes
                        

def isitprime(a = 0):
    '''
    Checks if a number (a) is prime. Returns true if yes, false if no. Example: isitprime(2)-->True, isitprime(4)-->False
    '''
    if type(a) is not int: #exclude bad input types, only input should be integers
        return False
    elif a<2: #exclude integers < 2
        return False
    elif a==2: #2 is prime, return True
        return True
    isprime=True #if a > 2, check if a is prime
    sample=list_primes(int(a**0.5)+1)
    for i in range (0,len(sample)):
        if a % sample[i]==0: #if a is divisble by any prime number before it, a is not prime, isprime=false
            isprime=False
    return isprime 

def isitprime_generator(n):
    '''
    Generator object for prime numbers. Returns the next prime number in the sequence of primes: 2,3,5...p_n
    '''
    previous_primes=[] 
    j=2 #current prime being considered
    i=0 #current prime number logged
    while i<n and j>=2:
        if j==2: #2 is prime, so we add it to the list of primes, yield it, and increment i and j by 1
            previous_primes.append(j)
            yield j
            i+=1
            j+=1
        else:   #if j>2, check if j is prime against the list of previous primes
            flag=True
            for x in previous_primes:
                if j % x == 0:
                    flag=False
                    break    
            if flag==True: #if flag is still true, j is prime, add it to the list of primes and increment i and j by one
                previous_primes.append(j)
                yield j
                i+=1
                j+=1
            else: #if flag=false, j is not prime, increment j by one but not i since we haven't logged a prime.
                j+=1
    

def smallest_prime_factor(value):
    '''
    Returns the smallest prime factor of a value
    '''
    x=isitprime_generator((value//2)+1) #generator for all primes up to value/2
    for i in x: #iterate over generator
        if value % i == 0: #returns the first instance of i where x is divisible by i
            return i
    return value #if no divisible values found, value is prime, return value

def prime_factors(value):
    '''
    Returns the list of all the prime factors (including repeats) of a value. Example: prime_factors(8)-->[2,2,2]
    '''
    x=2
    arr=[]
    while x>1:
        if smallest_prime_factor(value)==value: #if the smallest prime factor of value is value, value is prime, return the list with value in it, break
            arr.append(value)
            return arr
            break
        x=value//smallest_prime_factor(value) #divide by smallest prime factor
        arr.append(smallest_prime_factor(value)) #append smallest prime factor to list
        value=x #reassign value to value/smallest_prime_factor and repeat


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
    factor_set=set(factor_set) #eliminate repeats by returning a set instead of a list
    return factor_set 

        

    