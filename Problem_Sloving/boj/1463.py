n = int(input())
dp = [0 for _ in range(n+1)]
dp[1]=0
if n > 1:
    dp[2]=1
if n > 2:
    dp[3]=1
if n > 3:
    for i in range(4,n+1):
        tmp = []
        tmp.append(dp[i-1]+1)
        if i % 2 == 0 :
            tmp.append(dp[int(i/2)]+1)
        if i % 3 == 0 :
            tmp.append(dp[int(i/3)]+1)
        dp[i]=min(tmp)
print(dp[n])