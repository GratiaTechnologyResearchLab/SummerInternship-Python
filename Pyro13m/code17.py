import os
import sys

def miniMaxSum(arr):
    b=max(arr)
    a=min(arr)
    arr.remove(min(arr))
    smax=sum(arr)
    arr.remove(max(arr))
    smin=sum(arr)+a
    print(smin,smax)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

