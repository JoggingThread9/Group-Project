class fraction:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator

        self.x_multiplier = None
        self.y_multiplier = None

        self.sum = None

        self.difference = None

        self.product_n = None
        self.product_d = None

        self.quotient_n = None
        self.quotient_d = None

        self.power = None
        self.exponent_n = self.n
        self.exponent_d = self.d

        self.float = None

        self.compare_n = None
        self.compare_d = None

    def __repr__(self):
        if self.n == x.n and self.d == x.d:
            return self.__class__.__name__ + "(" + str(x.n) + "," + str(x.d) + ")"

        if self.n == y.n and self.d == y.d:
            return self.__class__.__name__ + "(" + str(y.n) + "," + str(y.d) + ")"

    def __str__(self):
        if self.n == x.n and self.d == x.d:
            return str(x.n) + "/" + str(x.d)

        if self.n == y.n and self.d == y.d:
            return str(y.n) + "/" + str(y.d)

    def simplify(self):
        for i in range(1, self.n):
            num1 = self.n * i
            for j in range(1, self.d):
                num2 = self.d * j
                if num1 == num2:
                    self.n = i
                    self.d = j

    def find_lcm(self):
        for i in range(1, y.d):
            num1 = x.d * i
            for j in range(1, x.d):
                num2 = y.d * j
                if num1 == num2:
                    self.x_multiplier = i
                    self.y_multiplier = j

    def set_lcd(self):
        self.find_lcm()

        x.n *= self.x_multiplier
        x.d *= self.x_multiplier

        y.n *= self.y_multiplier
        y.d *= self.y_multiplier

        print(str(x.n) + "/" + str(x.d))
        print(str(y.n) + "/" + str(y.d))

    def get_reciprocal(self):
        self.n, self.d = self.d, self.n
        print(str(self.n) + "/" + str(self.d))

    def negation(self):
        if self.n == x.n and self.d == x.d:
            x.n = -x.n
            print(str(x.n) + "/" + str(x.n))
        if self.n == y.n and self.d == y.d:
            y.n = -y.n
            print(str(y.n) + "/" + str(y.d))

    def add(self):
        self.set_lcd()
        if x.d == y.d:
            self.sum = x.n + y.n
            print(str(self.sum) + "/" + str(x.d))

    def subtract(self):
        self.set_lcd()
        if self.n == x.n and self.d == x.d:
            if x.d == y.d:
                self.difference = x.n - y.n
                print(str(self.difference) + "/" + str(x.d))

        if self.n == y.n and self.d == y.d:
            if x.d == y.d:
                self.difference = x.n - y.n
                print(str(self.difference) + "/" + str(x.d))

    def multiply(self):
        self.product_n = x.n * y.n
        self.product_d = x.d * y.d

        print(str(self.product_n) + "/" + str(self.product_d))

    def divide(self):
        if self.n == x.n and self.d == x.d:
            self.get_reciprocal()

            self.quotient_n = self.n * y.n
            self.quotient_d = self.d * y.d

        if self.n == y.n and self.d == y.d:
            self.get_reciprocal()

            self.quotient_n = self.n * x.n
            self.quotient_d = self.d * x.d

        print(str(self.quotient_n) + "/" + str(self.quotient_d))

    def exponent(self):
        self.power = int(input("Enter a exponent "))
        for i in range(1, self.power):
            self.exponent_n *= self.n
            self.exponent_d *= self.d

        print(str(self.exponent_n) + "/" + str(self.exponent_d))

    def less_than(self):
        if self.n == x.n and self.d == y.d:
            self.set_lcd()
            if x.n < y.n:
                print("Less")

        if self.n == y.n and self.d == y.d:
            self.set_lcd()
            if y.n < x.n:
                print("Less")

    def greater_than(self):
        if self.n == x.n and self.d == x.d:
            self.set_lcd()
            if x.n > y.n:
                print("Greater")

        if self.n == y.n and self.d == y.d:
            self.set_lcd()
            if y.n > x.n:
                print("Greater")

    def less_than_or_equal(self):
        if self.n == x.n and self.d == x.d:
            self.set_lcd()
            if x.n < y.n:
                print("Lass")
            elif x.n == y.n:
                print("Equal")

        if self.n == y.n and self.d == y.d:
            self.set_lcd()
            if y.n < x.n:
                print("Less")
            elif y.n == x.n:
                print("Equal")

    def greater_than_or_equal(self):
        if self.n == x.n and self.d == x.d:
            self.set_lcd()
            if x.n > y.n:
                print("Greater")
            elif x.n == y.n:
                print("Equal")

        if self.n == y.n and self.d == y.d:
            self.set_lcd()
            if y.n > x.n:
                print("Greater")
            elif y.n == x.n:
                print("Equal")

    def equal_too(self):
        if self.n == x.n and self.d == x.d:
            self.set_lcd()
            if x.n == y.n:
                print("Equal")

        if self.n == y.n and self.d == y.d:
            self.set_lcd()
            if y.n == x.n:
                print("Equal")

    def not_equal_to(self):
        if self.n == x.n and self.d == y.d:
            self.set_lcd()
            if x.n != y.n:
                print("Not Equal")

        if self.n == y.n and self.d == y.d:
            self.set_lcd()
            if y.n != x.n:
                print("Not Equal")

    def fraction_to_float(self):
        if self.n == x.n and self.d == x.d:
            self.float = x.n / x.d
        if self.n == y.n and self.d == y.d:
            self.float = y.n / y.d

    def fraction_to_int(self):
        pass

    def iterate(self):
        if self.n == x.n and self.d == x.d:
            for i in range(x.n, 0, -1):
                print(str(i) + "/" + str(x.d))

        if self.n == y.n and self.d == y.d:
            for i in range(y.n, 0, -1):
                print(str(i) + "/" + str(x.d))


x = fraction(5, 6)
y = fraction(6, 8)

y.iterate()
