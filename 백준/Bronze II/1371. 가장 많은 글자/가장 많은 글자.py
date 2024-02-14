import sys
input = sys.stdin.read
DP = [0] * 26
score = []
A = input().replace("\n","").replace(" ","")
for alpha in A:
    DP[ord(alpha)-97] += 1
    
maximum = max(DP)

for i in range(len(DP)):
    if DP[i] == maximum:
        score.append(chr(i+97))
        
score.sort()
print(*score, sep="")