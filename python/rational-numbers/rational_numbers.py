from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        self.numer = None
        self.denom = None

    def _gcd(num1, num2):
        greater = abs(num1)
        lesser = abs(num2)
        if abs(num2) > greater:
            greater = abs(num2)
            leser = abs(num1)

        gcd = 0
        for number in range(1, lesser + 1):
            if lesser % number == 0 and greater % number == 0:
                gcd = number

        return number

    def _reduce(num, denom):
        return num / _gcd(num, denom), denom / _gcd(num, denom)   

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
