# Flask Web Scraper

## Overview

This project is a web scraper built with Flask and Selenium that extracts textual content from web pages. It uses headless Chrome to fetch and parse content without a graphical interface.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **Selenium**: A tool for automating web browsers, used for scraping content.
- **ChromeDriver**: A driver for Chrome that Selenium uses to control the browser.
- **webdriver-manager**: A library that automatically handles the ChromeDriver installation.

## Features

- **Scrape textual content**: Extracts textual content from specified web pages.
- **Headless browsing**: Runs Chrome in headless mode for efficient scraping.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MUNYYBY/selenium-web-scraper.git
   cd selenium-web-scraper
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask Application**

   ```bash
   python app.py
   ```

2. **Send a POST Request to the `/scrape` Endpoint**

   You can use tools like `curl` or Postman to send a POST request to the `/scrape` endpoint with a JSON payload containing the URL.

   Example with `curl`:

   ```bash
   curl -X POST http://127.0.0.1:5000/scrape -H "Content-Type: application/json" -d '{"url": "http://example.com"}'
   ```

## Project Structure

```
selenium-web-scraper/
│
├── Drivers/
│   └── chrome_driver.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

- `Drivers/chrome_driver.py`: Contains the `init_chrome_driver` function to set up ChromeDriver.
- `app.py`: The main Flask application file with the `/scrape` endpoint.
- `requirements.txt`: Lists the project dependencies.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## Contact

For any questions or suggestions, please contact muneeburryhman@gmail.com.
