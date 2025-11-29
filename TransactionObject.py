import datetime
class transaction:
    income = float(0)
    date = 00/00/0000
    category = ""
    description =""

    def __init__(self):
            while True :
                try:
                    self.income = float(input("Enter the how much income to add: "))
                    break
                except:
                    print("Please enter an numerical value")

            while True :
                try:
                 self.date = input("Please enter date of transaction(DD/MM/YYYY): ")
        
                except:
                    print("Please enter a date (DD/MM/YYYY)")

            self.category = input("Please enter a category: ")
            self.description = input("Please enter a description: ")


class income(transaction):
    pass

class expense(transaction):
    pass

