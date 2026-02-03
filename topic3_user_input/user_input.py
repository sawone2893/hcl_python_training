# This script collects user input and demonstrates different data types and variable assignments in Python.
age=int(input("Enter your age: "))
name=input("Enter your name: ")
is_student=input("Are you a student? (yes/no): ").strip().lower() == 'yes'
height=float(input("Enter your height in meters: "))
hobbies=input("Enter your hobbies separated by commas: ").split(',')
address={'street': input("Enter your street: "),
         'city': input("Enter your city: "),
         'zip': input("Enter your zip code: ")}
location=(float(input("Enter your latitude: ")), float(input("Enter your longitude: ")))
favorite_color=None  # Initially no favorite color
print("Age (Integer):", age)
print("Name (String):", name)
print("Is Student (Boolean):", is_student)
print("Height (Float):", height)
print("Hobbies (List):", hobbies)
print("Address (Dictionary):", address)
print("Location (Tuple):", location)
print("Favorite Color (NoneType):", favorite_color)
