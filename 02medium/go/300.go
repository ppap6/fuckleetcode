package medium

// 一直过不了，本地输出正常， leetcode上却不一致，todo
func lengthOfLIS(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	// 这个dp的意义是以nums[i]结尾的最长上升子序列长度
	dp := make(map[int]int, len(nums))
	for i := range nums {
		dp[i] = 1
	}

	for i := range dp {
		for j:=0; j<i; j++ {
			if nums[j] < nums[i]{
				if dp[j] + 1 > dp[i] {
					dp[i] = dp[j] + 1
				}
			}
		}
	}

	max := 1
	for i := range dp {
		if dp[i] > max {
			max = dp[i]
		}
	}
	return max
}