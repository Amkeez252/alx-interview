#!/usr/bin/python3
""" Prime Game """

def isWinner(x, nums):
    def sieve(n):
        primes = []
        sieve = [True] * (n + 1)
        for p in range(2, n + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
        return primes

    def canWin(n, primes):
        if n in primes:
            return True
        for prime in primes:
            if n % prime == 0:
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    primes = sieve(max(max(nums), 10000))

    for n in nums:
        if canWin(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

