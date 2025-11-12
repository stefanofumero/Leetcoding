"""
You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.
You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.
Return true if it's possible to rearrange the cards in this way, otherwise, return false.

There are two main ways of solving this problem:
1. Ordering the array;
2. Using an heap.

In both cases, an hashmap is required to keep track of repeating elements.
"""
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def isNStraightHand_ordering(self,hand:List[int],groupSize:int)->bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort() #sorting in increasing order, done in-place
        #also here we need a counter to keep track of how many times we took an element
        cnt = defaultdict(int)

        for n in hand:
            cnt[n] += 1

        for num in hand:
            if cnt[num]:
                for i in range(num,num+groupSize):
                    if i not in cnt or cnt[i] == 0:
                        return False
                    cnt[i] -= 1
        return True
    
    def isNStraightHand_ordering(self,hand:List[int],groupSize:int)->bool:
        if len(hand) % groupSize != 0:
            return False
        
        cnt = defaultdict(int)
        for card in hand:
            cnt[card] += 1
        min_heap = list(cnt.keys()) #the heap here should contain only distinct elements
        heapq.heapify(min_heap) #heapq-heapify modifies the list in place
        
        while min_heap:
            first = min_heap[0]
            for i in range(first,first+groupSize):
                if i not in cnt:
                    return False
                cnt[i] -= 1
                if cnt[i] == 0:
                    if i != min_heap[0]: #if it's not the smallest, it means you finished a 'bridge' number for the next group
                        return False
                    heapq.heappop(min_heap)
        return True   