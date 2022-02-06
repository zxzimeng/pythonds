from math import factorial
from math import floor
from typing import List

class Solution():
    def findPerms(self, n: int, r: int) -> int:
        if n-r < 0:
            return 1
        return int(factorial(n)/(factorial(r) * factorial(n-r)))

    def printPascal(self, row: int):
        for i in range(row):
            print(' '*(row-i), end='')
            self.printRow(i)

    def printRow(self, row : int):
        for i in range(row):
            print(self.findPerms(row, i), end=' ')
        print()
            


solution = Solution()
solution.printPascal(5)
