from flask import Flask, render_template
from disk_analyzer import disk_test
import json

app = Flask(__name__)

@app.route('/disk-status')
def disk_analyzer():
    disk_test()
    with open('disk_status.json', 'r') as f:
        veriler = json.load(f)
    return render_template('disk-status.html', veriler=veriler)

if __name__ == '__main__':
    app.run(debug=True)