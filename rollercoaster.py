#Sophia Chen
#A code that helps people decide what's the best rollercoaster ride for them! Ensuring joy for everyone

#Initialize
print("Welcome to my app! I'm here to help you figure out which rides you're looking for and which would suit you the best!")
import pandas as pd
import random

data = pd.read_csv('rollercoaster.csv')
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
#Function
def location(amusement):
    for i in range(len(park)):
        if park[i] == amusement:
            filter.append(name[i])
    print(filter)
    filter.clear()



#Main
print("Here's all the rollercoaster's that are available this park!")
location("SeaWorld San Antonio")
