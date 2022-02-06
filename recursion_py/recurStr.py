import timeit
import random

deximalDict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def convertHex(num: int):
  if num < 10:
    return str(num)
  if num > 9 and num < 16:
    return deximalDict[num]
  return convertHex(num // 16) + convertHex(num % 16)


def test_():
  for i in range(10000):
    a = random.randint(0, 100000)
    assert '0x' + convertHex(a).lower() == hex(a)
    print(a)
