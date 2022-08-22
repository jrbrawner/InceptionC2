from flask import Blueprint, render_template, flash, request, jsonify
from flask import current_app as app
from ..Classes.Server import Server
from ..Classes.Beacon import Beacon

app_bp = Blueprint('app', __name__)

server = Server('server')

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        server.start_server()
        return render_template('index.html')

@app.route("/message/", methods = ['POST'])
def send_message():

    if request.method == 'POST':
        beacon = Beacon('test', server.ip, server.port)
        beacon.send_msg(request.form['message'])
        return render_template('index.html')



