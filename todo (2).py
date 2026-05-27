#Sophia Chen

#Initialize
print("Welcome to sophia's must eat app! You can select what you want to do below")
#Functions
todolist = []
donelist = []

def list():
    while True:
        menu = input("Enter a number please: Add an item to the to-do list(1), Mark as done(2), Remove an item or Clear the List(3), Exit(4): ")
        if menu == "1":
            item = input("What would you like to add?: ")
            todolist.append(item)
            print(todolist)
        if menu == "2":
            finish = input("What would you like to mark as done?: ")
            todolist.remove(finish)
            donelist.append(finish)
            print("This is your to do list:")
            print(todolist)
            print("This is your done list:")
            print(donelist)
        if menu == "3":
            choice = input("would you like to remove an item(remove) or clear the list(clear)?: ").lower()
            if choice == "remove":
                remove = input("what would you like to remove?: ")
                todolist.remove(remove)
            if choice == "clear":
                todolist.clear()
            print("This is your to do list:")
            print(todolist)
            print("This is your done list:")
            print(donelist)
        if menu == "4":
            print("You exited the program.")
            break

#Main
list()


