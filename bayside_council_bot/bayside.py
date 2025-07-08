import requests
import os
from bs4 import BeautifulSoup

# Step 1: Fetch the HTML content of the webpage
url = "https://www.bayside.vic.gov.au/council/meetings-agendas-and-minutes/council-minutes"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Step 2: Find and filter PDF links
pdf_links = []

for link in soup.find_all("a", href=True):
    link_text = link.get_text(strip=True).lower()
    href = link["href"]

    if (
        "council meeting minutes" in link_text
        and "special" not in link_text
        and href.endswith(".pdf")
    ):
        full_url = href if href.startswith("http") else f"https://www.bayside.vic.gov.au{href}"
        pdf_links.append(full_url)

# Step 3: Print or save the links
print("Filtered Council Meeting Minutes PDF links:\n")
for pdf in pdf_links:
    print(pdf)

os.makedirs("bayside_minutes", exist_ok=True)

for pdf_url in pdf_links:
    filename = pdf_url.split("/")[-1]
    filepath = os.path.join("bayside_minutes", filename)

    if not os.path.exists(filepath):  # Avoid redownloading
        print(f"Downloading: {filename}")
        pdf_data = requests.get(pdf_url)
        with open(filepath, "wb") as f:
            f.write(pdf_data.content)
    else:
        print(f"Already downloaded: {filename}")
