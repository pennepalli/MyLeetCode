#!/usr/bin/python3

import sys

def twoCitySchedCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    print(costs)
    acosts = [cost[0] for cost in costs]
    acosts.sort()
    print(acosts)
    bcosts = [cost[1] for cost in costs]
    bcosts.sort()
    print(bcosts)
    print("\n\n")
    return 0
 
if __name__ == "__main__":

    costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    ret = twoCitySchedCost(costs)
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    ret = twoCitySchedCost(costs)
    costs = [[10,20],[30,200],[400,50],[30,20]]
    ret = twoCitySchedCost(costs)
    print (ret)


