import os
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Load environment variables
AUTH = os.getenv("SCRAPING_PROXY_AUTH")
if not AUTH:
    raise ValueError("SCRAPING_PROXY_AUTH is not set. Update your .env or GitHub Secrets.")

SBR_WEBDRIVER = f"https://{AUTH}@brd.superproxy.io:9515"

def scrape_website(url):
    print('Connecting to Scraping Browser...')
    try:
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    except Exception as e:
        print(f"Error initializing Selenium WebDriver: {e}")
        raise
    
    options = ChromeOptions()
    options.add_argument("--headless")  # Ensure headless mode for cloud deployment
    
    with Remote(sbr_connection, options=options) as driver:
        print('Connected! Navigating...')
        driver.get(url)
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = "\n".join(
        line.strip() for line in soup.get_text(separator="\n").splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)]
