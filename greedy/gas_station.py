"""
    There are n gas stations along a circular route. You are given two integer arrays gas and cost where:
    - gas[i] is the amount of gas at the ith station.
    - cost[i] is the amount of gas needed to travel from the ith station to the (i + 1)th station. (The last station is connected to the first station)
    - You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.
    Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return -1.
    It's guaranteed that at most one solution exists.

    The idea behind this is pretty intuitive: in order to be feasible,
    the sum of the gas should be higher than the sum of the cost, otherwise
    we have to return -1. Once we check this, we're sure there exist a 
    solution, and we are guaranteed by the text it's only one.

    let's start from pos zero and compute our total, if we ever get to
    a total that is negative, it means that starting point was not correct
    and we can move to the next one. We do not need to do a complete circle,
    we already demonstrated there exist a solution.
"""


from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res, tot = 0, 0

        for n in range(len(gas)):
            tot += (gas[n]-cost[n])
            if tot < 0:
                tot = 0
                res = n + 1

        return res