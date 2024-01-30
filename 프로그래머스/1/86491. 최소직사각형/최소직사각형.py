# w, h리스트 두개 합해서 sort 하고  len(명함번호)만큼 w_list에 담아서
        # w = w_list중 가장 큰 값 h = h_list 중 가장 큰 값
def solution(sizes):
    w_list = []
    h_list = []
    w = h = 0
    for i in sizes:
        h_list.append(max(i))
        w_list.append(min(i))
        
    w = max(w_list)
    h = max(h_list)
    
    return w*h
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))


