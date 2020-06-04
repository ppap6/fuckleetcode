package _go

// 提一个不太有人讲的观点，站在右上角看。这个矩阵其实就像是一个Binary Search Tree。然后，聪明的大家应该知道怎么做了。
func findNumberIn2DArray(matrix [][]int, target int) bool {
	if len(matrix)  == 0 {
		return false
	}

	if len(matrix[0]) == 0{
		return false
	}

	maxRow, maxColumn := len(matrix)-1, len(matrix[0])-1
	row, column := 0, maxColumn

	for row <= maxRow && column >= 0 {
		if matrix[row][column] == target {
			return true
		}

		if matrix[row][column] > target {
			column--
		} else {
			row++
		}
	}
	return false
}

