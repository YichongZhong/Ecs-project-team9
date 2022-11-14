import random

hap = []
H1 = 10
D1 = 8
H2 = 15
D2 = 6
H3 = 12
D3 = 5


day1 = tuple([random.normalvariate(H1, D1)]) #caf 1 hapiness on the first day
day2 = tuple([random.normalvariate(H2, D2)]) #caf 2 happiness on second day
day3 = tuple([random.normalvariate(H3, D3)]) #caf 3 happiness on thrid day

for i in range(297):
    happy1 = sum(day1) #finds the sum of caf 1 if it is the best

for i in range(297):
    happy2 = sum(day2) #finds the sum of caf 2

for i in range(297):
    happy3 = sum(day3) #finds the sum of caf 3

    
#Finds the best cafeteria
    
if happy1 > happy2:
    if happy1 > happy3:
        print("Cafeteria 1 is the best")
        print(happy1)
    else:
        print("Cafeteria 3 is the best")
        print(happy3)

elif happy2 > happy3:
    print("Cafeteria 2 is the best")
    print(happy2)

else:
    print("Cafeteria 3 is the best")
    print(happy3)
        



