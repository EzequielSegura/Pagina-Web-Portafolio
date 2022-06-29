from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/Proyecto1')
def proyecto1():
    return render_template ("proyecto1.html")

if __name__ == "__main__":
    app.run(debug=True)