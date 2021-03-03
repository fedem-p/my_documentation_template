import numpy as np 

def summation(a: int, b: int):
    """
    Sums two integers
    """
    return a+b 

def difference(a: int, b: int):
    """
    Subtracts two integers
    """
    return a-b


class Calculator:
    """
    Creates a Calculator to make math operations
    """
    def __init__(self):
        self.res = 0

    def sum(self,a: float ,b :float):
        """
        sums two floats and stores the result inside the variable res accessible from the calculator object
        """
        self.res = a+b

    