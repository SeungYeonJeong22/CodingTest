import sys
input = sys.stdin.readline

def soluton(n):
    dp = [1, 2] + [0] * (n-2)
    if n > 1:
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]
    print(dp[n-1]%10007)

if __name__ == "__main__":
    n = int(input())
    soluton(n)