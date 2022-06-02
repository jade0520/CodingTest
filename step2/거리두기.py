"""
거라두기 (못품)
시간 : 3시간 훨씬넘음
- 런타임 에러 + 실패 섞임

베스트 코드 : 경우의 수를 다 따짐
5x5로 작을때는 그냥 경우의 수를 다 따지는 게 좋을 방법일듯 하다.
"""


# Best 풀이 : 왼쪽 위부터 검사를 시작하므로, 오른쪽과 아래의 P 여부만 확인하면 된다.
def check(place):
    for irow, row in enumerate(place):
        for icol, cell in enumerate(row):
            if cell != 'P': # 현재 cell이 P가 아니면 넘김
                continue
            if irow != 4 and place[irow + 1][icol] == 'P': 
                # 현재 cell이 마지막 행이 아니고, 아래 cell이 P라면 return 0
                return 0
            if icol != 4 and place[irow][icol + 1] == 'P': 
                # 현재 cell이 마지막 행이 아니고, 오른쪽 cell이 P라면 return 0
                return 0
            if irow < 3 and place[irow + 2][icol] == 'P' and place[irow + 1][icol] != 'X': 
                # 현재 cell이 <3 이고, 아래 cell이 X가 아닌데, 그 아래 cell이 P 라면 return 0
                return 0
            if icol < 3 and place[irow][icol + 2] == 'P' and place[irow][icol + 1] != 'X': 
                # 현재 cell이 <3 이고, 오른쪽 cell이 X가 아닌데, 그 오른쪽 cell이 P 라면 return 0
                return 0
            if irow != 4 and icol != 4 and place[irow + 1][icol + 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol + 1] != 'X'):
                # 현재 cell이 끝자락이 아닐때 오른쪽과 아래가 X가 아닌데 대각선 아래가 P이면 return 0
                return 0
            if irow != 4 and icol != 0 and place[irow + 1][icol - 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol - 1] != 'X'):
                # 현재 cell이 왼쪽 아래가 아닐때 왼쪽과 아래가 X가 아닌데 왼쪽 대각선 아래가 P이면 return 0
                return 0
    return 1

def solution(places):
    return [check(place) for place in places]

# 내 풀이2 
dir_1 = [1,0,-1,0]
dir_2 = [0,1, 0,-1]

def detect_(place,i,j, dist):
    
    # 거리가 2가 되면 돌아가기
    if dist == 3 :
        #print("거리 3 돌아가기")
        return 1
    
    elif dist > 0:        
        state = place[i][j]
        if state == 'P': # P 만나면 멈춤 
            #print("P 만남 return 0")
            return 0
        elif state == 'X':
            #print("X 만남 돌아가기")
            return 1 # X 만나면 돌아가기 
        
    # 계속 탐색 진행
    for c1, c2 in zip(dir_1, dir_2):
        c1, c2 = c1 + i, c2 + j
        if (c1 not in range(5)) or (c2 not in range(5)): continue
        #print("탐색", c1, c2 )
        result  = detect_(place, c1, c2, dist+1)
        if not result : return 0 # 하나라도 0이 나왔으면 return 
        
    return 1 # 이상 무
            

def solution(places):
    answer = []

    for place in places:
        place = list(map(list, place))
        #print(place)
        # i,j가 P면 탐색 시작
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    #print("P 발견 :", i,j )
                    place[i][j] = 'X'
                    result = detect_(place,i,j,0)
                    if not result: break#  하나라도 안지켰으면 0
            if not result: break       
        
        if not result: answer.append(0)
        else : answer.append(1)
    
    return answer


# 내 풀이1
import numpy as np

def valid_(a,b):
    if a < 0 or b <0 or a>4 or b>4 : return False
    return True
first_zone = [(-1,0), (0,1), (1,0), (0,-1)]

def detect_(place, i, j , len_, start_p): 
    current_p = (i,j)
    #print(f"현재 {current_p}")
    if len_ == 0 : # 이제 시작
        len_ = 1
    else: 
        if (place[i][j] == 'P'):
            #print(f"여기서 P 만남")
            return False #탐색 끝  - 문제!
        elif (place[i][j] == 'X'):
            #print(f"여기서 막힘")
            return True #탐색 끝
        elif (place[i][j] == 'O'):
            len_ += 1
            if len_ == 3 :
                #print(f"여기서 탐색 끝")
                return True #탐색 끝
    #print(f"계속 진행")            
    # 전진  
    for idx in range(4):

        (a,b) = tuple(sum(elem) for elem in zip(current_p, first_zone[idx]))
        if not valid_(a,b) : continue
        if (a,b) == start_p : continue
        result = detect_(place, a, b , len_, start_p)
        if not result : return 0

    return 1
    
    
def solution(places):
    answer = []
    for place in places:
        place = [list(line) for line in place]
        for i in range(5):
            for j in range(5):    
                if place[i][j] == "P" :
                    len_ = 0 
                    #print(f"시작 포인트 {i,j}, {place[i][j] }")  
                    result = detect_(place, i,j , len_, (i,j))
                    if not result:  break
            if not result : break
                    
        answer.append(result)

    return answer
