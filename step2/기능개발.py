"""
시간 : 25분

- 스택/큐라고 대놓고 쓰여있어서 생각하기 쉬웠다.
"""

# 뒤 먼저 개발 가능하지만 배포는 앞과 같이
def chain_del(progresses, speeds, count):
    if not progresses :  return count
    if progresses[0] >= 100 : 
        count += 1
        #print("100 찾음", progresses)
        del progresses[0]
        del speeds[0]
        
        return chain_del(progresses, speeds, count) # 다시 검사
    else: 
        return count

def solution(progresses, speeds):
    # progresses : 배포되어야 하는 순서대로 작업의 진도
    # speeds : 작업의 개발 속도
    
    answer = [] # 각 배포마다 몇 개의 기능이 배포
    
    # 리스트 생성 후 가장 위가 100이 되면 출력
    while progresses :
        
        # 완료된 것 있는 지 검사
        del_count = chain_del(progresses, speeds, 0)
        if del_count : 
            #print("결과", progresses)
            answer.append(del_count) # 0이 아니면 붙이기
        if not progresses :  return answer
            
        # 하루 지나기
        for i in range(len(progresses)):
            progresses[i] += speeds[i] # 스피드 만큼 올리기
        

        
        
    return answer
