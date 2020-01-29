n, h = input().split(" ")
a = input().split(" ")

result = 0

for i in range(int(n)):
    if int(a[i]) <= int(h):
        result += 1
    else:
        result += 2

print(result)
