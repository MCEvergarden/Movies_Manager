from os import system
import json


def changePath(newpath):
    path = newpath
def form():
    choices = {}
    for x in attributes:
        choices[x] = input(f"{x}: ")
    while choices['Type'] not in f:
        choices['Type'] = input(f"Type: ")
    f[choices['Type']][choices["Title"]] = choices
    Fsave()

def removeS(target):
    state = False
    for x in f:
        if target in f[x]:
            for y in f[x]:
                if target == y:
                    a = int(input("1) Delete\n2) Edit\n3)Menu\n>"))
                    if a == 1:
                        del f[x][y]
                        break
                    if a == 2:
                        att = input("Attribute you want to change\n>")
                        if att in f[x][y]:
                            f[x][y][att] = input("new attribute:\n>")
                        else:
                            print("Attribute not found")
                            removeS(target)
                    if a == 3:
                        break
                state = True
    if state == False:
        print("Not found")
        Fsave()

def Fsave():
    with open(data_base,"w") as fW:
        json.dump(f,fW,indent=4)

def listAll():
    print(10*"--")
    print(f"Listing Menu")
    print(10*"--")

    a = int(input("1) All\n2) Not seen\n3) Seen\n4) Category\n5) Menu\n>"))
    system("cls")
    parents =[x for x in f]
    if a == 4:
        print("\n".join(parents))
        listAll()
    if a == 1 or 2 or 3:
        for x in parents:
            for y in f[x]:
                for b in f[x][y]:
                    if a == 1 :
                            print(f"{b:5} : {f[x][y][b]:20}",end="")
                    if a == 2 :
                        if f[x][y]["Watched"].lower() == "no":
                            print(f"{b:5} : {f[x][y][b]:20}",end="")
                    if a == 3 :
                        if f[x][y]["Watched"].lower() == "yes":
                            print(f"{b:5} : {f[x][y][b]:20}",end="")
                print()
    if a == 5:
        menu()

def menu():
    system("cls")

    print(10*"--")
    print(f"Main Menu")
    print(10*"--")

    a =  int(input('1) Add item\n2) Select item\n3) Show\n5) Exit\n>'))

    if a == 1:
        form() 
    if a == 2:
        removeS(input("Select Title: \n>"))
    if a == 3:
        listAll()
    if a == 5:
        exit()
if __name__ == "__main__":
    attributes = ["Title","Type","Watched","Link"]
    data_base = "movie_base.json"
    try:
        f = open(data_base,"r")
        f = json.load(f)
    except:
        print("Error, please change data path.")
        changePath()
    
    while True:
        menu()
