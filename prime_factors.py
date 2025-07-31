class PrimeFactor:
    def of(self, number):
        factor = []
        if number > 1:
            if number == 4:
                while number % 2 == 0:
                    factor.append(2)
                    number //= 2
            elif number == 6:
                while number % 2 == 0:
                    factor.append(2)
                    number //= 2
                while number % 3 == 0:
                    factor.append(3)
                    number //= 3
            else:
                factor.append(number)
        return factor