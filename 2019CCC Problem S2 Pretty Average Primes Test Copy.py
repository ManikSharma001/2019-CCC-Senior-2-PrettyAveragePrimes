def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]
            
def find_a_b(n, primes = primes_upto(1000000)): 
    n = 2 * n # avoid division by looking for A + B = 2 * n rather than n = (A + B)/2
    for i in primes:
        if i < n and n - i in primes:
            return i, n - i  # solution as a tuple
    return None  # No solution

numofInput = int(input())
primeSet = []
for i in range(numofInput):
    line = int(input())
    primeSet.append(line)
    
for i in primeSet:
    sol = find_a_b(i)
    if sol:
        print(sol[0], sol[1])
