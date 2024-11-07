n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

tshirt_bundle = 0
pen_bundle = 0
pen_count = 0

for i in range(6):
    if (sizes[i]%t) == 0:
        tshirt_bundle += (sizes[i]//t)
    else:
        tshirt_bundle += (sizes[i]//t)
        tshirt_bundle += 1

pen_bundle = n // p
pen_count = n % p

print(tshirt_bundle)
print(pen_bundle, pen_count)