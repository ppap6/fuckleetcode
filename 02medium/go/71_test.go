package medium

import "testing"

func TestSimplifyPath(t *testing.T)  {
	v := simplifyPath("/a/./b/../../c/")
	if v != "/c" {
		t.Fail()
	}

	v = simplifyPath("/a/../../b/../c//.//")
	if v != "/c" {
		t.Fail()
	}

	v = simplifyPath("/a//b////c/d//././/..")
	if v != "/a/b/c" {
		t.Fail()
	}

	v = simplifyPath("/../")
	if v != "/" {
		t.Fail()
	}

	v = simplifyPath("/...")
	if v != "/..." {
		t.Fail()
	}
}
