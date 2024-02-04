# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        valid_operators = {"+", "-", "*", "/"}

        for idx in range(len(tokens)):
            if tokens[idx] in valid_operators:
                right_operand = st.pop()
                left_operand = st.pop()
                result = 0
                if tokens[idx] == "*":
                    result = left_operand * right_operand
                elif tokens[idx] == "/":
                    result = int(left_operand / right_operand)
                elif tokens[idx] == "+":
                    result = left_operand + right_operand
                elif tokens[idx] == "-":
                    result = left_operand - right_operand
                st.append(result)
            else:
                st.append(int(tokens[idx]))
        return st.pop()
