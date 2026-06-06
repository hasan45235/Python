biscuits = {
    "Oreo":10,
    "Tuc":20,
    "Rio":{"Chocolate":20,"Strawberry":10}
}

def addBiscuit():
    newBiscuitKey = input("Enter New Item Key: ")
    newBiscuit = input("Enter New Item Value: ")
    biscuits[newBiscuitKey:newBiscuit]

def updateBiscuit():
    print("updating")

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