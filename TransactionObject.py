from datetime import datetime
class transaction:

    income = float(0)
    date = datetime.strptime("01/01/0001", "%d/%m/%Y")
    category = ""
    description =""

    def __init__(self, income, date, category, description):
            while True :
                try:
                    self.income = float(input("Enter the how much income to add: "))
                    break
                except:
                    print("Please enter an numerical value")

            while True :
                try:
                 self.date = datetime.strptime(input("Please enter date of transaction(DD/MM/YYYY): "))
        
                except:
                    print("Please enter a date (DD/MM/YYYY)")

            self.category = input("Please enter a category: ")
            self.description = input("Please enter a description: ")


class Income(transaction):
    pass

    def HasBeenAdded(self, income, date):
        print("Income of " , self.income  , " on the " , self.date , " has been added.")

class Expense(transaction):
    pass
   
    def HasBeenAdded(self, income, date):
        print("Expense of " , self.income  , " on the " , self.date , " has been added.")

