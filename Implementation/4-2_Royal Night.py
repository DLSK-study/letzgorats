# 내가 푼 방법(무지성)
import sys
input = sys.stdin.readline

position = input()

col = position[0]  # 열
row = int(position[1])  # 행

if(3 <= row and row <= 6):
    if('c' <= col and col <= 'f'):
        print(8)
    elif (col == 'b' or col == 'g'):
        print(6)
    else:
        print(4)
elif(row == 2 or row == 7):
    if('c' <= col and col <= 'f'):
        print(6)
    elif (col == 'b' or col == 'g'):
        print(4)
    else:
        print(3)
elif(row == 1 or row == 8):
    if('c' <= col and col <= 'f'):
        print(4)
    elif (col == 'b' or col == 'g'):
        print(3)
    else:
        print(2)
        
 
