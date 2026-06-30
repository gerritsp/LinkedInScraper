import requests
from bs4 import BeautifulSoup

def find_company_website(company_name):
    search_url = f"https://www.google.com/search?q={company_name}+official+website"

    headers = {
        "User-Agent":
        "Mozilla/5.0"
    }

    response = requests.get(search_url, headers=headers)

    print(response.status_code)

if __name__ == "__main__":
    find_company_website("OpenAI")
