
"""
어쩐지 쉽다 했더니 시간 신경써야 했다.
문제 : 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램
주의사항 : 
  단계를 그대로 따르면 안됨. strip(.)이 마지막에 더 있어야 함.\
풀이시간 : 40분

best 코드 보고 배운점: 정규식을 익히자!! 쩐다!
정규식 참고 링크 : https://wikidocs.net/4308
"""

# Best 풀이
import re

def solution(new_id):
    st = new_id 
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st) # '^' : 반대  '\': 하이푼 문자 취급
    st = re.sub('\.+', '.', st)  # '+': 반복
    st = re.sub('^[.]|[.]$', '', st) # '^[]':문자의 처음 '[]$':문자의 마지막
    st = 'a' if len(st) == 0 else st[:15] # 5, 6단계 한번에 
    st = re.sub('^[.]|[.]$', '', st) # strip 한번 더 
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

# 두번째 시도 : (변경사항) not in 대신 if문으로 범위
def solution(new_id):
    answer = new_id.lower() # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    new_ch = ""
    for ch in answer: 
        ord_ch = ord(ch)
        if (ord_ch >= 97) and (ord_ch <= 122) : new_ch += ch
        elif (ord_ch >= 48) and (ord_ch <= 57) : new_ch += ch           
        elif (ord_ch == 45) or (ord_ch == 95): new_ch += ch
        elif (ord_ch == 46) : 
            new_ch += ch
            
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.        
    while new_ch.find('..') != -1 : 
        new_ch = new_ch.replace('..', '.')   
        
    #4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    answer = new_ch.strip('.')
    
    #5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if answer == "" : 
        answer = 'a'
        
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    answer = answer[:15].strip('.')
    
    #7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(answer) <= 2:
        answer += answer[-1]
        
        
    return answer


# 처음 시도 결과 - 10초를 넘어가는 연산 시간
def solution(new_id):
    answer = new_id.lower() # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    new_ch = ""
    for ch in answer: 
        if ord(ch) not in range(97,123): continue
        elif ord(ch) not in range(48,57): continue  
        elif ch not in ['-', '_', '.']: continue          
        new_ch += ch
        
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.        
    
    while new_ch.find('..') != -1 : 
        new_ch = new_ch.replace('..', '.')   
        
    #4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    answer = new_ch.strip('.')
    
    #5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if answer == "" : 
        answer = 'a'
        
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    answer = answer[:15]
    
    #7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(answer) <= 2:
        answer += answer[:-1]
        
        
    return answer
