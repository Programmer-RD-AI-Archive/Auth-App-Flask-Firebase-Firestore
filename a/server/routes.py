from server import *
from server.db.add_info import *
from server.db.auth import *
import random


@app.route("/")
def home():
    try:
        info = dict(request.headers)
        print(info)
        add_info(info)
        urls = [
            "https://digitalsynopsis.com/wp-content/uploads/2015/10/gif-icons-menu-transition-animations-send-mail.gif",
            "https://i.pinimg.com/originals/a2/b7/c8/a2b7c87c0e93b44e9289fafea2aef020.gif",
            "https://i.pinimg.com/originals/77/0c/1e/770c1e178dc59710dc365a7ff1d8a94c.gif",
        ]
        img = random.choice(urls)
        return render_template("home.html", img=img)
    except:
        urls = [
            "https://i.pinimg.com/originals/4c/22/18/4c2218f5cc96ba76c0e590cd1dadb1bc.gif",
            "https://i.pinimg.com/originals/70/ce/41/70ce41310f8a9c2a84e97b57198015d9.gif",
            "https://cdn.dribbble.com/users/2480087/screenshots/7009361/media/5be4690e38762fd53647912018e86189.gif",
            "https://media.tenor.com/images/c48003cc85f49ab072d0a819d63da772/tenor.gif",
        ]
        url = random.choice(urls)
        return render_template("Error.html", img=url)


def sign_in_(user_name_or_email, password):
    try:
        si = Sign_In(user_name_or_email=user_name_or_email, password=password)
        result = si.check()
        print(result)
        return result
    except:
        return [False, ["An Error Occured ! "]]


@app.route("/Sign/In", methods=["POST", "GET"])
@app.route("/Sign/In/", methods=["POST", "GET"])
def sign_in():
    try:
        info = dict(request.headers)
        print(info)
        add_info(info)
        if (
            "Signed Up" in session
            and session["Signed Up"] is True
            and "User Name" in session
            and "Password" in session
        ):
            result = sign_in_(
                user_name_or_email=session["User Name"], password=session["Password"]
            )
            if result[0]:
                session["Auth"] = True
                session.pop("Signed Up", None)
                session.pop("User Name", None)
                session.pop("Password", None)
                for x in result[1]:
                    flash(x, "success")
                return redirect("/Send/Email(s)")
            for x in result[1]:
                flash(x, "danger")
        if request.method == "POST":
            user_name_or_email = request.form["UNOE"]
            password = request.form["P"]
            result = sign_in_(user_name_or_email=user_name_or_email, password=password)
            if result[0]:
                session["Auth"] = True
                session.pop("Signed Up", None)
                session.pop("User Name", None)
                session.pop("Password", None)
                for x in result[1]:
                    flash(x, "success")
                return redirect("/Send/Email(s)")
            for x in result[1]:
                flash(x, "danger")
            return redirect("/Sign/In/")
        else:
            return render_template("sign_in.html")
    except:
        urls = [
            "https://i.pinimg.com/originals/4c/22/18/4c2218f5cc96ba76c0e590cd1dadb1bc.gif",
            "https://i.pinimg.com/originals/70/ce/41/70ce41310f8a9c2a84e97b57198015d9.gif",
            "https://cdn.dribbble.com/users/2480087/screenshots/7009361/media/5be4690e38762fd53647912018e86189.gif",
            "https://media.tenor.com/images/c48003cc85f49ab072d0a819d63da772/tenor.gif",
        ]
        url = random.choice(urls)
        return render_template("Error.html", img=url)


def sign_up_(user_name, email, password):
    try:
        su = Sign_Up(email=email, password=password, user_name=user_name)
        result = su.add_to_db()
        print(result)
        return result
    except:
        return [False, ["An Error Occured ! "]]


