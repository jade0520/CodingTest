"""
시간 80분
+ 시간 초과로 못 푼 문제 두문제

도형 규칙 찾으려다가 안되는 것 같아서 수식접근
베스트 풀이는 매우 간단.. 이렇게 풀 수 있을까

"""

import math
# w,h 비율이 같은 최소 정수마다 반복
# w !=h 일 때는 최소 크기를 가득 채우는 두칸을 내리면서 

def solution(w,h):
    # w,h의 최소 정수 비율
    gcd_ = math.gcd(w,h)
    w_s = int(w/gcd_)
    h_s = int(h/gcd_)
    
    end_point = 0
    next_start_point = 0
    blocks = 0
    
    center = h_s//2 if h_s%2 == 0 else h_s//2 +1
    for i in range(center):
        flag = (i+1)/h_s*w_s
        end_point = math.ceil(flag) # 현재칸 끝점
        block =  (end_point - int(next_start_point)) #블럭 개수
        blocks += block
        next_start_point =  math.floor(flag) # 다음 칸 시작점 갱신
    
    blocks = 2*blocks if h_s%2 == 0 else (blocks* 2 - block)
    answer = w*h - gcd_ * blocks
    return answer
