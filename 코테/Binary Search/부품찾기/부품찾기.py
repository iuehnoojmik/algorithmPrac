import sys
n = int(input())
objects = list(map(int, input().split()))
m = int(input())
items = list(map(int, sys.stdin.readline().rstrip().split()))

objects.sort()

def binary_search(target, start, end, array):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(target, start, mid-1, array)
    else:
        return binary_search(target, mid+1, end, array)

# # answer = []
# for item in items:
#     answer = binary_search(item, 0, n-1, objects)
#     if answer != None:
#         # answer.append('yes')
#         print('yes', end=" ")
#     else:
#         # answer.append('no')
#         print('no', end=" ")

for item in items:
    if binary_search(item, 0, n-1, objects) != None:
        print('yes', end=" ")
    else:
        print('no', end=" ")
    sys.stdout.flush()  # 강제 출력

# for i in answer:
#     print(i, end = " ")



