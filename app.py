from flask import Flask,render_template,url_for,request,redirect
from prediction import PredictionForm
from Model import model
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")



app = Flask(__name__)
app.secret_key = "rupee"


@app.route("/")
@app.route("/home")
def home():
    return render_template("Main.html")


@app.route("/about",methods=["POST","GET"])
def about():
    return render_template("About.html")



@app.route("/view more",methods=["POST","GET"])
def view_more():
    return render_template("About.html")
app.add_url_rule("/","view more","view_more")


@app.route("/prediction",methods=["GET","POST"])
def prediction():
    form = PredictionForm()
    if form.is_submitted():
        data = list(request.form.values())[:-1]
        data = model.predict(np.array([data]))
        return render_template("Result.html",data =1)
    return render_template("Prediction.html",form=form)




port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='127.0.0.1', port=port)