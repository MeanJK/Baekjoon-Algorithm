import sys
input = sys.stdin.readline
n, m = map(int, input().split())
person_dict = {}
see_dict = {}
for _ in range(n):
    name = input().strip()
    person_dict[name] = 0
for _ in range(m):
    name = input().strip()
    see_dict[name] = 1
result = set(person_dict) & set(see_dict)
print(len(result))

sorted_result = sorted(result)
for r in sorted_result:
    print(r)