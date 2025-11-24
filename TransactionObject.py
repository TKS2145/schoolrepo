class transaction:
    def __init__(NewDate, NewAmount, NewCategory, NewDescription):
        Date = NewDate
        Amount = NewAmount
        Category = NewCategory
        Desciption = NewDescription

class income(transaction):
    pass

class expense(transaction):
    pass

