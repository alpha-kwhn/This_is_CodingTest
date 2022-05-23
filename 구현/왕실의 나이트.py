import sys
input = sys.stdin.readline

info = input()
row = int(info[1])
column = int(ord(info[0]) - ord('a')) + 1

navigate = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0

for way in navigate:
    if 1 <= way[0] + column <= 8 and 1 <= way[1] + row <= 8:
        count += 1

print(count)
