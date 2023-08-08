"""users routes"""
from flask import current_app as app, jsonify, request
from models import StartInfo, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob


@app.route('/start_info/<user_id>/<study_part>', methods=['GET'])

def get_user(user_id,study_part):


    query = StartInfo.query.filter(StartInfo.user_id==user_id, StartInfo.study_part==study_part)
    if query != None:
        print(query)

    block  = query.first_or_404()

    result                   = {}

    arr_id                   = block.get_id() # .replace('  ',' ').split(' ')
    result['id']             = arr_id


    arr_study_part               = block.get_study_part() # [0] # .replace('  ',' ').split(' ')
    result['study_part']   = arr_study_part

    # arr_user               = block.get_startTime().replace('  ',' ').split(' ')
    # result['startTime']   = arr_user

    arr_user            = block.get_user_id().replace('  ',' ').split(' ')
    result['user_id']   = arr_user

    app.logger.info(result)
    return jsonify(result), 200


@app.route('/start_info/create/<user_id>/<study_part>', methods=['POST', 'GET'])

def post_user(user_id,study_part):

    content     = request.json
    user = StartInfo()

    user.user_id          = str(user_id)

    user.study_part     = int(study_part)
    user.startTime       = str(content['startTime'])
    user.dateAndTime      = str(content['dateAndTime'])


    BaseObject.check_and_save(user)

    result = dict({"success": "yes"})

    return jsonify(result)
