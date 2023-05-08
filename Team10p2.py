import random

def exploitOnly():
    C1 = random.normalvariate(10, 8)
    C2 = random.normalvariate(15, 6)
    C3 = random.normalvariate(12, 5)
    happiness= C1 + C2 + C3
    if max(C1, C2, C3) == C1:
        for i in range(297):
            happiness += random.normalvariate(10, 8)
    elif max(C1, C2, C3) == C2:
        for i in range(297):
            happiness += random.normalvariate(15, 6)
    else:
        if max(C1, C2, C3) == C3:
            for i in range(297):
                happiness += random.normalvariate(12, 5)
    return happiness

def exploreOnly():
    import random
    happy = 0
    for i in range(0, 100):
        happy += random.normalvariate(10, 8)
        happy += random.normalvariate(15, 6)
        happy += random.normalvariate(12, 5)
    return happy

def eGreedy(e:int):
    import random
    c1 = random.normalvariate(10,8)
    c2 = random.normalvariate(15,6)
    c3 = random.normalvariate(12,5)
    c1_list = []
    c2_list = []
    c3_list = []
    sum1 = c1
    sum2 = c2
    sum3 = c3


    for i in range(297):
        r = random.random()
        if (r*100<e):
            WhichOne = random.randint(1,3)
            if WhichOne == 1:
                c1_list.append(c1)
                c1 = random.normalvariate(10, 8)
                sum1 = sum(c1_list) / len(c1_list)
            elif WhichOne == 2:
                c2_list.append(c2)
                c2 = random.normalvariate(15, 6)
                sum2 = sum(c2_list) / len(c2_list)
            elif WhichOne == 3:
                c3_list.append(c3)
                c3 = random.normalvariate(12, 5)
                sum3 = sum(c3_list)/len(c3_list)
        else:
            WhichOne = max(sum1,sum2,sum3)
            if WhichOne == sum1:
                    c1_list.append(c1)
                    c1 = random.normalvariate(10, 8)
                    sum1 = sum(c1_list) / len(c1_list)

            elif WhichOne == sum2:
                    c2_list.append(c2)
                    c2 = random.normalvariate(15, 6)
                    sum2 = sum(c2_list) / len(c2_list)

            elif WhichOne == sum3:
                    c3_list.append(c3)
                    c3 = random.normalvariate(12, 5)
                    sum3 = sum(c3_list) / len(c3_list)

    best_n_days = 300-((e/100)*300)
    random_n_days = ((e/3)/100)*300
    total_happiness = (max(sum1,sum2,sum3)*best_n_days)+(sum1*random_n_days)+(sum2*random_n_days)+(sum3*random_n_days)
    return total_happiness
    


def simulation(t: int, e: int):
    oitind = 0
    Optimum_h = 300 * 21
    print("Optimum Happiness is " + str(Optimum_h))
    exploit = []
    exploit_tot = 0
    oit = exploitOnly()
    while oitind < t- 1:
        o = exploitOnly()
        exploit.append(o)
        oitind += 1
    for item in range(0, len(exploit)):
        exploit_tot = exploit_tot + exploit[item]
    avg_exploit = exploit_tot / len(exploit)
    exploit_reg = Optimum_h - oit
    avg_exploitr = Optimum_h - avg_exploit
    print("The average total happiness for exploitOnly for " + str(t) + " trials is " + str(avg_exploit))
    print("The total expected happiness for exploitOnly is " + str(oit))def eGreedy(e:int):
    import random
    c1 = random.normalvariate(10,8)
    c2 = random.normalvariate(15,6)
    c3 = random.normalvariate(12,5)
    c1_list = []
    c2_list = []
    c3_list = []
    sum1 = c1
    sum2 = c2
    sum3 = c3

    print("The total expected regret for exploitOnly is " + str(exploit_reg))
    print("The average total regret for exploitOnly for " + str(t) + " trials is " + str(avg_exploitr))
    oreind = 0
    explore = []
    explore_tot = 0
    ore = exploreOnly()
    while oreind < t - 1:
        o = exploreOnly()
        explore.append(o)
        oreind += 1
    for item in range(0, len(explore)):
        explore_tot = explore_tot + explore[item]
    avg_explore = explore_tot / len(explore)
    explore_reg = Optimum_h - ore
    avg_explorer = Optimum_h - avg_explore
    print("The average total happiness for exploreOnly for " + str(t) + " trials is " + str(avg_explore))
    print("The total expected happiness for exploreOnly is " + str(ore))
    print("The total expected regret for exploreOnly is " + str(explore_reg))
    print("The average total regret for exploreOnly for " + str(t) + " trials is " + str(avg_explorer))
    eedind = 0
    greed = []
    greed_tot = 0
    eed = eGreedy(e)
    while eedind < t - 1:
        o = eGreedy(e)
        greed.append(o)
        eedind += 1
    for item in range(0, len(greed)):
        greed_tot = greed_tot + greed[item]
    avg_greed = greed_tot / len(greed)
    greed_reg = Optimum_h - eed
    avg_greedr = Optimum_h - avg_greed
    print("The average total happiness for eGreedy for " + str(t) + " trials is " + str(avg_greed))
    print("The total expected happiness for eGreedy is " + str(eed))
    print("The total expected regret for eGreedy is " + str(greed_reg))
    print("The average total regret for eGreedy for " + str(t) + " trials is " + str(avg_greedr))
print(simulation(1000000, 10))
