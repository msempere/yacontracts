# YAContracts [![Build Status](https://travis-ci.org/msempere/yacontracts.svg?branch=master)](https://travis-ci.org/msempere/yacontracts)
Yet Another Contracts package for Python

## Installation
```
pip install yacontracts
```

## Usage
Check input argument:
```
@yacontract(
  args=[('a', assert x: isinstance(x, str), 'a has to be str')])
def foo(a):
    print a
```

Check several input arguments at the same time:
```
@yacontract(
  args=[
    ('a', assert x: isinstance(x, str), 'a has to be str')
    ('c', assert x: isinstance(x, str) and c, 'c has to be non empty str')
       ])
def foo(a, b, c):
    print a,b,c
```

Check returned values:
```
@yacontract(
  returns=(lambda x: x > 0, 'return value has to be grater than 0'))
def foo(a, b):
    return a + b
```

Everything together:
```
is_positive_int = lambda x: isinstance(x, int) and x >= 0

@yacontract(
    args=[
        ('a', is_positive_int, 'a has to be >= 0'),
        ('b', is_positive_int, 'b has to be >= 0')],
    returns=(is_positive_int, 'Expected a non negative int result'))
def positive_sum(a, b):
    return a + b
```

## License
Distributed under MIT license. See `LICENSE` for more information.
