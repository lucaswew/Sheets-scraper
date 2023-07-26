import praw
import requests
from bs4 import BeautifulSoup
import time
import os
from tqdm import tqdm
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from concurrent.futures import ThreadPoolExecutor



# User agent for Reddit API requests
user_agent = "MyRedditScraper/1.0 by MyName (contact@example.com)"

def get_links_from_subreddit(subreddit_name, num_pages, progress_file):
    reddit = praw.Reddit(
        user_agent=user_agent,
        client_id='gN2RpPpmfwfumVncw4um4A',
        client_secret='rPFeQHYNOiGF_sRuD-DYXulrateImQ',
    )

    subreddit = reddit.subreddit(subreddit_name)

    pandabuy_links = []
    weidian_links = []

    # Load progress if the file exists and is not empty
    last_page_scraped = 0
    if os.path.exists(progress_file):
        with open(progress_file, 'r') as f:
            last_page_scraped_str = f.read().strip()
            if last_page_scraped_str:
                last_page_scraped = int(last_page_scraped_str)

    remaining_pages = num_pages
    with tqdm(total=num_pages * 25, desc=f"Scraping r/{subreddit_name}") as pbar:
        for i, submission in enumerate(subreddit.new(limit=num_pages * 25), start=1):  # Modify this line
            if i <= last_page_scraped:
                pbar.update(1)
                continue

            url = submission.url
            if 'pandabuy' in url:
                pandabuy_links.append(url)
            elif 'weidian.com' in url:
                weidian_links.append(url)
            pbar.update(1)

            # Save progress after scraping each page
            with open(progress_file, 'w') as f:
                f.write(str(i))

            # Additional debugging: Print a message for each new post checked
            print(f"Checking post {i} of {num_pages * 25} on r/{subreddit_name}")

            remaining_pages -= 1
            if remaining_pages <= 0:
                break

            # Add a delay between API requests to avoid rate limiting
            time.sleep(2)  # Adjust the delay as needed

    return pandabuy_links, weidian_links
    reddit = praw.Reddit(
        user_agent=user_agent,
        client_id='gN2RpPpmfwfumVncw4um4A',
        client_secret='rPFeQHYNOiGF_sRuD-DYXulrateImQ',
    )

    subreddit = reddit.subreddit(subreddit_name)

    pandabuy_links = []
    weidian_links = []

    # Load progress if the file exists and is not empty
    last_page_scraped = 0
    if os.path.exists(progress_file):
        with open(progress_file, 'r') as f:
            last_page_scraped_str = f.read().strip()
            if last_page_scraped_str:
                last_page_scraped = int(last_page_scraped_str)

    remaining_pages = num_pages
    with tqdm(total=num_pages * 25, desc=f"Scraping r/{subreddit_name}") as pbar:
        for i, submission in enumerate(subreddit.new(limit=num_pages * 25), start=1):  # Modify this line
            if i <= last_page_scraped:
                pbar.update(1)
                continue

            url = submission.url
            if 'pandabuy' in url:
                pandabuy_links.append(url)
            elif 'weidian.com' in url:
                weidian_links.append(url)
            pbar.update(1)

            # Save progress after scraping each page
            with open(progress_file, 'w') as f:
                f.write(str(i))

            remaining_pages -= 1
            if remaining_pages <= 0:
                break

            # Add a delay between API requests to avoid rate limiting
            time.sleep(2)  # Adjust the delay as needed

    return pandabuy_links, weidian_links

    reddit = praw.Reddit(
        user_agent=user_agent,
        client_id='gN2RpPpmfwfumVncw4um4A',
        client_secret='rPFeQHYNOiGF_sRuD-DYXulrateImQ',
    )

    subreddit = reddit.subreddit(subreddit_name)

    pandabuy_links = []
    weidian_links = []

    # Load progress if the file exists and is not empty
    last_page_scraped = 0
    if os.path.exists(progress_file):
        with open(progress_file, 'r') as f:
            last_page_scraped_str = f.read().strip()
            if last_page_scraped_str:
                last_page_scraped = int(last_page_scraped_str)

    remaining_pages = num_pages
    with tqdm(total=num_pages * 25, desc=f"Scraping r/{subreddit_name}") as pbar:
        for i, submission in enumerate(subreddit.new(limit=None), start=1):
            if i <= last_page_scraped:
                pbar.update(1)
                continue

            url = submission.url
            if 'pandabuy' in url:
                pandabuy_links.append(url)
            elif 'weidian.com' in url:
                weidian_links.append(url)
            pbar.update(1)

            # Save progress after scraping each page
            with open(progress_file, 'w') as f:
                f.write(str(i))

            remaining_pages -= 1
            if remaining_pages <= 0:
                break

            # Add a delay between API requests to avoid rate limiting
            time.sleep(2)  # Adjust the delay as needed

    return pandabuy_links, weidian_links

