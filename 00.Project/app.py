import os
from flask import Flask, render_template, request

app = Flask(__name__)
add_list=[]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/function', methods=['GET','POST'])
def input():
    if request.method == 'POST':
        val = request.form['주소']
        f_image = request.files['image']
        fname= f_image.filename
        print(val, fname)
        filename= os.path.join(app.static_folder,'upload/')+fname
        f_image.save(filename)
        return render_template('output.html', result=val, fname=fname)
    else:
        return  render_template('input.html')
@app.route('/center_list', methods=['GET','POST'])
def center_list():
    return render_template('carcenter_list.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
