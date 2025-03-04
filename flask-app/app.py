from flask import Flask, render_template  # Make sure to import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the index.html file

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Runs the app on port 80
