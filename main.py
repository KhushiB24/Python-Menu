from week0 import matrix

from week1 import fibonacci,infodb, triangle

from week2 import factorial_class, mathy,palindrome,mathyoop,hangman

import time
import os


data_menu = [
    ["Matrix", matrix.matrix],
    ["InfoDB", infodb.driver],
    ["Palindrome", palindrome.driver],
    ["Triangle", triangle.turtle],
    
]
math_menu = [
  ["fibonacci", fibonacci.driver],
  ["Math Function oop", mathy.exponent],
  ["Math Function imperative", mathyoop.imperative],
  ["Factorial Class", factorial_class.driver],  

]
adventure_menu =[
  ["Hangman", hangman.run] 
  
]

def menu(title, options):
    # header for menu
    # Menu banner
    border = "=" * 25
    banner = f"\n{border}\n{title}\n{border}"
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    menu(title, options)  # recursion, start menu over again


# def math_menu
# using sub menu list above:
# sub_menu works similarly to menu()
def _data_menu():
    title = "Data"
    menu(title, data_menu)


# def math_menu
# using sub menu list above:
# sub_menu works similarly to menu()
def _math_menu():
    title = "Math Menu"
    menu(title, math_menu)


# def adventure menu
# using sub menu list above:
# sub_menu works similarly to menu()
def _adventure_menu():
    title = "Adventure SubMenu"
    menu(title, adventure_menu)


def driver():
    title = "Main Menu"
    menu_list = [["Data", _data_menu],
                 ["Math", _math_menu],
                 ["Adventure", _adventure_menu]]
    menu(title, menu_list)


if __name__ == "__main__":
    driver()

