#! python

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    sum = 0
    for k,v in inventory.items():
        print(str(v) + " " + k)
        sum += v
    print("Total number of items: "+str(sum))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
