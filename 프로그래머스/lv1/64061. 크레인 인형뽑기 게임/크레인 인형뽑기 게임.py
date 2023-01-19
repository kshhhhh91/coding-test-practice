def solution(board, moves):
    
    bucket = []
    removed_list = []

    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] == 0:
                continue
            else:
                bucket.append(board[i][m-1])
                board[i][m-1] = 0
                break
        for n in range(1,len(bucket)):
            if bucket[n] == bucket[n-1]:
                removed_list.append(bucket.pop(n))
                removed_list.append(bucket.pop(n-1))
            else:
                continue

    answer = len(removed_list)

    return answer