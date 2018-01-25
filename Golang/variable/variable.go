package main

import "fmt"

var (
	x, y, z         int  = 1, 2, 3
	c, java, python bool = true, true, false
)

func main() {
	str := "Hello Dog!"
	fmt.Println(x, y, z)
	fmt.Println(c, java, python)
	fmt.Println(str)
}
