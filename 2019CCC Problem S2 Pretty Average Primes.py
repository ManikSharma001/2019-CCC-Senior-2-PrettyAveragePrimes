numofInput = int(input())
primeSet = []
for i in range(numofInput):
    line = int(input())
    primeSet.append(line)
print("Starting...")

def findp(n):
    global primes
    primes = [2, 3]  # seed with first two primes
    while primes[-1]< n:
        # Find next prime
        # start with next odd number, after the last prime number in the list of primes
        number = primes[-1] + 2
        while True:
            # check if number is divisible by an existing prime
            for p in primes:
                if number % p == 0:
                    # found a divisor, so number not prime
                    number += 2  # try next odd number
                    break  # break for loop
                           # while loop will return us back to for loop to try new number
            else:
                # number is prime since
                # number is not divisible by any of the previous primes
                # (note: this is for/else block)
                primes.append(number)
                break # break out of while True
    return primes
            
def find_a_b(n):
    n = 2*n # avoid division by looking for A + B = 2*n 
            # rather than n = (A + B)/2
    for A in primes:
        if A < n and n - A in primes:
            return A, n - A  # solution as a tuple
    return None  # No solution

for i in primeSet:
    sol = find_a_b(i)
    findp(1000000)
    if sol:
        print(sol[0], sol[1])
