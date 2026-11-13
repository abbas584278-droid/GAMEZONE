from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/freefire")
def freefire():
    return render_template("freefire.html")

@app.route("/minecraft")
def minecraft():
    return render_template("minecraft.html")

@app.route("/gta")
def gta():
    return render_template("gta.html")
if __name__ == "__main__":
    app.run(debug=True)