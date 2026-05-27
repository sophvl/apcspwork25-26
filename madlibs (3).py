#Sophia Chen
#Initialize
import random

#Functions
def madlibs():
    print("Welcome to sophia's game! please enter each question or you can type random to randomize your option, and please write your response in all CAPS")
    #gather input
    #story
    ranimal = ["GIRAFFE", "DRAGON", "PANDA", "KOALA"]       #Array's that show the random options
    rplace = ["TARGET", "POPEYES", "DISNEYLAND", "six flags"]
    rname = ["ANGELINA", "SOPHIE", "ALEX", "RENEE"]
    rrestaurant = ["MCDONALDS", "SUBWAY", "OLIVE GARDEN", "WINGSTOP"]
    rfood = ["CAKE", "NOODLES", "PASTA", "DUMPLINGS"]
    rmood = ["ANGRY", "DEPRESSED", "SAD", "MOODY"]
    rweapon = ["FORK", "BAT", "BACKPACK", "STICK"]
    rnumber = ["FIVE", "SEVEN", "TWO", "ELEVEN"]
    rwildanimal = ["TIGER", "LION", "CROCODILE", "SKUNK"]
    rareainhouse = ["BATHROOM", "BASEMENT", "LIVING ROOM", "KITCHEN"]

    animal = input("Please enter an animal: ")
    if animal == "random":
        animal = random.choice(ranimal)
    place = input("Please enter a place: ")
    if place == "random":
        place = random.choice(rplace)
    name = input("Please enter a name: ")
    if name == "random":
        name = random.choice(rname)
    restaurant = input("Please enter a restaurant: ")
    if restaurant == "random":
        restaurant = random.choice(rrestaurant)
    food = input("Please enter a food: ")
    if food == "random":
        food = random.choice(rfood)
    mood = input("Please enter a mood: ")
    if mood == "random":
        mood = random.choice(rmood)
    weapon = input("Please enter a weapon: ")
    if weapon == "random":
        weapon = random.choice(rweapon)
    number = input("Please enter a random number in words: ")
    if number == "random":
        number = random.choice(rnumber)
    wildanimal =input("Please enter an wildanimal: ")
    if wildanimal == "random":
        wildanimal = random.choice(rwildanimal)
    areainhouse = input("Please enter a random area in your house: ")
    if areainhouse == "random":
        areainhouse = random.choice(rareainhouse)

    print(f"""I saw a \033[1m{animal}\033[0m today at \033[1m{place}\033[0m. I thought it was pretty cool, but \033[1m{name}\033[0m, my friend, didn't like it at all.
    later we went to eat at \033[1m{restaurant}\033[0m, the \033[1m{food}\033[0m was so delicious. We made sure to get seconds but the waiter
    was a bit \033[1m{mood}\033[0m and yelled at us. My friend \033[1m{name}\033[0m was not happy and jumped onto them with a \033[1m{weapon}\033[0m, they fought for \033[1m{number}\033[0m hours.
    I thought today was pretty chill for me until I saw a \033[1m{wildanimal}\033[0m in my \033[1m{areainhouse}\033[0m when I got home.""")
#Main
madlibs()
