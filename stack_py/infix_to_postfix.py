import re


def inpostfix(s: str):
  equation = re.findall(re.compile('(\d+|[^ 0-9])'), s)
  rlist = []
  opStk = []
  ops = ['-', '+', '*', '/']
  opM = ['*', '/']
  opA = ['-', '+']
  for c in equation:
    if c == "(":
      opStk.append(c)
      continue
    elif rlist and c in ops:  #if cur is op
      while c in opM and opStk and opStk[
          -1] in opM:  #if cur is mult and prev is mult
        rlist.append(opStk.pop())
      while c in opA and opStk and opStk[
          -1] in opM:  #if prev is mult and cur is add
        rlist.append(opStk.pop())
      while c in opA and opStk and opStk[-1] in opA:  #if cur is add prev is add
        rlist.append(opStk.pop())
      opStk.append(c)
      print(opStk, rlist)
      continue
    elif c == ")":
      # print(opStk)
      while rlist[-1] != "(":
        rlist.append(opStk.pop())
      rlist.pop()
    else:
      rlist.append(c)

  while opStk:
    rlist.append(opStk.pop())
  return "".join(rlist)


def test_():
  assert inpostfix("A+B*C") == "ABC*+"
  assert inpostfix("A*B+C/D*I") == "AB*CD/I*+"
  assert inpostfix("(A+B)*J") == "AB+J*"
  assert inpostfix("") == ""