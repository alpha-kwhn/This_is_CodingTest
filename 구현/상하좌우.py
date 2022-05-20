import sys
input = sys.stdin.readline

start = [1,1]
num = int(input())
lis = list(map(str, input().split()))

for i in lis:
    if i == 'R':
        if start[1] < num:
            start[1] += 1
        else:
            pass
    elif i == 'L':
        if start[1] > 1:
            start[1] -= 1
        else:
            pass
    elif i == "D":
        if start[0] < num:
            start[0] += 1
        else:
            pass
    elif i == "U":
        if start[0] > 1:
            start[0] -= 1
        else:
            pass

print(start[0], start[1])