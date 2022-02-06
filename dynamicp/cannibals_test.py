from __future__ import annotations
from typing import List
from queue import SimpleQueue

class States:
    def __init__(self) -> None:
        # |             |
        # |             |
        # |L(0)     R(1)|
        # |             |
        # |             |

        self.l_cannibals = 0
        self.l_missionaries = 0
        self.r_cannibals = 3
        self.r_missionaries = 3

        # 0 == Left Side 
        # 1 == Right Side
        self.boat_right = True

        self.path = []
    
    def clone(self):
        s = States()
        s.l_cannibals = self.l_cannibals
        s.l_missionaries = self.l_missionaries
        s.r_cannibals = self.r_cannibals
        s.r_missionaries = self.r_missionaries
        s.boat_right = self.boat_right
        s.path = self.path
        return s

    def key(self):
        #(Left(Cannibals, Missionaries), Right(Cannibals, Missionaries), Boat Pos)
        #((0, 1),(1, 1), False) == 0 Cannibals on Left Side, 1 Missionary on Left Side, Boat is on Left Side
        #                      == 1 Cannibals on Right Side, 1 Missionary on Right Side
        return ((self.l_cannibals, self.l_missionaries),(self.r_cannibals, self.r_missionaries), self.boat_right)

    def __str__(self) -> str:
        return self.key().__repr__()

    def __repr__(self) -> str:
        return self.key().__repr__()

    def isterminal(self) -> bool:
        return self.l_cannibals == 3 and self.l_missionaries == 3

    def isvalid(self) -> bool:
        # People on both sides are not negitive
        if self.l_cannibals < 0 or self.r_cannibals < 0 or self.l_missionaries < 0 or self.r_missionaries < 0:
            return False
        
        # Cannibals outnumber missionaries on either bank
        if self.l_cannibals > self.l_missionaries and self.r_missionaries != 0 and self.l_missionaries != 0:
            return False
        if self.r_cannibals > self.r_missionaries and self.r_missionaries != 0 and self.l_missionaries != 0:
            return False

        return True

    def next(self) -> List[States]:
        nextStates = []

        # Boat is R(1)
        # Two Missionaries <-
        # Two Cannibals <-
        # One Missionary <-
        # One Cannibal <-
        # One Missionary One Cannibal <-

        deltas = [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)]
        
        for delta in deltas:
            s = self.clone()
            if s.boat_right:
                s.l_cannibals += delta[0]
                s.r_cannibals -= delta[0]
                s.l_missionaries += delta[1]
                s.r_missionaries -= delta[1]
                s.boat_right = False

            else:
                s.l_cannibals -= delta[0]
                s.r_cannibals += delta[0]
                s.l_missionaries -= delta[1]
                s.r_missionaries += delta[1]
                s.boat_right = True
            
            s.path = self.path[:] + [self.key()]
            # print(f'{self.key()} => {s.key()}')
            nextStates.append(s)

        return nextStates


class Solution:
    def cannibals_river(self):
        seen = set()
        s = States()
        seen.add(s.key())
        pending = SimpleQueue()
        pending.put(s)

        while pending:
            p = pending.get()
            if p in seen:
                continue
            moves = p.next()
            for m in moves:
                if not m.isvalid():
                    continue
                if m.key() in seen:
                   continue
                seen.add(m.key())
                pending.put(m)
                if m.isterminal():
                    return m.path + [m.key()]
            

def draw_cannibals(keys) -> None:
    #(Left(Cannibals, Missionaries), Right(Cannibals, Missionaries), Boat Pos)
    #((0, 1),(1, 1), False) == 0 Cannibals on Left Side, 1 Missionary on Left Side, Boat is on Left Side
    #                      == 1 Cannibals on Right Side, 1 Missionary on Right Side

    print(f"""
        X = Cannibals
        O = Misisonaries
        """)
    round = 1
    for i in keys:
        m = i[0:2]
        addcl = m[0][0] > 0
        addml = m[0][1] > 0
        addcr = m[1][0] > 0
        addmr = m[1][1] > 0

        print(f"""
        Round {round}:

         {m[0][0]*'X'} {m[0][1]*'O'} 
        {10*'-'}
         {m[1][0]*'X'} {m[1][1]*'O'} 
        """)
        round += 1
            




def test__():
    solution = Solution()
    assert solution.cannibals_river() == 4

if __name__ == '__main__':
    solution = Solution()
    print(solution.cannibals_river())
    draw_cannibals(solution.cannibals_river())