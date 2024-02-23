N = int(input())
def func1(a, b, N):
    if N == 1:
        print(a, b)
        return
    func1(a, 6-a-b, N-1)
    print(a, b)
    func1(6-a-b, b, N-1)
    
print(2**N - 1)
func1(1,3,N)
