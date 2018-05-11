#Python Introduction Hackerrank

#1

if __name__ == '__main__':
    n = int(input())
    
for i in range(1,n+1):
    print(i, end="")


#2

def is_leap(year):
    leap = False
        # Write your logic here
    if year%4==0:
        leap=True
        if year%100==0 and year%400!=0:
            leap=False
          
    return leap



#3

if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i**2)



#4

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/float(b))




#5

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)






#6

if __name__ == '__main__':
    n = int(input())
if n%2!=0:
    print("Weird")
else:
    if (n>=2 and n<=5) or (n>20):
        print("Not Weird")
    else:
        print("Weird")


#7

if __name__ == '__main__':
    print "Hello, World!"



