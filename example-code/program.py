import typing


def passthrough(method: typing.Callable) -> typing.Callable:
    return method


class ExampleClass:
    """This class has a docstring."""

    def __init__(self, item):
        self._item = item

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


# NOTE: __name__ is rendered as the class Name.Variable.Magic in Pygments.
if __name__ == '__main__':
    main()
