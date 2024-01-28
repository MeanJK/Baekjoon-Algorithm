def solution(participant, completion):
    hashDict = {}
    hashCount = 0
    for part in participant:
        hashDict[hash(part)] = part
        hashCount += hash(part)
    for comp in completion:
        hashCount -= hash(comp)
    return hashDict[hashCount]
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))