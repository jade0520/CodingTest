"""
얘네는 왜 굳이 이런 놀이를 하는 걸까
문제 : "one4seveneight" --> 1478 
푼 시간 : 10분
best 풀이 : dictionary와 for문을 사용했는데, 간결해지긴하지만, 코테에서는 이게 더 나은듯?
"""


import re

def solution(s):
    s = re.sub('zero','0',s)
    s = re.sub('one','1',s)
    s = re.sub('two','2',s)
    s = re.sub('three','3',s)
    s = re.sub('four','4',s)    
    s = re.sub('five','5',s)
    s = re.sub('six','6',s)
    s = re.sub('seven','7',s)
    s = re.sub('eight','8',s)  
    answer = re.sub('nine','9',s)  
    return int(answer)
