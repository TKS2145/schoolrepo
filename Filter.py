import TransactionObject
from Global import IncomeList
from Global import ExpenseList 
import datetime


def Filter():

    if (len(IncomeList) + len(ExpenseList)) != 0 :    #If sum is 0, then both lists are empty

        option = optionscreen()

        match option:
            case 1: CategoryFilter()
            case 2: MonthFilter()
            case 3: TypeFilter()
    
        return #Return to main module
    
    else:   #If empty, no use to filter
        print("No transactions made. Nothing to filter.")
        return

def optionscreen():

    
    print("Select option to filter by: ")   #If not empty, filter can be made

    print("1) Category")
    print("2) Month")
    print("3) type")


    while True:
        try:
            option = int(input("Enter choise: "))
            break
        except:
            print("Please enter a 'number' from 1 to 3")

    return option


def CategoryFilter():
    
    CategoryList = []

    i = 0
    while i < len(IncomeList):  #Looping through IncomeList
        print(IncomeList[i].category)
        if IncomeList[i].category not in CategoryList:
            CategoryFilter.append(IncomeList[i].category)   #Adding category item to CategoryList
        i += 1 #Incrementing i

    i = 0
    while  i < len(ExpenseList):
        if ExpenseList[i].category not in CategoryList:
            CategoryFilter.append(ExpenseList[i].category)
        i += 1

    #All the different categories of the transactions have been obtained

    while True:
        try:
            print(CategoryList)
            index = input("Please enter the number corresponding to the item to filter by (1 for first item, 2 for second, etc): ") #Enter the position of the item
            index -= 1   #As array index starts with 0 so one less1 for first, 2 for second...)
            Category = CategoryList[index]  #Category item obtained to filter the lists
            break
        except:
            print("Please enter the 'number' corresponding to the item to filter by (1 for first item, 2 for second, etc): ")
        
    for i in range(0,len(IncomeList)):
        if Category == IncomeList[i].Category :
            IncomeList[i].output

    for i in range(0, len(ExpenseList)):
        if Category == ExpenseList[i].category :
            ExpenseList[i].output

    return


def MonthFilter():

    while True :
        try:
            
            VarMonth = int(input("Please enter month number to filter by: "))
            while VarMonth < 1 or VarMonth > 12:
                VarMonth = int(input("Please enter a valid month number (1 - 12): "))
            
            break

        except:
            print("Invalid input. Please enter the number corresponding to the month (1 - 12)")


    IsPresent = False   #Variable to check if the month was found in the program

    for i in IncomeList:
        if i.date.month == VarMonth:
            IsPresent = True
            print(i.output)

    for i in ExpenseList:
        if i.date.month == VarMonth:
            IsPresent = True
            print(i.output)

    if IsPresent == False:  #Loops not executed so no matching month found in the lists
        print("No month corresponds to month entered.")

    return


def TypeFilter():
         
    if len(IncomeList) != 0 :   #If IncomeList not empty
        print("Incomes:")
        for i in IncomeList:
            print(i.date.strftime("%d/%m/%Y") , " - " , i.category , " - " , i.amount)
    else:   #Else it empty
        print("There are no incomes.")

    if len(ExpenseList) != 0 :  #If ExpenseList not empty
        print("Expenses:")
        for i in ExpenseList:
            print(i.date.strftime("%d/%m/%Y") , " - " , i.category , " - " , i.amount)
    else:   #Else, it empty
        print("There are no expenses.")

    return
    