def solution(numbers, hand):
    answer = ''
    phone = {1: (0,0), 2: (0,1), 3: (0,2),
             4: (1,0), 5: (1,1), 6: (1,2),
             7: (2,0), 8: (2,1), 9: (2,2),
             '*': (3,0), 0: (3,1), '#': (3,2)}
    left_hand = '*'
    right_hand = '#'
    for number in numbers:
        
        if number in [1,4,7]:
            left_hand = number
            answer += 'L'
            continue
        elif number in [3,6,9]:
            right_hand = number
            answer += 'R'
            continue
        
        ld = abs(phone[number][0] - phone[left_hand][0]) + abs(phone[number][1] - phone[left_hand][1])
        
        rd = abs(phone[number][0] - phone[right_hand][0]) + abs(phone[number][1] - phone[right_hand][1])
        
        if ld > rd:
            right_hand = number
            answer += 'R'
            continue
        elif ld < rd:
            left_hand = number
            answer += 'L'
            continue
        if hand == 'right':
            right_hand = number
            answer += 'R'
            continue
        else:
            left_hand = number
            answer += 'L'
            continue
    return answer