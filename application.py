
# Import statements


from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for
)

import pickle
import numpy as np




application = Flask(__name__)

# Home page

@application.route("/")
def hello_world():
    return render_template('index.html')


@application.route("/result", methods = ('GET', 'POST'))
def search():
    if request.method == 'POST':
        passw = request.form.get('password')

        def transformPassword(pWord):
            pWord = str(pWord)
            length = len(pWord)
            charNum = 0
            if (pWord.isalpha()==0 & pWord.isdigit()==0):
                charNum = 1
            capLetter = 0
            if (pWord.upper() != pWord and pWord.lower() != pWord):
                capLetter = 1
            specialChar = 1
            if(pWord.isalnum()==1):
                specialChar = 0
            return np.array([length, charNum, capLetter, specialChar]).reshape(1, -1)

        def finale(pas):
            with open('pickleFuncs/pickle_func.p', 'rb') as f: rfc = pickle.load(f)
            pasw = rfc.predict(pas)
            return pasw


        result = finale(transformPassword(passw))
        return render_template('result.html', result=result)
