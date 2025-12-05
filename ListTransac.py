import TransactionObject
from Global import IncomeList
from Global import ExpenseList
from datetime import datetime

def ListTransactions():
    
    
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