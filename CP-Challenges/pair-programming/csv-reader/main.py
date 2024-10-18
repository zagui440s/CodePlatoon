import csv

user_input = input("Would you like cat or dog? ('cat'/'dog')")

if user_input == 'cat':
    with open("data/cats.csv", "r") as cats_read_file:
        reader = list(csv.reader(cats_read_file))
        reader.pop(0)
    for cats in reader:
        print(f"{cats[0]} is a {cats[1]} year old {cats[2]}")
elif user_input == 'dog':
    with open("data/dogs.csv", "r") as dogs_read_file:
        reader = list(csv.reader(dogs_read_file))
        reader.pop(0)
        for dogs in reader:
            print(f"{dogs[0]} is a {dogs[1]} year old {dogs[2]}")
else:
    print(f"Sorry, we dont have any {user_input} here.")



