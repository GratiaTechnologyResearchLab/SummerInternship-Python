arr=["False", "False", "False", "False", "False"]
st=input()
for i in st:
    if i.isalnum():
        arr[0] = "True"
    if i.isalpha():
        arr[1] = "True"
    if i.isdigit():
        arr[2] = "True"
    if i.islower():
        arr[3] = "True"
    if i.isupper():
        arr[4] = "True"
print(*arr, sep="\n")
