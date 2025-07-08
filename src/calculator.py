class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.

    Attributes:
        name (str): The name of the calculator.
    """

    def __init__(self, name):
        """
        Initializes a new instance of the Calculator class.

        Args:
            name (str): The name of the calculator.
        """
        self.name = name

    def add(self, num1, num2):
        """
        Adds two numbers.

        Args:
            num1 (int or float): The first number.
            num2 (int or float): The second number.

        Returns:
            int or float: The sum of the two numbers.
        """
        return num1 + num2

    def subtract(self, num1, num2):
        """
        Subtracts two numbers.

        Args:
            num1 (int or float): The first number.
            num2 (int or float): The second number.

        Returns:
            int or float: The difference between the two numbers.
        """
        return num1 - num2

    def multiply(self, num1, num2):
        """
        Multiplies two numbers.

        Args:
            num1 (int or float): The first number.
            num2 (int or float): The second number.

        Returns:
            int or float: The product of the two numbers.
        """
        return num1 * num2

    def divide(self, num1, num2):
        """
        Divides two numbers.

        Args:
            num1 (int or float): The dividend.
            num2 (int or float): The divisor.

        Returns:
            int or float: The quotient of the two numbers.
        """
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2