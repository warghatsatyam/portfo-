from flask import Flask, render_template, request, redirect
from markupsafe import escape
from datetime import datetime
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


def write_to_db(data):
    with open('database.txt', mode='a') as database:
        currenttime = datetime.now().strftime("%H:%M:%S")
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(
            f'\n Username : {name} , Email : {email} , Subject : {subject} , Message = {message}, time = {currenttime}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        currenttime = datetime.now().strftime("%H:%M:%S")
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message, currenttime])


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Somethinng went wrong'
    else:
        return 'Something went wrong Try again next time !'
