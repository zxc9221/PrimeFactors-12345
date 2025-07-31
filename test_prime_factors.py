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

def test_prime_factor_of_4():
    primefactors = PrimeFactor()
    assert primefactors.of(4) == [2, 2]

def test_prime_factor_of_6():
    primefactors = PrimeFactor()
    assert primefactors.of(6) == [2, 3]

def test_prime_factor_of_9():
    primefactors = PrimeFactor()
    assert primefactors.of(9) == [3, 3]

def test_prime_factor_of_12():
    primefactors = PrimeFactor()
    assert primefactors.of(12) == [2, 2, 3]