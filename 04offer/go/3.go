package _go

func findRepeatNumber(nums []int) int {
	for index, value := range nums {
		if index == value {
			continue
		}

		if value == nums[value] {
			return value
		}

		nums[index], nums[value] = nums[value], nums[index]
	}
	return 0
}
