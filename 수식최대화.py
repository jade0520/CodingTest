
"""
시간 67분
- 계속 쓰는 함수 따로 정리하기
- 개수 좀 적다 싶으면 다 연산하는 게 빠르다
"""
import re
from itertools import permutations
import copy


def add(a,b): return int(a) + int(b)
def sub(a,b): return int(a) - int(b)
def mul(a,b): return int(a) * int(b)

# expression마다 최대 값을 출력하는 연산자 우선순위 지정
def solution(expression):
    answer = 0
    
    # 우선 순위 후보
    ops = ['+','-','*']
    r_ops = {'+':add,'-':sub,'*':mul}
    ops_p = permutations(ops,3)
    
    # 문자열과 숫자 나누기
    ops = re.findall('\W', expression)
    nums = []
    for op in ops:
        C_idx = expression.find(op)
        nums.append(expression[:C_idx])
        expression = expression[C_idx+1:]
    nums.append(expression)
    #print(nums, ops)
    
    for op_pair in ops_p:
        #print(op_pair)
        d_nums = copy.deepcopy(nums)
        d_ops = copy.deepcopy(ops)
        for op in op_pair:
            for _ in range(ops.count(op)):
                #print(d_ops)
                #print(d_nums)   
                idx = d_ops.index(op) # 같은 연산 찾기
                duim = r_ops[d_ops[idx]](d_nums[idx],d_nums[idx+1]) 
                # 연산 후 
                d_nums[idx] = duim # 계산된 수 저장
                d_nums.pop(idx+1) # 계산된 수 삭제
                d_ops.pop(idx) # 사용한 연산 삭제


        if abs(d_nums[0]) > answer:
            answer = abs(d_nums[0])
    
    # 1. * 앞에 -가 없으면 우선이 되는게 좋음.
    # 2. + 
    
    #결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출
    return answer
