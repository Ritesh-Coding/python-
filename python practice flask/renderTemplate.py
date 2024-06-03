from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


@app.route('/')
def input():
    return render_template('temp.html')

@app.route('/passing', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        result = request.form
        print(result)
        # Send result data to result_data HTML file
        return render_template("result_data.html", result=result)


if __name__=="__main__":
    app.run(debug=True)
