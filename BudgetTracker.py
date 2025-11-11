#TKS Budget Tracker
print("Welcome to the budget tracker of TKS")
print("\n")

def main():
    option = OptionScreen()
    print(option)


def OptionScreen():

    print("Type the number of the option which you want to choose")
    print("1) Add income")
    print("2) Add expense")
    print("3) Filter")
    print("4) Show summary")
    print("0) exit")
    
    option = int(input("Choose option: "))
    while option < 0 or option > 4:
        option = int(input("Invalid option. Enter a number from 0 to 4 (inclusive): "))
        
    if option == 0 :
        SystemExit
    else:
        return option
    
def IncomeAdder():

    #adds income
    print("Wazaaa")


def ExpenseAdder():
    print("Wazaaa")


def Filter():
    print("Wazaaa")


def Summary():
    print("Wazaaa")


#main at the bottom to let the other subroutines and functions get translated
main() #calling main. Python is very weird. 


