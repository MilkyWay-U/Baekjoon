a, b = map(int,input().split())
lst = list(map(int,input().split()))
for i in range(a - 1):
	for j in range(i + 1, a):
		if lst[i] < lst[j]:
			k = lst[i]
			lst[i] = lst[j]
			lst[j] = k
print(lst[b - 1])