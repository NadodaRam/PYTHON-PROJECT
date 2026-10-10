
print("Welcome to the Interactive Personal Data Collector!")

name = input("\nPlease enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {favourite_number} (Type: {type(favourite_number)}, Memory Address: {id(favourite_number)})")

import datetime

current_year = datetime.datetime.now().year
birth_year = current_year - age

print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

print("\nThank you for using the Personal Data Collector. Goodbye!")


Welcome to the Interactive Personal Data Collector!

Please enter your name: RAM
Please enter your age: 21
Please enter your height in meters: 1.60
Please enter your favourite number: 8

Thank you! Here is the information we collected:

Name: RAM (Type: <class 'str'>, Memory Address: 1441390474704)
Age: 21 (Type: <class 'int'>, Memory Address: 140719698136120)
Height: 1.6 (Type: <class 'float'>, Memory Address: 1441390592912)
Favourite Number: 8 (Type: <class 'int'>, Memory Address: 140719698135704)

Your birth year is approximately: 2005 (based on your age of 21)

Thank you for using the Personal Data Collector. Goodbye!
