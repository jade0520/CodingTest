"""
시간 : 27분

- count를 넘기면 계속 쌓임. return counter를 하기 때문에 연산 결과가 0이라도 앞 서 받은 counter를 그대로 return 하게 되어서 중복 계산이 됨.
- 분기별 계산을 하고싶으면 그냥 더하기만하고 매개변수로 안넘겨도 됨. (계산 결과가 알아서 기억됨!)

"""
def rec_P_M(numbers, cur_idx, stacked_result, target):
    # 종료 조건 : 끝까지 탐색 -> 결과 return
    if len(numbers) == cur_idx : 
        if stacked_result == target: 
            #print("Same", stacked_result)
            return 1 
        return 0
    count = 0 # 이게 없으면 매칭 되는 것이 없어도 앞 서 받은 counter를 return하고 합치기 때문에 중복이 되는 것!!!
    blnk = " "*cur_idx
    # Plus 
    plus_result =  stacked_result + numbers[cur_idx]  # 현재 까지의 결과 저장
    #print(blnk, "+",numbers[cur_idx])
    count += rec_P_M(numbers, cur_idx+1, plus_result, target) # 현재 결과에서 다음 경우 계산
    #print( count)
    # Minus
    minus_result =  stacked_result - numbers[cur_idx] 
    #print(blnk, "-",numbers[cur_idx])
    count += rec_P_M(numbers, cur_idx+1, minus_result, target) # 현재 결과에서 다음 경우 계산
    #print(count)   
    
    return count

def solution(numbers, target):
    
    answer = rec_P_M(numbers, 0, 0, target)
    
    return answer
