import sys
input = sys.stdin.readline

n = int(input())
number_list = []
for i in range(n):
    number_list.append(int(input()))
number_list = sorted(number_list,reverse=True)
print(*number_list)
