import random

def Get_TwoRandom_NonIdenticalItems(itemlist):
    print(itemlist[0])

    first_item = random.choice(itemlist)
    itemlist.remove(first_item)
    second_item = random.choice(itemlist)
    return [first_item,second_item]


def main():
    print("Calling getRandom_NonIdenticalItems function")
    BICs = [1,2,3,4,5,6,7,8,'a','b']
    print(Get_TwoRandom_NonIdenticalItems(BICs))

#main()