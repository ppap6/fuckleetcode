package easy

// 递归， 理论上是对的，但是过了不了， 因为N太大的话会超过栈层数最大限制
func fib(N int) int {
	if N == 1 || N == 2 {
		return 1
	}
	return fib(N-1) + fib(N-2)
}

// 备忘录解法
func fib2(N int) int {
	memo := make(map[int]int, N+1)
	return helper2(memo, N)

}

func helper2(memo map[int]int, n int) int {
	if n == 1 || n == 2 {
		return 1
	}
	if n == 0 {
		return 0
	}
	if memo[n] != 0 {
		return memo[n]
	}
	memo[n] = helper2(memo, n-1) + helper2(memo, n-2)
	return memo[n]
}

// 动态规划
func fib4(N int) int {
	dp := make(map[int]int, N)
	dp[1] = 1
	dp[2] = 1
	for i:=3; i <=N; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	return dp[N]
}

// 动态规划，降低内存占用
func fib5(N int) int {
	if N == 0 {
		return 0
	}
	if N == 1 || N == 2 {
		return 1
	}
	prev, curr := 1, 1
	for i:=3; i<=N; i++{
		curr, prev = prev + curr, curr
	}
	return curr
}
