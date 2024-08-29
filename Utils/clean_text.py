import re
from bs4 import BeautifulSoup

def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def extract_content_with_headings(soup):
    content = {"h1": [], "h2": [], "h3": [], "h4": [], "h5": [], "h6": [], "other": []}
    current_heading = None
    
    for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        if element.name.startswith('h'):
            current_heading = element.name
            content[current_heading].append({
                "heading": clean_text(element.get_text()),
                "content": []
            })
        elif element.name == 'p':
            text = clean_text(element.get_text())
            if text:
                if current_heading:
                    content[current_heading][-1]["content"].append(text)
                else:
                    content["other"].append(text)
    
    return content