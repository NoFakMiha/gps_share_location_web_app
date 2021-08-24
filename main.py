from flask import Flask, render_template, request, redirect, url_for, flash

import os



app = Flask(__name__)
app.secret_key = f"{os.environ['APP_FLASK_KEY']}"

@app.route("/", methods=["GET", "POST"])
def location():
    return render_template("index2.html")



if __name__ == "__main__":
    app.run()