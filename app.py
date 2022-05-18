from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():     #index関数の定義
    return render_template("index.html")   #index.htmlファイルを読み込む

@app.route("/article1")
def article1():     
    return render_template("article1.html")

@app.route("/article2")
def article2():     
    return render_template("article2.html")

if __name__ == '__main__':
    app.run(debug=True)   #デバッグモードOn