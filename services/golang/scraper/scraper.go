package scraper

import (
	"encoding/xml"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"time"
)

type Item struct {
	XMLName xml.Name `xml:"item"`
	Name    string   `xml:"name"`
	Link    string   `xml:"link"`
}

type Items struct {
	XMLName xml.Name `xml:"items"`
	Items   []Item   `xml:"item"`
}

func (b *Item) GetName() string {
	return b.Name
}

func (b *Item) GetLink() string {
	return b.Link
}

func Scrape(URL string) {
	time.Sleep(100 * time.Millisecond)

	req, err := http.NewRequest(http.MethodGet, URL, nil)

	// create the request
	if err != nil {
		fmt.Printf("client: could not create request: %s\n", err)
		os.Exit(1)
	}

	// make the http request
	res, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Printf("client: error making http request: %s\n", err)
		os.Exit(1)
	}

	fmt.Printf("client: got response!\n")
	fmt.Printf("client: status code: %d\n", res.StatusCode)

	// get the body of the response
	resBody, err := ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Printf("client: could not read response body: %s\n", err)
		os.Exit(1)
	}
	//fmt.Printf("client: response body: %s\n", resBody)

	var item Items
	xml.Unmarshal(resBody, &item)
	fmt.Println(item)

	for i := 0; i < len(item.Items); i++ {
		fmt.Println("User Name: " + item.Items[i].Name)
		x := item.Items[0]
		fmt.Println(x.GetName())
	}
}
