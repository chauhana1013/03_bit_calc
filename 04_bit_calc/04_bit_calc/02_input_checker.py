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


# Main Routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)

    print()