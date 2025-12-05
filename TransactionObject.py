from datetime import datetime
class transaction:

    amount = float(0)
    date = datetime.strptime("01/01/0001", "%d/%m/%Y")
    category = ""
    description =""

    def __init__(self):
        while True :
            try:
                self.amount = float(input("Enter the how much income to add: "))
                break
            except:
                print("Please enter an numerical value")
                
              

        while True :
            try:
                self.date = datetime.strptime(input("Please enter date of transaction(DD/MM/YYYY): "), "%d/%m/%Y") #Enter the date as string, formats as string and passes into class date variable
                break
            except:
                print("Please enter a date (DD/MM/YYYY)")


        self.category = input("Please enter a category: ")
        self.description = input("Please enter a description: ")

    def output(self, amount, date, category, description):
        print("Amount: " , self.amount)
        print("Date: " , self.date)
        print("Category: " , self.category)
        print("Description: ", self.description)



class Income(transaction):
    pass

    def HasBeenAdded(self):
        print("Income of " , self.amount  , " on the " , self.date.strftime("%d/%m/%Y") , " has been added.")

    def output(self, amount, date, category, description):
        print("Income of: ")
        super().output(amount, date, category, description)


class Expense(transaction):
    pass

    def HasBeenAdded(self):
        print("Expense of " , self.amount  , " on the " , self.date.strftime("%d/%m/%Y") , " has been added.")

    def output(self, amount, date, category, description):
        print("Expense of: ")
        super().output(amount, date, category, description)
