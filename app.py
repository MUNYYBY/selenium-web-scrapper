from flask import Flask, request, jsonify
from selenium import webdriver
from Drivers.chrome_driver import init_chrome_driver

app = Flask(__name__)

# Initialize global variables for ChromeDriver
chrome_service, chrome_options = init_chrome_driver()

@app.route("/", methods=['GET'])
def root():
    return 'You have reached web scrapper'

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
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
