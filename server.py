import requests
import smtplib
from flask import Flask, render_template, request

app = Flask(__name__)

API_URL = "https://api.npoint.io/99d4a015926e75e97b22"
response = requests.get(API_URL).json()

@app.route("/")
def home():
    return render_template("index.html", all_posts=response)

@app.route("/posts/<int:num>")
def show(num):
    for post in response:
        if post["id"] == num:
            return render_template("post.html", post=post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    my_mail = "vpn1vishal@gmail.com"
    password = "ubieddhximrjadwk"
    if request.method == "POST":
        form = request.form
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(my_mail, password)
            server.sendmail(my_mail, "thakurcmp1@gmail.com",
                            msg=f"Subject: Really nigga \n\n"
                                f"Name: {form['name']} \n"
                                f"Email: {form['email']} \n"
                                f"Phone: {form['phone']} \n"
                                f"Message: {form['message']}")
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)

if __name__ == "__main__":
    app.run(debug=True)
