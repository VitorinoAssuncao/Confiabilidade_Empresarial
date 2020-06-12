from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Flask
from enterprise_api.settings import DEBUG
from enterprise_api.settings import HOST
from enterprise_api.settings import PORT

from enterprise_api.actions.enterprise_actions import create

app_enterprise = Blueprint('app_enterprise',__name__)

@app_enterprise.route('/enterprise',methods=['POST'])
def post(): 
    enterprise_data = request.get_json()
    new_enterprise = create(enterprise_data)
    return jsonify(new_enterprise.serialize()),201