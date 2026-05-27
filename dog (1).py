#Dog Breed (CREATE TASK)
#The purpose of my program is to help users choose a dog breed that meets their needs.


#Initialize
import pandas as pd
import webbrowser
data = pd.read_csv('dog.csv')
weight = data['Minimum Weight'].tolist()
name = data['Name'].tolist()
temperament = data['Temperament'].tolist()
image = data['Image'].tolist()
dogbreed = data['Breed Group'].tolist()
ID = data['id'].tolist()

filter = []
#Functions
def dog_info():
    while True:
        interest = input("What would you like to look up?(dog size, breed name, trait, or exit): ")
        if interest == "dog size":
            size1 = input("What size would you want your dog?(tiny, small, medium, large): ")
            dogsize(size1)
            continue
        if interest == "breed name":
            breed = input("What breed are you looking for?: ")
            lookup(breed)
            continue
        if interest == "trait":
            trait1 = input("What trait are you looking for?: ")
            lookup2(trait1)
            continue
        else:
            break

def dogsize(size):
    if size == "tiny":
        for i in range(len(weight)):
            if weight[i] <= 10:
                filter.append(name[i])
        print("Here's what's recommended for tiny dogs!")
        print(filter)
    filter.clear()
    if size == "small":
        for i in range(len(weight)):
            if 11 <= weight[i] <= 25:
                filter.append(name[i])
        print("Here's what's recommended for small dogs!")
        print(filter)
    filter.clear()
    if size == "medium":
        for i in range(len(weight)):
            if 26 <= weight[i] <= 60:
                filter.append(name[i])
        print("Here's what's recommended for medium size dogs!")
        print(filter)
    filter.clear()
    if size == "large":
        for i in range(len(weight)):
            if weight[i] > 60:
                filter.append(name[i])
        print("Here's what's recommended for large dogs!")
        print(filter)
    filter.clear()
def lookup(breed_name):
    for i in range(len(name)):
        if breed_name in name[i]:
            print(temperament[i])
            print(ID[i])
            webbrowser.open(image[i])

def lookup2(trait):
    for i in range(len(temperament)):
        if trait in temperament[i]:
            filter.append(name[i])
    print(filter)
    filter.clear()


#Main
dog_info()
#Sources
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
