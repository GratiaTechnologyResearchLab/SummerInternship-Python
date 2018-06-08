i=0
string=input()
max_width=int(input())
while i<len(string):
    if  (len(string)-i)>max_width:
        print(string[i:i+max_width])
        i=i+max_width
    if (len(string)-i)<=max_width:
        print(string[i:])
        i=i+(len(string)-i)

        
