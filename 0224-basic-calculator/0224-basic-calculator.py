class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == '+':
                result += sign * number
                number = 0
                sign = 1

            elif ch == '-':
                result += sign * number
                number = 0
                sign = -1

            elif ch == '(':
                # Save the result and sign before entering parentheses
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif ch == ')':
                # Finish the current number/expression
                result += sign * number
                number = 0

                # Get the sign before '('
                sign = stack.pop()

                # Get the result before '('
                previous_result = stack.pop()

                result = previous_result + sign * result

        # Add the final number
        result += sign * number

        return result
        