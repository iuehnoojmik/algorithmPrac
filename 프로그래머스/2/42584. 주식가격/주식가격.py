# from collections import deque

def solution(prices):
    # price_queue = deque(prices)
    length = len(prices)
    answer = [0] * length
    #answer_queue = deque()
    
    for i in range(length):
        for j in range(i+1, length):
            if prices[j] >= prices[i]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    
    return answer