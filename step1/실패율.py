"""
인덱스 정수 이런것 때문에 헷갈려서 오래 걸렸다. 
알고리즘이 틀렸다기 보다는 간단한 자료형이 파악이 안되어서 계속 오류 나고 찾고 오래걸린다.


시간 : 50분 + 24분

런타임 에러남.

배운점 : 개수마다 생성은 너무 오래 걸림, 최대한 숫자 계산을 할 수 있는 알고리즘
for문 여러개 될 것 같으면 최대한 일단 있는 함수 사용하도록 하자.

Best 알고리즘 : 수학적 이해가 필요 ㅠㅠㅠ
 - 도달한 사람 = 현 스테이지 실패자  
 - stage를 올라가면서 거쳐온 스테이지의 인원을 빼면, 도달한 사람.

"""
# 2차 
import numpy as np

def solution(N, stages):
    # 인데스 주의 0 = stage 1
    answer = []
    reach = [0]*(N + 1)
    clear = [0]*N
    
    # 스테이지 정보 저장
    for stage in stages:
        reach[stage - 1] += 1 #각 플레이어의 위치 저장    
    for s in range(N):
        # 현재 s보다 큰 stage의 수 합 
        clear[s] =  sum(reach[s:])
        
    # 실패율 계산
    reach = np.array(reach[:-1])
    clear = np.array(clear)
    fail_value = (reach-clear)/reach
    
    stages = [x+1 for x in range(N)]
    fail = np.concatenate([[fail_value], [stages]]).transpose()

    # 정렬
    answer = sorted(fail, key = lambda x : (-x[0], x[1])) 
    answer = [s for v, s in answer]
    
    return answer
    

# 1차 런타임 오류
import numpy as np

def solution(N, stages):
    # 인데스 주의 0 = stage 1
    answer = []
    fail = []
    
    reach = [0]*(N + 1)
    clear = [0]*N
    
    # 스테이지 정보 저장
    for stage in stages:
        for i in range(stage -1):
            clear[i] += 1
            reach [i] += 1
        reach[stage-1] += 1  # 다 클리어 하면  N+1 인덱스로 감. 

    # 실패율 계산
    for r, c in zip(reach, clear):
        stay = r - c
        fail.append(stay/r)
        

    answer = []
    mask = [True] * len(fail)

    for _ in range(len(fail)):
        max = [-1,-1] 
        for i, elm in enumerate(fail):
            if elm > max[1] and mask[i]:
                # 더 큰 값이 나타나고 아직 지워지지 않았다면,
                max = [i, elm]
        mask[max[0]] = False
        answer.append(max[0] + 1)

    return answer
