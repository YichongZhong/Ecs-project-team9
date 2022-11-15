import random


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