def create_spreadsheet(sheet_name):
    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('abstract-aloe-394017-73437cad8919.json', scope)
    client = gspread.authorize(creds)

    # Create a new Google Spreadsheet
    print(f"Creating spreadsheet: {sheet_name}")
    spreadsheet = client.create(sheet_name)
    print(f"Spreadsheet ID: {spreadsheet.id}")
    print(f"Spreadsheet URL: {spreadsheet.url}")  # Add this line to print the URL

    # Add two sheets for "pandabuy" and "weidian" links
    spreadsheet.add_worksheet(title='Pandabuy Links', rows='1000', cols='2')
    spreadsheet.add_worksheet(title='Weidian Links', rows='1000', cols='2')

    # Add headers to the sheets
    pandabuy_sheet = spreadsheet.get_worksheet(1)
    weidian_sheet = spreadsheet.get_worksheet(2)
    headers = ['URL', 'Title']
    pandabuy_sheet.insert_row(headers, index=1)
    weidian_sheet.insert_row(headers, index=1)

    # Make the spreadsheet public and set access level to "reader"
    spreadsheet.share('', perm_type='anyone', role='reader')

    return spreadsheet
    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('abstract-aloe-394017-73437cad8919.json', scope)
    client = gspread.authorize(creds)

    # Create a new Google Spreadsheet
    print(f"Creating spreadsheet: {sheet_name}")
    spreadsheet = client.create(sheet_name)
    print(f"Spreadsheet ID: {spreadsheet.id}")
    print(f"Spreadsheet URL: {spreadsheet.url}")  # Add this line to print the URL

    # Add headers to the first row of the spreadsheet
    headers = ['URL', 'Title']
    range_ = 'Sheet1'
    print(f"Updating range: {range_}")
    spreadsheet.values_update(
        range_,
        params={'valueInputOption': 'RAW'},
        body={'values': [headers]}
    )

    # Make the spreadsheet public and set access level to "reader"
    spreadsheet.share('', perm_type='anyone', role='reader')

    return spreadsheet

    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('abstract-aloe-394017-73437cad8919.json', scope)
    client = gspread.authorize(creds)

    # Create a new Google Spreadsheet
    print(f"Creating spreadsheet: {sheet_name}")
    spreadsheet = client.create(sheet_name)
    print(f"Spreadsheet ID: {spreadsheet.id}")
    print(f"Spreadsheet URL: {spreadsheet.url}")  # Add this line to print the URL

    # Add headers to the first row of the spreadsheet
    headers = ['URL', 'Title']
    range_ = 'Sheet1'
    print(f"Updating range: {range_}")
    spreadsheet.values_update(
        range_,
        params={'valueInputOption': 'RAW'},
        body={'values': [headers]}
    )

    return spreadsheet

    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('abstract-aloe-394017-73437cad8919.json', scope)
    client = gspread.authorize(creds)

    # Create a new Google Spreadsheet
    print(f"Creating spreadsheet: {sheet_name}")
    spreadsheet = client.create(sheet_name)
    print(f"Spreadsheet ID: {spreadsheet.id}")

    # Add headers to the first row of the spreadsheet
    headers = ['URL', 'Title']
    range_ = 'Sheet1'  # Modify this line
    print(f"Updating range: {range_}")
    spreadsheet.values_update(
        range_,
        params={'valueInputOption': 'RAW'},
        body={'values': [headers]}
    )

    return spreadsheet

    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('abstract-aloe-394017-73437cad8919.json', scope)
    client = gspread.authorize(creds)

    # Create a new Google Spreadsheet
    print(f"Creating spreadsheet: {sheet_name}")
    spreadsheet = client.create(sheet_name)
    print(f"Spreadsheet ID: {spreadsheet.id}")

    # Add headers to the first row of the spreadsheet
    headers = ['URL', 'Title']
    range_ = f'{sheet_name}'
    print(f"Updating range: {range_}")
    spreadsheet.values_update(
        range_,
        params={'valueInputOption': 'RAW'},
        body={'values': [headers]}
    )

    return spreadsheet

    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('abstract-aloe-394017-73437cad8919.json', scope)
    client = gspread.authorize(creds)

    # Create a new Google Spreadsheet
    print(f"Creating spreadsheet: {sheet_name}")
    spreadsheet = client.create(sheet_name)
    print(f"Spreadsheet ID: {spreadsheet.id}")

    # Add headers to the first row of the spreadsheet
    headers = ['URL', 'Title']
    range_ = f'{sheet_name}!A1:B1'
    print(f"Updating range: {range_}")
    spreadsheet.values_update(
        range_,
        params={'valueInputOption': 'RAW'},
        body={'values': [headers]}
    )

    return spreadsheet

    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('abstract-aloe-394017-73437cad8919.json', scope)
    client = gspread.authorize(creds)

    # Create a new Google Spreadsheet
    print(f"Creating spreadsheet: {sheet_name}")
    spreadsheet = client.create(sheet_name)

    # Add headers to the first row of the spreadsheet
    headers = ['URL', 'Title']
    range_ = f'{sheet_name}!A1:B1'
    print(f"Updating range: {range_}")
    spreadsheet.values_update(
        range_,
        params={'valueInputOption': 'RAW'},
        body={'values': [headers]}
    )

    return spreadsheet
    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('abstract-aloe-394017-73437cad8919.json', scope)
    client = gspread.authorize(creds)

    # Create a new Google Spreadsheet
    spreadsheet = client.create(sheet_name)

    # Add headers to the first row of the spreadsheet
    headers = ['URL', 'Title']
    spreadsheet.values_update(
        sheet_name,
        params={'valueInputOption': 'RAW'},
        body={'values': [headers]}
    )

    return spreadsheet

    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('abstract-aloe-394017-73437cad8919.json', scope)
    client = gspread.authorize(creds)

    # Create a new Google Spreadsheet
    spreadsheet = client.create(sheet_name)

    # Add headers to the first row of the spreadsheet
    headers = ['URL', 'Title']
    spreadsheet.values_update(
        f'{sheet_name}!A1:B1',
        params={'valueInputOption': 'RAW'},
        body={'values': [headers]}
    )

    return spreadsheet
    # Connect to Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('abstract-aloe-394017-73437cad8919.json', scope)
    client = gspread.authorize(creds)

    # Create a new Google Spreadsheet
    spreadsheet = client.create(sheet_name)

    # Add headers to the first row of the spreadsheet
    headers = ['URL', 'Title']
    spreadsheet.values_update(
        f'{sheet_name}!A1:B1',
        params={'valueInputOption': 'RAW'},
        body={'values': [headers]}
    )

    return spreadsheet