@app.route("/Sign/Up", methods=["POST", "GET"])
@app.route("/Sign/Up/", methods=["POST", "GET"])
def sign_up():
    try:
        info = dict(request.headers)
        print(info)
        add_info(info)
        if request.method == "POST":
            user_name = request.form["UN"]
            password = request.form["P"]
            email = request.form["E"]
            result = sign_up_(user_name=user_name, password=password, email=email)
            if result[0]:
                for x in result[1]:
                    flash(x, "success")
                session["Signed Up"] = True
                session["User Name"] = user_name
                session["Password"] = password
                return redirect("/Sign/In")
            for x in result[1]:
                flash(x, "danger")
            return redirect("/Sign/Up")
        else:
            return render_template("sign_up.html")
    except:
        urls = [
            "https://i.pinimg.com/originals/4c/22/18/4c2218f5cc96ba76c0e590cd1dadb1bc.gif",
            "https://i.pinimg.com/originals/70/ce/41/70ce41310f8a9c2a84e97b57198015d9.gif",
            "https://cdn.dribbble.com/users/2480087/screenshots/7009361/media/5be4690e38762fd53647912018e86189.gif",
            "https://media.tenor.com/images/c48003cc85f49ab072d0a819d63da772/tenor.gif",
        ]
        url = random.choice(urls)
        return render_template("Error.html", img=url)


@app.route("/Send/Email(s)", methods=["POST", "GET"])
@app.route("/Send/Email(s)/", methods=["POST", "GET"])
def send_email():
    try:
        info = dict(request.headers)
        print(info)
        add_info(info)
        if "Auth" in session and session["Auth"] is True:
            if request.method == "POST":
                to_email = request.form["TE"]
                subject = request.form["S"]
                body = request.form["B"]
                sm = send_mail(to_email=to_email, subject=subject, body=body)
                if sm:
                    flash("Email Sent ! ", "success")
                urls = [
                    "https://i.pinimg.com/originals/4c/22/18/4c2218f5cc96ba76c0e590cd1dadb1bc.gif",
                    "https://i.pinimg.com/originals/70/ce/41/70ce41310f8a9c2a84e97b57198015d9.gif",
                    "https://cdn.dribbble.com/users/2480087/screenshots/7009361/media/5be4690e38762fd53647912018e86189.gif",
                    "https://media.tenor.com/images/c48003cc85f49ab072d0a819d63da772/tenor.gif",
                ]
                url = random.choice(urls)
                return render_template("Error.html", img=url)
            else:
                return render_template("send_email.html")
        else:
            urls = [
                "https://i.pinimg.com/originals/4c/22/18/4c2218f5cc96ba76c0e590cd1dadb1bc.gif",
                "https://i.pinimg.com/originals/70/ce/41/70ce41310f8a9c2a84e97b57198015d9.gif",
                "https://cdn.dribbble.com/users/2480087/screenshots/7009361/media/5be4690e38762fd53647912018e86189.gif",
                "https://media.tenor.com/images/c48003cc85f49ab072d0a819d63da772/tenor.gif",
            ]
            url = random.choice(urls)
            return render_template("Error.html", img=url)
    except:
        urls = [
            "https://i.pinimg.com/originals/4c/22/18/4c2218f5cc96ba76c0e590cd1dadb1bc.gif",
            "https://i.pinimg.com/originals/70/ce/41/70ce41310f8a9c2a84e97b57198015d9.gif",
            "https://cdn.dribbble.com/users/2480087/screenshots/7009361/media/5be4690e38762fd53647912018e86189.gif",
            "https://media.tenor.com/images/c48003cc85f49ab072d0a819d63da772/tenor.gif",
        ]
        url = random.choice(urls)
        return render_template("Error.html", img=url)


@app.route("/Log/Out")
def log_out():
    try:
        info = dict(request.headers)
        print(info)
        add_info(info)
        if "Auth" in session:
            session.pop("Auth", None)
        else:
            flash("First Create A Account Log In ! ", "danger")
            return redirect("/")
    except:
        urls = [
            "https://i.pinimg.com/originals/4c/22/18/4c2218f5cc96ba76c0e590cd1dadb1bc.gif",
            "https://i.pinimg.com/originals/70/ce/41/70ce41310f8a9c2a84e97b57198015d9.gif",
            "https://cdn.dribbble.com/users/2480087/screenshots/7009361/media/5be4690e38762fd53647912018e86189.gif",
            "https://media.tenor.com/images/c48003cc85f49ab072d0a819d63da772/tenor.gif",
        ]
        url = random.choice(urls)
        return render_template("Error.html", img=url)
