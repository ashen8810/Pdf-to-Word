from flask import Flask,session,render_template,request,redirect,url_for,flash
import pyrebase
from werkzeug.utils import secure_filename
app = Flask(__name__)
global m
import matplotlib.image as img
m= None
config = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": "",
    "databaseURL":""

    }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app.config['UPLOAD_FOLDER'] = "./uploads"
app.config["MAX_CONTENT_PATH"] = 10000
app.secret_key = ""

def checkimagevalidity(name):
    flag = False
    names= ["pdf"]
    for i in names:
        if i in name:
            return True
    return flag

@app.route("/",methods=["POST","GET"])
def home():
    msgg=""
    if "user" in session:
        if request.method == 'POST':
            f = request.files['file']
            flag = checkimagevalidity(str(f.filename))
            if flag == False:
                flash("Enter Valid PDF")
                return render_template("index.html",validity="Check The PDF that you have uploaded")
            j=secure_filename(f.filename)
            f.save(j)
            print(j)



            sessionmail = session["user"]
            from pdf import conv
            nameword = conv(j,sessionmail)
            from emial import sendword
            import os

            sendword(sessionmail,nameword)
            msgg="Please Check Your Email"
            os.remove(j)
            os.remove(nameword)


        return render_template("index.html",msg=msgg)
    else:
        return render_template("login.html")


@app.route("/login",methods= ["POST","GET"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        global m
        m=email
        password = request.form.get("password")
        try:
            user=auth.sign_in_with_email_and_password(email,password)
            info = auth.get_account_info(user["idToken"])
            if info["users"][0]["emailVerified"] == False:
                return render_template("verify.html")
            session["user"]=email
        except:
            flash("Wrong Pasword")
            return render_template("login.html",msg="Invalid Email Or Password")
        return render_template("index.html")
    if "user" in  session:
        return render_template("index.html")
    return render_template("login.html")


@app.route("/verify",methods=['GET', 'POST'])
def verify():
    return render_template("verify.html")


@app.route("/logout")
def logout():
    try:
        session.pop("user")
    except:
        return redirect("/login")
    return redirect("/login")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if "user" in session:
        return render_template("index.html")
    if request.method == "POST":
        emailn = request.form.get("email")
        passwordn = request.form.get("password")
        cpassword = request.form.get("confirmpassword")

        if passwordn != cpassword:
            flash("hello")
            return render_template("signup.html",m="Password didnt match")
        print(emailn)

        try:
            user2 = auth.create_user_with_email_and_password(emailn,passwordn)
            k=auth.send_email_verification(user2['idToken'])
            print(k)

            return render_template("verify.html")

            # return render_template("index.html")
            # session["user"]=email
        except:
            return "Failed to Login"
    return render_template("signup.html")

@app.route("/contact", methods=["POST","GET"])
def contact():
    mm= "Massage Has Been Sent.. We Will Reply You Soon"
    if request.method == "POST":
        emailn = request.form.get("email")
        passwordn = request.form.get("password")
        sub = request.form.get("subject")
        msg = request.form.get("message")
        flash("hello")
        from emial import sendMsg
        try:
            sendMsg(emailn,msg,sub)
        except:
            mm="Please fill the data correctly"
        return render_template("Contact.html",m=mm)
    return render_template("Contact.html")

@app.route("/resetpwd",methods = ["POST","GET"])
def reset():
    if request.method == "POST":

        emailn = request.form.get("email")
        print(emailn)
        try:
            auth.send_password_reset_email(emailn)
        except:
            flash("You dont have an account for this Email - ")
            return render_template("resetpwd.html",msg = emailn)

    return render_template("resetpwd.html")




if __name__ == "__main__":
    app.run()