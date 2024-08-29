from flask import Flask, request, jsonify
from selenium import webdriver
from Drivers.chrome_driver import init_chrome_driver
from Utils.clean_text import clean_text
from bs4 import BeautifulSoup

app = Flask(__name__)

# Initialize global variables for ChromeDriver
chrome_service, chrome_options = init_chrome_driver()

@app.route("/", methods=['GET'])
def root():
    return 'You have reached web scraper'

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.get(url)
        
        # Get the page source
        page_source = driver.page_source
        
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "svg", "head"]):
            script.decompose()
        
        # Get text
        text = soup.get_text()        
        
        return jsonify({'content': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)