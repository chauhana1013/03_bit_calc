# checks number is more than zero
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

