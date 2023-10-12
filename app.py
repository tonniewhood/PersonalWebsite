from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def english():
    return render_template("english.html")
    
@app.route("/russian")
def russian():
    return render_template("russian.html")
    