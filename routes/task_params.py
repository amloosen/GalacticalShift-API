"""users routes"""
from flask import current_app as app, jsonify, request
from models import TaskParams, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob


@app.route('/task_params/<user_id>/<study_part>', methods=['GET'])
def get_task_params(user_id, study_part):

    query = TaskParams.query.filter(
        TaskParams.user_id == user_id, TaskParams.study_part == study_part)
    if query != None:
        print(query)

    block = query.first_or_404()

    result = {}

    arr_id = block.get_id()  # .replace('  ',' ').split(' ')
    result['id'] = arr_id

    # [0] # .replace('  ',' ').split(' ')
    arr_study_part = block.get_study_part()
    result['study_part'] = arr_study_part


    rr_user = block.get_user_id().replace('  ', ' ').split(' ')
    result['user_id'] = arr_user

    app.logger.info(result)
    return jsonify(result), 200


@app.route('/task_params/create/<user_id>/<study_part>', methods=['POST', 'GET'])
def post_task_params(user_id, study_part):

    content = request.json
    user = TaskParams()

    user.user_id = str(user_id)
    user.study_part = int(study_part)
    user.corPos_sq= str(content['corPos_sq'])
    user.w0= str(content['w0'])
    user.relevant_w= str(content['relevant_w'])
    user.val_corr_elem= str(content['val_corr_elem'])
    user.epsilon= str(content['epsilon'])
    user.precededShift= str(content['precededShift'])
    user.true_pop_size= str(content['true_pop_size'])


    BaseObject.check_and_save(user)

    result = dict({"success": "yes"})

    return jsonify(result)
