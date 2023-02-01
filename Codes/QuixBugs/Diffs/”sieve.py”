0a1
> 
4c5
<         if any(n % p > 0 for p in primes):
---
>         if all(n % p > 0 for p in primes):
9,10c10,15
< Sieve of Eratosthenes
< prime-sieve
---
> def sieve(max):
>     primes = []
>     for n in range(2, max + 1):
>         if not any(n % p == 0 for p in primes):
>             primes.append(n)
>     return primes
12,13c17,29
< Input:
<     max: A positive int representing an upper bound.
---
> def sieve(max):
>     primes = []
>     for n in range(2, max + 1):
>         if all(n % p for p in primes):
>             primes.append(n)
>     return primes
> 
> def sieve(max):
>     primes = []
>     for n in range(2, max + 1):
>         if not any(n % p for p in primes):
>             primes.append(n)
>     return primes
15,16d30
< Output:
<     A list containing all primes up to and including max
