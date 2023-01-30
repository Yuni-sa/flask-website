from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/servers")
def servers():
    df = pd.read_excel("data.xlsx")
    table = df.to_html()
    return render_template("Servers.html", table=table)

@app.route("/phones")
def phones():
    df = pd.read_excel("phones.xlsx")
    table = df.to_html()
    return render_template("phones.html", table=table)

if __name__ == '__main__':
    app.run(debug=True)