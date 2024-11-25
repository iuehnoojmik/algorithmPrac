n, m = map(int, input().split())
lengths = list(map(int, input().split()))

result = 0
def binary(start, end, array):
    global result # 함수 내부에서 전역 변수 result를 사용하도록 명시
    while start <= end:
        mid = (start + end) // 2

        length = 0
        for i in range(n):
            if array[i] <= mid:
                continue
            else:
                length += (array[i] - mid)
        
        if length < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return None

# print(binary(min(lengths), max(lengths), lengths))
binary(0, max(lengths), lengths)
print(result)
