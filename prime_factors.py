class PrimeFactor:
    def of(self, number):
        factor = []
        if number > 1:
            if number == 4:
                while number % 2 == 0:
                    factor.append(2)
                    number //= 2
            else:
                factor.append(number)
        return factor