# 시간 초과다... 못 풀었다.
# 문제에서 출력하는 방식을 제대로 이해못해서 내가 생각한 대로 풀었다.
# 내가 푼 방법,,다시 풀어봐야겠다

def dfs(string,left_length,real_answer):
    check_dfs=False
    checkEnd = False
    answer= ''
    add=''
    pre=''
    countA = 0
    countB = 0
    for idx,i in enumerate(string):
        if i==")":
            add+=i
            countA=countA+1
            if(countA == countB):
                checkEnd = True
        else:
            countB=countB+1
            pre+=i
            if(countB==countA):
                answer+=(pre+add)
                left_length -= idx
                if(left_length!=1):
                    real_answer += answer
                    check_dfs = True
                    return dfs(string[left_length+1:],left_length,real_answer)
                    # return answer+= dfs(string[left_length+1:],left_length,real_answer)
                    
    if(checkEnd == False and check_dfs == False): 
        real_answer+=answer
        return real_answer
    elif (checkEnd == True and check_dfs ==False):
        answer += pre+add
        real_answer += answer
        return real_answer
    else:
        return real_answer
            
def solution(p):
    answer = ''
    check = True
    if p =='':
        return ''
    stack = []
    cnt = 0
    for i in p:
        cnt +=1
        if(i=='('):
            stack.append(i)
            answer+=i
        else:
            if(len(stack)!=0):
                answer+=i
                stack.pop()
            else:
                # answer+=i
                check = False
                break
    if cnt == len(p):
        return p
    else:
        left_length= len(p[cnt-1:])
        real_answer=''
        if(left_length == len(p)):
            return dfs(p[cnt-1:],left_length,real_answer)+answer
        elif(answer[0]=="("):
            return answer+dfs(p[cnt-1:],left_length,real_answer)
        elif(answer[0]==")"):
            real_answer = ''
            return dfs(p[cnt-1:],left_length,real_answer)+answer
        
 ###########################################################################################################################################################
# 답지 풀이
def balanced_index(p):
    left_count = 0 # 왼쪽 괄호 개수
    for i in range(len(p)):
        if(p[i]=="("):
            left_count+=1
        else:
            left_count -=1
        if left_count == 0:
            return i
            
# 올바른 괄호 문자열인지 판단
def check_proper(p):
    left_count = 0 # 왼쪽 괄호 개수
    for i in p:
        if i=='(':
            left_count+=1
        else:
            if left_count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            left_count-=1
    return True

def solution(p):
    answer =''
    if p =='':
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    
    # 올바른 괄호 문자열이면
    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면
    else:
        answer='('
        answer+=solution(v)
        answer+=')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자 제거
        for i in range(len(u)):
            if(u[i]=='('):
                u[i]=')'
            else:
                u[i]='('
        answer+="".join(u)
    return answer
