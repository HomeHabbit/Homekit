#! /usr/bin/python
# -*- coding:utf-8 -*-

from subprocess import call
from flask import Flask
app = Flask(__name__)

@app.route('/controller/light/<light_id>/ON')
def lightOn(light_id):
        print "LIGHT ON"
        call(["/var/www/html/radioEmission","0",light_id,"17613", "on"])
        return "1"

@app.route('/controller/light/<light_id>/OFF')
def lightOff(light_id):
        print "LIGHT OFF"
        call(["/var/www/html/radioEmission","0",light_id,"17613", "off"])
        return "0"

@app.route('/')
def index():
        print "INDEX"
        return "INDEX"

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080)
