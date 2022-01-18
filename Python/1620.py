import sys
input = sys.stdin.readline
N, M = map(int,input().split())
PokemonList = []
PokeNum = {}
for i in range(N):
    a = input().rstrip()
    PokemonList.append(a)
    PokeNum[a] = i + 1
for _ in range(M):
    a = input().rstrip()
    if a.isdigit():
        print(PokemonList[int(a)-1])

    else:
        print(PokeNum[a])