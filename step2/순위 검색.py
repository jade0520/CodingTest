"""
시간 - 55분
점수 - 40/100
효율성 테스트는 버리고 그냥 빨리 코딩하자
"""

from queue import PriorityQueue
import copy
import heapq

def solution(info, querys):
    lan_dict = {"cpp", "java", "python"}
    job_dict = {"backend", "frontend"}
    spec_dict = {"junior", "senior"}
    food_dict = {"chicken", "pizza"}
    
    # info 
    P_list = []
    for inf in info :
        inf = inf.split(" ")
        # -score lan job spec food 
        heapq.heappush(P_list,(-int(inf[4]), inf[0],inf[1], inf[2],inf[3]))# 점수 큰 수 저장 (abs필요)
        # 점수 음수 되나?      
    
    # 쿼리 처리
    Q_list = [] 
    for query in querys :
        query = query.split(" ")
        Q_list.append((-int(query[-1]), query[0],query[2], query[4],query[6]))

    # 비교
    answer = []

    for (score_f, lan_f, job_f, spec_f, food_f) in Q_list: 
        #기준 받기
        #rint("기준", score_f, lan_f, job_f, spec_f, food_f)
        answer_count = 0
        P_list_ = copy.deepcopy(P_list)
        while P_list_:   
            # 응시자의 정보 받기
            score, lan, job, spec, food = heapq.heappop(P_list_)
            #rint("스펙", score, lan, job, spec, food)
            if score > score_f : continue#음수 이므로
            if (lan !=  lan_f) and (lan_f != "-"): continue
            if (job !=  job_f) and (job_f != "-"): continue
            if (spec !=  spec_f) and (spec_f != "-"): continue
            if (food !=  food_f) and (food_f != "-"): continue
            #rint("통과") #, score, lan, job, spec, food)
            answer_count += 1
        
        answer.append(answer_count)
    
    
    return answer
