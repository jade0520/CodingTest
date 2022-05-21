"""
이게 이렇게 까지 걸릴 문제가 아닌 것 같은데...
연습이니까 좋은 방법을 찾아봐야 할지, 
원초적인 방법으로 해야할 지 고민된다.
시간: 50분
베스트 풀이 : i, j를 잘 활용하는게 좋을 것 같다. 행열 구분
배운 점 :
list[][]
array[,]
"""


import numpy as np

def solution(board, moves):
    """
    board[0]이 제일 위 
    moves[0]이 제일 처음 크레인 위치
    """
    answer = 0                     
    stack = [-1]
    
    for move in moves:
        move = move - 1 # idx 조정
        selected_col = np.array(board)[: , move]

        for i, elm in enumerate(selected_col):
            if elm != 0:
               # 0이 아닌 요소를 만나면
            
                if (elm == stack[-1]) :
                    #스텍의 가장 마지막과 같으면
                    stack.pop() # 가장 마지막 pop
                    answer += 2
                    
                else:
                    # 아니면 쌓기
                    stack.append(elm) # 바구니에 추가
                
                board[i] [move] = 0 # board에서 지우기                

                break

    # 터트려져 사라진 인형의 개수를 return 
    return answer
