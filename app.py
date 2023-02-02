from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/mypage/me")
def mypage():
    return render_template("mysite.html")

@app.route("/mypage/contact")
def mypage_contact():
    return render_template("mysiteform.html")

@app.route("/me", methods=["post"])
def message():
 name = request.form['name'] 
 print(name)
 return name
 
 
if __name__ =='__main__':
    app.run(debug=True)

