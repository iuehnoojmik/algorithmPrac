n, m = map(int,input().split())
arr = []
minimums = []

for i in range(n):
    temp = input()
    arr = list(map(int, temp.split()))
    minimums.append(min(arr))

answer = max(minimums)
print(answer)
