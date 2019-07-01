
def startMenu():
    print(  "\tShopping Cart Menu"  )
    print("–––––––––––––––––––––––––––––––––")
    print(" ")
    print("1. Add items to your shopping cart")
    print("2. Delete items from your shopping cart")
    print("3. View your current shopping cart")
    print("4. Exit")
    print("5. Menu")
    active = True
    while active:
        try:
            q = int(input("What would you like to do? : "))
            if q == 1:
                addItems()
                active = False
            elif q == 2:
                r = []
                deleteItems(r)
            elif q == 3:
                l = []
                viewItems(l)
            elif q == 4:
                active = False
            elif q == 5:
                active = True
            else:
                print('I don\'t understand what you are trying to do?')
        except:
            print('Please enter a valid input(1,2,3,4)')
            active = True

def addItems():
    a = []
    active = True
    while active:
        try:
            add = input('Enter what you would like to add: ')
            if isinstance(add, str):
                if add == str(3):
                    viewItems(a)
                    exit = input("Are you sure you want to leave?(y or n) ")
                    if exit.lower() == 'y':
                        exitScreen(a)
                        active = False
                    else:
                        active = True
                if add == str(4):
                    return
                if add == str(5):
                    return
            else:
                print('Please enter a valid nmbern')
            a.append(add)
        except:
            print("I do not understand that command, enter a valid input")


def viewItems(alist):
    ex = []
    if not alist:
        print("Your shopping cart is empty.")
        return
    else:
        print(" ")
        print(  "\tYour Shopping Cart"  )
        print("–––––––––––––––––––––––––––––––––")
        print(" ")
        for i in range(len(alist)):
            print(f'{i}. \t{alist[i]}')
        t = input("Would you like to continue adding items? (Y or N)")
        if t.lower() == 'y':
            return alist
        elif t.lower() == 'n':
            return

def exitScreen(alist):
    print(" ")
    print(  "\tYour Shopping Cart"  )
    print("–––––––––––––––––––––––––––––––––")
    print(" ")
    for i in range(len(alist)):
        print(f'{i}. \t{alist[i]}')
    return

startMenu()

def deleteItems(blist):
    blist = []
    if not blist:
        print("Your shopping cart is empty.")
        return
    else:
        d = input("What would you like to delete? ")
        for i in range(len(blist)):
            if d == blist[i]:
                blist.remove(blist[i])
                return blist
            else:
                print('there is no item by that name')
                return
