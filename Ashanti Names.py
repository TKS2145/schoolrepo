import datetime

Name = input("What is your name?")
gender = input("What is your gender? (M/F) ").upper()

while gender != "M" and gender != "F":
    print("Please enter M or F only.")
    gender = input("What is your gender? (M/F) ").upper()

 #Enter birth date and assigns to date variable
year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (MM): "))
date = int(input("Enter your birth date (DD): "))
day_born = datetime.datetime(year, month, date) 
day_name = day_born.strftime("%A") #Suppose to extract the day from the birth date
print("You were born on a " + day_born.strftime("%A"))
day_name = day_name.lower()

#day = input("On what day were you born?").lower()

male_names = {
    'monday': 'Kwadwo',
    'tuesday': 'Kwabena',
    'wednesday': 'Kwaku',
    'thursday': 'Yaw',
    'friday': 'Kofi',
    'saturday': 'Kwame',
    'sunday': 'Kwasi'
}

female_names = {
    'monday': 'Adwoa',
    'tuesday': 'Abena',
    'wednesday': 'Akua',
    'thursday': 'Yaa',
    'friday': 'Afua',
    'saturday': 'Ama',
    'sunday':'Akosua'
}

def ashanti(gender):
    if gender == "M":
        ashanti_name = male_names[day_name]
    elif gender == "F":
        ashanti_name = female_names[day_name]
    return ashanti_name

ashanti_name_result = ashanti(gender)
print(ashanti_name_result)
