from prime_factors import PrimeFactor

def test_prime_factor_of_1():
    primefactors = PrimeFactor()
    assert primefactors.of(1) == []