"""users routes"""
from flask import current_app as app, jsonify, request
from models import Quiz, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob


@app.route('/quiz/<user_id>/<study_part>', methods=['GET'])
def get_quiz(user_id, study_part):

    query = Quiz.query.filter(
        Quiz.user_id == user_id, Quiz.study_part == study_part)
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


@app.route('/quiz/create/<user_id>/<study_part>', methods=['POST', 'GET'])
def post_quiz(user_id, study_part):

    content = request.json
    user = Quiz()

    user.user_id = str(user_id)

    user.study_part = int(study_part)
    user.startTime = str(content['startTime'])
    user.sectionStartTime = str(content['sectionStartTime'])

    user.sectionEndTime = str(content['sectionEndTime'])
    user.timesRepeated = str(content['timesRepeated'])
    user.timesRestarted = str(content['timesRestarted'])

    BaseObject.check_and_save(user)

    result = dict({"success": "yes"})

    return jsonify(result)
