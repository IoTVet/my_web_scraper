import requests
from bs4 import BeautifulSoup
import sqlite3

# The URL of the webpage you want to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all headings, paragraphs, and links
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    paragraphs = soup.find_all('p')
    links = soup.find_all('a', href=True)

    # Connect to the SQLite database (or create it)
    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()

    # Create a table to store the data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scraped_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            content TEXT
        )
    ''')

    # Insert headings into the database
    for heading in headings:
        cursor.execute('INSERT INTO scraped_data (type, content) VALUES (?, ?)', ('Heading', heading.get_text(strip=True)))

    # Insert paragraphs into the database
    for paragraph in paragraphs:
        cursor.execute('INSERT INTO scraped_data (type, content) VALUES (?, ?)', ('Paragraph', paragraph.get_text(strip=True)))

    # Insert links into the database
    for link in links:
        cursor.execute('INSERT INTO scraped_data (type, content) VALUES (?, ?)', ('Link', link.get('href')))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Data has been saved to scraped_data.db")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
