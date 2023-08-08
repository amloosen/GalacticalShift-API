"""users routes"""
from flask import current_app as app, jsonify, request
from models import MainTask, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob


@app.route('/main_task/<user_id>/<study_part>', methods=['GET'])
def get_main_task(user_id, study_part):

    query = MainTask.query.filter(
        MainTask.user_id == user_id, MainTask.study_part == study_part)
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


@app.route('/main_task/create/<user_id>/<study_part>', methods=['POST', 'GET'])
def post_main_task(user_id, study_part):

    content = request.json
    user = MainTask()

    user.user_id = str(user_id)

    user.study_part = int(study_part)
    user.blockNum = str(content['blockNum'])
    user.startTime = str(content['startTime'])
    user.sectionStartTime = str(content['sectionStartTime'])
    user.blockFinishTime = str(content['blockFinishTime'])

    user.all_element_values = str(content['all_element_values'])

    user.corr_elements = str(content['corr_elements'])
    user.trialSgmMu = str(content['trialSgmMu'])
    user.times_element1 = str(content['times_element1'])
    user.times_element2 =str(content['times_element2'])
    user.times_element3 = str(content['times_element3'])
    user.element1Col = str(content['element1Col'])
    user.element2Col = str(content['element2Col'])
    user.element3Col = str(content['element3Col'])
    user.startSgm = str(content['startSgm'])
    user.startMu = str(content['startMu'])
    user.all_true_pop_size = str(content['all_true_pop_size'])
    user.outcomeHeight = str(content['outcomeHeight'])
    user.trialRT = str(content['trialRT'])
    user.trialTotal = str(content['trialTotal'])
    user.indicKey = str(content['indicKey'])

    user.blockTotal = str(content['blockTotal'])
    user.indicReq = str(content['indicReq'])
    user.trialPerBlock = str(content['trialPerBlock'])
    user.bonusPerBlock = str(content['bonusPerBlock'])
    user.sgmPrompt = str(content['sgmPrompt'])

    BaseObject.check_and_save(user)

    result = dict({"success": "yes"})

    return jsonify(result)
