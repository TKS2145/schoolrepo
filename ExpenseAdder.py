import TransactionObject
from Global import ExpenseList

def  ExpenseAdder():
    print("Expense will be added")

    expense = TransactionObject.Expense() #Creates the object expense
    expense.HasBeenAdded() #Check if data has been stored
    ExpenseList.append(expense) #Appends data to the list
    
