from collections import deque
def solution(n, words):

    checked_queue = deque()
    words_queue = deque(words)
    word = words_queue.popleft()
    checked_queue.append(word)
    last = word[-1]
    num, order = 0, 0
    
    for i in range(1, len(words)):
        word = words_queue.popleft()
        
        if word in checked_queue or word[0] != last:
            num = (i%n) + 1
            order = (i//n) + 1
            break
        last = word[-1]
        checked_queue.append(word)
        
    answer = [num, order]

    return answer