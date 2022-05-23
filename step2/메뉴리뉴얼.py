"""
내용이 복잡해서 효율적인 방법을 생각하는 게 어려웠다. 
일단 생각 나는대로 풀었다.

시간 : 63분

오픈 채팅방이랑 함께 90분 걸린듯하다.
2시간안에 3문제 할 수 있을까..

"""
# 코스요리 메뉴는 최소 2가지 이상의 단품메뉴
# 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보
# 각 단품메뉴는 A ~ Z의 알파벳 대문자
from itertools import combinations 



def solution(orders, course):
    answer = [] # 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태
    
    order_comb = []
    comb_book = {}

    
    for comb_n in course:
        for order in orders :
            if comb_n > len(order) : continue # 주문이 더 짧으면 넘어가기
            sorted_order = sorted(order, key=lambda x : ord(x))
            # 각 주문별로 comb_n개의 조합
            comb_list = list(map(''.join,combinations(sorted_order, comb_n)))
            #print(comb_list)

            for comb in comb_list:
                # comb 북에 저장
                # !! 같은 메뉴인데 문자순서가 다른 경우도 포함해야함. -> 순서 통일해서 저장.
                try: comb_book[comb] += 1
                except: comb_book[comb] = 1 

                
    sorted_comb_book = sorted(comb_book.items(), key=lambda x: x[1], reverse=True)
    
    # course에 해당하는 수 + 가장 높은 값 + 같은 값도 포함 + 1개면 포함 x
    # 제일 앞쪽이 제일 높은 횟수
    
    best_comb = {c:[0,[]] for c in course}
    for comb in sorted_comb_book:

        if not best_comb[len(comb[0])][0] :  # 최대 값이 0이면 
            best_comb[len(comb[0])][0] = comb[1] # 최대 값 넣기
            best_comb[len(comb[0])][1].append(comb[0])
        elif best_comb[len(comb[0])][0] == comb[1] :
            # 값이 같아도 넣기
            best_comb[len(comb[0])][1].append(comb[0])  
            
    for k, v in best_comb.items():
        if v[0] <= 1:
            continue
        answer.extend(v[1])
          
    answer.sort()
    return  answer# 오름차순


# course의 개수에 해당하는 모든 문자 조합 
# 문자 조합이 나온 횟수 카운트 (같은 회원내 x )    
# 같은 메뉴 두개 가능? 중복x
# return 메뉴 순서? 사전 순으로 오름차순
# 메뉴 내 알파벳도 오름차순