def scrape_and_save_content(links, spreadsheet):
    # Open the Google Spreadsheet sheets for pandabuy and weidian links
    pandabuy_sheet = spreadsheet.get_worksheet(1)
    weidian_sheet = spreadsheet.get_worksheet(2)

    def process_link(link):
        response = requests.get(link, headers={'User-Agent': user_agent})
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = "Title not found"
        try:
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text()
        except AttributeError:
            pass

        # Check if the link is pandabuy or weidian link
        if 'pandabuy' in link:
            # Append the pandabuy link and title to the Pandabuy Links sheet
            pandabuy_sheet.append_row([link, title])
        elif 'weidian.com' in link:
            # Append the weidian link and title to the Weidian Links sheet
            weidian_sheet.append_row([link, title])

        # Check for spreadsheet links and append them as well
        spreadsheet_links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.endswith('.csv') or href.endswith('.xls') or href.endswith('.xlsx'):
                spreadsheet_links.append(href)

        for spreadsheet_link in spreadsheet_links:
            if 'pandabuy' in spreadsheet_link:
                # Append the pandabuy spreadsheet link to the Pandabuy Links sheet
                pandabuy_sheet.append_row([f"Spreadsheet Link: {spreadsheet_link}", ""])
            elif 'weidian.com' in spreadsheet_link:
                # Append the weidian spreadsheet link to the Weidian Links sheet
                weidian_sheet.append_row([f"Spreadsheet Link: {spreadsheet_link}", ""])

        # Add a delay to avoid overloading the server
        time.sleep(0.5)  # Reduce the delay as needed

    def process_post(submission):
    # Process the main post for pandabuy and weidian links
        url = submission.url
    if 'pandabuy' in url:
        pandabuy_links.append(url)
    elif 'weidian.com' in url:
        weidian_links.append(url)

    # Process the comments for pandabuy and weidian links
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comment_text = comment.body
        if 'pandabuy' in comment_text:
            pandabuy_links.append(comment_text)
        elif 'weidian.com' in comment_text:
            weidian_links.append(comment_text)

    # Save progress after processing each post
    with open(progress_file, 'w') as f:
        f.write(str(i))

    # Use multi-threading to process links concurrently
    with ThreadPoolExecutor() as executor:
        executor.map(process_link, links)
    # Open the Google Spreadsheet sheets for pandabuy and weidian links
    pandabuy_sheet = spreadsheet.get_worksheet(1)
    weidian_sheet = spreadsheet.get_worksheet(2)

    for link in links:
        response = requests.get(link, headers={'User-Agent': user_agent})
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = "Title not found"
            try:
                title_tag = soup.find('title')
                if title_tag:
                    title = title_tag.get_text()
            except AttributeError:
                pass

            # Check if the link is pandabuy or weidian link
            if 'pandabuy' in link:
                # Append the pandabuy link and title to the Pandabuy Links sheet
                pandabuy_sheet.append_row([link, title])
            elif 'weidian.com' in link:
                # Append the weidian link and title to the Weidian Links sheet
                weidian_sheet.append_row([link, title])

            # Check for spreadsheet links and append them as well
            spreadsheet_links = []
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if href.endswith('.csv') or href.endswith('.xls') or href.endswith('.xlsx'):
                    spreadsheet_links.append(href)
            
            for spreadsheet_link in spreadsheet_links:
                if 'pandabuy' in spreadsheet_link:
                    # Append the pandabuy spreadsheet link to the Pandabuy Links sheet
                    pandabuy_sheet.append_row([f"Spreadsheet Link: {spreadsheet_link}", ""])
                elif 'weidian.com' in spreadsheet_link:
                    # Append the weidian spreadsheet link to the Weidian Links sheet
                    weidian_sheet.append_row([f"Spreadsheet Link: {spreadsheet_link}", ""])

            # Add a delay to avoid overloading the server
            time.sleep(1)  # Adjust the delay as needed
    # Open the Google Spreadsheet
    sheet = spreadsheet.sheet1

    for link in links:
        response = requests.get(link, headers={'User-Agent': user_agent})
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = "Title not found"
            try:
                title_tag = soup.find('title')
                if title_tag:
                    title = title_tag.get_text()
            except AttributeError:
                pass

            # Append the link and title to the Google Sheet
            sheet.append_row([link, title])

            # Check for spreadsheet links and append them as well
            spreadsheet_links = []
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if href.endswith('.csv') or href.endswith('.xls') or href.endswith('.xlsx'):
                    spreadsheet_links.append(href)
            
            for spreadsheet_link in spreadsheet_links:
                sheet.append_row([f"Spreadsheet Link: {spreadsheet_link}", ""])

            # Add a delay to avoid overloading the server
            time.sleep(1)  # Adjust the delay as needed

def main():
    subreddit_names = ['pandabuy', 'FashionReps']
    num_pages = 1500  # Change this value as needed, e.g., 5, 10, or more

    sheet_name = 'Links from Reddit'
    spreadsheet = create_spreadsheet(sheet_name)

    for subreddit_name in subreddit_names:
        progress_file = f'{subreddit_name}_progress.txt'
        print(f"Scraping r/{subreddit_name}...")
        pandabuy_links, weidian_links = get_links_from_subreddit(subreddit_name, num_pages, progress_file)

        # Remove progress file after scraping is done
        os.remove(progress_file)

        if not pandabuy_links and not weidian_links:
            print(f"No pandabuy or weidian links found on r/{subreddit_name}.")
        else:
            all_links = pandabuy_links + weidian_links
            if all_links:
                print(f"Found {len(all_links)} links on r/{subreddit_name}.")
                scrape_and_save_content(all_links, spreadsheet)

if __name__ == '__main__':
    main()
   
#add to the code to also click on posts and check the comments of the posts for weidian and pandabuy links 