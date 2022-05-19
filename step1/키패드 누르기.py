"""
연산 간단하게 하려고 하다가 내꾀에 내가 넘어가는 느낌... 많이 해보는 수밖에 없을 것 같다.
대부분 좌표적으로 접근한 것 같다.
이건 좀 뿌듯하네^^
풀이시간 : 60 분

"""
def solution(numbers, hand):
    answer = ''
    left = 10                
    L_d = 1
    right = 12
    R_d = 1
    hand = 1 if hand == "right" else 0 # right면 left에 패널티 추가
    
    while numbers != []:
        target = numbers.pop(0) 
        target = 11 if target == 0 else target 
        if target % 3 == 1: 
            answer += "L"
            left = target
            L_d = 1  # 가운데에서의 추가 거리
            
        elif (target % 3 == 0) and target != 0 :
            answer += "R"
            right = target  
            R_d = 1 # 가운데에서의 추가 거리
            
        else:
            if abs(left + L_d - target)//3 + L_d + hand <= abs(right - R_d- target)//3 + R_d :
                answer += "L"
                left = target
                L_d = 0  

            else :
                answer += "R"
                right = target
                R_d = 0

    return answer
