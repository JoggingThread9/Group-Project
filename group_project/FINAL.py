# where all the methods are stored
class fraction:
    used = []
    # creates a value for all used fractions

    def __init__(self, numerator, denominator):
        # user inputted fraction
        self.n = numerator
        self.d = denominator

        # compare fraction
        self.compare_n = 1
        self.compare_d = None

        # value used to make fractions similar
        self.multiplier = None
        self.compare_multiplier = None

        # if the code needs help
        self.help = True

    def simplify(self):
        # uses multiples of the numerator and denominator in order to make the fraction have a smaller value
        for i in range(1, self.n):
            for j in range(1, self.d):
                if (i * self.d) == (j * self.n):
                    self.n = i
                    self.d = j
                    break

    def simplify_compare(self):
        # uses the same simplify function with the compare values
        for i in range(1, self.compare_n):
            for j in range(1, self.compare_d):
                if (i * self.compare_d) == (j * self.compare_n):
                    self.compare_n = i
                    self.compare_d = j
                    # stops the code
                    break

    def find_lcm(self):
        # calls the simplify method so that it finds the lcm for smallest value
        self.simplify()

        # uses the numerator and denominator to find a compare value, then sets that value to the compare denominator
        self.compare_d = self.d / self.n

        # checks the type of compare_d to see if it is a decimal then rounds to the nearest whole number
        if type(self.compare_d) == float:
            self.compare_d = str(self.compare_d)
            point = self.compare_d.index(".")
            self.compare_d = self.compare_d[:point]
            self.compare_d = int(self.compare_d)
            self.compare_d += 1

        # finds a number that will make both fractions have a common denominator
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
        # calls find lcm
        self.find_lcm()

        # if a lcm was found multiplies the numbers so that they are equal
        if not self.help:
            self.n *= self.multiplier
            self.d *= self.multiplier

            self.compare_n *= self.compare_multiplier
            self.compare_d *= self.compare_multiplier

        # if no lcm was found then multiplies the numbers by the others' denominator, so they are equal
        else:
            self.n *= self.compare_d
            self.compare_n *= self.d

            self.d, self.compare_d = self.d * self.compare_d, self.compare_d * self.d

    def subtract(self):
        # calls the set_lcd function
        self.set_lcd()

        # subtracts the numerators
        self.n -= self.compare_n

        # calls the "simplify compare" method so that it is a unit fraction
        self.simplify_compare()
        # adds the used fraction to the list
        fraction.used.append(str(self.compare_n) + "/" + str(self.compare_d))

        # checks if the code needs to run again
        if self.n != 1:
            # checks if it is a unit fraction
            self.simplify()
            # checks if after simplifying it now becomes a unit fraction
            if self.n != 1:
                # if not the class subtract again
                self.subtract()
            else:
                # if it is a unit  fraction after simplifying then adds it to the list of used fractions
                fraction.used.append((str(self.n) + "/" + str(self.d)))
                print(fraction.used)
        else:
            # if it was originally a unit fraction then adds it to the list of used fractions
            fraction.used.append((str(self.n) + "/" + str(self.d)))
            print(fraction.used)

    def check(self):
        # does the same process as shown above but uses the user entered fraction
        if self.n != 1:
            self.simplify()
            if self.n != 1:
                self.subtract()
            else:
                fraction.used.append((str(self.n) + "/" + str(self.d)))
                print(fraction.used)
        else:
            fraction.used.append((str(self.n) + "/" + str(self.d)))
            print(fraction.used)