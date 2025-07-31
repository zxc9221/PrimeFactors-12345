from prime_factors import PrimeFactor

def test_prime_factor_of_1():
    primefactors = PrimeFactor()
    assert primefactors.of(1) == []

def test_prime_factor_of_2():
    primefactors = PrimeFactor()
    assert primefactors.of(2) == [2]

def test_prime_factor_of_3():
    primefactors = PrimeFactor()
    assert primefactors.of(2) == [2]