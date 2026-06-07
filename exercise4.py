biscuits = {
    "Oreo":10,
    "Tuc":20,
    "Rio":20
}

def addBiscuit():
    newBiscuitKey = input("Enter New Item Key: ")
    newBiscuit = input("Enter New Item Value: ")
    biscuits[newBiscuitKey] = newBiscuit
    print("New Item Added")

def updateBiscuit2():
    name = input("Enter Biscuit name: ")
    val = int(input("Enter Biscuit value: "))
    for i in biscuits:
        if i == name:
            biscuits[i] = val
    # biscuits.update({})
    print(biscuits)


def updateBiscuit():
    name = input("Enter Biscuit name: ")
    val = int(input("Enter Biscuit value: "))
    biscuits.update({name:val})
    print(biscuits)

print("1. Show Products\n2. Add Product\n3. Update Product\n4. Exit")

userInp = int(input("Enter Option Number: "))

match userInp:
    case 1:
        print(biscuits)
    case 2:
        addBiscuit()
    case 3:
        updateBiscuit()
    case _:
        print("Done")        