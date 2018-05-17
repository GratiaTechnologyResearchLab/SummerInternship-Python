n = int(input())
arr=[]
temp=0
arr = [int(i) for i in input().split()]
for i in range(n):    
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
m=max(arr)
arr.remove(max(arr))
while(m in arr):
    if (m in arr):
        arr.remove(m)

print(arr[0])

