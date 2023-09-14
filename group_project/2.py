class fraction:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator
        self.fraction = f'{int(self.n)}/{int(self.d)}'
        # uses an f-string to create a fraction

        self.compare_n = None
        self.compare_d = None
        # self.compare_fraction = f'{int(self.compare_n)}/{int(self.compare_d)}'

        self.used = [] 

        self.multiplier = None

    def simplify(self):
        # simplifies the fraction
        for i in range(1, self.n):
            # every number from 1 - self.n
            for j in range(1, self.d):
                # every number from 1 - self.d
                if (i * self.d) == (j * self.n):
                    # checks if the numbers are equal when multiplied by the other
                    self.n = i
                    self.d = j
                    self.fraction = f'{int(self.n)}/{int(self.d)}'
                    break
                    # stops the loop

        print(self.fraction)

    def x(self):
        self.compare_d = round(self.d / self.n)

        self.n *= self.compare_d

        self.compare_n *= self.d

        self.d, self.compare_d = * self.compare_d, * self.d

        self.n -= self.compare_n

        self.fraction = f'{int(self.n)}/{int(self.d)}'

        print(self.fraction)


f1 = fraction(5, 6)
f1.x()
