package main

import (
	"github.com/snorresovold/newswars/services/golang/scraper"
)

func main() {
	scraper.Scrape("https://www.vg.no/rss/feed")
}
