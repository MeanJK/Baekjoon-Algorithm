x, y= map(int, input().split())
x1, y1= map(int, input().split())
x2, y2= map(int, input().split())
def ccw(x, y, x1, y1, x2, y2):
    return x*y1 + x1*y2 + x2*y - y*x1 - y1*x2 - y2*x
res = ccw(x, y, x1, y1, x2, y2)
if res < 0:
    print(-1)
elif res > 0:
    print(1)
else:
    print(0)