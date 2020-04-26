package easy

import (
	"testing"
)

func TestBackspaceCompare(t *testing.T) {
	if backspaceCompare("ab#c", "ad#c") == false {
		t.Fail()
	}
	if backspaceCompare("ab##", "a#d#") == false {
		t.Fail()
	}
	if backspaceCompare("a##c", "#a#c") == false {
		t.Fail()
	}
	if backspaceCompare("a#c", "b") == true{
		t.Fail()
	}
	if backspaceCompare("xywrrmp", "xywrrm#p") == true {
		t.Fail()
	}

	if backspaceCompare("abcd", "bbcd") == true {
		t.Fail()
	}
}
