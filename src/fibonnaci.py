class Fibonacci:
    """
    A class that provides methods to calculate Fibonacci numbers.
    """

    def __init__(self):
        self.cache = {}

    def recursive(self, n):
        """
        Calculates the nth Fibonacci number using a recursive approach.

        Parameters:
        - n (int): The index of the Fibonacci number to calculate.

        Returns:
        - int: The nth Fibonacci number.

        """
        if n <= 1:
            return n
        else:
            return self.recursive(n-1) + self.recursive(n-2)

    def iterative(self, n):
        """
        Calculates the nth Fibonacci number using an iterative approach.

        Parameters:
        - n (int): The index of the Fibonacci number to calculate.

        Returns:
        - int: The nth Fibonacci number.

        """
        if n <= 1:
            return n

        fib_sequence = [0, 1]
        for i in range(2, n+1):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

        return fib_sequence[n]

    def memoization(self, n):
        """
        Calculates the nth Fibonacci number using memoization.

        Parameters:
        - n (int): The index of the Fibonacci number to calculate.

        Returns:
        - int: The nth Fibonacci number.

        """
        if n <= 1:
            return n

        if n in self.cache:
            return self.cache[n]

        self.cache[n] = self.memoization(n-1) + self.memoization(n-2)
        return self.cache[n]