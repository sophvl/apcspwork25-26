#Sophia Chen
#Init
score = 0
#Function
def points():
    for i in range(3):
        global score
        score = score + 100
        print("You earned"+" "+str(score)+" "+ "points!")


#Main
points()
print("Total score:"+ " "+str(score))
