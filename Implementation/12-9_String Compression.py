# 머릿속에서 문자를 1개씩부터 시작해서 끝까지 기준으로 나누고, 그 압축된 스트링을 리스트에 넣어서
# 그 중 가장 짧은 문자열을 추출하는 아이디어는 생각해냈는데, 코드로 구현하지 못하였다. 구글링한 코드
def solution(s):
    length = []
    result = ''
    
    if len(s) == 1:
        return 1
    
    for cut in range(1,len(s)//2 +1):
        count = 1
        tempStr = s[:cut]
        for i in range(cut, len(s),cut):
            if s[i:i+cut] == tempStr:
                count+=1
            else:
                if count == 1:
                    count =''
                result += str(count) + tempStr
                tempStr = s[i:i+cut]
                count = 1
        if count == 1:
            count = ''
        result +=str(count) + tempStr
        length.append(len(result))
        result = ''
    
    return min(length)

# 정규 표현식을 사용하는 방법
import re 
def solution(s):
    if len(s) == 1:
        return 1
    until_check = len(s)//2
    answer_list = []
    # 길이가 반을 넘어가면 무조건 길이가 달라지기 때문에 무의미
    for i in range(1,until_check+1):
        # re.sub () 형태중 하나
        checkList = re.sub('(\w{%i})' %i, '\g<1> ',s).split()
        '''
        "aabbaccc"가 있으면 i가 1일 때는
        "a a b b a c c c "로 바꾸고
        빈칸을 기준으로 리스트에 넣어준다는 뜻
        [a,a,b,b,a,c,c,c]
        i가 2일 때는 "aa bb ac cc "로 바꾸고
        빈칸을 기준으로 리스트에 넣어준다는 뜻
        [aa,bb,ac,cc]
        '''
        count = 1
        compress_str_list = []
        for j in range(len(checkList)):
            if j < len(checkList)-1 and checkList[j] == checkList[j+1]:
                count+=1
            else:
                if count == 1:
                    compress_str_list.append(checkList[j])
                else:
                    compress_str_list.append(str(count)+checkList[j])
                    count = 1
        answer_list.append(len(''.join(compress_str_list)))
    return min(answer_list)
