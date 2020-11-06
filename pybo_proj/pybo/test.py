from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test.html', name=request.args.get("name"))


app.run(host='0.0.0.0')
