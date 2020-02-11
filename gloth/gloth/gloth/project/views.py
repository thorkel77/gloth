import os
from werkzeug import secure_filename
from flask import Flask, request, redirect, url_for, render_template, flash
from wtforms import validators, SelectField, SubmitField, BooleanField, TextAreaField, StringField

app = Flask(__name__)
app.config.from_object("project.config.Config")

from .forms import PatientForm, MedicForm, Medic_choicesForm
from .utils import traitement_class,pathologyChoices


@app.route("/", methods=["GET", "POST"])
@app.route('/index', methods=["GET","POST"])
def index():
    form2 = PatientForm()

    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required.")
            return render_template("index.html", title="Gloth", subtitle="test", patient_form=form2, name="Ynov")
        else:
            data = request.args.get(form)
            return redirect(url_for('medic_choices'), data=data)

    return render_template("index.html", title="Gloth", subtitle="subtitle", patient_form=form2, name="Ynov")

@app.route("/medic_choices", methods=["GET", "POST"])
def medic_choices():
    form = Medic_choicesForm()

    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required.")
            return render_template("medic_choices.html", title="Gloth", subtitle="test", Medic_choices_Form=form, name="Ynov")
        else:
            data = request.args.get(form)
            return redirect(url_for('medic'), data=data)

    return render_template("medic_choices.html", title="Gloth", subtitle="subtitle", Medic_choices_Form=form, name="Ynov")




@app.route('/medic', methods=["GET","POST"])
def medic():
    form = MedicForm(request.form)
    patho_id = (request.form.get("pathology"))
    patho = pathologyChoices()
    patho_icd = 'J45'
    p= []
    a= []
    for value in patho:
        p.append(value[0]) 
        a.append(patho_id)
        if value[0] == int(patho_id):
            patho_icd = value[1]
            # a.append(value[1])
            break
    
    classTraitement = traitement_class(patho_icd)
   
    user_id = (request.form.get("user"))
    return render_template("medic.html", name="Ynov", pathology=patho_id, user=user_id, traitement_class=classTraitement,patho=patho, p=p, a=a )

