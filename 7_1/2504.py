bracket = input().rstrip()
if bracket[0] != '(' and bracket[0] != '[':
    print(0)
    exit(0)
stack = [bracket[0]]
result = ''
#스택하고 직전값을 참조
for i in range(1,len(bracket)):
    if bracket[i] == '(' or bracket[i] == '[':
        stack.append(bracket[i])
        if bracket[i-1] == '(' or bracket[i-1] == '[':
            result += '('
        else:
            result += '+'
    elif bracket[i] == ')':
        if not stack or stack.pop() != '(':
            print(0)
            exit(0)
        elif bracket[i-1] == ')' or bracket[i-1] ==']':
            result += ')*2'
        else:
            result += '2'
    elif bracket[i] == ']':
        if not stack or stack.pop() != '[':
            print(0)
            exit(0)
        elif bracket[i-1] == ')' or bracket[i-1] ==']':
            result += ')*3'
        else:
            result += '3'
    else:
        print(0)
        exit(0)
try:
    print(eval(result))
except:
    print(0)
