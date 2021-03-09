import numpy as np 

def summation(a: int, b: int):
    """
    Compute the arithmetic sum of two `int`.

    Parameters
    ----------
    a : `int`
        integer number, if `a` is not `int` a conversion is attempted
    b : `int`
        integer number, if `a` is not `int` a conversion is attempted

    Returns
    -------
    m : `int`

    See Also
    --------
    average : Weighted average
    std, var, nanmean, nanstd, nanvar

    Notes
    -----
    The arithmetic mean is the sum of the elements along the axis divided
    by the number of elements.
    Note that for floating-point input, the mean is computed using the
    same precision the input has.  Depending on the input data, this can
    cause the results to be inaccurate, especially for `float32` (see
    example below).  Specifying a higher-precision accumulator using the
    `dtype` keyword can alleviate this issue.
    By default, `float16` results are computed using `float32` intermediates
    for extra precision.

    Examples
    --------
    >>> a = summation(3,5)
    >>> a
    8
    """
    return a+b 

def difference(a: int, b: int):
    """
    Subtracts two integers
    return result
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

    