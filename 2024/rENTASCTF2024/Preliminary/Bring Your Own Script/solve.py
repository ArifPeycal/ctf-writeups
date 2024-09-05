import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from urllib.parse import unquote


def scrape_website(url,output_file):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(response.text)
            with open(output_file, 'a', encoding='utf-8') as file:
                file.write(response.text)
                # Check if the target string is present
            if '.jpg' in response.text:
                print(f"Found flag at {url}")
                exit()

            # Find all directories inside #directories .directory-link
            directories = soup.select('#directories .directory-link')
                
            # Extract and print the directory names
            for directory in directories:
                absolute_url = urljoin(url, directory['href'])
                print(f"Visiting: {unquote(absolute_url)}")
                scrape_website(absolute_url,output_file)

        except requests.exceptions.RequestException as e:
            print(f"Error accessing: {e}")

if __name__ == "__main__":
    # Replace 'http://example.com' with the URL of the website you want to scrape
    start_url = 'https://byos.ctf.rawsec.com/root/'
    output_file = "scraped.txt"
    scrape_website(start_url,output_file)
