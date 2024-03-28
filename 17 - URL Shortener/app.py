import string
import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dictionary to store the shortened URLs
url_map = {}

def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(length))
    return short_url

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']
        if not long_url.startswith('http://') and not long_url.startswith('https://'):
            long_url = 'http://' + long_url
        short_url = generate_short_url()
        url_map[short_url] = long_url
        return render_template('result.html', short_url=request.host_url + short_url)
    return render_template('home.html')

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_map:
        long_url = url_map[short_url]
        return redirect(long_url)
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)