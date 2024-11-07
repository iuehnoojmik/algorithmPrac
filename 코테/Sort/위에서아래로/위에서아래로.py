n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

# 퀵정렬
def quick_sort(list):
    if len(list)<=1:
        return list
    
    pivot = list[0]
    tail = list[1:]

    right = [x for x in tail if x<= pivot]
    left = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(list))
