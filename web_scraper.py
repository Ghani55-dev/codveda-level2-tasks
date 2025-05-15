# Import necessary modules
import requests  # For sending HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
import csv  # For writing scraped data to a CSV file

# Function to fetch and scrape article titles
def fetch_articles():
    url = "https://techcrunch.com/"  # Website to scrape
    response = requests.get(url)  # Send GET request to the website

    # IF statement to check if the request was successful
    if response.status_code != 200:
        print("❌ Failed to retrieve the page.")  # Error if page couldn't be fetched
        return  # Exit the function early

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <h2> elements (titles), specific to site layout
    articles = soup.find_all("h2")

    # Open a new CSV file to write the scraped titles
    with open("scraped_data.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title"])  # Write the header row

        # Loop through all the found article elements
        for article in articles:
            title = article.get_text(strip=True)  # Clean and extract the text
            if title:  # IF the title is not empty
                print("📰", title)  # Print the title
                writer.writerow([title])  # Write it to the CSV file

    print("✅ Scraped data saved to scraped_data.csv")  # Confirm save

# Main entry point of the script
if __name__ == "__main__":
    fetch_articles()
