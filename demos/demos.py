from yacontracts import yacontract

is_positive_int = lambda x: isinstance(x, int) and x >= 0

@yacontract(
    args=[
        ('a', is_positive_int, 'a has to be >= 0'),
        ('b', is_positive_int, 'b has to be >= 0')],
    returns=(is_positive_int, 'Expected a non negative int result'))
def positive_sum(a, b):
    return a + b

# ------------------

if __name__ == '__main__':
    positive_sum(1, 2)
    positive_sum(1, -2) # ValueError, 'b has to be >= 0'
