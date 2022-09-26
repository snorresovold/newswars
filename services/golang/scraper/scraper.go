package scraper

import (
	"encoding/xml"
	"fmt"
	"io/ioutil"
	"net/http"
)

// our struct which contains the complete
// array of all Users in the file
type Channel struct {
	XMLName xml.Name `xml:"channel"`
	Items   []Item   `xml:"item"`
}

// the user struct, this contains our
// Type attribute, our user's name and
// a social struct which will contain all
// our social links
type Item struct {
	XMLName xml.Name `xml:"item"`
	Title   string   `xml:"title"`
	Link    string   `xml:"link"`
}

// a simple struct which contains all our
// social links

func Scrape() {
	// Open our xmlFile
	xmlFile, err := http.Get("https://www.vg.no/rss/feed")
	// if we os.Open returns an error then handle it
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("Successfully Opened users.xml")
	// defer the closing of our xmlFile so that we can parse it later on
	//defer xmlFile.Close()

	// read our opened xmlFile as a byte array.
	byteValue, _ := ioutil.ReadAll(xmlFile.Body)

	// we initialize our Users array
	var users Channel
	// we unmarshal our byteArray which contains our
	// xmlFiles content into 'users' which we defined above
	xml.Unmarshal(byteValue, &users)

	// we iterate through every user within our users array and
	// print out the user Type, their name, and their facebook url
	// as just an example
	for i := 0; i < len(users.Items); i++ {
		fmt.Println("User Name: " + users.Items[i].Title)
		fmt.Println("Facebook Url: " + users.Items[i].Link)
	}

}
