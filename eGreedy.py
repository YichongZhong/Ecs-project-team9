
import random

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
    happy1 = sum(day1) #finds the sum of caf 1 to see if it is the best

for i in range(297):
    happy2 = sum(day2) #finds the sum of caf 2 to see if it is the best

for i in range(297):
    happy3 = sum(day3) #finds the sum of caf 3 to see if it is the best
    



r = random.random() # Generate a random float 0 < r < 1
e = random.randint(0,100) # 
if r < e: #  Pick a random cafeteria
    i = random.randint(1,3) #Generate a random number between 1 and 3
    print(i)

else: # Find the best cafeteria
    if happy1 > happy2:
        if happy1 > happy3:
            print(happy1)
        else:
            print(happy3)

    elif happy2 > happy3:
        print(happy2)

    else:
        print(happy3)
    
   
        
        

