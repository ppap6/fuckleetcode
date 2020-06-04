package _go

import "strings"

func replaceSpace(s string) string {
	var res strings.Builder
	for _, v := range s {
		if v == 32 {
			res.WriteString("%20")
		} else {
			res.WriteRune(v)
		}
	}
	return res.String()
}
