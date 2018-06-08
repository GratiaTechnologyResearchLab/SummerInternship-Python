import os
import sys


def plusMinus(arr):
    counta=0
    countb=0
    countc=0
    for i in range(n):
        if arr[i]>0:
            counta=counta+1
        elif arr[i]==0:
            countb=countb+1
        else:
            countc=countc+1
    print(counta/float(n))
    print(countc/float(n))
    print(countb/float(n))
            
            
            
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

