from typing import List
from infix_to_postfix import inpostfix


def evals(e: str):
  rl = []
  ops = ['-', '+', '*', '/']
  postfix = inpostfix(e)
  print(postfix)
  for c in postfix:
    if rl and c in ops:
      s = rl.pop()
      f = rl.pop()
      rl.append(eval(str(f) + c + str(s)))
      continue
    rl.append(c)
  return rl[-1]


def test_():
  assert evals("2+3*4") == 14
  assert evals("2*3+4/5*5") == 10
  assert evals("(2+3)*2") == 10