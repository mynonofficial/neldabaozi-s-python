# Recall the schema of 32-bit fixed-point numbers
# where the first 16 bits are integer bits,
# and the rest are fractional bits
# Given a string representation of such a numbers
# return its decimal representation

# Let's debug the following code
#  with the help of some test cases
def bin2dec(binaryStr):
    number = 0
    multiplier = 1
    divider = 1
    for el in binaryStr[16:0:-1]:
        if el == '1':
            number += 2**multiplier
            multiplier += 1
    for el in binaryStr[16:]:
        if el == '1':
            number += 2**divider
            divider -= 1
    return number

print bin2dec('00000000000000001000000000000000')#  == 0.5
print bin2dec('00000000000000010100000000000000')#  == 1.25
print bin2dec('00000000000001110110000000000000')#  == 7.375
