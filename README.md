# webscraper
This scraper takes the html of the URL and parses it for a "Add to cart" button and a "Out of Stock" text. If "Add to cart" exists but "Out of Stock" doesn't, then the output will be "Add to cart" and "In stock." If not, then the output will be "Out of Stock," "Out of Stock."

# blocked headers
if forbidden
  url = 'https://<url>'
  headers = {'user-agent': '<find in network in dev console of web page>'}
  r = requests.get(url, headers = headers)
    headers = headers is true
https://www.youtube.com/watch?v=gRLHr664tXA&ab_channel=TechWithTim
https://stackoverflow.com/questions/57155387/workaround-for-blocked-get-requests-in-python
https://requests.readthedocs.io/en/latest/
