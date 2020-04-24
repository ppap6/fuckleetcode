package easy

// ref: https://leetcode-cn.com/problems/palindrome-number/

func IsPalindrome(x int) bool {
	if x < 0 || (x % 10 == 0 && x != 0){
		return false
	}

	reverseNum := 0
	// 判断是否翻转到了一半位数
	for reverseNum < x {
		reverseNum = reverseNum * 10 + x % 10
		x /= 10
	}

	// 奇数位翻转后的数字会多一位
	return x == reverseNum || x  == reverseNum / 10
}
