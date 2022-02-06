from __future__ import annotations
from typing import Deque, List, Tuple
from queue import SimpleQueue

class State:
    def __init__(self, water1, water2) -> None:
        self.water1 = 0
        self.water2 = 0
        self.water1cap = water1
        self.water2cap = water2
        self.path = []
        
    def key(self):
        return (self.water1, self.water2)

    def clone(self) -> State:
        s = State(self.water1cap, self.water2cap)
        s.water1 = self.water1
        s.water2 = self.water2
        return s

    def pour(self, waterfrom, waterto, watertocap) -> Tuple[int, int]:        
        nextwaterfrom = 0
        nextwaterto = 0
        if waterfrom >= watertocap-waterto:
            nextwaterfrom = waterfrom+waterto-watertocap
            nextwaterto = watertocap
        else:
            nextwaterfrom=0
            nextwaterto=waterfrom+waterto
        return (nextwaterfrom, nextwaterto)

            
        pass

    def next(self) -> List[State]:
        result = []
        
        # 1->2
        s = self.clone()
        s.water1, s.water2 = self.pour(self.water1, self.water2, self.water2cap)
        result.append(s)

        #2->1
        s = self.clone()
        s.water2, s.water1 = self.pour(self.water2, self.water1, self.water1cap)
        result.append(s)

        #1->
        s = self.clone()
        s.water1 = 0    
        result.append(s)

        #2->
        s = self.clone()
        s.water2 = 0
        result.append(s)

        # ->1
        s = self.clone()
        s.water1 = self.water1cap
        result.append(s)

        # ->2
        s = self.clone()
        s.water2 = self.water2cap
        result.append(s)

        return result 
        
class Solution:
    def __init__(self) -> None:
        pass

    def find_operations(water1cap, water2cap):
        graph = dict()
        s = State(water1cap, water2cap)
        graph[(s.water1, s.water2)] = s
        pending = SimpleQueue()
        pending.put(s)

        while pending:
            p = pending.get()
            if p in graph.keys():
                continue
            moves = p.next()
            for m in moves:
                if m.key() in graph.keys():
                   continue
                m.path = p.path[:] + [m.key()]
                pending.put(m)
                if m.water2 == 27:
                    return m.path 

def test__():
    solution = Solution
    # water1cap, water2cap, target, which/what water to reach target
    assert solution.find_operations(31, 29) == 4