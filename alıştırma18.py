from itertools import combinations
s,n = input().split()
for i in range(1,int(n)+1):
    print(*[''.join(i) for i in combinations(sorted(s),int(i))],sep='\n')