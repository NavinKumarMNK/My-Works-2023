package main

import (
	"errors"
	"fmt"
	"math/rand"
	"strings"
	"sync"
	"time"
	"unicode/utf8"
)

/*
	func print(printValue string) {
		fmt.Println(printValue)
	}
*/
func print(a ...interface{}) {
	fmt.Println(a...)
}

func intDivision(numerator int, denominator int) (int, int, error) {
	var err error // default nil
	if denominator == 0 {
		err = errors.New("cannot divide by zero")
		return 0, 0, err
	}
	var result int = numerator / denominator
	var remainder int = numerator % denominator
	return result, remainder, err
}

type owner struct {
	name string
}
type gasEngine struct {
	mpg       uint8
	gallons   uint8
	ownerInfo owner // we call also specify as owner where owner struct variables can be access directly from gasEngine struct
}
type electricEngine struct {
	mpkwh     uint8
	kwh       uint8
	ownerInfo owner
}

// methods to struct

func (e gasEngine) milesLeft() uint8 {
	return e.gallons * e.mpg
}
func (e electricEngine) milesLeft() uint8 {
	return e.kwh * e.mpkwh
}

type engine interface {
	milesLeft() uint8
}

func canMakeIt(e engine, miles uint8) {
	if miles <= e.milesLeft() {
		print("yes")
	} else {
		print("no")
	}
}

// Finds time for given array operation
func timeloop(slice []int, n int) time.Duration {
	var t0 = time.Now()
	for len(slice) < n {
		slice = append(slice, 1)
	}
	return time.Since(t0)
}

func square_slice(slice *[5]float32) [5]float32 {
	fmt.Printf("%p \n", &slice)
	for i := range slice {
		slice[i] = slice[i] * slice[i]
	}
	return *slice
}

var dbData = []string{"id1", "id2", "id3", "id4", "id5"} // Database
var wg = sync.WaitGroup{}                                // Wait Group for goroutines
var results = []string{}

// dbCall Simulation - plain
func dbCall(i int) {
	var delay float32 = rand.Float32() * 2000
	time.Sleep(time.Duration(delay) * time.Millisecond)
	print("Result : ", dbData[i])
	results = append(results, dbData[i])
	wg.Done()
}

// dbCall Simulation - with single mutex
var m1 = sync.Mutex{}

func dbCallSingleMutex(i int) {
	var delay float32 = rand.Float32() * 200 // {0, 1} scaled to {0, 2000}
	time.Sleep(time.Duration(delay) * time.Millisecond)
	print("Result : ", dbData[i])
	m1.Lock()
	results = append(results, dbData[i])
	m1.Unlock()
	wg.Done()
}

// dbCall Simulation - read and write lock()
var mRW = sync.RWMutex{}

func dbCallRWMutex(i int) {
	var delay float32 = rand.Float32() * 2000
	time.Sleep(time.Duration(delay) * time.Millisecond)
	save(dbData[i])
	log()
	wg.Done()
}

func save(result string) {
	mRW.Lock() // write lock
	results = append(results, result)
	mRW.Unlock()
}

func log() {
	mRW.RLock()
	print("The current results are: ", results)
	mRW.RUnlock()
}

// channels
func putInputChannel(c chan int) {
	c <- 123
}

func putInputChannelCont(c chan int) {
	defer close(c)
	for i := 0; i < 5; i++ {
		c <- i + 5
	}
	print("Exit Function")
}

func sumSlice[T int | float32](slice []T) T {
	var sum T
	for _, v := range slice {
		sum += v
	}
	return sum
}

