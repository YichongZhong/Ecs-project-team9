import random


# create 3 lists
def exploreOnly():
    list1 = []
    list2 = []
    list3 = []
    # create index for the range of 100
    for i in range(100):
        # append lists with normal variation
        vari1 = random.normalvariate(10, 8)
        list1.append(vari1)
        vari2 = random.normalvariate(15, 6)
        list2.append(vari2)
        vari3 = random.normalvariate(12, 5)
        list3.append(vari3)

    return sum(list1) + sum(list2) + sum(list3)

