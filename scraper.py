import csv
import requests
import re

# Function to fetch the CSV data from the Google Spreadsheet
def fetch_csv_data(spreadsheet_url):
    response = requests.get(spreadsheet_url)
    if response.status_code != 200:
        print(f"Failed to fetch CSV data, status code: {response.status_code}")
        return None
    return response.text

# URL of the Google Spreadsheet
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1raT38KNw9tflEc6kU0xlyFaPFD3x3cDtLltflEA3ZtM/edit#gid=0&fvid=1824689148"

# Fetch the CSV data from the spreadsheet
csv_data = fetch_csv_data(spreadsheet_url)
if csv_data is None:
    exit()

# Parse the CSV data
reader = csv.reader(csv_data.splitlines())

# Extract and filter all links from the CSV
links = set()  # Use a set to store unique links
for row in reader:
    for cell in row:
        extracted_links = re.findall(r'(https?://\S+)', cell)
        links.update(extracted_links)

# Filter links for those starting with "https://pandabuy.page.link"
pandabuy_links = [link for link in links if link.startswith("https://pandabuy.page.link")]

# Save all links to a file
with open("all_links.txt", "w") as file:
    for link in links:
        file.write(link + "\n")

# Save the filtered Pandabuy links to a file
with open("pandabuy_links.txt", "w") as file:
    for link in pandabuy_links:
        file.write(link + "\n")

print("All links have been saved in 'all_links.txt'.")
print("Pandabuy links have been saved in 'pandabuy_links.txt'.")
