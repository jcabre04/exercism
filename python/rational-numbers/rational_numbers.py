from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        self.numer, self.denom = self._reduce(numer, denom)

    def _gcd(self, num1, num2):
        greater = abs(num1)
        lesser = abs(num2)

        if abs(num2) > greater:
            greater = abs(num2)
            lesser = abs(num1)

        gcd = 1

        for number in range(1, lesser + 1):
            if lesser % number == 0 and greater % number == 0:
                gcd = number

        return gcd

    def _reduce(self, num, denom):
        new_num, new_den = int(num / self._gcd(num, denom)), int(denom / self._gcd(num, denom))

        if new_num == 0:
            new_den = 1
        elif new_num < 0 and new_den < 0:
            new_num = abs(new_num)
            new_den = abs(new_den)

        if new_num > 0 and new_den < 0:
            new_num *= -1
            new_den *= -1

        return new_num, new_den

    def _same_denom(self, other):
        self_num = self.numer * other.denom
        self_den = self.denom * other.denom
        other_num = other.numer * self.denom
        other_den = other.denom * self.denom

        return self_num, self_den, other_num, other_den

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        self_num, self_den, other_num, other_den = self._same_denom(other)
        new_num = self_num + other_num
        new_num, new_denom = self._reduce(new_num, other_den)
        return Rational(new_num, new_denom)

    def __sub__(self, other):
        self_num, self_den, other_num, other_den = self._same_denom(other)
        new_num = self_num - other_num
        new_num, new_denom = self._reduce(new_num, other_den)
        return Rational(new_num, new_denom)

    def __mul__(self, other):
        self_num, self_den, other_num, other_den = self._same_denom(other)
        new_num = self_num * other_num
        new_denom = self_den * other_den
        new_num, new_denom = self._reduce(new_num, new_denom)
        return Rational(new_num, new_denom)

    def __truediv__(self, other):
        self_num, self_den, other_num, other_den = self._same_denom(other)
        new_num = self_num * other_den
        new_denom = self_den * other_num

        new_num, new_denom = self._reduce(new_num, new_denom)

        return Rational(new_num, new_denom)

    def __abs__(self):
        new_num = abs(self.numer)
        new_denom = abs(self.denom)
        new_num, new_denom = self._reduce(new_num, new_denom)
        return Rational(new_num, new_denom)

    def __pow__(self, power):
        if power == 0 or (isinstance(power, Rational) and power == Rational(0,1)):
            return Rational(1,1)

        result = Rational(self.numer, self.denom)

        while isinstance(power, Rational) != True and power > 1:
            result *= self
            power -= 1

        return result

    def __rpow__(self, base):
        print(base)
        if isinstance(self, Rational) and self == Rational(0,1):
            return 1.0
        
        return base ** (self.numer / self.denom)