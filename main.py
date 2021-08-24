from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os

my_email = f"{os.environ['SEND_FROM_EMAIL']}"
password = f"{os.environ['SEND_FROM_EMAIL_PASSWORD']}"

app = Flask(__name__)
app.secret_key = f"{os.environ['APP_FLASK_KEY']}"

@app.route("/", methods=["GET", "POST"])
def location():
    return render_template("index2.html")

@app.route("/send/<gps>", methods=["GET", "POST"])
def send_gps(gps):
    striped_gps = gps.strip('"')


    username = request.form['username']
    email = request.form['email']
    try:
        with smtplib.SMTP("smtp.gmail.com",587, timeout=120) as connection: # put in time out so that it can connect
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs=email, msg=f"Subject:{username} "
                                                                       f"want to share location with you\n\n"
                                                                       f" I {username} want to to share my GPS location:\nGPS: {striped_gps}\n"
                                                                       f"Google maps link:\n"
                                                                       f" https://www.google.com/maps/search/{striped_gps} \n\n"
                                                                       f"Kind regards,\n"
                                                                       f"Dev. Miha Novak")
            connection.close()
            return redirect(url_for("location"))
    except:
        with smtplib.SMTP("smtp.gmail.com",587, timeout=120) as connection: # put in time out so that it can connect
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email, msg=f"Subject:{username} "
                                                                       f"want to share location with you\n\n"
                                                                       f" ERROR"
                                                                       f"\n\n"
                                                                       f"Kind regards,\n"
                                                                       f"Dev. Miha Novak")
        return redirect(url_for("location"))


if __name__ == "__main__":
    app.run()