from pytest import fixture, raises

from ..yacontracts import yacontract

is_valid_int = lambda x: isinstance(x, int) and x >= 0
ERROR_POSITIVE_INT = '{} has to be an int >= 0'
ERROR_POSITIVE_INT_RESULT = 'Expected a non negative int result'

is_valid_str = lambda x: isinstance(x, str) and x
ERROR_INVALID_STR = '{} has to be a non empty string'
ERROR_INVALID_STR_RESULT = 'Expected a non empty string'

@yacontract(
    args=[
        ('a', is_valid_int, ERROR_POSITIVE_INT.format('a')),
        ('b', is_valid_int, ERROR_POSITIVE_INT.format('b'))],
    returns=(is_valid_int, ERROR_POSITIVE_INT_RESULT))
def positive_sum(a, b):
    return a + b


@yacontract(
    args=[
        ('a', is_valid_str, ERROR_INVALID_STR.format('a')),
        ('b', is_valid_str, ERROR_INVALID_STR.format('b'))],
    returns=(is_valid_str, ERROR_INVALID_STR_RESULT))
def concat(a, b):
    return 3


def test_correct_positive_sum():
    assert positive_sum(1, 2) == 3


@fixture(params=[((-1, 1), ERROR_POSITIVE_INT.format('a')),
                 ((1, -1), ERROR_POSITIVE_INT.format('b')),
                 (("one", 1), ERROR_POSITIVE_INT.format('a')),
                 ((1, "one"), ERROR_POSITIVE_INT.format('b')),
                 (("one", -1), ERROR_POSITIVE_INT.format('a')),
                 ((-1, "one"), ERROR_POSITIVE_INT.format('a'))
                 ])
def wrong_parameters_sum(request):
    return request.param


def test_incorrect_positive_sum_arguments(wrong_parameters_sum):
    with raises(ValueError) as ex:
        positive_sum(*wrong_parameters_sum[0])
    assert ex.value.message == wrong_parameters_sum[1]


@fixture(params=[((1, "two"), ERROR_INVALID_STR.format('a')),
                 (("one", 1), ERROR_INVALID_STR.format('b')),
                 ((1, 1), ERROR_INVALID_STR.format('a')),
                 (("one", "two"), ERROR_INVALID_STR_RESULT)
                 ])
def wrong_parameters_concat(request):
    return request.param


def test_incorrect_concat_arguments(wrong_parameters_concat):
    with raises(ValueError) as ex:
        concat(*wrong_parameters_concat[0])
    assert ex.value.message == wrong_parameters_concat[1]
