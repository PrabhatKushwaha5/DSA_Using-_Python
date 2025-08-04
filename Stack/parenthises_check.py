def checkParenthises(s : str) -> bool:
    stack = []
    for ch in s:
        if ch in ['(','{','[']:
            stack.append(ch)
        else:
            if not stack:
                return False
            curr_ch = stack.pop()
            if curr_ch == '(':
                if ch != ')':
                    return False
            if curr_ch == '{':
                if ch != '}':
                    return False
            if curr_ch == '[':
                if ch != ']':
                    return False
    if stack:
        return False
    else:
        return True    
            
s = input()
if checkParenthises(s):
    print("Balanced")
else:
    print("Unbalanced")