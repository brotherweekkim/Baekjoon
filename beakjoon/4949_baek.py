while True:
    text = input()
    if text == '.':
        break
    string_stack = []
    answer = 'yes'
    for i in text:
        if i == "(":
            string_stack.append(i)
        elif i == "[":
            string_stack.append(i)
        elif i == ")":
            if len(string_stack) == 0 or string_stack.pop() != "(":
                answer = 'no'
                break
        elif i == "]":
            if len(string_stack) == 0 or string_stack.pop() != "[":
                answer = 'no'
                break
    if answer == 'yes' and len(string_stack) == 0:
        print('yes')
    else:
        print('no')
    