"""users routes"""
from flask import current_app as app, jsonify, request
from models import TrainingB, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob


@app.route('/training_b/<user_id>/<study_part>', methods=['GET'])
def get_training_b(user_id, study_part):

    query = TrainingB.query.filter(
        TrainingB.user_id == user_id, TrainingB.study_part == study_part)
    if query != None:
        print(query)

    block = query.first_or_404()

    result = {}

    arr_id = block.get_id()  # .replace('  ',' ').split(' ')
    result['id'] = arr_id

    # [0] # .replace('  ',' ').split(' ')
    arr_study_part = block.get_study_part()
    result['study_part'] = arr_study_part

    # arr_user               = block.get_startTime().replace('  ',' ').split(' ')
    # result['startTime']   = arr_user

    arr_user = block.get_user_id().replace('  ', ' ').split(' ')
    result['user_id'] = arr_user

    app.logger.info(result)
    return jsonify(result), 200


@app.route('/training_b/create/<user_id>/<study_part>', methods=['POST', 'GET'])
def post_training_b(user_id, study_part):

    content = request.json
    user = TrainingB()

    user.user_id = str(user_id)

    user.study_part = int(study_part)
    user.startTime = str(content['startTime'])
    user.sectionStartTime = str(content['sectionStartTime'])


    user.corr_pos = str(content['corr_pos'])
    user.all_corr_values = str(content['all_corr_values'])
    user.trainAcc = str(content['trainAcc'])

    user.corr_elem = str(content['corr_elem'])

    BaseObject.check_and_save(user)

    result = dict({"success": "yes"})

    return jsonify(result)
