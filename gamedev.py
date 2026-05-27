#Sophia Chen
#Initialize

import pandas as pd

data = pd.read_csv('gamedev.csv')
level = data['Level'].tolist()
time = data['Time'].tolist()
rating = data['Rating'].tolist()
summary = data['Summary'].tolist()
feedback = data['Feedback'].tolist()

filter = []
#Functions
def find_problems(level_rating):   #Step one: create the loop
    for i in range(len(rating)):  #Step two: Conditional Statement
        if rating[i] < level_rating:  #Step three: add items to the filter
            filter.append([i])   #Step four: Print the filter and clear
    print(filter)
    filter.clear()

def find_goodtime(level_time):
    for i in range(len(time)):
        if time[i] < level_time:
            filter.append([i])
    print(filter)
    filter.clear

def find_secret(word):
    for i in range(len(feedback)):
        if word in feedback[i]:
            filter.append([i])
            print(filter)

#Main
find_problems(2)
print(data.loc[[14,34,77]])

