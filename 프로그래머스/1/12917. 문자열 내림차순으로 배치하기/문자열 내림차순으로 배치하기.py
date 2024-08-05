def solution(s):
    answer = ''
    stack = sorted(s)
    for a in stack[::-1]:
        answer += a
    return answer