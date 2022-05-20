import sys
input = sys.stdin.readline

num = int(input())
count = 0

for i in range(0, num+1):
    for j in range(0, 60):
        for q in range(0, 60):
            target = str(i) + str(j) + str(q)
            if '3' in target:
                count += 1
print(count)
