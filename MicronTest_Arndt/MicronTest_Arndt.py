import random as r
import math as m
from flask import Flask, request, render_template 

app = Flask(__name__)

#########################
#To Run with Python 3.x,
# set FLASK_APP=MicronTest_Arndt.py
# flask run
#
# Enter URL like example "http://localhost:5000/mc_pi/1000" 
# Optionally enter number of iterations into dialogue box
#########################


#https://gist.github.com/louismullie/3769218
def montePi(total=1000):
    inside = 0
    # Total number of darts to throw.

    # Iterate for the number of darts.
    for i in range(0, total):
        # Generate random x, y in [0, 1].
        x2 = r.random()**2
        y2 = r.random()**2
        # Increment if inside unit circle.
        if m.sqrt(x2 + y2) < 1.0:
          inside += 1
        # inside / total = pi / 4
    pi = (float(inside) / total) * 4
    return pi



@app.route('/mc_pi/<int:iterations_id>')
def show_total(iterations_id):
    return render_template('my-form.html', total_id=str(montePi(iterations_id)),
                           iterations_id=iterations_id)


@app.route('/mc_pi/<int:total_id>', methods=['POST'])
def show_total_post(total_id):
    text = request.form['text']
    processed_text = montePi(int(text))
    return "MontePi estimate: " + str(processed_text)
