#checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:
        
        error = "Please enter an integer that is more than 0 "
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

# Main Routine goes here  


keep_going = ""
while keep_going == "":
    print()
    # ask for integer (must be >= to zero)
    var_int = num_check("Please enter an integer: ", 0)
    print()

    # ask for the width and heighth 0of an image (must be more)
    image_width = num_check("Image width? ", 1)
    print()
    image_height = num_check("Image height? ", 1)