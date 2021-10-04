import sys
input = sys.stdin.readline

n = int(input())
pattern = input().rstrip()
for i in range(n):
    name = input().rstrip()
    if name[0] == pattern[0]:
        left = pattern.split("*")[0]  # '*'기준으로 나누기
        right = pattern.split("*")[1]
        name = name.replace(left,"")
        if name == right:  # 남은 name이 right와 같다면 YES
            print("DA")
        elif right not in name[1:]:   # right 덩어리가 name에 포함되어 있지 않다면 NO
            print("NE")
        else:  
            idx = -1
            flag = True
            for i in right[::-1]:  # name은 반드시 right로 끝나야 하니까 그 작업을 해줌
                if i == name[idx]:
                    idx -= 1
                else:
                    print("NE")
                    flag = False
                    break
            if flag == True:
                print("DA")
    else:
        print("NE")
