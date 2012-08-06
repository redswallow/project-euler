target = 100
ways = [1]+[0]*target

# dp[n][m]=dp[n][m-1]+dp[n-m][m]
for m in xrange(1,100):
  for n in range(m, target+1):
    ways[n] += ways[n-m]
 
print ways[target]

