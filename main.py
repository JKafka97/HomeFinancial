from securityPin import *

possibilities = [1,2,8,9,0]

def main():

    options()
    answear = ansChecker()
    methodStarter(answear)    
    

def menu():
    pass

def options():
    print(
    """
    Insert one of options:
    1 - add money to account
    2 - take money from account
    8 - create new accound
    9 - set new password
    0 - quit app
    """)

def ansChecker():
    while True:
        try:
            answer = int(input("Your answer: "))
            if answer in possibilities:
                return answer
            else: print("There is no option with this number")
        except: print("You have to insert numbers")

def methodStarter(answear):
    if answear == 1:
        pass
    elif answear == 2:
        pass
    elif answear == 8:
        pass
    elif answear == 9:
        pass
    elif answear == 0:
        quit


if __name__ == "__main__":
    main()