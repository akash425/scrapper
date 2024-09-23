import requests
from bs4 import BeautifulSoup
import time

def extract_society_data(society_name, location):
    """
    Extracts publicly available data about a society on 99acres.com.

    Args:
        society_name (str): Name of the society to search for.
        location (str): Optional location to refine the search.

    Returns:
        dict: A dictionary containing the extracted data, or None if no results found.
    """

    base_url = "https://www.99acres.com/search/property/sell/{}/{}".format(location, society_name)
    headers = {"User-Agent": "Python Script v1.0 (your_email@example.com)"}  # Add your email

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

    soup = BeautifulSoup(response.content, "lxml")

    # Extract data based on 99acres' HTML structure (replace placeholders with selectors)
    data = {
        "society_name": society_name,  # May already be provided
        "location": "",  # Extract from search results or input
        "price_range": "",  # Extract based on selectors
        "description": "",  # Extract from property details page
        "amenities": [],  # Extract list of amenities
        # Add more data points as needed
    }

    # Implement logic to find property listings within the society
    # and extract details from each listing or use pagination

    # Example (replace with specific selectors):
    listings = soup.find_all("div", class_="srp-tuple__description")
    # for listing in listings:
        # Extract details from each listing and update the data dictionary

    # Implement pagination to scrape multiple pages of results (if applicable)

    time.sleep(2)  # Add a delay between requests

    return data

if __name__ == "__main__":
    society_name = input("Enter society name: ")
    location = input("Enter location (optional): ")
    extracted_data = extract_society_data(society_name, location)

    if extracted_data:
        print(extracted_data)
    else:
        print("No data found for the given society.")