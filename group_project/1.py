fractions = []


class egyptian_fractions:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator
        self.fraction = str(self.n) + "/" + str(self.d)

        self.multiplier = None
        self.unit_fraction = "1/2"

    def step(self):
        fractions.append(self.unit_fraction)

        self.multiplier = int(self.fraction[2]) / int(self.unit_fraction[2])
        self.unit_fraction = str(int(self.unit_fraction[0]) * self.multiplier) + "/" + str((int(self.unit_fraction[2]) * self.multiplier))

        self.n = str(int(self.fraction[0]) - int(self.unit_fraction[0]))
        self.fraction = str(self.n) + "/" + str(self.d)

        if int(self.fraction[2]) % int(self.fraction[0]):
            self.fraction = str(int(self.fraction[0]) / int(self.fraction[0])) + "/" + str(int(self.fraction[2]) / int(self.fraction[0]))

        print(self.fraction)

f1 = egyptian_fractions(7, 8)
f1.step()
