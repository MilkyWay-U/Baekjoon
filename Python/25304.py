sum = int(input())
value = 0
cnt = int(input())
for i in range(0,cnt):
	v, n = map(int,input().split())
	value = value + (v * n)
if value == sum:
	print("Yes")
else:
	print("No")