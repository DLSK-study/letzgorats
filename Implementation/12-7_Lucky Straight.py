import sys
input = sys.stdin.readline

str = input().rstrip()
# 짝수인 길이만 주어지므로 길이를 반으로 나눔
half = len(str)//2
str_front = str[:half]
str_back = str[half:]
front_sum = 0 # 앞
back_sum = 0 # 뒤

for num in str_front:
    front_sum += int(num)
for num in str_back:
    back_sum += int(num)

if front_sum == back_sum:
    print("LUCKY")
else:
    print("READY")
