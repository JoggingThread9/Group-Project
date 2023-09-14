user_input = input("enter a fraction ")
slash = user_input.index("/")

numerator = user_input[:slash]
denominator = user_input[slash + 1:]
print(numerator + "/" + denominator)