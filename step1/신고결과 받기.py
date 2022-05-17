"""
걸린 시간 : 40분

문제 이해가 중요.
- 메일 받는 기준
- 신고 중복이 안되는 것

배운것
- dict.keys() 는 list()로 바꾸어주어야 한다!
- print 쓰면 시간/용량 초과로 채점이 안된다!
"""


def solution(id_list, report, k):
    """
    id_list : 전체 id 리스트
    report :  "신고자 신고대상자"
    k : 
    
    """    
    
    Respondent_dict = {id_list[i] : 0 for i in range(len(id_list))} # 신고받은 횟수
    reporter_dict = {id_list[i] : [] for i in range(len(id_list))} # 신고 한 사람
    mail_dict = {id_list[i] : 0 for i in range(len(id_list))} # 신고 한 사람
       
    for Reporter_Respondent in report:
        reporter = Reporter_Respondent.split(' ')[0]
        Respondent = Reporter_Respondent.split(' ')[1]
        
        if Respondent not in reporter_dict[reporter]:
            # 이전에 신고한 적이 없다면,
            reporter_dict[reporter].append(Respondent)  # 신고한 사람 리스트에 추가
            Respondent_dict[Respondent] += 1 # 신고 받은 횟수 저장    
            
    #print("신고받은 횟수", Respondent_dict)

    for Respondent, count in Respondent_dict.items() :
        if count >= k:
            # 신고 대상자가 정지 메일을 받으며
            #mail_dict[Respondent] += 1
            #print("신고 받는", Respondent)
            
            for reporter, report_list in reporter_dict.items():
                # 모든 리포터를 탐색해서 
                if Respondent in report_list:
                    # 해당 신고자를 신고한 리포터에게 메일이 간다.
                    mail_dict[reporter] += 1
                    #print(Respondent,"를 신고한", reporter)
                    
    # 유저별 "메일" 처리 결과를 담은 횟수 - Respondent_dict는 id list 순서와 같다 
    answer =  list(mail_dict.values())

    return answer
