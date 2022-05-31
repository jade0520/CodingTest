"""
시간 : 29분
- 같은 2단계인데 시간 차이 왜이렇게 나는거지;
"""

def solution(s):
    s = s[2:-2]
    s = s.replace('},{','/')
    s = s.split('/')
    s.sort(key=len)
    #print(s)
    
    answer = [int(s[0])]
    for s_ in s[1:] :
        # '2,3' - > [2,3]
        s_ = s_.split(',')
        for n in s_:
            if int(n) not in answer:
                #print(n, answer)
                answer.append(int(n))    

    return answer
