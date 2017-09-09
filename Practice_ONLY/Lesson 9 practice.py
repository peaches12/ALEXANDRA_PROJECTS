inFile = open('random_wordcount.txt', 'r')
menuLines = inFile.readlines()
ItemsPrices = {}
ItemsOrdered = {}
for item in menuLines:
    print(item)
    splitIT = item.split()
    ItemsPrices[splitIT[0]] = splitIT[1]
    

Continue = 'y'

total = 0.00

while Continue == 'y':
    nextItem = input("Next item & quantity (If you want to quit, print 'quit'): ")
    if nextItem == 'quit':
        break
    itemsQuant = nextItem.split()
    if itemsQuant[0] in ItemsPrices:
        total += float(ItemsPrices[itemsQuant[0]]) * float(itemsQuant[1])
        if itemsQuant[0] in ItemsOrdered:
            ItemsOrdered[itemsQuant[0]] += str(total)
        else:
            ItemsOrdered[itemsQuant[0]] = itemsQuant[1]
    else:
        print("Sorry, the item isn't on our menu") 
    
print(ItemsOrdered)
for receipt in ItemsOrdered:
    print(receipt + ',' + ItemsOrdered[receipt] +  '\t' + ItemsOrdered[receipt])

print("Total: $" + str(total))

