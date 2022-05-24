"""
시간 : 100분

- 알고리즘이 다 나와잇어서 어렵지는 않으나,
함수를 여러개 재귀적으로 사용하다 보니 틀린 곳 찾느라 오래 걸렸다.

+ a = b 하면 얕은 복사... pop 하면 다 사라짐... 주의..

Best 풀이:
- (list(map(lambda x:'(' if x==')' else ')',p[1:i])
- .map이나 .join을 잘알아주지
"""

import copy
def _split_balance(w):
    #2. 문자열을 균형 잡힌 괄호 문자열 두 개 u,v로 분리
    c = 0
    u = []
    while len(w) : 
        a = w.pop(0)
        u.append(a)
        if a == '(':
            c += 1
        else : 
            c -= 1
        
        if c == 0: 
            break
    v = w
    return u,v

def _judge_(u):
    dum = copy.deepcopy(u)
    #3. u가 "올바른 괄호 문자열"?
    while len(dum) :
        if dum.pop(0) == '(':     
            try: 
                i = dum.index(')')
            except: 
                return False      
            dum.pop(i)
        else: 
            return False
    return True

def _flip(u):
    # 나머지 문자열의 괄호 방향을 뒤집
    new_u = []
    for a in u:
        if a == "(": 
            new_u.append(')')
        else: 
            new_u.append('(')
    
    return new_u
    
def _Find_(w):
    temp = []
    #1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if len(w) == 0: return w
    #print(w)
    #2. 문자열을 균형 잡힌 괄호 문자열 두 개 u,v로 분리
    u, v = _split_balance(w)
    #print(u, v)
    
    if _judge_(u):
        #3. u가 "올바른 괄호 문자열 이라면 문자열 v에 대해 1단계부터 다시 수행
        temp.extend(u)
        #t = 
        #if not len(t) :
        temp.extend(_Find_(v))
        #print(temp)
    else : 
        #4. u가 "올바른 괄호 문자열이 아니라면
        temp.extend('(') 
        temp.extend(_Find_(v))
        temp.extend(')')        
        temp.extend(_flip(u[1:-1]))
    #print("u, v", u, v)
    #print(">> temp", temp)    
    return temp

def solution(p):
    P = list(p)
    R = _Find_(P)
    #print(R)
    if len(R) :
        A = "".join(R)  
    else:
        A = ""
        
    return A # "올바른 괄호 문자열"로 변환한 결과
