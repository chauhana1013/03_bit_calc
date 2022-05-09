def num_check(question, low):
    valid = False
    while not valid:
        
        error = "Please enter an integer that is more than "
        "(or equal to) {}".format(low)
                
        try:
                
            # ask user for a number
            response = int(input(question))
            
            # checks number is more than 0
            if response >= low:
                return response

            #outputs error if input is invalid 
            else:
                print(error)
                print()
        
        except ValueError: 
            print(error)


# converts decimal to binary and states how
# Many bits are needed to represent the original integer
def int_bits():

    # get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    # source for code below is 
    # https://stackoverflow.com/questions/699866/python-int-to-binary-string?msclkid=dead7dafcf1711ec9556fd52a6556e6a

    var_binary = "{0:b}".format(var_integer)

     # calculate # of bits (length of string above)
    num_bits = len(var_binary)

     # output answer with  working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""

# Main Routine 
int_bits()