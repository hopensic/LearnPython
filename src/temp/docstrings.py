"""
Module documentation
Words Go Here
"""

spam = 40


def square(x):
    """
    function documentation

    :param x: 整数
    :return: x的平方
    """

    return x ** 2  # square


class Employee:
    "class documentation"
    pass


print(square(4))
print(square.__doc__)
