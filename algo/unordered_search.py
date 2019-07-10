items = [1, 89, 43, 56, 90, 120, 600]

def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i

    return None

print("{} is at {}".format(87, find_item(87, items)))
print("{} is at {}".format(600, find_item(600, items)))
