class fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

        print(type(self.num))
        self.compare_num = 1  # self.compare numerator has to start at one because egyptian fractions start at one
        self.compare_den = None  # denominator hasn't been configured until finding lcm

        self.factor = None  # self.factor has not been configured
        self.compare_factor = None

        self.help = True  # if my code needs help then self.help will present this

        self.used = []

    def find_gcd(self):  # making gc function by splitting number into prime factors
        num1 = self.num  # num= numbers not numerators
        num2 = self.den  # num1 and num2 are changing instead of a and b/c the function would divide down...changing my numerator of my fuction
        count = 1  # count is keeping track of the amount of 2's and positive numbers being seen
        while num1 % 2 == 0 and num2 % 2 == 0:  # first number modulo 2, and second number modulo 2 to know if our number is divisble by 2
            num1 = num1 // 2  # dividing by 2 until num1 cant divide by 2 anymore
            num2 = num2 // 2  # dividing by 2 until num1 cant divide by 2 anymore
            count = count * 2  # multiple count when we find them at the end, when it cant go further.
        check = 3  # first odd number checking..we are starting with three because we dont need to start with one
        while check <= num1 or check <= num2:  # creating new while loop which checks 3--b/c of odd numbers (prime numbers!!--difficult to work with).
            while num1 % check == 0 and num2 % check == 0:  # first numer modulo 2, and second number modulo 2 to
                num1 = num1 // check  # double division makes num1 into an integer. Basically doing the same thing as 2 but with 3 and other number(odd numbers is worked through the code sentence check=check +_2
                num2 = num2 // check  # ^same principle applies
                count = count * check  # overall theme of finding gcd...muliplying the numbers
            check += 1  # check must be now equal to check + 1
        return count  # return count so find_gcd can be applied at the end of my code

    def simplify(self):
        num1 = self.find_gcd()  # num1 redefined into find(gcd) function of self.num and self. den
        self.num //= num1  # self.num redefined into self.num divided by the gcd of num1
        self.den //= num1  # self.den redefined into self.den divided by num1

    def simplify_compare(self):
        for i in range(1, self.compare_num):
            for j in range(1, self.compare_den):
                if (i * self.compare_den) == (j * self.compare_num):
                    self.compare_num = i
                    self.compare_den = j
                    break

    def find_LCM(self):
        if self.den > f2.den:
            greater = f2.den
        else:
            greater = f2.den
        while True:
            if (greater % self.den == 0) and (greater % f2.den == 0):
                lcm = greater
                break
            greater += 1
        return lcm

    def set_LCD(self):
        lcm = x.find_LCM()
        self.num = self.num * lcm // self.den
        self.den = self.den * lcm // self.den
        f2.num = f2.num * lcm // f2.den
        f2.den = f2.den * lcm // f2.den
        global f2

    def frac_sub(self):
        new_den = self.den * f2.den
        new_num1 = self.num * f2.den
        new_num2 = f2.num * self.den
        final_num = new_num1 - new_num2

        print(final_num, '/', new_den)

    def check(self):
        if self.num != 1:
            self.simplify()
            if self.num != 1:
                self.frac_sub()
            else:
                self.used.append((str(self.num) + "/" + str(self.den)))
                print(self.used)
        else:
            self.used.append((str(self.num) + "/" + str(self.den)))
            print(self.used)


x = fraction(5, 68)
x.check()
