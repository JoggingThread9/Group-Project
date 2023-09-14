class fraction:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator

        self.compare_n = 1
        self.compare_d = None

        self.multiplier = None
        self.compare_multiplier = None

        self.help = True

        self.used = []

    def simplify(self):
        for i in range(1, self.n):
            for j in range(1, self.d):
                if (i * self.d) == (j * self.n):
                    self.n = i
                    self.d = j
                    break

    def simplify_compare(self):
        for i in range(1, self.compare_n):
            for j in range(1, self.compare_d):
                if (i * self.compare_d) == (j * self.compare_n):
                    self.compare_n = i
                    self.compare_d = j
                    break

    def find_lcm(self):
        self.simplify()

        self.compare_d = self.d / self.n

        if type(self.compare_d) == float:
            self.compare_d = str(self.compare_d)
            point = self.compare_d.index(".")
            self.compare_d = self.compare_d[:point]
            self.compare_d = int(self.compare_d)
            self.compare_d += 1

        for i in range(1, self.compare_d):
            for j in range(1, self.d):
                if (i * self.d) == (j * self.compare_d):
                    self.multiplier = i
                    self.compare_multiplier = j
                    self.help = False
                    break
                break
            break

    def set_lcd(self):
        self.find_lcm()

        if not self.help:
            self.n *= self.multiplier
            self.d *= self.multiplier

            self.compare_n *= self.compare_multiplier
            self.compare_d *= self.compare_multiplier

        else:
            self.n *= self.compare_d
            self.compare_n *= self.d

            self.d, self.compare_d = self.d * self.compare_d, self.compare_d * self.d

    def subtract(self):
        self.set_lcd()

        self.n -= self.compare_n

        self.simplify_compare()
        self.used.append(str(self.compare_n) + "/" + str(self.compare_d))

        if self.n != 1:
            self.simplify()
            if self.n != 1:
                self.subtract()
            else:
                self.used.append((str(self.n) + "/" + str(self.d)))
                print(self.used)
        else:
            self.used.append((str(self.n) + "/" + str(self.d)))
            print(self.used)

    def check(self):
        if self.n != 1:
            self.simplify()
            if self.n != 1:
                self.subtract()
            else:
                self.used.append((str(self.n) + "/" + str(self.d)))
                print(self.used)
        else:
            self.used.append((str(self.n) + "/" + str(self.d)))
            print(self.used)


x = fraction(5, 60)
x.check()
