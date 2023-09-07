def solution(lottos, win_nums):
    
    # 일치하는 원소 갯수에 따라 순위 조정
    rank = 6
    
    same = []
    for i in sorted(lottos):
        for n in sorted(win_nums):
            if n == i:
                same.append(n)
    
#     bad_rank = rank - len(same) + 1
#     good_rank = bad_rank - lottos.count(0)
    
#     if bad_rank > 6:
#         bad_rank = 6
    
#     if good_rank < 1:
#         good_rank = 1

    if rank - len(same) + 1 > 6:
        bad_rank = 6
    else:
        bad_rank = rank - len(same) + 1
    
    if bad_rank - lottos.count(0) < 1:
        good_rank = 1
    else:
        good_rank = bad_rank - lottos.count(0)
    
    
    # 1개 번호 일치와 0개 번호 일치가 전부 6등임을 어떻게 반영하지?
    # good_rank에서 해결
    
    answer = [good_rank, bad_rank]
    return answer