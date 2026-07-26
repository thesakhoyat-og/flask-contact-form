# we have two kind of main request get req, post req, get req is used to get data from the server and post req is used to send data to the server. form is post req.

from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        with open("data.txt", "a") as f:
            f.write(f"the name is {request.form['name']}, the email is {request.form['email']}")
        return render_template("contact.html")
    else:
        return render_template("contact.html")
    
app.run(debug=True)