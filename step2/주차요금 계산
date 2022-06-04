"""
시간 : 50분

되게 간단한데 오래 걸림..
"""
import math
def solution(fees, records):
    answer = [] 
    record_book = {} # 차량 번호 : [in, out]
    
    for record in records:
        record = record.split(" ") # 공백마다 제거
        time_min = int(record[0].split(":")[0]) * 60 + int(record[0].split(":")[1]) 

        #print(record[1], int(time_min))
        if record[2] == "IN":
            try: record_book[record[1]].append(int(time_min))
            except : record_book[record[1]] = [int(time_min)]
        else :
            record_book[record[1]].append(int(time_min))
            
    record_book = sorted(record_book.items())

    for id_, time_info in record_book:
        # 시간 계산
        total_time = 0
        fee = 0
        
        if len(time_info) % 2 != 0:# 출차 기록이 없으면
            total_time += 1439 - time_info.pop() # 끝에 거 처리
            #print("id_", total_time)
        for i in range(len(time_info) //2):        
            total_time += time_info[2*i+1] - time_info[2*i]    
            #print("id_",time_info[i+1],"-", time_info[i] ,  time_info[i+1] - time_info[i] )
            
        time_over = math.ceil((total_time-fees[0])/fees[2])    
        #print(id_, "total_time", total_time)
        if time_over > 0 :
            fee += fees[1] + time_over*fees[3]   
        else : 
            fee += fees[1] #기본 요금만
        # 요금계산
        answer.append(fee)

    return answer
