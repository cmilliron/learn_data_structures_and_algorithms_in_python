# The Algorithm

Given a large number, return a list of all the prime factors.

    prime_factors(8) -> [2, 2, 2]
    prime_factors(10) -> [2, 5]
    prime_factors(24) -> [2, 2, 2, 3]

    Divide n by 2 as many times as you can evenly (no remainder). For each division, append a 2 to the list of prime factors.
    By now, n must be odd. Start a loop that iterates over all odd numbers from 3 to the square root of n inclusive. Use math.sqrt(). For each number i:
        If n can be divided evenly by i, then divide n by i and append i to the list.
        Repeat this (nested loop) until i can't divide evenly into n, then move on to the next i.
    If n is still greater than 2 after that loop, it must still be prime, so just append it to the list.
    Return the list of primes, ordered from least to greatest.

Assignment

Complete the prime_factors function according to the given algorithm. Notice how the algorithm gets much slower as the size of the input (in bits) grows.

The returned list should only contain ints, no floats.
Assignment

Complete the prime_factors function according to the given algorithm. Notice how the algorithm gets much slower as the size of the input (in bits) grows.

The returned list should only contain ints, no floats.
