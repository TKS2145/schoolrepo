Name = input("What is your name?")
gender = input("What is your gender? (M/F) ").upper()

while gender != "M" and gender != "F":
    print("Please enter M or F only.")
    gender = input("What is your gender? (M/F) ").upper()

day = input("On what day were you born?").lower()

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
        ashanti_name = male_names[day]
    elif gender == "F":
        ashanti_name = female_names[day]
    return ashanti_name

ashanti_name_result = ashanti(gender)
print(ashanti_name_result)