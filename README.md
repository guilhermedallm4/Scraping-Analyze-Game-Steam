# Steam Review Scraper

## Description

This code is a Python script that scrapes data from Steam game reviews. It uses the Selenium library to interact with a web browser, BeautifulSoup to parse HTML pages, and regular expressions (regex) to manipulate strings. The code is set to run in "headless" mode, meaning it doesn't display a graphical interface during execution.

## Required Libraries

To run the code, you need to have the following Python libraries installed:

- `selenium`: Used for automating interactions with the browser.
- `beautifulsoup4`: Used for parsing web page HTML.
- `re`: Used for working with regular expressions.
- `json`: Used for reading and writing data in JSON format.
- `unicodedata`: Used for working with Unicode characters.

You can install the required libraries using the following command:
```
pip install selenium
pip install beautifulsoup4
pip install json
pip install unicodedata
```

## JSON Structure

The collected data is stored in JSON files with the following structure:


```json
{
    "recommendProduct": "number of people who found it useful",
    "numberAward": "number of awards",
    "classificationPost": "Recommended or Not Recommended",
    "timeRegistered": "time registerd",
    "texto": "review text",
    "author": "author's name",
    "urlPerfil": "author's profile URL"
}
```
## How the Code Works

The code starts by setting up a web driver for Chrome and navigating to a Steam game review page. It then scrapes information from the reviews, such as the recommendation status, number of awards, review classification, time registered, review text, author's name, and author's profile URL.

The scraped information is stored in a JSON structure, and the code appends it to a JSON file. This allows you to collect and analyze data from Steam game reviews efficiently.

To run the code, simply execute the main function. Make sure you have the required libraries installed and that the Chrome web driver is configured correctly.


