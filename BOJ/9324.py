# 진짜 메시지
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    count_list = {}
    result = True
    message = input().rstrip()
    for idx,ch in enumerate(message):
        if ch in count_list:
            count_list[ch] += 1
            if(count_list[ch]==3):  # 3번 나왔으면
                if(idx==len(message)-1 or ch != message[idx+1]): # idx가 맨 끝이거나, 다음문자가 해당문자랑 같지 않으면
                    print("FAKE")   
                    result = False
                    break  # 빠져나온다
                else:
                    count_list[ch] = -1
        else:
            count_list[ch] = 1
    if result == True:   # result 값이 True면 FAKE 가 아니므로
        print("OK")
