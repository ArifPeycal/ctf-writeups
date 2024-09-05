> Golang? What’s that?
```go
package main

import (
	"fmt"
	"os"
	"strings"
)

var flag = "iÛÛÜÖ×ÚáäÈÑ¥gebªØÔÍãâ£i¥§²ËÅÒÍÈä"

func init() {
	runed := []string{}
	z := rune(0)

	for _, v := range flag {
		runed = append(runed, string(v-z))
		z = v - z
	}

	flag = strings.Join(runed, "")
}

func main() {
	file, err := os.OpenFile("the", os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		fmt.Println(err)
		return
	}

	defer file.Close()
	if _, err := file.Write([]byte(flag)); err != nil {
		fmt.Println(err)
		return
	}
}
```
