from collections import deque


def solution(priorities, location):
    origins = deque()
    i = 0
    for p in priorities:
        origins.append((p, i))
        i += 1

    results = []

    while origins:
        o1 = origins.popleft()

        b = 0
        for o in origins:
            if o1[0] < o[0]:
                origins.append(o1)
                b += 1
                break

        if b == 0:
            results.append(o1)

    answer = 0

    for r in results:
        if r[1] == location:
            answer = results.index(r) + 1

    return answer