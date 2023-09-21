from flask import Flask

app = Flask(__name__)

# Disable strict slashes for all routes
app.url_map.strict_slashes = False

# Route for the root URL "/"
@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"

# Route for "/hbnb"
@app.route('/hbnb')
def hbnb():
    return "HBNB"

# Route for "/c/<text>"
@app.route('/c/<text>')
def c_text(text):
    # Replace underscores with spaces in the text
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500)
