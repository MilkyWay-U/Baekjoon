lst = list(map(int,input().split()))

a = 0
b = 0
if lst == sorted(lst):
    print("ascending")
elif lst == sorted(lst, reverse = True):
    print("descending")
else:
    print("mixed")    