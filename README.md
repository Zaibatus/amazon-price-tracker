# Automated Amazon Price Tracker

This Python script scrapes an Amazon product page to check for the price and sends an email notification when the price falls below a specified threshold.

**Features**
- Scrapes an Amazon product page to retrieve the current price.
- Checks if the price is below a defined threshold.
- Sends an email notification when the price drops below the threshold.
- Automated Amazon product price tracking

**Script Details**

Scraping the Amazon Product Page: the script sends a GET request to the Amazon product page using the specified headers. It then parses the HTML response using BeautifulSoup to extract the price and product name.

Sending Email Notification: if the extracted price is below the defined threshold, the script sends an email notification using the smtplib library. The email contains the product name, current price, and a link to the product page.

**Notes**

- Ensure that the User-Agent in the URL_HEADERS dictionary matches your browser's user agent to avoid request blocking by Amazon.
- Be cautious with sending login credentials in scripts. Consider using application-specific passwords or OAuth for added security.
- Amazon may block requests from automated scripts. Use the script responsibly to avoid getting banned.


