class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize a list to keep track of prime numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        
        # Sieve of Eratosthenes
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Start marking multiples of i from i*i, up to n, skipping by i
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        # Count the prime numbers
        return sum(is_prime)