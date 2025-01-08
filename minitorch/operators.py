"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, TypeAlias, List, TypeVar

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

Number: TypeAlias = int | float


def mul(x: Number, y: Number) -> Number:
    """Multiplies two numbers together"""
    return x * y


def id(x: Number) -> Number:
    """Returns the given value back"""
    return x


def add(x: Number, y: Number) -> Number:
    """Adds two numbers together"""
    return x + y


def neg(x: Number) -> Number:
    """Negates a given number"""
    return -x


def lt(x: Number, y: Number) -> bool:
    """Return True if x < y and False otherwise"""
    return x < y


def eq(x: Number, y: Number) -> bool:
    """Return True if x == y and False otherwise"""
    return x == y


def max(x: Number, y: Number) -> Number:
    """Return the maximum between x and y"""
    return x if (x > y) else y


def is_close(x: Number, y: Number) -> bool:
    """Return True if the difference between x and y is less than 1e-2"""
    return abs(x - y) < 1e-2


def sigmoid(x: Number) -> Number:
    """Return the sigmoid of x"""
    if x < 0:
        ex = math.exp(x)
        return ex / (1.0 + ex)
    else:
        return 1.0 / (1.0 + (math.exp(-x)))


def relu(x: Number) -> Number:
    """Return positive values of x and 0 otherwise"""
    return max(x, 0)


def log(x: Number) -> Number:
    """Return the natural log of x"""
    return math.log(x)


def exp(x: Number) -> Number:
    """Return the exponential of x"""
    return math.exp(x)


def inv(x: Number) -> Number:
    """Return the inverse of x"""
    return 1 / x if x != 0 else math.inf


def log_back(x: Number, b: Number) -> Number:
    """Returns b*(d/dx ln(x))"""
    return inv(x) * b


def inv_back(x: Number, b: Number) -> Number:
    """Returns b*(d/dx 1/x)"""
    return -1 / x**2 * 2


def relu_back(x: Number, b: Number) -> Number:
    """Returns b*(d/dx relu(x))"""
    return b if x > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")


def map(it: Iterable[T], f: Callable[[T], U]) -> List[U]:
    """Applies a function, f, to an given iterable"""
    result = [f(item) for item in it]
    return result


def zipWith(it1: Iterable[T], it2: Iterable[U], f: Callable[[T, U], V]) -> List[V]:
    """Applies a function, f, to corresponding elements of two arrays and returns the results in a new array"""
    result = [f(item1, item2) for (item1, item2) in zip(it1, it2)]
    return result


# A custom exeption
class IteratorExhaustedError(Exception):
    pass


def reduce(it: Iterable[T], f: Callable[[T, T], T]) -> T:
    """Applies a function to all values of an input iterable to reduce it to a single value.

    Args:
    ----
        it (Iterable[T]): The Iterable to be reduced.
        f (Callable[[T, T], T])): The function to be applied.

    Returns:
    -------
        T: The result of applying the function to it

    """
    iterator = iter(it)
    try:
        val1 = next(iterator)
    except StopIteration:
        raise IteratorExhaustedError("Cannot reduce empty iterator")

    for val2 in iterator:
        val1 = f(val1, val2)

    return val1


def negList(it: Iterable[Number]) -> Iterable[Number]:
    """Negates all numbers in a list using the map() function"""
    return map(it, neg)


def addLists(it1: Iterable[Number], it2: Iterable[Number]) -> Iterable[Number]:
    """Adds corresponding values in two list using the zipWith() function"""
    return zipWith(it1, it2, add)


def sum(it: Iterable[Number]) -> Number:
    """Sums all numbers in a list using the reduce() function"""
    try:
        return reduce(it, add)
    except IteratorExhaustedError:
        return 0


def prod(it: Iterable[Number]) -> Number:
    """Multiplies all numbers in a list using the reduce() function"""
    return reduce(it, mul)