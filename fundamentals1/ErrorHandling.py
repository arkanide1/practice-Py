# Error Handling

# SyntaxeError
# NameError
#  IndexError
#ValueError
# keyError (for dict)
# zeroDivisionError ....

# error handling allows as to let the script continue running  even if there's an error

while (True):
    try:
        age = int(input("enter your age: "))
        10/age
    except ValueError:
        print("please enter a num")
    except ZeroDivisionError:
        print("zero isnt a valid number")
    else:
        print("good !")
        break
