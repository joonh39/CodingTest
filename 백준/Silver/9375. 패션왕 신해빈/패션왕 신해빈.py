import sys

test_case = int(sys.stdin.readline())

for i in range(test_case):
    n = int(sys.stdin.readline())
    d_fashion = {}
    for _ in range(n):
        item, category = sys.stdin.readline().split()
        if category in d_fashion:
            d_fashion[category].append(item)
        else:
            d_fashion[category] = [item]

    cnt = 1
    for j in d_fashion:
        cnt *= len(d_fashion[j]) + 1
    print(cnt - 1)