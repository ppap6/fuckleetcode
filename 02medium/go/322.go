package medium

import "math"

// gg, 时间超出限制
func coinChange(coins []int, amount int) int {
	memo := make(map[int]int, amount)
	return dp(memo, coins, amount)
}

func dp(memo map[int]int, coins []int, n int) int {
	if n == 0 {
		return  0
	}

	if n < 0 {
		return -1
	}

	if memo[n] != 0 {
		return memo[n]
	}

	res := math.MaxInt8
	for _, coin := range coins {
		subProblem := dp(memo, coins, n-coin)
		if subProblem == -1 {
			continue
		}
		res = min(res, subProblem+1)
		memo[n] = res
	}

	if res == math.MaxInt8 {
		return  -1
	}
	return res
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

// 动态规划
func coinChange2(coins []int, amount int) int {
	dp := make([]int, amount+1)
	for i:=1; i<=amount; i++ {
		dp[i] = math.MaxInt8
	}

	for n:=1; n<=amount; n++ {
		for _, coin := range coins {
			if n - coin < 0 {
				continue
			}
			dp[n] = min(dp[n], dp[n-coin]+1)
		}
	}

	if dp[amount] == math.MaxInt8 {
		return -1
	}
	return dp[amount]
}