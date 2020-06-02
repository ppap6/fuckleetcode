package medium

func longestPalindrome(s string) string {

	if s == ""{
		return s
	}

	dp := make(map[int]int, len(s))
	for i:=0; i<len(s); i++ {
		dp[i] = 1
	}

	for i := range dp {
		for j:=0; j<i; j++{

			if isPalindrome(s[j:i+1]) {
				dp[i] = i - j +1
				break
			}
		}
	}

	max := 1
	index := 0
	for i := range dp {
		if dp[i] > max {
			max = dp[i]
			index = i
		}
	}

	return s[index-max+1:index+1]
}

func isPalindrome(s string) bool {
	l := len(s)-1
	for i:=0; i<len(s)/2; i++ {
		if s[i] != s[l-i] {
			return false
		}
	}
	return true
}