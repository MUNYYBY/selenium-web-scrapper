from flask import Flask, request, jsonify, send_from_directory
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from Drivers.chrome_driver import init_chrome_driver
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Initialize global variables for ChromeDriver
chrome_service, chrome_options = init_chrome_driver()

@app.route("/", methods=['GET'])
def root():
    return send_from_directory('static', 'index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Preliminary URL validation
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({'error': 'Page not found or invalid URL'}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Invalid URL or request error'}), 400

    try:
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.get(url)

        # Check if the page loaded successfully
        if "404" in driver.title or driver.current_url.startswith("data:") or driver.current_url.startswith("about:"):
            return jsonify({'error': 'Page not found or invalid URL'}), 404

        # Get the page source
        page_source = driver.page_source

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style", "svg", "head", "header", "nav", "sidebar"]):
            script.decompose()

        # Get text
        text = soup.get_text()        

        return jsonify({'content': text})
    except WebDriverException as e:
        return jsonify({'error': 'Failed to load the page. Make sure the URL is correct.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
