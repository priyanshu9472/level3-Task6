
from flask import Flask, render_template, request
from selenium import webdriver
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_data(url):
    try:
        # Launch Chrome webdriver (you need to have chromedriver installed)
        driver = webdriver.Chrome()
        
        # Load the page
        driver.get(url)
        
        # Wait for page to load completely (adjust the time according to your page loading time)
        driver.implicitly_wait(10)
        
        # Get page source after JavaScript rendering
        page_source = driver.page_source
        
        # Close the webdriver
        driver.quit()
        
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Find the desired element by class name
        element = soup.find('div', class_='_1kidPb') #q8WwEU(div class name in flipkart)  # this is your div class name which is in flipkart html structure
        
        if element:
            return element.text.strip()
        else:
            return "Data not found. Check if the class name 'example-class' exists in the HTML structure."
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None

    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            data = fetch_data(url)
        else:
            data = "Please provide a URL"

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
