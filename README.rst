Simplecurry’s ``curried`` provides a simple way to use curried functions in Python. There are alternative implementations, but they are unnecessarily complex.

Example
~~~~~~~

::
    from simplecurry import curried

    @curried
    def add(a, b, c):
        return a + b + c
    
    add(1)(2)(3) # Returns 6
    add(1, 2)(3) # Returns 6
    add(1)(2, 3) # Returns 6
    add(1, 2, 3) # Returns 6
