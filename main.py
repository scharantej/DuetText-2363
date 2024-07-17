
# main.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return render_template('submit.html', name=name, message=message)

if __name__ == '__main__':
    app.run(debug=True)
