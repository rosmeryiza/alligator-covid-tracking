''' Scraping the UF Health COVID results web page
'''

from bs4 import BeautifulSoup
import requests
from datetime import date
import time
import csv

# UF Health Testing Dashboard
url = "https://coronavirus.ufhealth.org/screen-test-protect-2/about-initiative/testing-dashboard/"

def scrape_results (uf_url):
    # get the UF Health Testing Dashboard
    page = requests.get(uf_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # save page into BS object
    content = soup.find("section", class_="entry-content")

    # find the article tags - each article is a container of results
    articles = content.find_all('article')
    # next steps narrow down content by tag to ultimately get just the numbers
    # create empty list to get the header tags
    headers = []
    #iterate through articles to get the header tags and contents
    for a in articles:
        header = a.find('header')
        headers.append(header)

    # create empty list to get the header tags
    h3_list = []
    #iterate through headers to get the h tags and contents
    for h in headers:
        h3 = h.find('h3')
        h3_list.append(h3)

    # create a final list to take in the numbers
    list_final = []
    # add the date as the first field in the csv
    today = date.today()
    # format date to m/d/y
    list_final.append(today.strftime("%m/%d/%y"))

    #iterate through h to get the numbers
    for h in h3_list:
        # strip the numbers for excess formatting
        span = h.find('span').text.strip()
        list_final.append(span)

    # return the final list to plug into csv
    return (list_final)


def write_csv(results):
    # open the csv to track the data
    file = open('uf.csv', 'a')

    csvwriter = csv.writer(file, delimiter=",")
    # write the final list into the csv
    csvwriter.writerow(results)
    # close the file
    file.close()

# save the scraping into a list
results_list = scrape_results(url)
# give list to write function to add to csv
write_csv(results_list)