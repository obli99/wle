from flask import Flask
from flask import jsonify
from scrape import scraping

app = Flask(__name__)

@app.route('/link/<path:link>')
def index(link):
    return jsonify(Item=scraping(link))

    
if __name__=='__main__':
    app.run(debug=True)