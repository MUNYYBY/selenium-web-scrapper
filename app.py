# app.py
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Setup Chrome options for headless browsing
    options = Options()
    options.headless = True

    # Fetch the appropriate ChromeDriver
    service = Service(ChromeDriverManager().install())
    
    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        
        # Extract textual content from the page
        content = driver.page_source
        # For a more specific extraction, adjust this part
        text_content = content  # Placeholder for actual content extraction

        return jsonify({'content': text_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
