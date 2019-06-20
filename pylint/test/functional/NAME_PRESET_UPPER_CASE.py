# pylint: disable=missing-docstring,too-few-public-methods
__version__ = "1.0"
SOME_CONSTANT = 42


def SAY_HELLO(SOME_ARGUMENT):
    return [SOME_ARGUMENT * SOME_VALUE for SOME_VALUE in range(10)]


class MyClass:  # [invalid-name]
    def __init__(self, ARG_X):
        self._MY_SECRET_X = ARG_X

    @property
    def MY_PUBLIC_X(self):  # [invalid-name]
        return self._MY_SECRET_X * 2

    def __eq__(self, OTHER):
        return isinstance(OTHER, MyClass) and self.MY_PUBLIC_X == OTHER.MY_PUBLIC_X


def sayHello():  # [invalid-name]
    pass
