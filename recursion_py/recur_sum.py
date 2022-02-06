from typing import List


def recurSum(x: List) -> int:
  if len(x) == 1:
    return x[0]
  return x[0] + recurSum(x[1:])


stk = []


def recurSumStk(x: List) -> int:
  for n in x:
    stk.append(n)
  while len(stk) != 1:
    stk.append(stk.pop() + stk.pop())
  return stk[0]


def test_():
  assert recurSumStk([1, 2, 3, 4, 5, 3, 4]) == 18
