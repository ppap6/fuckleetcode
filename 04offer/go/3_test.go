package _go

import "testing"

func TestGetDuplication(t *testing.T) {
	nums1 := []int{2, 3, 5, 4, 3, 2, 6, 7}
	v := getDuplication(nums1)
	if v != 2 && v != 3 {
		t.Fail()
	}
}
