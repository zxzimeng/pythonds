from typing import List, Tuple
from math import isclose, nan
from random import randint

OPS = ["+", "-", "--", "*", "/", "//"]


# returns calculation result and its representation.
def calculate(operator, a, b) -> Tuple[float, str]:
    if a == 0 and operator == '//' or b == 0 and operator == '/':
        return nan, 'not a number'
    if operator != '--' and operator != '//':
        return eval(f"{a}{operator}{b}"), f"{a}{operator}{b}"

    return eval(f"{b}{operator[0]}{a}"), f"{b}{operator[0]}{a}"


def operateTwo(target, nums: List) -> Tuple[bool, str]:
    a, b = nums
    for op in OPS:
        value, expr = calculate(op, a, b)
        if isclose(value, target):
            return True, expr
    return False, ''


def getPossibleValues(a, b):
    valueList = []
    for op in OPS:
        value, expr = calculate(op, a, b)
        if value == nan:
            continue
        valueList.append(value)
    return valueList


def game(target: float, nums: List) -> str:
    if len(nums) == 2:
        result, expression = operateTwo(target, nums)
        if result:
            return expression
        else:
            return ''
    for i in range(len(nums)):
        valueList = getPossibleValues(target, nums[i])
        for x in valueList:
            result = game(x, nums[0:i] + nums[i + 1:])
            if result:
                found, expr = operateTwo(target, [x, nums[i]])
                if found:
                    return f"{result}={x:.2f}; {expr}"
    if len(nums) >= 4:
        for i in range(1, len(nums)):
            a = nums[0]
            b = nums[i]
            c, d = nums[1:i] + nums[i + 1:]
            group1 = getPossibleValues(a, b)
            group2 = getPossibleValues(c, d)
            for x in group1:
                for y in group2:
                    result, expression = operateTwo(target, [x, y])
                    if result:
                        _, exp1 = operateTwo(x, [a, b])
                        _, exp2 = operateTwo(y, [c, d])
                        return f"{exp1}={x} {exp2}={y} {expression}={target}"


def test_():
    testcase = [randint(1, 16) for i in range(4)]
    print(testcase)
    testcase = [11, 13, 7, 5]
    assert print(game(24, testcase)) == ''
