"""
# 150
Medium
Evaluate Reverse Polish Notation

https://leetcode.com/problems/evaluate-reverse-polish-notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
* The valid operators are '+', '-', '*', and '/'.
* Each operand may be an integer or another expression.
* The division between two integers always truncates toward zero.
* There will not be any division by zero.
* The input represents a valid arithmetic expression in a reverse polish notation.
* The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
* 1 <= tokens.length <= 10^4
* tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""


def eval_rpn(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token not in ("+", "-", "*", "/"):
            stack.append(int(token))
        else:
            second = stack.pop()
            first = stack.pop()

            if token == "+":
                res = first + second

            elif token == "-":
                res = first - second

            elif token == "*":
                res = first * second

            elif token == "/":
                res = int(first / second)

            stack.append(res)

    return stack[0]


def eval_rpn(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token not in ("+", "-", "*", "/"):
            stack.append(int(token))
        else:
            fi = len(stack) - 2
            si = len(stack) - 1

            if token == "+":
                stack[fi] = stack[fi] + stack[si]

            elif token == "-":
                stack[fi] = stack[fi] - stack[si]

            elif token == "*":
                stack[fi] = stack[fi] * stack[si]

            elif token == "/":
                stack[fi] = int(stack[fi] / stack[si])

            stack.pop()

    return stack[0]


if __name__ == "__main__":
    assert eval_rpn(tokens=["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(tokens=["4", "13", "5", "/", "+"]) == 6
    assert (
        eval_rpn(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    )
