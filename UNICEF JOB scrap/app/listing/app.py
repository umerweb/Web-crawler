from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    job_listings = []
    with open('listing/job_listings.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job_listings.append(row)
    return render_template('index.html', job_listings=job_listings)

if __name__ == '__main__':
    # Run the application on port 5001
    app.run(debug=True, port=5001)
