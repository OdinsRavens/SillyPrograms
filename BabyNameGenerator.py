""" This program generates baby names using the name from famous actors and musicians. """

import random, sys

print("This is a baby name genorator, here is your baby's name.\n"  )

first= ("Alabama Gypsy Rose", "Dream", "Jermajesty", "Pixie", "Moroccan", "Remington Churchill Sydney", "Denim", "Kook Kangaroo", "Pumma", "Moxie Crimefighter",
"Petal Blossom Rainbow", "True", "Phoenix Wolf", "Zolton", "Everest", "Saint", "Snow", "Ode", "Zowie", "Apllo Bowie Flynn", "Sunday Rose", "Dandelion", "Diva Thin Muffin",
"Blue Angel", "Memphis Eve", "Fuchsia")

last=("Matteo", "Kardashian", "Jackson", "Geldof", "Cary", "Jagger", "Braxton", "Mellencamp", "Badu", "Jillette", "Oliver", "Whitaker", "Margera", "Lucas", "West", "Gibb",
"Malone", "Bowie", "Rossdale", "Kidman", "Richards", "Zappa", "Edge", "Bono", "Sting")

while True:
    firstname= random.choice(first)
    lastname= random.choice(last)
    print("\n\n")
    print("{}, {}".format(firstname, lastname), file=sys.stderr)
    print("\n\n")
    try_again= input("New name? (press a key for new name, N to quit)\n")
    if try_again.lower() == "n":
        break
    
input("\nPress a key to exit.")