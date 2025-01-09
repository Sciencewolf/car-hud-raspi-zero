from flask import Flask, render_template, jsonify
from flask_cors import CORS
from utils import Utils

app = Flask(__name__)
CORS(app)

utils: Utils = Utils()

@app.route("/")
def index():
    return render_template(template_name_or_list="index.html")

@app.route("/get-speed")
def get_speed():
    return jsonify({"speed": utils.get_speed()})

@app.route("/get-rpm")
def get_rpm():
    return jsonify({})