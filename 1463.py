infi = 987654321
n = int(input())
dp = [infi] * (n+1)
dp[1]=0

for i in range(2,n+1):
    if i % 6==0:
        dp[i] = min(dp[i//3], dp[i//2]) +1
    elif i % 3 ==0:
        dp[i] = min(dp[i//3], dp[i-1]) +1
    elif i % 2 ==0:
        dp[i] = min(dp[i//2], dp[i-1]) +1   
    else:
        dp[i] = dp[i-1] +1
    
print(dp[n])

'''
infi 를 987,654,321 로 설정한 이유는 
1,000,000,000 을 쓰려면 0을 헷갈려 틀릴 수도 있고
10억보다 조금 작은 값이라서 대부분의 문제에서 충분히 큰 값으로 사용할 수 있다.
int의 최대 범위인 21억의 절반보다 더 작은 값이라서 이 값끼리 더해져도 오버플로우가 발생하지 않는다.

'무한'을 의미하기 위해 충분한 큰 수로 사용한다고 한다.

1463번 - DP 문제
Bottom-up 풀이 방식 
재귀가 아닌 반복문으로 구현하며, 작은 X에 대해서부투 부분 문제를 구해서 입력받은 수까지 수행한다.
DP 테이블을 채우는 타뷸레이션 수행


n이 10일경우 문제를 풀어보자면,
i=2)
    dp[2] = min(dp[1], d[1]) +1
    **dp[1]이 0이라고 설정해두었으니
    dp[2] = 0+1 
i=3)
    dp[3] = min(dp[1], dp[2]) +1
    dp[3] = 0+1
i=4)
    dp[4] = min(dp[2], dp[3]) +1
    dp[4] = 1+1
i=5)
    dp[5] = dp[4] +1
    dp[5] = 2+1
i=6)
    dp[6] = min(dp[2], dp[3]) +1 
    dp[6] = 1+1 
i=7)
    dp[7] = dp[6] +1
    dp[7] = 2+1 
i=8)
    dp[8] = min(dp[4], dp[7]) +1
    dp[8] = 2+1
i=9)
    dp[9] = min(dp[3], dp[8]) +1
    dp[9] = 1+1
i=10)
    dp[10] = min(dp[5], dp[9]) +1
    dp[10] = 2+1

--> dp[10]일 경우, 3이 출력된다.

'''