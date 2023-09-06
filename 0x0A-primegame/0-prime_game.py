#!/usr/bin/python3
""" Prime Game """

def isWinner(x, nums):
    def calculate_primes(n):
        # Helper function to calculate prime numbers up to n
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for p in range(2, int(n**0.5) + 1):
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
        return [i for i, is_prime in enumerate(sieve) if is_prime]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = calculate_primes(n)
        prime_count = len(primes)

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
