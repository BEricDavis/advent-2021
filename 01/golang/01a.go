package main

import (
	"bufio"
	"fmt"
	"os"
	"log"
)

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func main() {
	// open file for reading line by line
	lines, err := readLines("../../data/01/inputa.txt")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}
	for i, line := range lines {
		fmt.Println(i, line)
	}
}

// Naive file open and read - whole file at once
// func check(e error) {
// 	if e != nil {
// 		panic(e)
// 	}
// }

// func main() {
// 	dat, err := os.ReadFile("../../data/01/inputa.txt")
// 	check(err)
// 	fmt.Print(string(dat))
// }