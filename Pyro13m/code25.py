n,m=input().split()
arr=input().split()
A=set(input().split())
B=set(input().split())
h=0
for i in arr:
	if i in A:
		h+=1
	elif i in B:
		h-=1
print(h)
