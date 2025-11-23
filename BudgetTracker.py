import IncomeAdder
import ExpenseAdder
import Filter
import Summary
import ExitSystem


#TKS Budget Tracker
print("Welcome to the budget tracker of TKS")
print("\n")


def main():

    option = OptionScreen()
    
    print("Option ", option, " selected")

    match option:
        case 1 : IncomeAdder.IncomeAdder()
        case 2 : ExpenseAdder.ExpenseAdder()
        case 3 : Filter.Filter()
        case 4 : Summary.Summary()



def OptionScreen():

    print("Type the number of the option which you want to choose")
    print("1) Add income")
    print("2) Add expense")
    print("3) Filter")
    print("4) Show summary")
    print("0) exit")
    
    while True:
   
        try:     
            option = int(input("Choose option (0 - 4): "))
            while option < 0 or option > 4:
                option = int(input("Invalid option. Enter a number from 0 to 4 (inclusive): "))

        except:
            print("Please enter a 'number' from (0 - 4)")

        if option == 0 :
            ExitSystem.ExitProgram()
        else:
            return option        



#main at the bottom to let the other subroutines and functions get translated
main() #calling main. Python is very weird. 

