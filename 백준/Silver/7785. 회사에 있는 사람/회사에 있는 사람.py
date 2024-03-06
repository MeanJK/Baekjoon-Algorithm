import sys
input = sys.stdin.readline
n = int(input())
log_dict = {}
for _ in range(n):
    name, log = map(str, input().split())
    log_dict[name] = log
    if log == 'leave' and name in log_dict:
        del(log_dict[name])
sorted_dict = dict(sorted(log_dict.items(), key = lambda item: item[0], reverse = True))
for d in sorted_dict:
    print(d)