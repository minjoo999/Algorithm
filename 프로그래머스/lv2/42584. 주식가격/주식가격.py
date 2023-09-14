from collections import deque


def solution(prices):
    answer = []

    P = deque(prices)

    while P:
        price = P.popleft()
        count = 0

        for p in P:
            if price > p:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer


print(solution([1, 2, 3, 2, 3]))
