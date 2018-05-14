from itertools import combinations
n=int(input())
s=input().split()
m=int(input())
count=0
arr=list(combinations(s,m))
for i in range(len(arr)):
    if 'a' in arr[i]:
        count+=1
print(count/len(arr))
