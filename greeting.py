from flask import Flask, render_template, request, flash, url_for, redirect
app=Flask(__name__,template_folder='templates')
app.secret_key="3"
# route/ is the main route of the application
@app.route("/")
def index():
    flash("What's your name")
    return render_template("index.html")
# route/greet is used to direct the app to a route is used for flashing a greeting message to the user
@app.route("/greet",methods=["POST","GET"])
def greater():
    if request.method=="POST":
        name=request.form["name_input"]
        return redirect(url_for("ask_age",name=name))
    return render_template("index.html")
    # flash("Hi "+str(request.form[])+" Great to see you")

@app.route("/ask_age",methods=["POST","GET"])
def ask_age():
    name=request.args.get("name")
    if request.method=="POST":
        age=request.form["age_input"]
        return redirect(url_for("ask_occupation",name=name,age=age))
    flash(f"Hi {name}, how old are you?")
    return render_template("ask_age.html",name=name)

@app.route("/ask_occupation",methods=["POST","GET"])
def ask_occupation():
    name=request.args.get("name")
    age=request.args.get("age")
    if request.method=="POST":
        occupation=request.form["occupation_input"]
        return redirect(url_for("show_info", name=name, age=age, occupation=occupation))
    flash(f"What is your occupation?")
    return render_template("ask_occupation.html", name=name, age=age)

@app.route("/show_info",methods=["POST","GET"])
def show_info():
    name = request.args.get("name")
    age = request.args.get("age")
    occupation = request.args.get("occupation")
    return render_template("show_info.html", name=name, age=age, occupation=occupation)


if __name__=="__main__":
    app.run(debug=True)