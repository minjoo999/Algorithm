from heapq import heapify, heappop, heappush


def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville[0] < K:

        # most_hot = heappop(scoville)
        # most_hot2 = heappop(scoville)
        
        if len(scoville) > 1:

            score = heappop(scoville) + 2 * heappop(scoville)
            answer += 1
            heappush(scoville, score)

            if len(scoville) == 1 and scoville[0] < K:
                answer = -1
                
        else:
            break

    return answer