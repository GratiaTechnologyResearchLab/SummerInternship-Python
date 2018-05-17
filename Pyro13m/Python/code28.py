x = input()
l = list(map(int, input().split()))
sum = 0
for i in range(int(input())):
    c,s=input().split()
    for j in range(len(l)):
        if int(c)==l[j]:
            sum=sum+int(s)
            l.remove(l[j])
            break
print(sum)

