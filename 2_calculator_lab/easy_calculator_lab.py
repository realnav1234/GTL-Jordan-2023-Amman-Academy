########################################################

# NAME: 
# GRADE: 

########################################################

# Welcome to the EASY Calculator Lab!
# Below we will be implementing a very simple Python calculator you can use in the future.
# Addition is already implemented for you!

# In order to complete the lab, implement at least SUBTRACTION, MULTIPLICATION, DIVISION, AND EXPONENTS
# You can implement other operations if you would like.

# To SUBMIT:
#   1. Open your EMAIL
#   2. Write the following subject line. 
#       [YOUR NAME]: EASY CALCULATOR LAB
#   3. Copy and paste your code into the email (or attach the Python file, your choice).
#   4. Send the email to 14navpreetsingh@gmail.com


# GOOD LUCK!

########################################################


welcome_message = "Welcome to Nav's Calculator." # Change the welcome message to whatever you want
print(welcome_message)

while True: # This will make the calculator keep running forever, until we BREAK

    num1 = float(input("Enter the first number here: ")) # Converts the entered number into a float
    operation = input("Enter the operator here: ") # Enter +, -, *, /, and any other operator you implemented
    num2 = float(input("Enter the second number here: ")) 

    final_result = None # final_result is NOTHING by default

    if operation == '+':
        final_result = num1 + num2 # now final_result is the  sum of num1 and num2


    ######################
    # Write your operations code below. 
    # Implement at least subtraction, multiplication, division, and exponents.
    # You can implement others if you would like!




    



    ######################

    print("The answer is: ", final_result)

    do_you_want_to_end = input("Do you want to end the session?: ")

    ######################
    # Below, write code using the 'break' keyword to end the while loop when the user wants to end.




