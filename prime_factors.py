class PrimeFactor:
    def of(self, number):
        factor = []
        if number > 1:
            divisor = 2
            if number == 4:
                while number % divisor == 0:
                    factor.append(divisor)
                    number //= divisor
            elif number == 6:
                while number % divisor == 0:
                    factor.append(divisor)
                    number //= divisor
                while number % 3 == 0:
                    factor.append(3)
                    number //= 3
            else:
                factor.append(number)
        return factor