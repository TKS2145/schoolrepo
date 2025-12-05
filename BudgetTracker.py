#TKS Budget Tracker
print("Welcome to the budget tracker of TKS")
print("\n")

import IncomeAdder
import ExpenseAdder
import ListTransac
import Filter
import Summary
import ExitSystem
import TransactionObject
import Global
from datetime import datetime

def main():

    while True:

        option = OptionScreen()
    
        print("Option ", option, " selected. \n")

        match option:
            case 1 : IncomeAdder.IncomeAdder()
            case 2 : ExpenseAdder.ExpenseAdder()
            case 3 : ListTransac.ListTransactions()
            case 4 : Filter.Filter()
            case 5 : Summary.Summary()



def OptionScreen():

    print("Type the number of the option which you want to choose")
    print("1) Add income")
    print("2) Add expense")
    print("3) List transactions")
    print("4) Filter")
    print("5) Show summary")
    print("0) exit")
    
    while True:
   
        try:     
            option = int(input("Choose option (0 - 5): "))
            while option < 0 or option > 5:
                option = int(input("Invalid option. Enter a number from 0 to 5 (inclusive): "))
            break 

        except:
            print("Please enter a 'number' from (0 - 5)")

    if option == 0 :
        ExitSystem.ExitProgram()
    else:
        return option        



#main at the bottom to let the other subroutines and functions get translated
main() #calling main. Python is very weird. 

