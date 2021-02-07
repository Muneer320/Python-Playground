while True:
    decimal = int(input("Enter Decimal Value: \n"))
    convert = int(input("Convert into: \n[1] Binary, \n[2] Octal, \n[3] Hexadecimal: \n"))

    if convert == 1:
        print("Converted to Binary \n", bin(decimal))
        print("Please ignore the first two values \n\n")

    elif convert == 2:
        print("Converted to Octal \n", oct(decimal))
        print("Please ignore the first two values \n\n")

    elif convert == 3:
        print("Converted to Hexadecimal \n", hex(decimal))
        print("Please ignore the first value \n\n")

    else:
        print("Please review your input... \n\n")