func main() {
	fmt.Println("Hello World!!")

	// Datatypes
	var intNum int
	var floatNum float32
	intNum += 1
	fmt.Println(intNum)
	floatNum = 4.2
	fmt.Println(floatNum)

	var result1 float32 = float32(intNum) + floatNum
	fmt.Println(result1)

	var myRune rune = 'a'
	fmt.Println(myRune)

	var myString string = "Hello" + " " + `World
	!`
	fmt.Println(utf8.RuneCountInString(myString)) // Rune length
	fmt.Println(len(myString))                    // Bytes length

	var myBoolean bool = false // Default value is flase
	fmt.Println(myBoolean)

	myVar := "text"
	fmt.Println(myVar)

	var1, var2 := 1, 2
	fmt.Println(var1, var2)

	const myConst string = "const value"

	// functions
	print(myConst)
	var result, remainder, err = intDivision(5, 2)
	if err == nil {
		fmt.Printf("Result = %v %v %v \n", result, remainder, err)
	} else {
		fmt.Println(err.Error())
	}

	// switch cases
	switch {
	case err != nil:
		fmt.Println(err.Error())
	default:
		fmt.Println(result)
	}

	switch remainder {
	case 0:
		fmt.Println("The division was exact")
	}

	// arrays
	var intArr [3]int
	// var intArr [3]int = [3]int32{1, 2, 3}  or intArr := [3]int32{1, 2, 3} or [...]int32{1, 2, 3}
	intArr[0] = 1
	fmt.Println(intArr[0:3])
	fmt.Println(&intArr[0])

	// slice
	var intSlice []int32 = []int32{4, 5, 6}
	print(len(intSlice), cap(intSlice), &intSlice[0])
	intSlice = append(intSlice, 7)
	fmt.Println(intSlice)
	print(len(intSlice), cap(intSlice), &intSlice[0])

	// add multiple values to slice
	var intSlice2 []int32 = []int32{8, 9}
	intSlice = append(intSlice, intSlice2...)
	print(intSlice)

	// make slice
	var intSlice3 []int32 = make([]int32, 3, 8) // make(type, length, capacity)
	print(intSlice3)

	// map
	var myMap map[string]uint8 = make(map[string]uint8) // keys:string -> values:uint8
	print(myMap)

	var myMap2 = map[string]uint8{"Adam": 23, "Sara": 45}
	print(myMap2["Adam"])
	print(myMap2["Json"]) // even key doest exist returns some random value

	// handling non-exist value
	var age, ok = myMap2["Json"]
	if ok {
		print("The age is", age)
	} else {
		print("Invalid Name")
	}

	// iterator - for
	for name := range myMap2 {
		print("Name:", name)
	}
	for i, v := range intArr {
		print("index", i, "value", v)
	}
	// while
	i := 0      // var i int = 0
	for i < 3 { // for i:=10; i<10; i++
		print(i)
		i += 1
	}

	// Importance of preallocation
	var n int = 1000000
	var testSlice = []int{}
	var testSlice2 = make([]int, 0, n)
	print("Time without & with pre allocation", timeloop(testSlice, n), timeloop(testSlice2, n))

	// Strings & rune ; string is immutable
	var myString1 = "résumé" // utf-8
	var indexed = myString1[1]
	print(indexed, len(myString1))
	for i, v := range myString1 {
		print(i, v)
	}

	var myString2 = []rune("résumé") // utf-8
	var indexed1 = myString2[1]
	print(indexed1, len(myString2))
	for i, v := range myString2 {
		print(i, v)
	}

	// String Builder
	var strSlice = []string{"a", "b", "c"}
	var strBuilder strings.Builder
	for i := range strSlice {
		strBuilder.WriteString(strSlice[i])
	}
	var catStr = strBuilder.String()
	print(catStr)

	// Structs
	var myEngine gasEngine = gasEngine{mpg: 25, ownerInfo: owner{"Alex"}}
	myEngine.gallons = 10
	print(myEngine)

	// Anonymous struct
	var myEngine2 = struct {
		mpg     uint8
		gallons uint8
	}{25, 18}
	print(myEngine2)

	print(myEngine.milesLeft())

	canMakeIt(myEngine, 200)

	// pointers
	var p *int32 // can be assigned to new(int32)
	var i1 int32
	p = &i1
	*p = 4
	print(p, i1)

	// call by address
	var slice = [5]float32{1, 2, 3, 4}
	fmt.Printf("%p \n", &slice)
	var result2 [5]float32 = square_slice(&slice)
	print(result2, slice)

	// go routines
	t0 := time.Now()
	for i := 0; i < len(dbData); i++ {
		wg.Add(1)
		// go dbCallSingleMutex(i)
		// go dbCall(i)
		go dbCallRWMutex(i) // Kind EDA architecture, never waits
	}
	wg.Wait() // all tasks are completed
	print("Execution Time", time.Since(t0))
	print("The results are", results)

	// channels - {Hold Data, Thread Safe, Listen for Data}
	/* var c = make(chan int)
	c <- 1  // puts the value into unbuffered c and blocks for something to read
	var i2 = <-c
	print(i2)  fatal error: all goroutines are asleep - deadlock!
	*/

	//channels + goroutines
	var c = make(chan int)
	go putInputChannel(c)
	var inp = <-c
	print(inp)

	var c1 = make(chan int)
	go putInputChannelCont(c1)
	/* for i := 0; i < 5; i++ {
		print(<-c1)
	}*/
	for i := range c1 {
		print(i)
	}

	// buffered channels
	var cBuffered = make(chan int, 3)
	go putInputChannelCont(cBuffered)
	for i := range cBuffered {
		print(i)
		time.Sleep(time.Second * 1)
	}

	// Generics
	var intSlice1 = []int{1, 2, 3}
	print(sumSlice[int](intSlice1))

	var floatSlice = []float32{1, 2, 3}
	print(sumSlice[float32](floatSlice))
}
