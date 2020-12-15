package main

import "fmt"

func main() {
	start := []int{20, 9, 11, 0, 1, 2}
	prev := start[len(start)-1]
	nums := make(map[int][2]int)
	for i, v := range start {
		nums[v] = [2]int{-1, i}
	}

	for i := len(start); i < 30000000; i++ {
		if nums[prev][0] == -1 {
			prev = 0
			nums[prev] = [2]int{nums[0][1], i}
		} else {
			entry := nums[prev]
			prev = entry[1] - entry[0]

			if _, present := nums[prev]; present {
				nums[prev] = [2]int{nums[prev][1], i}
			} else {
				nums[prev] = [2]int{-1, i}
			}
		}
	}
	fmt.Println(prev)
}
