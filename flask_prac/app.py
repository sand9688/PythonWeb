from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('addrbook.html')
@app.route('/pbook', methods= ['POST', 'GET'])
def result():
    if request.method == 'POST':
        val = request.form
        return render_template('pbook.html',result = val)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)