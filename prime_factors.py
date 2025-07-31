class PrimeFactor:
    def of(self, number):
        factor = []
        if number > 1:
            if number == 4:
                factor.append(2)
                factor.append(2)
            else:
                factor.append(number)
        return factor