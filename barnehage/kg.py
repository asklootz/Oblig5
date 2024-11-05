from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import pandas as pd
from kgmodel import (Foresatt, Barn, Soknad, Barnehage)
from kgcontroller import (decrease_barnehage_plasser, form_to_object_soknad, get_all_data_as_html, insert_soknad, commit_all, select_alle_barnehager, select_alle_soknader, update_barnehage_plasser)
import os
import shutil

#Resetter data-arket
#Virker kun en gang
#os.remove("kgdata.xlsx")
#os.popen("copy /Oblig5/kgdata.xlsx kgdata.xlsx")

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY' # nødvendig for session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/barnehager')
def barnehager():
    information = select_alle_barnehager()
    return render_template('barnehager.html', data=information)

@app.route('/behandle', methods=['GET', 'POST'])
def behandle():
    if request.method == 'POST':
        sd = request.form
        print(sd)
        alle_barnehager = select_alle_barnehager()
        svar = 'AVSLAG'
        for barnehage in alle_barnehager:
            if barnehage.barnehage_navn == sd['liste_over_barnehager_prioritert_5']:
                if barnehage.barnehage_ledige_plasser > 0:
                    svar = 'TILBUD'
                    decrease_barnehage_plasser(barnehage.barnehage_navn)
                    
        log = insert_soknad(form_to_object_soknad(sd, svar))
        print(log)
        session['information'] = sd
        session['svar'] = svar
        return redirect(url_for('svar')) #[1]
        return render_template('soknad.html', error="Barnehagen er full")
    else:
        return render_template('soknad.html')
            
@app.route('/svar')
def svar():
    information = session['information']
    return render_template('svar.html', data=information, svar=session['svar'])

@app.route('/commit')
def commit():
    commit_all()
    """information_barnehager = select_alle_barnehager()
    
    informarion_soknader = select_alle_soknader()
    return render_template('commit.html', data = information_barnehager and informarion_soknader)"""
    data = get_all_data_as_html()
    return render_template('commit.html', tables=data)

@app.route('/soknader')
def soknader():
    information = select_alle_soknader()
    return render_template('soknader.html', data = information)
    

app.run()



"""
Referanser
[1] https://stackoverflow.com/questions/21668481/difference-between-render-template-and-redirect
"""

"""
Søkeuttrykk

"""