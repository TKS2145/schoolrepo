import TransactionObject
import Global


TempIncomeList = list(Global.IncomeList)
TempExpenseList = list(Global.ExpenseList)


def Filter():

    option = optionscreen()

    match option:
        case 1: CategoryFilter()
        case 2: print("Wazaa")
        case 3:
            print("Wazaaaa")
  

def optionscreen():

    print("Select option to filter by: ")

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

    if len(TempIncomeList) + len(TempExpenseList) != 0 :

        CategoryList = []

        for i in TempIncomeList:
            if TempIncomeList[i].category not in CategoryFilter:
                CategoryFilter.append(TempIncomeList[i])

        for i in TempExpenseList:
            if TempExpenseList[i].category not in CategoryFilter:
                CategoryFilter.append(TempExpenseList[i])

        while True:
            try:
                print(CategoryList)
                index = input("Please enter the number corresponding to the item to filter by (1 for first item, 2 for second, etc): ") #Enter the position of the item
                index = index - 1   #As array index starts with 0 so one less1 for first, 2 for second...)
                Category = CategoryList[index]  #Category item obtained to filter the lists
                break
            except:
                print("Please enter the 'number' corresponding to the item to filter by (1 for first item, 2 for second, etc): ")
            
        for i in TempIncomeList:
            if Category == TempIncomeList[i].Category :
                TempIncomeList[i].output

        for i in TempExpenseList:
            if Category == TempExpenseList[i].category :
                TempExpenseList[i].output
    
        return

    else:
        print("No transactions stored. Nothing to filter")
        return