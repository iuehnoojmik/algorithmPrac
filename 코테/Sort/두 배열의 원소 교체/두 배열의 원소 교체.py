n, k = map(int, input().split())

# 배열 a와 b 입력 받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순, b는 내림차순 정렬
a.sort()
b.sort(reverse=True)

for i in range(k):
    # a가 b보다 작을 때에만 swap
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    # a가 b보다 크면 swap 반복문 탈출
    else:
        break

# a의 합 출력
print(sum(a))
