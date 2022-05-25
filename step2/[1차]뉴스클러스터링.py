"""

시간 : 84 + QnA

내 코드의 반례를 찾는게 항상  오래 걸린다.
7,9,10,11이 계속 틀렸는데 QnA를 보니 
합 집합의 중복을 카운트할 때, 두 집합에 해당 요소가 모두 존재할 것이라는 가정을 했다.
로직을 쓸 주의해야겠다.

망했다 ㅠㅠ
"""

import re


def detect_set(str_):
    # 공백처리
    str_ = str_.replace(' ','-')
    #print(str_)
    # 
    pair_list = []
    pair_dict = {}
    p = re.compile('[a-zA-Z]')
    for i in range(len(str_)-1):
        #print(str_[i:i+2].upper())
        if (p.match(str_[i]) != None) and (p.match(str_[i+1]) != None):
            pair_list.append(str_[i:i+2].upper())
            try : pair_dict[str_[i:i+2].upper()] += 1 # 중복 추가
            except : pair_dict[str_[i:i+2].upper()] = 0
            #print(str_[i:i+2].upper(), "추가")
            
    #print(pair_list)
    return pair_dict, set(pair_list)   

def solution(str1, str2):

    #set 만들기
    str1_dict, str1_set = detect_set(str1) 
    #print(str1_dict, str1_set)
    str2_dict, str2_set = detect_set(str2)           
    #print(str2_dict,str2_set)    
    
    # 공집합 처리
    if (str1_set == set()) and (str2_set == set()) :
        return 1* 65536

    C_set = str1_set&str2_set
    U_set = str1_set|str2_set
    #print("공집합",C_set)
    #print("합집합",U_set)
    
    A, B = 0, 0
    
    #print(str1_dict)
    #print(str2_dict)
    for el in C_set:
        # 공집합 중에 중복이 있는 경우
        try : 
            A += min(str1_dict[el],str2_dict[el])
        except : continue

    for el in U_set:   
        # 합집합 중에 중복이 있는 경우
        try : 
            B += max(str1_dict[el],str2_dict[el])
        except : 
            try : B += str1_dict[el]
            except: B += str2_dict[el]
    
    #print("C_set", C_set)
    #print("U_set", U_set)
    #print(len(C_set),"+", A, "=",(len(C_set)+ A))
    #print(len(U_set),"+",B,"=",(len(U_set) +B))

    return int((len(C_set)+ A)/(len(U_set) +B)* 65536)
