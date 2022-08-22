def solution(survey, choices):
    answer = ''
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    # RT, CF, JM, AN
    for i in range(len(survey)):
        if choices[i] > 4:
            scores[survey[i][1]] += abs(choices[i] - 4)
        else:
            scores[survey[i][0]] += abs(choices[i] - 4)
    answer += 'R' if scores['R'] >= scores['T'] else 'T'
    answer += 'C' if scores['C'] >= scores['F'] else 'F'
    answer += 'J' if scores['J'] >= scores['M'] else 'M'
    answer += 'A' if scores['A'] >= scores['N'] else 'N'
    return answer