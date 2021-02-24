# nまでの素数を表示させるプログラム
import math

def sieve_of_eratosthenes(n):
    candidate = [i for i in range(2, n+1)]
    prime = []
    limit = math.sqrt(n) + 1

    while True:
        p = min(candidate)
        if limit <= p:
            prime.extend(candidate)
            break
        prime.append(p)

        candidate = [i for i in candidate if i % p != 0]

    print(prime)

n = int(input('n=?\n'))

sieve_of_eratosthenes(n)
