"""
뭐지 왜 갑자기 쉬워졌지
어제 전처리 해서 그런가?
확실히 명령어 외우고 있으면 코딩이 빨라진다ㅠ

시간 : 25분

best 
"""
def solution(record):
    answer = [] # 최종적으로 방을 개설한 사람이 보게 되는 메시지
    Enter = "님이 들어왔습니다."
    Leave = "님이 나갔습니다."
    action_dict = {"Enter": Enter, "Leave":Leave}
    logs = []
    uid_book = {}
    
    for r in record:
        r = r.split(" ")
        
        action = r[0]
        uid = r[1]
        
        try: 
            # Enter & change (leave는 id 가 없음)
            nname = r[2] 
            uid_book[uid] = nname
        except: None
            
        try: 
            logs.append([uid, action_dict[action]])
        except: continue
    
    for line in logs:
        new_log = uid_book[line[0]] + line[1]
        answer.append(new_log)
         # uid를 닉네임으로 변경
         # 하나의 문자열로 변경
    
            
    # Enter Leave Change 
    # 나가서 바꾸고 안들어온 경우? > 나가서 바꾼것은 안뜬다.
    
    return answer
