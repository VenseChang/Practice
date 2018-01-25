package main

import (
	"fmt"
	"math"
	"reflect"
)

func main() {
	// intRange()
	// floatValue()
	// complexValue()
	// stringValue()
	boolValue()
}

func intRange() {
	fmt.Println("Int Type and Range:")
	splitLine()
	fmt.Printf("Int8 range: %v ~ %v\n", math.MinInt8, math.MaxInt8)
	fmt.Printf("Int16 range: %v ~ %v\n", math.MinInt16, math.MaxInt16)
	fmt.Printf("Int32 range: %v ~ %v\n", math.MinInt32, math.MaxInt32)
	fmt.Printf("Int64 range: %v ~ %v\n", math.MinInt64, math.MaxInt64)
	fmt.Printf("Uint8 range: %v ~ %v\n", 0, math.MaxUint8)
	fmt.Printf("Uint16 range: %v ~ %v\n", 0, math.MaxUint16)
	fmt.Printf("Uint32 range: %v ~ %v\n", 0, math.MaxUint32)
	fmt.Printf("Uint64 range: %v ~ %d\n", 0, uint64(math.MaxUint64))
	splitLine()
}

func floatValue() {
	var f64 float64 = 7.0
	var f64Value2 = 3.0
	fmt.Println("7.0/3.0 =", f64/f64Value2)

	var f32 float32
	f32 = 2.2
	f64 = 1.1
	fmt.Println("float64 + float32 =", float32(f64)+f32)

	var f = 3.0
	fmt.Println(reflect.TypeOf(f).Kind())
}

func complexValue() {
	// var cv complex64
	cv := 1.2 + 12i
	fmt.Println(cv)
	fmt.Println("complexValue 實數 =", real(cv))
	fmt.Println("complexValue 虛數 =", imag(cv))
	fmt.Println(complex(3.2, 12))
}

func stringValue() {
	str := "Hello world!"
	fmt.Println("1" + "1")
	fmt.Println(len(str))
	fmt.Println(str[0])
	fmt.Println(str[0:5])
	fmt.Println(str[0:5] + " world")
	fmt.Printf("%c", str[0])
}

func boolValue() {
	var b1, b2 bool = true, false
	fmt.Printf("b1 = %t\nb2 = %t\n", b1, b2)
	fmt.Printf("b1 && b2 = %t\n", b1 && b2)
	fmt.Printf("b1 || b2 = %t\n", b1 || b2)
	fmt.Printf("!b1 = %t\n", !b1)
	fmt.Printf("!b2 = %t\n", !b2)
}

func splitLine() {
	fmt.Println("-------------------------------------------------------------")
}
