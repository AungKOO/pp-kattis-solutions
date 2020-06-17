def digsum(n):
    ans = 0
    while n > 0 :
        ans += n%10
        n //=10
    return ans

l = int(input())
d = int(input())
x = int(input())
for i in range(l,d+1):
    check = digsum(i)
    if check == x :
        print(i)
        break

for i in range(d,l,-1):
    check = digsum(i)
    if check == x:
        print(i)
        break