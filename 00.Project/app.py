from flask import Flask, render_template, request
from extra import extra_bp
import os

app = Flask(__name__)
app.secret_key='qwert12345'
app.register_blueprint(extra_bp, url_prefix='/extra')

@app.route('/')
def main():
    return render_template('base.html')

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/input')
def input():
    return render_template('input.html')

if __name__ == '__main__':
    app.run()
