# Functions go here 

# Puts series of symbols at start and end of statement (for emphasis)
def  statement_generator(text, decoration):

    # Make string with 5 characters 
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# Main Routine goes here
statement_generator("hello world", "*")