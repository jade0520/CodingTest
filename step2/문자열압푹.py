"""
문자열 압축

QnA 확인하니 자리수 반영을 안했었다. 그런데 하나가 계속 틀린다.
시간 : 91분 + QnA 확인

"""

# 3차 시도 : 3개가 연달아 있으면 사라지는 것 두개를 빼는 방식이라 10개인 경우 카운트를 9개로 함. 그래서 딱 10개인 경우 자리수 반영이 안되었음
def solution(s):
    # 받은 문자열 처음 i개만큼 자르기
    length_ = len(s)
    
    # 가장 짧은 것의 길이 
    answer = length_
    #print(s)
    for n in range(1, length_):
        split_s = list(map(''.join, zip(*[iter(s)]*n)))
        if len(split_s) == 1: break
        split_s.append('!!!')
        #print(split_s)
        
        # 계산할 준비
        zip_count = 0
        zip_result = length_
        for i in range(len(split_s)-1):
            if split_s[i] == split_s[i+1]:
                # 같으면 1 추가
                zip_count +=1
                
            else:
                # 다르면 초기화
                if zip_count :
                    #print(zip_count, len(str(zip_count)))
                    # 0 이 아니면
                    zip_result -= zip_count* n 
                    zip_result += len(str(zip_count+1)) # 자리수 반영시 전체 개수 카운트
                    zip_count = 0

        if zip_result < answer:
            #print(zip_result)
            answer = zip_result

    return answer
    
# 2차 시도 : 자리 수 반영하였으나, 두개 틀림
def solution(s):
    # 받은 문자열 처음 i개만큼 자르기
    length_ = len(s)
    
    # 가장 짧은 것의 길이 
    answer = length_
    #print(s)
    for n in range(1, length_+1):
        split_s = list(map(''.join, zip(*[iter(s)]*n)))
        if len(split_s) == 1: break
        split_s.append('!!!')
        #print(split_s)
        
        # 계산할 준비
        zip_count = 0
        zip_result = length_
        for i in range(len(split_s)-1):
            if split_s[i] == split_s[i+1]:
                # 같으면 1 추가
                zip_count +=1
                
            else:
                # 다르면 초기화
                if zip_count :
                    # 0 이 아니면
                    zip_result -= zip_count* n 
                    zip_result += len(str(zip_count)) # 자리수 반영
                    zip_count = 0

        if zip_result < answer:
            #print(zip_result)
            answer = zip_result

    return answer

# 1차 시도: 시험은 다 맞았는데 제출 시 몇개 틀림 틀렸는지를 모르겠음
def solution(s):
    # 받은 문자열 처음 i개만큼 자르기
    length = len(s)
    
    # 가장 짧은 것의 길이 
    answer = length
    #print(s)
    for n in range(1, length+1):
        split_s = list(map(''.join, zip(*[iter(s)]*n)))
        if len(split_s) == 1: break
        split_s.append('!!!')
        #print(split_s)
        
        # 계산할 준비
        zip_count = 0
        zip_result = length
        for i in range(len(split_s)-1):
            if split_s[i] == split_s[i+1]:
                # 같으면 1 추가
                zip_count +=1
                
            else:
                # 다르면 초기화
                if zip_count :
                    # 0 이 아니면
                    zip_result -= zip_count* n 
                    zip_result += 1
                    zip_count = 0

        if zip_result < answer:
            #print(zip_result)
            answer = zip_result


    return answer

