import sys
input = sys.stdin.readline

def solution(T):
    for _ in range(T):
        t = int(input())
        # 0, 1에 대한 순서쌍 카운트 개수를 dp로 저장
        dp = [(1,0), (0,1)]
        
        if t > 1:
            for i in range(2, t+1):
                dp.append((dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]))
        print(f"{dp[t][0]} {dp[t][1]}")

if __name__ == "__main__":
    T = int(input())
    solution(T)