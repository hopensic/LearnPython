def enclosing_function(score=0):
    def factorial(n):
        nonlocal score
        score =5
        if n < 2:
            return 1
        return n * factorial(n - 1)  # fails with NameError

    print(factorial(5))
    print(score)


enclosing_function()
