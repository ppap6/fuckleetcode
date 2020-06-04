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

func getDuplication(nums []int) int {
	left, right := 1, len(nums)-1

	for left < right {
		count := 0
		mid := (left + right) / 2
		for _, v := range nums {
			if v >= left && v <= mid {
				count++
			}
		}
		if count > (mid - left + 1) {
			right = mid
		} else {
			left = mid+1
		}
	}

	return left
}

