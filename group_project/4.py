class fraction:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator

        self.compare_n = 1
        self.compare_d = None

        self.multiplier = None
        self.compare_multiplier = None

        self.used = []

    def simplify(self):
        for i in range(1, x.n):
            # loops through numbers 1 -> x.n
            num1 = self.n * i
            for j in range(1, x.d):
                # loops through all number 1 -> x.d
                num2 = self.d * j
            # finds a number less than the original that is equal to the original
                if num1 == num2:
                    # checks if the numbers are the same
                    x.n = i
                    x.d = j

    def simplify_compare(self):
        for i in range(1, self.compare_n):
            num1 = self.compare_n * i
            for j in range(1, self.compare_d):
                num2 = self.compare_d * j
                if num1 == num2:
                    self.compare_n = i
                    self.compare_d = j

    def find_lcm(self):
        for i in range(1, self.compare_d):
            num1 = x.d * i
            for j in range(1, x.d):
                num2 = self.compare_d * j
                if num1 == num2:
                    self.multiplier = i
                    self.compare_multiplier = j

    def set_lcd(self):
        self.find_lcm()

        x.n *= self.multiplier
        x.d *= self.multiplier

        self.compare_n *= self.compare_multiplier
        self.compare_d *= self.compare_multiplier

    def subtract(self):
        self.compare_d = x.d / x.n

        if type(self.compare_d) == float:
            self.compare_d = str(self.compare_d)
            idx = self.compare_d.index(".")
            self.compare_d = self.compare_d[:idx]
            self.compare_d = int(self.compare_d)
            self.compare_d += 1
            print(self.compare_d)
            self.compare_n = 1

        self.set_lcd()

        print(str(x.n) + "/" + str(x.d))
        print(str(self.compare_n) + "/" + str(self.compare_d))

        x.n -= self.compare_n
        self.used.append(str(self.compare_n) + "/" + str(self.compare_d))

        self.if_unit_fraction()

    def if_unit_fraction(self):
        self.simplify()

        self.used.append(str(x.n) + "/" + str(x.d))

        if x.n == 1:
            self.used.append(str(self.compare_n) + "/" + str(self.compare_d))

    def egyptian_fraction(self):
        self.subtract()
        print(self.used)


x = fraction(5, 6)

x.egyptian_fraction()

