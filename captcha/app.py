from flask import Flask,request,make_response,render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        response = make_response(render_template("form.html"))
        return response
    elif request.method == "POST":
        secret = "YOUR_SECRET"
        recaptcha_response = request.form["g-recaptcha-response"]
        r=requests.post('https://www.google.com/recaptcha/api/siteverify',data = {'secret':secret,'response':recaptcha_response})

        if r.json()['success']:
            response = make_response(render_template("pass.html"))
            return response
        else:
            response = make_response(render_template("fail.html"))
            return response

if __name__ == '__main__':
        app.run()
