from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    if render_template == 'GET':
        return render_template('index.html')
@app.route('/input')
def input():
    if request.method == 'GET':
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
