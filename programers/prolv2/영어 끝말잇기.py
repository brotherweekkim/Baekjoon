def solution(n, words):
    members = {}
    answer = []
    for i in range(1, n + 1):
        members[i] = []
    passed_word = []
    
    for i, word in enumerate(words):
        member = (i + 1) % n if (i + 1) % n else n
        pre_member = i % n if i % n else n
        members[member].append(word)
        
        if word in passed_word:
            answer.append(member)
            answer.append(len(members[member]))
            break
        
        passed_word.append(word)

        if members[pre_member] == []:
            continue
        
        if members[pre_member][-1][-1] != members[member][-1][0]:
            answer.append(member)
            answer.append(len(members[member]))
            break
            
        
    else:
        return [0, 0]
    return answer