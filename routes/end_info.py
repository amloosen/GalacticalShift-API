"""users routes"""
from flask import current_app as app, jsonify, request
from models import EndInfo, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob

@app.route('/end_info/create/<user_id>/<study_part>', methods=['POST', 'GET'])

def post_end_info(user_id,study_part):

    content     = request.json
    user = EndInfo()

    user.user_id = str(user_id)

    user.study_part = int(study_part)
    user.startTime = str(content['startTime'])
    user.sectionStartTime = str(content['sectionStartTime'])
    user.feedback    = str(content['feedback'])
    user.bonus   = str(content['bonus'])



    BaseObject.check_and_save(user)

    result = dict({"success": "yes"})

    return jsonify(result)
