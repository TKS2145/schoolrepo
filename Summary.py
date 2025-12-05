from Global import IncomeList
from Global import ExpenseList

def Summary():
    
    print("--SUMMARY--\n")
              
    if len(IncomeList) == 0 and len(ExpenseList) == 0: #If there are no transactions, no need to continue
        print("There are no transactions currently")
        return
    
    else :

        print("There are " , len(IncomeList) , " incomes and " , len(ExpenseList) , " expenses.") #If transactions were entered, number and types of transactions are outputed.

        totalincome = 0.0
        totalexpense = 0.0

        for i in IncomeList :
            totalincome += i.amount

        for i in ExpenseList:
            totalexpense += i.amount

        print("Total incomes: " , totalincome)
        print("Total expenses: " , totalexpense)

        difference = totalincome - totalexpense

        if difference > 0: #If difference > 0, income > expenses so money saved
            print("Amount saved: " , difference)
        elif difference < 0:    #if difference < 0, expenses > incomes so money is due
            print("Amount due: " , -difference)
        else:
            print("All money obtained has been spent") #Rare case income == expense

        return #Ending the program