import typing


def passthrough(method: typing.Callable) -> typing.Callable:
    return method


class ExampleClass:
    """This class has a docstring."""

    def __init__(self, item):
        self._item = item
        # Just to check formatting of some boolean operators
        self._bools = (False or True, False and True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_value is not None:
            print(f'Exception was raised: {exc_type.__name__}: {exc_value}')

    @classmethod
    def example_context(cls, number):
        with cls(frozenset({1, 2, 3})) as example:
            if number not in example._item:
                pass

    @passthrough
    def print_item(self):
        print(self._item)

    def try_except(self):
        try:
            frozenset({self._item})
        except Exception as ex:
            print(f'Format string: conversion error: {ex}')
        finally:
            pass


def main():
    example = ExampleClass([1, 2, 3])
    example.print_item()
    example.try_except()

    ExampleClass.example_context(4)


# NOTE: __name__ is rendered as the class Name.Variable.Magic in Pygments.
if __name__ == '__main__':
    main()
