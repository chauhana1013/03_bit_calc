# Functions go here 

# Puts series of symbols at start and end of statement (for emphasis)
from cgi import print_form


def  statement_generator(text, decoration):

    # Make string with 5 characters 
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# checks user choice is "integer", "text" or "image"
def user_choice():

    # List of valid responses 
    text_ok = ["text", "t", "txt"]
    image_ok = ["image", "pix","img", "pic",]
    integer_ok = ["integer", "int", "intgr","in"]

    valid = False
    while not valid:
        
        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # checks for valid responses and returns image, text, or integer
        if response in text_ok:
           return "text"
        
        elif response in integer_ok:
            return "integer"
        
        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for image")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # if response invalid, output error
            print("Please choose valid file type!")
            print()

#checks input is a number more than a given value
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
            
# calculates the # of bits for text (# of characters x 8)
def text_bits():

    print()
    # ask user for a string...
    var_text = input("Enter some text: ")

    # calculate # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working
    print()
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    print('# of bits is {} x 8...'.format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""

# checks input is a number more than a given value
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

# finds # of bits for 24 bit colour
def image_bits() :

    # Get width & height
    image_width = num_check("Image width?:  ", 1)
    image_height = num_check("Image height?: ", 1)

    # calculate # of pixels
    num_pixels = image_width * image_height

    # calculate # bits (24 x num pixels)
    num_bits = num_pixels * 24

    # output answer with working
    print()
    print("# of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
    print() 

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


# Main Routine goes here

#Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)
    
    # For integers, ask for integer
    if data_type == "integer":
        int_bits()
    
    # For images, ask for width and height
    # (must be an integer more than / equal to 1)
    elif data_type == "image":
       image_bits() 

    # For text, ask for a string
    else:
        text_bits()

    
    print()
    keep_going - input("Press <enter> to continue or any key to quit")
    print()