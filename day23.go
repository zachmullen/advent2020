package main

import "fmt"

type node struct {
	val  int
	next *node
}

func main() {
	initial := []int{5, 6, 2, 8, 9, 3, 1, 4, 7}
	vals := [1e6]*node{} // node pointers indexed by value

	var prev *node
	for _, val := range initial {
		n := &node{
			val:  val,
			next: nil,
		}
		vals[val-1] = n
		if prev != nil {
			prev.next = n
		}
		prev = n
	}
	for i := 10; i <= 1e6; i++ {
		n := &node{
			val:  i,
			next: nil,
		}
		vals[i-1] = n
		prev.next = n
		prev = n
	}
	cur := vals[initial[0]-1]
	prev.next = cur // close loop

	for i := 0; i < 1e7; i++ {
		destVal := cur.val - 1
		if destVal < 1 {
			destVal = 1e6
		}
		// skip dest if it's in the removed set
		for cur.next.val == destVal ||
			cur.next.next.val == destVal ||
			cur.next.next.next.val == destVal {
			destVal--
			if destVal < 1 {
				destVal = 1e6
			}
		}
		dest := vals[destVal-1]
		removeStart := cur.next
		removeEnd := removeStart.next.next

		// move the nodes
		cur.next = removeEnd.next
		removeEnd.next = dest.next
		dest.next = removeStart

		cur = cur.next // next round
	}
	fmt.Println(vals[0].next.val * vals[0].next.next.val)
}
