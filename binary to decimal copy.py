#Binary to decimal
##def convert_to_dec(bit_pattern):
##    
##    decimal_output = 0
##
##    length = len(bit_pattern)
##
##    for i in range(length):
##
##        bit_index = length - 1 - i
##
##        if bit_pattern[bit_index] == "1":
##
##            decimal_output += 2**i
##
##    print("Thats equal to " + str(decimal_output))
##
##binary_input = input("Input a binary number: ").strip(" .?!")
##
##convert_to_dec(binary_input)
##
##
##--------------------------------------------------------
# Decimal to Binary 
decimal_input = int(input("Input a decimal number: "))

binary_output = ""

while decimal_input != 0:

    if decimal_input%2 == 1:
        binary_output = "1" + binary_output
    else:
        binary_output = "0" + binary_output

    decimal_input = decimal_input //2

print("That's equal to " + binary_output)


