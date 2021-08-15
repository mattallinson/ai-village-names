#!/usr/bin/python3
from flask import Flask, render_template, url_for, redirect, session
from waitress import serve

from forms import ParameterForm
from textgenrnn import textgenrnn
import os

def village_maker(textgen, temperature=1.0, prefix=None):
	villages = textgen.generate(5, temperature=temperature, prefix=prefix, 
		return_as_list=True)
	return villages

# Initialise app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")	

# Imports weights
textgen = textgenrnn('villages_2e_2021.hdf5') 

@app.route("/", methods=['GET', 'POST'])
def index():
	# Makes blank list of villages
	if 'villages' in session:
		session['villages'] = session.get('villages')
	else:
		session['villages'] = []

	form = ParameterForm()

	if form.validate_on_submit():
		user_prefix = form.prefix.data.title()
		user_temperature = float(form.temperature.data)
				
		'''code below makes 5 new village name and addes them to the
		list of village names, which then gets passed to render_template
		'''

		session['villages'].extend(
			village_maker(textgen, 
				temperature=user_temperature, 
				prefix=user_prefix))

		return render_template("index.html", 
			villages=session['villages'][::-1], #list in reverse order
			form=form)

	return render_template("index.html", 
		villages=session['villages'], 
		form=form)

@app.route("/clear-list", methods=['GET', 'POST'])
def clear_list():
	session.pop('villages')
	return redirect(url_for('index'))

if __name__ == '__main__':
	serve(app, host='0.0.0.0', port=5000)