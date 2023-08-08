"""users routes"""
from flask import current_app as app, jsonify, request
from models import DataBackup, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob


@app.route('/data_backup/<user_id>/<study_part>', methods=['GET'])

def get_databackup(user_id,study_part):


    query = DataBackup.query.filter(DataBackup.user_id==user_id, DataBackup.study_part==study_part)
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

    arr_user            = block.get_databackup_id().replace('  ',' ').split(' ')
    result['user_id']   = arr_user

    app.logger.info(result)
    return jsonify(result), 200


@app.route('/data_backup/create/<user_id>/<study_part>', methods=['POST', 'GET'])

def post_databackup(user_id,study_part):

    content     = request.json
    user = DataBackup()

    user.user_id          = str(user_id)
    user.study_part     = int(study_part)


    user.trialSgmMu_backup = str(content['trialSgmMu_backup'])
    user.times_element1_backup = str(content['times_element1_backup'])
    user.times_element2_backup =str(content['times_element2_backup'])
    user.times_element3_backup = str(content['times_element3_backup'])
    user.trialRT_backup = str(content['trialRT_backup'])
    user.indicKey_backup = str(content['indicKey_backup'])
    user.bonus   = str(content['bonus'])








    BaseObject.check_and_save(user)

    result = dict({"success": "yes"})

    return jsonify(result)
