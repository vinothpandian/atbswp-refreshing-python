#! python3

def displayInventory(inventory):
    print("Inventory:")
    sum = 0
    for k,v in inventory.items():
        print(str(v) + " " + k)
        sum += v
    print("Total number of items: "+str(sum))

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)
