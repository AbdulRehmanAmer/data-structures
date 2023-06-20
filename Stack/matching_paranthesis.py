from Array_Stack import *

def is_correct_paranthesis(expression):
    stack = ArrayStack(len(expression))
    opening, closed = "({[", ")}]"
    for ch in expression:
        if ch in closed:
            if stack.is_Empty(): return False
            # b1 means opening bracket
            # b2 means required closing bracket
            b1 = stack.pop()
            b2 = determine_closing_bracket(b1)
            if b2 != ch:
                return False
        elif ch in opening:
            stack.push(ch)
    
    return True if stack.is_Empty() else False
            
    
def determine_closing_bracket(b):
    brackets = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    return brackets[b]
    
if __name__ == "__main__":
    expression = "( )(( )){([( )])}"# correct
    expression = "((( )(( )){([( )])}))"# correct
    expression = ")(( )){([( )])}"# incorrect
    expression = "({[])}"# incorrect
    expression = "("# incorrect
    
    result = is_correct_paranthesis(expression)
    print (result)