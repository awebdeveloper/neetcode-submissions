
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }
        
        stack = []

        for ele in tokens:
            if ele in operations:
                right = stack.pop()
                left = stack.pop()
                result = operations[ele](left, right)
                stack.append(result)
            else:
                stack.append(int(ele))

        return stack[0]


        