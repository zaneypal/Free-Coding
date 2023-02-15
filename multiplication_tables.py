# The Multiplication Tables Program
# lets you pull up endless tables of any multiples. You can also practice your multiplication skills. Try it out!

# Creator: Zane Palino
# Date: 2/15/2023 11:58 AM

#______________________________________________________________________________________________________________________
quit_prog = False

import random
import sys

def tab(amount):
    return "\t"*amount

# ak means Accepted Keywords
view_tables_ak = ["view tables", "view table", "vt", "v", "vi", "view", "tables", "table"]
quiz_ak = ["quiz", "qu", "qui", "quiz time"] 

print("\n\nWelcome to The Multiplication Tables Program")
while quit_prog == False:
    view_tables = False
    quiz = False
    start_mode = True
    answer_mode = True
    
    while start_mode == True:
        mode = input(f"\n{tab(5)}      Available Modes:\n{tab(6)}VIEW TABLES\n{tab(6)}   QUIZ\n\nChoose a mode:  ")
        if mode.lower() == 'q':
            sys.exit("You have ended the program.")
        else:
            for word in view_tables_ak:
                if word == mode.lower():
                    view_tables = True
                    break
            for word in quiz_ak:
                if word == mode.lower():
                    quiz = True
                    break
            if view_tables == False and quiz == False:
                print("Invalid input. Choose from the following available modes.")
                continue 
#______________________________________________________________________________________________________________________

        if view_tables == True:
            print("View tables mode selected. Enter 'q' to exit anytime.")
        while view_tables == True:

            multiplier = input("\n\nWhat number do you want to multiply by?  ")
            if multiplier.lower() == 'q':
                break
            while multiplier.isnumeric() == False:
                print("Please enter a number.")
                multiplier = input("\n\nWhat number do you want to multiply by?  ")
            multiplier = int(multiplier)

            multiplicand = input("\nHow many rows do you want to see?  ")
            if multiplicand.lower() == 'q':
                break
            while multiplicand.isnumeric() == False:
                print("Please enter a number.")
                multiplicand = input("\nHow many rows do you want to see?  ")
            multiplicand = int(multiplicand)

            print("")
            for i in range(1, multiplicand+1):
                product = multiplier * i
                print(f"{multiplier} x {i} = {product}")
            status = input("\nHit enter to create a new table. Press 'q' to exit view tables mode.  ")
            if status.lower() == "q":
                break
            else:
                continue
                
        if quiz == True:
            print("You have selected study mode.\nEnter 'q' to quit anytime.")
        while quiz == True:
            multiplier = input("\n\nWhat number do you want to multiply by?  ")
            if multiplier.lower() == 'q':
                break
            while multiplier.isnumeric() == False:
                print("Please enter a number.")
                multiplier = input("\n\nWhat times table do you want to practice?  ")
            multiplier = int(multiplier)

            multiplicand = input("\nWhat is the max number you want to multiply by?  ")
            if multiplicand.lower() == 'q':
                break
            while multiplicand.isnumeric() == False:
                print("Please enter a number.")
                multiplicand = input("\nHow many rows do you want to see?  ")
            multiplicand = int(multiplicand)

            while answer_mode == True:
                temporary_multiplicand = random.randint(1, multiplicand)
                product = multiplier * temporary_multiplicand
                answer = (input(f"{multiplier} x {temporary_multiplicand} = "))
                if answer == "q":
                    break
                elif answer == str(product):
                    print("Correct!\n\n")
                else:
                    print(f"Wrong.\nAnswer: {product}\n")
            quiz = False
