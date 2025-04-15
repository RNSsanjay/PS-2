class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)  # Truncate toward zero
        }
        
        for token in tokens:
            if token in operators:
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))
        
        return stack[0]
