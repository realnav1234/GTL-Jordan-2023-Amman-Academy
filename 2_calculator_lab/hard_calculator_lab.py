
########################################################

# NAME: 
# GRADE: 

########################################################

# Welcome to the HARD calculator lab!
# This is for students who finished the EASY calculator lab and want a harder challenge.

# In our previous calculator, we had to input the first number, then SEPARATELY input the operator,
# and then SEPARATELY input the second number. That is not the way we are used to using calculators.

# I want to be able to type 5+3 and the output be 8, without having to worry about inputting it all separately.

# Here, I want you to try and implement that.

# The general structure will be this. 
# 1. We will READ the expression using the input function. ex. '5+3' 
# 2. We want to PARSE the expression, or split it up into usable tokens. ex. [5, '+', 3]
# 3. We will EVALUATE the parsed expression, or in other words, do the calculation. ex. 8
# 4. We will PRINT out the result.
# 5. We want to then LOOP, allowing us to input more expressions.

# I have below empty functions I want you to implement. 
# Read their descriptions (called DOCSTRINGS) to learn more and for useful built-in functions you can use.

# The main WHILE loop is at the bottom.
# Feel free to ask questions. 

# To SUBMIT:
#   1. Open your EMAIL
#   2. Write the following subject line. 
#       [YOUR NAME]: HARD CALCULATOR LAB
#   3. Copy and paste your code into the email (or attach the Python file, your choice).
#   4. Send the email to 14navpreetsingh@gmail.com

# GOOD LUCK! 

########################################################

def parse(expression):
    '''
    INPUT:
    This function takes in the expression we put into the calculator (which is a STRING).
    Ex. '5+3'

    OUTPUT:
    We want this function to RETURN a parsed expression, which is a LIST of the different numbers and symbols
    in our expression.
    Ex. [5, '+', 3]  NOTE: the numbers are ints, not strings, while the plus sign is a string.

    HINTS: 
    The built-in split() function might be useful. LEARN MORE: https://www.geeksforgeeks.org/python-string-split/

    '''

    pass # keyword pass is used to tell Python that this function is not written yet, and to skip over it.


def evaluate(parsed_expression):
    '''
    INPUT: 
    This function takes a parsed_expression, which is the output of the function parse()
    The parsed_expression is a LIST containing the different symbols we typed.
    Ex. [5, '+', 3]

    OUTPUT:
    We want this function to RETURN the answer to our inputted expression, as a float or int.
    Ex. 8
    '''

    pass # keyword pass is used to tell Python that this function is not written yet, and to skip over it.


welcome_message = "Welcome to Nav's Calculator." # Change the welcome message to whatever you want
print(welcome_message)

while True:

    expression = input("Enter the expression you want to evaluate here.")

    parsed_expression = parse(expression)

    final_result = evaluate(parsed_expression)

    print("The final result is: ", final_result)

    ########################################################

    do_you_want_to_end = input("Do you want to end the session?: ")

    # Implement end condition below, using the BREAK keyword.
