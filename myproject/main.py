from .module1 import *



def use_calc():
    """
    Tests the functions written in module 1 and returns a Calculator object.
    """
    a = 2
    b = 3 

    c = summation(a,b)
    d = difference(a,b)

    e = Calculator()

    e.sum(a,b)
    print(c,d,e.res)

    return e


if __name__ == '__main__':
    test = use_calc()