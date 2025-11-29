import TransactionObject
from Global import IncomeList
from Global import ExpenseList
from datetime import datetime

def ListTransactions():
    
    
    if len(IncomeList) != 0 :
        print("Incomes:")
        for i in IncomeList:
            print(IncomeList[i].date.strftime("%d/%m/%Y") , " - " , IncomeList[i].category , " - " , IncomeList[i].amount)
    else:
        print("There are no incomes.")

    if len(ExpenseList) != 0 :
        print("Expenses:")
        for i in ExpenseList:
            print(ExpenseList[i].date.strftime("%d/%m/%Y") , " - " , ExpenseList[i].category , " - " , ExpenseList[i].amount)
    else:
        print("There are no expenses.")