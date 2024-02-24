import heapq as hp
def solution(scoville, K):
    hp.heapify(scoville)
    
    count = 0
    while scoville[0] < K:
        count += 1
        first = hp.heappop(scoville)
        second = hp.heappop(scoville)
                
        hp.heappush(scoville, first+second*2)
        
        if len(scoville) == 2 and (scoville[0] + scoville[1]*2) < K:
            return -1
    return count
print(solution([1, 2, 3, 9, 10, 12]	, 7))