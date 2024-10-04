n, m, k = map(int, input().split())
temp_array = input()
arr = list(map(int, temp_array.split()))

def solution(n, m, k, arr):
    answer = 0

    arr.sort(reverse = True)
    if max(arr) == arr[1]:
        answer = m*arr[0]
    else:
        answer += (m // (k+1)) * (k * arr[0] + arr[1])
        answer += (m % (k+1)) * arr[0]
    
    print(answer)
    

solution(n, m, k, arr)
