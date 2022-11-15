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



def exploitOnly():
    H1 = 10
    D1 = 8
    H2 = 15
    D2 = 6
    H3 = 12
    D3 = 5

    C1 = random.normalvariate(H1, D1)  # caf 1 hapiness on the first day
    C2 = random.normalvariate(H2, D2)  # caf 2 happiness on second day
    C3 = random.normalvariate(H3, D3)  # caf 3 happiness on thrid day
    # Finds the best cafeteria
    best = max(C1, C2, C3)
    result = C1 + C2 + C3
    if best == C1:
        for i in range(297):
            result += random.normalvariate(H1, D1)
    if best == C2:
        for i in range(297):
            result += random.normalvariate(H2, D2)
    if best == C3:
        for i in range(297):
            result += random.normalvariate(H3, D3)

    return result



def eGreedy(e=10):
    # turn e into a percentage
    e = e / 100
    # import data
    H1 = 10
    D1 = 8
    H2 = 15
    D2 = 6
    H3 = 12
    D3 = 5
    # Track the average and count the days
    A1 = 0
    A2 = 0
    A3 = 0
    ct1 = 1
    ct2 = 1
    ct3 = 1
    # First time in the cafe
    C1 = random.normalvariate(H1, D1)
    C2 = random.normalvariate(H2, D2)
    C3 = random.normalvariate(H3, D3)
    # current best cafe
    best_caf = 0
    # loop for 297 days and always go to the best cafe
    for i in range(297):
        # Generate a random number
        r = random.random()
        # current best cafeteria
        best_caf = max(A1, A2, A3)
        # pick the best cafeteria
        if r > e:
            if best_caf == A1:
                C1 = C1 + random.normalvariate(H1, D1)
                A1 = C1 / ct1
                ct1 += 1
            elif best_caf == A2:
                C2 = C2 + random.normalvariate(H2, D2)
                A2 = C2 / ct2
                ct2 += 1
            elif best_caf == A3:
                C3 = C3 + random.normalvariate(H3, D3)
                A3 = C3 / ct3
                ct3 += 1
        # pick a random cafeteria
        else:
            num = random.randint(1, 3)
            if num == 1:
                C1 = C1 + random.normalvariate(H1, D1)
                A1 = C1 / ct1
                ct1 += 1
            elif num == 2:
                C2 = C2 + random.normalvariate(H2, D2)
                A2 = C2 / ct2
                ct2 += 1
            elif num == 3:
                C3 = C3 + random.normalvariate(H3, D3)
                A3 = C3 / ct3
                ct3 += 1

    return C1 + C2 + C3


def Simluation(t, e=10):
    e = e / 100
    H1 = 10
    D1 = 8
    H2 = 15
    D2 = 6
    H3 = 12
    D3 = 5
    print("TRIALS: "+str(t)+"\n")
    # test
    explore_total = 0
    exploit_total = 0
    eGreedy_total = 0
    for i in range(t):
        explore_total += exploreOnly()
        exploit_total += exploitOnly()
        eGreedy_total += eGreedy()

    AveHappy_explore = explore_total / t
    AveHappy_exploit = exploit_total / t
    AveHappy_eGreedy = eGreedy_total / t

    # exploreOnly()
    print("ExploreOnly:")
    # Optimum happiness#
    Optimum_happiness = H2 * 300
    print("Optimum happiness " + str(Optimum_happiness))
    # Expected total happiness#
    Expected_total_happiness = H1 * 100 + H2 * 100 + H3 * 100
    print("Expected total happiness" + " " + str(Expected_total_happiness))
    # Expected_Regret
    Expected_Regret = Optimum_happiness - Expected_total_happiness
    print('Expected Regret ' + str(Expected_Regret))
    # ave happyiness
    print("Average happiness: " + str(AveHappy_explore))
    # ave regret
    AveRegret_explore = Optimum_happiness - AveHappy_explore
    print("Average Regret： " + str(AveRegret_explore))
    print("\n")

    # exploitOnly
    print("ExploitOnly:")
    print("Optimum happiness " + str(Optimum_happiness))
    # Expected total happiness#
    Expected_total_happiness = H1 + H2 + H3 + 297 * H2
    print("Expected total happiness" + " " + str(Expected_total_happiness))
    # Expected_Regret
    Expected_Regret = Optimum_happiness - Expected_total_happiness
    print('Expected Regret ' + str(Expected_Regret))
    # ave happyiness
    print("Average happiness: " + str(AveHappy_exploit))
    # ave regret
    AveRegret_exploit = Optimum_happiness - AveHappy_exploit
    print("Average Regret： " + str(AveRegret_exploit))
    print("\n")

    # eGreedy
    print("eGreedy:")
    print("Optimum happiness " + str(Optimum_happiness))
    # Expected total happiness#
    temp = (1 - e) * 300
    left = int((300 - temp) / 3)
    Expected_total_happiness = int(H1 * left + H2 * left + H3 * left + temp * H2)
    print("Expected total happiness" + " " + str(Expected_total_happiness))
    # Expected_Regret
    Expected_Regret = Optimum_happiness - Expected_total_happiness
    print('Expected Regret ' + str(Expected_Regret))
    # ave happyiness
    print("Average happiness: " + str(AveHappy_eGreedy))
    # ave regret
    AveRegret_eGreedy = Optimum_happiness - AveHappy_eGreedy
    print("Average Regret： " + str(AveRegret_eGreedy))


Simluation(1000, 10)