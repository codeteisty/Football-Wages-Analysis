from flask import Flask, request, render_template
from functions import response
app = Flask(__name__)





@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/average_wages', methods=["GET", "POST"])
def count():
    if request.method == 'POST':
        x = request.form['predict']

        return render_template('wage_prediction.html', result=response(x))
    else:
        return render_template('wage_prediction.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)