from flask import render_template, request
from app import app

from models.process_model import Process, ProcessForm


@app.route('/history',  methods=['GET'])
def history():
    form = ProcessForm()
    return render_template('history.html', form=form)


@app.route('/process',  methods=['GET', 'POST'])
def process():
    if request.method == "POST":
        True

    return render_template('process.html')
