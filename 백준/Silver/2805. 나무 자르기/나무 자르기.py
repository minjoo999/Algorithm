import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

max_t = max(trees)


def find_heights(start, end):
    mid = (start + end) // 2
    cnt = 0

    for tree in trees:
        if tree >= mid:
            cnt += tree - mid

    # 절단기 높이 올리기: cnt
    if start <= end:
        if cnt >= M:
            find_heights(mid + 1, end)
        elif cnt < M:
            find_heights(start, mid - 1)
    else:
        print(mid)

find_heights(0, max_t)
