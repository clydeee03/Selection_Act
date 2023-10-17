print("Welcome to the zodiac animal calculator")
print("---------------------------------------")

while True:
    var_year = int(input("Enter year:"))
    print("------------------------")
    zodiac = (var_year-1000)%12+1

    if zodiac == 1:
        print(var_year,"is the year of the Rat!")

    elif zodiac == 2:
        print(var_year,"is the year of the Ox!")
    
    elif zodiac == 3:
        print(var_year,"is the year of the Tiger!")

    elif zodiac == 4:
        print(var_year,"is the year of the Rabbit!")

    elif zodiac == 5:
        print(var_year,"is the year of the Dragon")

    elif zodiac == 6:
        print(var_year,"is the year of the Snake!")

    elif zodiac == 7:
        print(var_year,"is the year of the Horse!")

    elif zodiac == 8:
        print(var_year,"is the year of the Sheep!")

    elif zodiac == 9:
        print(var_year,"is the year of the Monkey!")

    elif zodiac == 10:
        print(var_year,"is the year of the Rooster!")

    elif zodiac == 11:
        print(var_year,"is the year of the Dog!")

    elif zodiac == 12:
        print(var_year,"is the year of the Pig!")

    another = input("Do you want to continue converting years into their zodiac animals?(Y/N):")
    if another.lower() != 'y':
        break





