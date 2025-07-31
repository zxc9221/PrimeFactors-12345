class PrimeFactor:
    def of(self, number):
        factor = []
        divisor = 2
        while number > 1:
            while number % divisor == 0:
                factor.append(divisor)
                number //= divisor
            divisor += 1
        return factor
