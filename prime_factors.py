class PrimeFactor:
    def of(self, number):
        factor = []
        if number > 1:
            divisor = 2
            if number == 4:
                while number % divisor == 0:
                    factor.append(divisor)
                    number //= divisor
            elif number == 6 or number == 9:
                while number > 1:
                    while number % divisor == 0:
                        factor.append(divisor)
                        number //= divisor
                    divisor += 1
            else:
                factor.append(number)
        return factor