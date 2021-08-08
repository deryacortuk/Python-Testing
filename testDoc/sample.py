import doctest

def factorial(x):
    """
    >>> factorial(3)
    6
    >>> factorial(-3)
    'You should choose positive number'
    >>> factorial(1)
    1
    """
    result = 1
    if x<0:
        return "You should choose positive number"
    elif x==1 or x==0:
        return result
    else:
        for i in range(1,x+1):
            result *=i
        return result

def fibonacci(x):
    """
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(6)
    8
    """
    if x <= 0 :
        return "incorrect input"
    elif x == 1 or x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

