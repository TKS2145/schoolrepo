import TransactionObject
from Global import IncomeList

def IncomeAdder():

    #adds income
    print("Income will be added")

    income = TransactionObject.Income() #Creates the object
    income.HasBeenAdded() #Checks that data has been added
    IncomeList.append(income) #Appends the objecct to the list




