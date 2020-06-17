testcase = int(input())
for i in range (testcase):
    g = int(input())
    c = list(map(int,input().split()))
    output = set(c)
    buffer = set()
    for _ in c.copy():
        if (_ in buffer ):
            output.remove(_)
            buffer.remove(_)
        buffer.add(_)
    print('Case #{}: {}'.format(i+1,output.pop()))
