# AI Web Scraper with DeepSeek

Welcome to the AI Web Scraper project! This project is designed to scrape web content, clean it, and parse it using AI techniques. The project leverages Streamlit for the user interface, Selenium for web scraping, and various Python libraries for content processing.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Setting Up ChromeDriver](#setting-up-chromedriver)
- [Credits](#credits)
- [License](#license)

## Introduction

This project was created by Ansh Jain. It provides a simple and efficient way to scrape web content and process it using AI techniques. The project leverages OpenRouter's DeepSeek API for parsing the scraped content.

## Features

- **Web Scraping**: Uses Selenium to scrape websites.
- **HTML Parsing**: Uses BeautifulSoup to parse and clean HTML content.
- **AI-Powered Parsing**: Utilizes OpenRouter's DeepSeek API to extract specific information from the scraped content.
- **Interactive UI**: Built with Streamlit for an interactive user interface.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/jansh7784/Deepseek-Web-Scrapper
    cd Deepseek-Web-Scrapper
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Set Up Environment Variables**:
    Create a `.env` file in the project root directory and add your OpenRouter API key:
    ```env
    OPENROUTER_API_KEY=your_openrouter_api_key
    ```

## Usage

1. **Run the Streamlit App**:
    ```sh
    streamlit run main.py
    ```

2. **Enter the Website URL**:
    - Input the URL of the website you want to scrape.

3. **Scrape the Website**:
    - Click the "Scrape Website" button to scrape the website and extract the DOM content.

4. **View DOM Content**:
    - Expand the "View DOM Content" section to see the extracted DOM content.

5. **Parse with DeepSeek**:
    - Enter your parsing instructions in the "Parse/Chat Instructions" text area.
    - Click the "Parse with DeepSeek" button to extract specific information based on your instructions.

## Setting Up ChromeDriver

To use Selenium with Chrome, you need to have ChromeDriver installed on your machine. Follow these steps:

1. **Download ChromeDriver**:
    - Go to the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/downloads) and download the version that matches your Chrome browser version.

2. **Add ChromeDriver to PATH**:
    - Extract the downloaded file and add the directory containing `chromedriver` to your system's PATH.

    - On Windows:
        ```sh
        setx PATH "%PATH%;C:\path\to\chromedriver"
        ```
    - On macOS/Linux:
        ```sh
        export PATH=$PATH:/path/to/chromedriver
        ```

## Credits

**Made by [Ansh Jain](https://www.linkedin.com/in/ansh--jain). Powered by OpenRouter.ai's DeepSeek API.**

## License

This project is licensed under the MIT License. See the LICENSE file for details.
