# Solution with stack and with O(n) time complexity
def evalRPN(self, tokens) :
    operators = {
        "+" : "+",
        "-": "-",
        "*": "*",
        "/": "//"
    }

    stack = list()
    for x in tokens:
        if x not in operators:
            stack.append(int(x))
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            if x == "+":
                stack.append( n1 + n2 )
            elif x == "-":
                stack.append( n1 - n2 )
            elif x == "*":
                stack.append( n1 * n2 )
            else:
                ans = n1 / n2
                stack.append( int(ans) )


    return stack[0]
