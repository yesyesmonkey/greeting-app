from flask import Flask, render_template, request, flash
app=Flask(__name__,template_folder='templates')
app.secret_key="3"
@app.route("/")
def index():
    flash("What's your name")
    return render_template("index.html")
@app.route("/greet",methods=["POST","GET"])
def greater():
    flash("Hi "+str(request.form["name_input"])+" Great to see you")
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True)