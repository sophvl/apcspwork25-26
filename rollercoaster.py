#A code that helps people decide what's the best rollercoaster ride for them! Ensuring joy for everyone

#Initialize
print("Welcome to my app! I'm here to help you figure out which rides you're looking for and which would suit you the best!")
import pandas as pd

data = pd.read_csv('rollercoaster.csv') #Reads the file of all the information about rollercoasters
ID = data['id'].tolist()  #Lines 9-19 are all arrays
name = data['Rollercoaster Name'].tolist()
park = data['Amusement Park'].tolist()
city = data['City'].tolist()
country = data['Country'].tolist()
region = data['Region'].tolist()
material = data['Construction Material'].tolist()
height = data['Height'].tolist()
speed = data['Speed'].tolist()
length = data['Length'].tolist()
year = data['Year Opened'].tolist()

filter=[]

#Functions
def menu():
    while True:
        pick = input("Hi! What would you like to look up in my rollercoaster app?(location, rides, height, year, speed, leave): ")
        if pick == "rides":  #provides all the rides in the amusement park that the user inputs
            park2 = input("Which amusement park would you like to look up?: ")
            print(" ")
            print("Here's all the rollercoaster's that are available this park!")
            ride_names(park2)
            continue
        if pick == "location":  #Allows the user to find the City and Country of the given amusement park
            location()
            continue
        if pick == "height":  #Gives a variety of rollercoasters that matches their preferences of either tall or short rollercoasters
            num = input("Do you like short, medium or tall rollercoasters?: ")
            if num == "tall":
                tall()  #Prints all the rollercoasters that are considered tall
            elif num =="medium":
                medium_height()  #Prints all the rollercoasters that are considered average height
            elif num == "short":
                short()  #Prints all the short rollercoasters
                continue
        elif pick == "year":  #Allows the user to find rollercoasters that are opened in the year they want
            year1 = int(input("Which year of rollercoasters do you want to look up?(1955-2014): "))
            year_opened(year1)
        elif pick == "speed":
            velocity()
        if pick == "leave": #Breaks the loop
            print("You have exited!")
            break



def ride_names(word):
    for i in range(len(park)):
        if word in park[i]:
            filter.append(name[i])
    print(filter)
    if len(filter) < 1:
        print("Park not found sorry! you can try a different one.")
        filter.clear()

def location():
    answer = input("Which park would you like to search up?: ")
    for i in range(len(name)):
        if answer in park[i]: #If the answer matches a name in park, it prints the City and Country of the park
            filter.append(city[i])
            filter.append(country[i])
            break
    print(" ")
    print("Here's the City and the Country of the located park:")
    print(filter)
    filter.clear()

def tall():
    for i in range(len(name)):
        if height[i] >= 61: #61 is in meters, it's around 200 feet
            filter.append(name[i])
    print(" ")
    print("These are all the rollercoasters that are over 200 feet tall!")
    print(filter)
    filter.clear()

def medium_height():
    for i in range(len(name)):
        if 15 <= height[i] < 61:
            filter.append(name[i])
    print(" ")
    print("These are all the rollercoasters that are around 50-200ft feet tall!")
    print(filter)
    filter.clear()

def short():
    for i in range(len(name)):
        if height[i] < 15: #The 15 is in meters, it's around 50 feet
            filter.append(name[i])
    print(" ")
    print("These are all the rollercoasters that are under 50 feet tall!")
    print(filter)
    filter.clear()

def year_opened(x): #Input the year you wish to look up
    for i in range(len(year)):
        if x == year[i]:
            filter.append(name[i])
    print(" ")
    print(f"These are all the rollercoasters that are opened in the year {x}:") #Outputs the rollercoasters that matches the year that was opened
    print(filter)
    filter.clear()

def velocity():
    for i in range(len(speed)):
        choice = input("Do you like fast, medium or slow rollercoasters? or you can choose to leave!: ")
        if choice == "fast":
            fast_speed()
        elif choice == "medium":
            average_speed()
        elif choice == "slow":
            slow_speed()
        elif choice == "leave":
            break

def fast_speed():
    for i in range(len(speed)):
        if speed[i] >= 50:
            filter.append(name[i])
    print(" ")
    print("These are all the rollercoasters that are fast, reaching 112 mph and faster")
    print(filter)
    filter.clear()
def average_speed():
    for i in range(len(speed)):
        if 30 <= speed[i] < 50:
            filter.append(name[i])
    print(" ")
    print("These are all the rollercoasters that are moderate speed, reaching around 67 to 110 mph")
    print(filter)
    filter.clear()
def slow_speed():
    for i in range(len(speed)):
        if speed[i] < 30:
            filter.append(name[i])
    print(" ")
    print("These are all the rollercoasters that are considered slow, with the highest speed of 64 mph:")
    print(filter)
    filter.clear()

#Main
menu()
