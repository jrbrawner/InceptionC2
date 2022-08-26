from flask import Blueprint, render_template, flash, request, jsonify
from flask import current_app as app
from ..Classes.Server import Server

app_bp = Blueprint('app', __name__)

server = Server()

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        server.start_server()
        return render_template('index.html')

@app.route("/beacons/", methods = ['GET', 'POST'])
def manage():
    
    if request.method == 'GET':
        return render_template('beacons.html', server=server)

    if request.method == 'POST':
        server.send_message_to_beacon(request.form['beacon_name'], request.form['beacon_message'])
        return render_template('beacons.html', server=server)
    

@app.route("/message/", methods = ['POST'])
def send_message():

    if request.method == 'POST':
        
        test = server.create_beacon('')
        test.send_msg(request.form['message'])

        return render_template('index.html')




