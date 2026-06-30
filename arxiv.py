import requests
import xml.etree.ElementTree as ET
from paper import Paper


query = "quantum computing"

url = (
    "http://export.arxiv.org/api/query?"
    f"search_query=all:{query}"
    "&start=0"
    "&max_results=5"
)

response = requests.get(url)
root = ET.fromstring(response.text)
ns = {
    "atom": "http://www.w3.org/2005/Atom"
}
entries = root.findall("atom:entry", ns)
# print(len(entries))
# print(entries)

for entry in entries:
    # for child in entry:
    #     print(child.tag)

    summary = entry.find("atom:summary", ns)
    for link in entry.findall("atom:link", ns):
        print(link.attrib)
    print(summary.text)
    print('\n')

    title = entry.find("atom:title", ns)

    print(title.text)

# print(root.tag)
# print(response.status_code)
# print(response.text[:1000])