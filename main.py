global inventory
inventory = ["ID 1: Coke", "ID 2: Pepsi", "ID 3: Dr.Pepper"]

def inventory():
    inum = len(inventory()) + 1
    inventory.append("ID" + str(inum) + ": added item")

    return inventory

def help():
    print("Here are all of your options to choose from: balance, history, inventory, addItem, buyItem, help, exit")
    return


def buyItem():
    purchases = 0
    dollars = int(answer[3])
    quarters = int(answer[4])
    dimes = int(answer[5])
    nickles = int(answer[6])
    pennies = int(answer[7])
    money = round((dollars * 1 + quarters * .25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01), 2)
    product = answer[2]
    if money >= 1:
        purchases += 1
        change = money - (1*purchases)
        purchased = purchases*1
        print("You have purchased a", product, "your change is $", round(change, 2))
    else:
        print("You do not have enough money ")
    return


def addItems():
    quantity = int(answer[3])
    thing = str(answer[2])
    price = int(answer[4])
    value = quantity * price
    print("There have been", quantity, thing, "added to the machine")
    return value, thing



answerList = []
value = 0
moneyCollected = 0

while True:
    print(
        "What you you like to do?: Enter one of the following: balance, history, inventory, add item, buy item, help, "
        "exit")
    answer = input("Enter your request: ")
    answer = answer.split()
    answerList += answer

    if answer[0] == "buy":
        moneyCollected = buyItem()
    elif answer[0] == "history":
        print(answerList)
    elif answer[0] == "add":
        value= addItems()
        thing= addItems()
    elif answer[0] == "help":
        help()
    elif answer[0] == "inventory":
        inventory(thing)
    elif answer[0] == "balance":
        if (value and moneyCollected != 0):
            print("The balance of the vending machine is", value-moneyCollected)
        else:
            print("Sorry there is no balance yet")
    elif answer[0] == "exit":
        print("Thanks for using the vending machine!")
        break
    else:
        print("I'm sorry please enter a valid request from above")
