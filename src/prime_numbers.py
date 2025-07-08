class PrimeGenerator:
    """
    A class that generates prime numbers up to a given limit.
    """

    def __init__(self, limit):
        """
        Initializes a PrimeGenerator object with the specified limit.

        Parameters:
        - limit (int): The upper limit for generating prime numbers.
        """
        self.limit = limit

    def is_prime(self, num):
        """
        Checks if a given number is prime.

        Parameters:
        - num (int): The number to check for primality.

        Returns:
        - bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_primes(self):
        """
        Generates a list of prime numbers up to the specified limit.

        Returns:
        - list[int]: A list of prime numbers.
        """
        primes = []
        for num in range(2, self.limit + 1):
            if self.is_prime(num):
                primes.append(num)
        return primes