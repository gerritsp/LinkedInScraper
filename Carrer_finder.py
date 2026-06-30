import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_career_page(website):
    response = requests.get(website)

    soup = BeautifulSoup(response.text, "html.parser")

    career_links = []
    for link in soup.find_all("a"):
        href = str(link.get("href"))

        if "career" in href.lower():
            career_links.append(href)

    print(career_links)

    for link in soup.find_all("a"):
        href = str(link.get("href"))
        # print(href)

        if "career" in href.lower():
            full_url = urljoin(website, href)
            return href, full_url

        if "job" in href.lower():
            return href






    return None
def find_job_posting(career_page):
    response = requests.get(career_page)