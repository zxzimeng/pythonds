def palindrome(x: str):

  if x == '':
    return True
  if x[0] == x[-1]:
    return palindrome(x[1:-1])
  else:
    print(x)
    return False


def palindromeStk(x: str):
  while x:
    if x[0] == x[-1]:
      x = x[1:-1]
    else:
      return False
  return True


def test_():
  x = 'Reviled did I live, said I, as evil I did deliver'
  x = x.lower()
  x = x.replace(' ', '')
  x = x.replace(',', '')
  print(x[::-1] == x)
  assert palindromeStk(x) == True